# !/usr/bin/env python

import os
import configparser
import subprocess
import threading
import colorama
from colorama import Fore
from time import sleep
from ppadb.client import Client as AdbClient


__author__ = 'themalwarenews ( @themalwarenews) '
__inspired_by__ = ' DROXES '

class Garuda:

    def __init__(self):
        self.apk_list = ['xposed.apk', 'drozer.apk', 'term.apk', 'busybox.apk', 'rootcloak.apk', 'inspeckage.apk', 'SSLunpin.apk']
        self.test_list = ['drozer.apk']
        self.server_list = ['tcpdump', 'frida_server', 'xposed_flash.zip']
        self.flashfile = ['xposed_flash.zip']
        self.tools_list = ['apktool','python-pip','python3-pip', 'python-dev', 'python-twisted']
        self.py_dependencies = ['frida','frida-tools','objection']
        self.sys_tools = ['drozer.deb']

    def welcome(self):
        __banner__='''\t ██████╗  █████╗ ██████╗ ██╗   ██╗██████╗  █████╗ 
\t██╔════╝ ██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗
\t██║  ███╗███████║██████╔╝██║   ██║██║  ██║███████║
\t██║   ██║██╔══██║██╔══██╗██║   ██║██║  ██║██╔══██║
\t╚██████╔╝██║  ██║██║  ██║╚██████╔╝██████╔╝██║  ██║
\t ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                                                  '''
        
        print("\n")
        print(Fore.RED+" \t WELCOME TO ALL IN ONE ANDROID PENTESTING SETUP TOOL\n")
        print(Fore.GREEN+__banner__)
       
        print ("      ------------------------------------------------------------------")
        print ("\n\t| TOOL    :  Android Pentesting setup \t\t|")
        print ("\t| AUTHOR  :  " + __author__ + " |")      
        print ("\t| Inspiration  :  " + __inspired_by__ + "\t\t\t|")

        print ("\t| VERSION :  1.0  \t\t\t\t|\n")
        print ("      ------------------------------------------------------------------")

        print("\n\n")
        print(Fore.RED+"\t NOTE: MAKE SURE YOU HAVE TURNED ON YOUR ANDROID VIRTUAL DEVICE / REAL DEVICE AND CONNECTED VIA ADB")


    def install_sys_tools(self):
        print (Fore.BLUE+"\n[+] Setting up the system")
        for i in self.tools_list:
            subprocess.call(['sudo', 'apt-get', '-f', 'install', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print (Fore.WHITE+"\t[+] Installed " + i)

        for j in self.py_dependencies:
            subprocess.call(['sudo', '-H', 'pip', 'install', j], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print ("\t[+] Installed " + j)

        for k in self.sys_tools:
            subprocess.call(['sudo', 'dpkg', '-i', os.getcwd() + "/system/" + k], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print ("\t[+] Installed " + k)

    def install_apks(self):
        print (Fore.BLUE+"\n[+] Installing APK Tools")
        for i in self.apk_list:
            subprocess.Popen(['adb', 'install', '-r', os.getcwd() + "/apk/" + i],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print (Fore.WHITE+"\n \t[+] Installed " + i)
            
    def install_xposed(self):
        print (Fore.BLUE+"\n[+] Installing xposedframework")
        for i in self.flashfile:
            subprocess.Popen(['adb', 'push', os.getcwd() + '/xposed/' + i, '/sdcard/Download'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print (Fore.WHITE+"\n \t[+] Installed " + i) 

    def install_server_files(self):
        print (Fore.BLUE+"\n[+] Installing Binary Tools")
        for i in self.server_list:
            subprocess.Popen(['adb', 'push', os.getcwd() + '/bin/' + i, '/data/local/tmp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print (Fore.WHITE+"\n \t[+] Installed " + i)   
        os.system('adb shell "chmod 777 /data/local/tmp/frida_server"')
        os.system('adb shell "chmod 777 /data/local/tmp/tcpdump"')
        
        #subprocess.run('adb shell "chmod 777 /data/local/tmp/tcpdump"', shell=True)
        #subprocess.run('adb shell "chmod 777 /data/local/tmp/frida_server"', shell=True)
        print(Fore.RED+"\n All the tools have been installed, Please goahead and configure the Xposed Framework.")
        print(Fore.RED+"\n watch this video to setup Xposed-framework link : https://youtu.be/Sy09edb57hg .")
                  

def main():
    ga = Garuda()
    ga.welcome()
    ga.install_sys_tools()   
    ga.install_apks()
    ga.install_xposed()
    ga.install_server_files()
   

if __name__ == '__main__':
    main()


