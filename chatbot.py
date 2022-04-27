from speech_recognition import UnknownValueError

for i in range(1):
    import random, json, pickle, nltk, requests, psutil, cpuinfo, pyttsx3 as tts, speech_recognition, numpy as np
    from nltk import metrics
    from nltk.classify import senna
    from psutil import virtual_memory
    from nltk.stem import WordNetLemmatizer
    from tensorflow.python.keras.models import load_model
    from tensorflow.python.keras.engine.functional import reconstruct_from_config

speaker = tts.init()
speaker.setProperty('rate', 134)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
recognizer = speech_recognition.Recognizer()
map = ""

lemmatizaer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizaer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results= [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    global map
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            map = i['tag']
            break
    return result

#Skills
def diagnostics(message):
    speaker.say("C P U report currently only works with an Intel C p u ")
    speaker.runAndWait()
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu = cpu.replace("Intel", "")
    cpu = cpu.replace("Core", "")
    cpu = cpu.replace("(TM)", "")
    cpu = cpu.replace("(R)", "")
    cpu = cpu.replace("CPU", "")
    cpu = cpu.replace("@", "With a clock speed at")
    cpu = cpu.replace("GHz", " Giga hertz")
    speaker.say("Systems Coming online, our Processor is an " + cpu)
    speaker.runAndWait()
    mem = virtual_memory()
    speaker.say("We Have " + str(round(mem.total / (2**30))) + " Gigabytes of RAM")
    speaker.runAndWait
    hdd = psutil.disk_usage('/')
    total = hdd.total / (2**30)
    Used = hdd.used / (2**30)
    Free = hdd.free / (2**30)
    speaker.say("Total Storage Space " + str(round(total)) + " Gigabytes")
    speaker.say("Used Storage Space " + str(round(Used)) + " Gigabytes")
    speaker.say(("Free Storage Space " + str(round(Free)) + " Gigabytes"))

    speaker.runAndWait()

#Process Voice Request
def process(tag, message):
    if tag == "diagnostics":
        diagnostics(message)

speaker.say("Systems Online")
speaker.runAndWait()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            ints = predict_class(message)
            res = get_response(ints, intents)
            process(map, message)
            speaker.say(str(res))
            speaker.runAndWait()

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()


    