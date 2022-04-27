def diagnostics():
    import cpuinfo, psutil
    from psutil import virtual_memory
    speaker()
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu = cpu.replace("(TM)", "")
    cpu = cpu.replace("(R)", "")
    cpu = cpu.replace("CPU", "")
    cpu = cpu.replace("@", "With a clock speed at")
    cpu = cpu.replace("GHz", " Giga hertz")
    mem = virtual_memory()
    hdd = psutil.disk_usage('/')
    total = hdd.total / (2**30)
    Used = hdd.used / (2**30)
    Free = hdd.free / (2**30)
    speaker.say("Systems Coming online, our Processor is an " + cpu)
    speaker.say("We Have " + str(round(mem.total / (2**30))) + " Gigabytes of RAM")
    speaker.say("Total Storage Space " + str(round(total)) + " Gigabytes")
    speaker.say("Used Storage Space " + str(round(Used)) + " Gigabytes")
    speaker.say(("Free Storage Space " + str(round(Free)) + " Gigabytes"))
    speaker.runAndWait()





#All Skill functions should be above this line
###############################################################################################
'''

██████╗░░█████╗░███╗░░██╗██╗████████╗ ███████╗██████╗░██╗████████╗
██╔══██╗██╔══██╗████╗░██║╚█║╚══██╔══╝ ██╔════╝██╔══██╗██║╚══██╔══╝
██║░░██║██║░░██║██╔██╗██║░╚╝░░░██║░░░ █████╗░░██║░░██║██║░░░██║░░░
██║░░██║██║░░██║██║╚████║░░░░░░██║░░░ ██╔══╝░░██║░░██║██║░░░██║░░░
██████╔╝╚█████╔╝██║░╚███║░░░░░░██║░░░ ███████╗██████╔╝██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚══╝░░░░░░╚═╝░░░ ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░

██████╗░███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗ ████████╗██╗░░██╗██╗░██████╗ ██╗░░░░░██╗███╗░░██╗███████╗
██╔══██╗██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║ ╚══██╔══╝██║░░██║██║██╔════╝ ██║░░░░░██║████╗░██║██╔════╝
██████╦╝█████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝ ░░░██║░░░███████║██║╚█████╗░ ██║░░░░░██║██╔██╗██║█████╗░░
██╔══██╗██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░ ░░░██║░░░██╔══██║██║░╚═══██╗ ██║░░░░░██║██║╚████║██╔══╝░░
██████╦╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░ ░░░██║░░░██║░░██║██║██████╔╝ ███████╗██║██║░╚███║███████╗
╚═════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░ ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░ ╚══════╝╚═╝╚═╝░░╚══╝╚══════╝
'''

###############################################################################################
def speaker():
    import pyttsx3 as tts

    speaker = tts.init()
    speaker.setProperty('rate', 134)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)


l = []
copy_dict = dict(locals())
for key, value in copy_dict.items():
    if "function" in str(value):
        l.append(key)
l = str(l)
l = l.replace("[", "")
l = l.replace("]", "")
l = l.replace("\'", "")
l = l.replace(",", "")
l = l.replace("__builtins__", "")
l = l.replace("speaker", "")
print(l)
skills = open("skills_list.txt", "w")
skills.truncate(0)
skills.write(l)
skills.close