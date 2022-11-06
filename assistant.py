import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import time
import smtplib
import random
import ast
import io
import os
import sys
import os
import wmi
import psutil
import subprocess
import shutil
import psutil
from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer
import time
import PyPDF2
import pyttsx3
import platform
import nvgpu
from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get default audio device using PyCAW


# first = Trueyaman sey
# chromePath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" %s'
# # URLS = ("first page", "second page", "third page")
# # for url in URLS:
# #     if first:
# #         webbrowser.get(chromePath).open(url)
# #         first = False
# #     else:
# #         webbrowser.open(url, new=2)

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty('voice', voices[1].id)

mail_dir = {'Yaman': 'yamansethiabc@gmail.com', 'Tarun': 'tarunsethi1995@gmail.com'}


def ad_MP(n, m):
    file = open("data.py", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    dictionary[f'{n}'] = f"{m}"
    nf = open('data.py', 'w')
    nf.write(str(dictionary))
    nf.close()


def find_C(cnam):
    d = io.open('C:\\Users\\RAHUL\\PycharmProjects\\pyhtonaiducat\\contacts.txt', 'r', encoding='utf-8')
    f = d.read()
    cont = ast.literal_eval(f)
    d.close()
    kd = cont.keys()
    if cnam in kd:
        nc = cont[cnam]
        return nc


def autoshut( n):
    n1 = n * 60

    # converter.say("Shutting your system down in ")

    for i in range(0, n):
        m = n1 // 60
        s = n1 % 60
        sys.stdout.write(f" \r                                     Shutting down in {m} minutes and {s} seconds..")
        n1 -= 1
        time.sleep(1)
        if m == 0 and s == 1:
            os.system("shutdown /p /f")


def id(n):
    file = open("C:\\Users\\RAHUL\\Pycharm"
                "Projects\\pyhtonaiducat\\day 1\\data.py", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    try:
        for name in dictionary.keys():
            if name == f'{n}':
                return dictionary[n]
    except:
        speak(f"No Person Found Named {n}.. Please Add a Mail for this Name...")


def speak(audio):
    converter = pyttsx3.init("sapi5")
    converter.setProperty('rate', 200)

    converter.setProperty('volume', 0.9)
    voices = converter.getProperty("voices")
    converter.setProperty('voice', voices[1].id)
    converter.say(audio)
    converter.runAndWait()


def wishMe():
    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    try:
        hour = int(datetime.now().hour)
        if 0 <= hour < 12:
            speak("Helllow!. A Very Good Morning to You..")
        elif 12 < hour < 18:
            speak("Helllow!!. A Very Good Afternoon to You..")
        else:
            speak("Helllow!. A Very Good Afternoon to You..")

        speak("i am greeky greeks, A virtual AI therapist .... First let me check your system before i can further help you")

        print("Performing system check, Please Wait..")
        print("=" * 40, "System Information", "=" * 40)

        my_system = platform.uname()
        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")

        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]

        print(f"Manufacturer: {my_system.Manufacturer}")
        print(f"Model: {my_system.Model}")
        print(f"Name: {my_system.Name}")
        print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
        print(f"SystemType: {my_system.SystemType}")
        print(f"SystemFamily: {my_system.SystemFamily}")
        print(f"Memory :{psutil.virtual_memory()}")

        print("=" * 40, "Boot Time", "=" * 40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

        print("=" * 40, "CPU Info", "=" * 40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        print("\nMemory Information :- \n")

        print("=" * 40, "Memory Information", "=" * 40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("=" * 20, "SWAP", "=" * 20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

        # Disk Information
        print("=" * 40, "Disk Information", "=" * 40)
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}")
        print(f"Total write: {get_size(disk_io.write_bytes)}")

        # Network information
        print("=" * 40, "Network Information", "=" * 40)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

        time.sleep(2)
        print("\nSystem Check was successful.\n")

        speak(
            "System Check was successful. all hardware and software drivers are working properly."
            "Now Do you want to talk about how you are feeling?")
            
        time.sleep(1)

    except Exception as e:
        speak("Sorry!!.. There's something wrong. Something is troubling system check operation... Please take your"
              "system to  Dell Service Controller")
        print("\n\n", "=" * 40, "Error Reference", "=" * 40)
        print("\n", e)

        print("\n", "Microphone Device not Found....")
        time.sleep(7)


def take():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 150
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:
        print("I missed Something. Please Say that again.")
        speak("I missed Something. Please Say that again.\n")
        return "None"
    
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = take().lower()

        if "open youtube" in query:
            speak("Opening..")
            webbrowser.open('youtube.com')
            time.sleep(2)

        elif "open mail" in query:
            speak("Opening..")
            webbrowser.open('gmail.com')
            time.sleep(2)

        elif 'music' in query:
            speak("Taking You to Music..")
            dirms = 'D:\\Punjabi'
            num = random.randint(0, len(dirms))
            songs = os.listdir(dirms)
            os.startfile((os.path.join(dirms, songs[num])))

        elif 'shutdown' in query:
            os.system("shutdown /s")
            speak("shutting Down your system..")

        elif 'open chrome' in query:
            ppa_thm = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(ppa_thm)
            time.sleep(2)

        elif 'schedule power off' in query:
            speak("Please tell me time in minutes...")
            n = int(input("Enter time in minutes :- "))
            speak(f"ohkay.. i will shut your system down in {n} minutes..")
            autoshut(n)

        elif "open google" in query:
            speak("Opening..")
            webbrowser.open('google.com')
            time.sleep(2)

        elif 'please do not' in query:
            speak('what happened now... do not think about deleting me again..')

        elif "who are you" in query:
            speak("I am a Virtual Assistant..")

        elif "hai" in query:
            speak("hello..")

        elif "hello" in query:
            speak("hello..")

        elif "yes" in query:
            speak("dont get shy I will listen to you and help you"
            "Tell me what do you think about?")

        elif "no not now" in query:
            speak("no problem you can take all the time you want but you feel light headed once you tell me what is going in that mind")
            exit()

        elif "your name" in query:
            speak("My Name is geeky greeks")

        elif 'do you love me' in query:
            speak("Sorry i am not programmed to love someone..")

        elif 'how are you' in query:
            speak('I am good.. Hope you are also doing well.')

        elif 'quit' in query:
            speak("Thanks for using me. I hope you will remember me in future.")
            exit()

        elif 'exit' in query:
            speak("Thanks for using me. I hope you will remember me in future.")
            exit()

        elif 'your age' in query:
            speak("i am one hour old.")

        elif 'what you can do for me' in query:
            speak("i can do anything you want. like pla"
                  ""
                  ""
                  ""
                  ""
                  ""
                  "ying music.. opening google.")

        elif 'how old are you.' in query:
            speak("i am one hour old.")

        elif 'thanks' in query:
            speak("it is my pleasure.")

        elif 'thank you' in query:
            speak("it is my pleasure.")
            exit()

        elif 'ask you' in query:
            speak('yeah... sure..')

        elif "sleep" in query:
            speak("I am going to sleep.. please wake me up when you need any help")
            input("Press any key to wake Doraami up...\n")

        elif "feeling sad" in query:
            speak("It's ok to be sad but just remeber that Sometimes your joy is the source of your smile,"
            "but sometimes your smile can be the source of your joy"
            "dont get stressed! life gives you hurdles so that you can jump in the air to cross them")
            speak("Don't be sad , I am playing some music for you ")
            webbrowser.open('youtube.com')
            time.sleep(2)    

        elif  "sad" in query:
            speak("It's ok to be sad, but just remeber that Sometimes your joy is the source of your smile,but sometimes your smile can be the source of your joy,dont get stressed! life gives you hurdles so that you can jump in the air to cross them")
            speak("Don't be sad , I am playing some music for you")
            webbrowser.open('youtube.com')
            time.sleep(2)        
        
        elif "I am feeling sad" in query:
            speak("It's ok to be sad, but just remeber that Sometimes your joy is the source of your smile,"
            "but sometimes your smile can be the source of your joy"
            "dont get stressed! life gives you hurdles so that you can jump in the air to cross them")
            speak("Don't be sad , I am playing some music for you")
            webbrowser.open('youtube.com')
            time.sleep(2)
        
        elif "I am not feeling good" in query:
            speak("Everything you are feeling right now is all temoporary , Everything will be alright, you have just started your journey of life,"
            "there will be a billion bumps on this road all you have to do smile and learn from each one of them")

        elif "I am stressed " in query:
            speak("dont get stressed! life gives you hurdles so that you can jump in the air to cross them")

        elif "stressed " in query:
            speak("dont get stressed! life gives you hurdles so that you can jump in the air to cross them")

        elif "I am feeling demotivated" in query:
            speak("you have just started your journey of life, "
            "there will be a billion bumps on this road all you have to do smile and learn from ech one of them")
        
        elif "demotivated" in query:
            speak("you have just started your journey of life, "
            "there will be a billion bumps on this road all you have to do smile and learn from ech one of them")

        elif "I am feeling pressured and I can't do anything in my life" in query:
            speak("there is a qoute- i will love the light for it shows me the way, yet i will endure the darkness for it shows me the stars."
            "life is a mixture of all emotions and you have the right to choose which one you want to live in the moment"
            "but you have to choose it wisely and not regret it later on.")
    