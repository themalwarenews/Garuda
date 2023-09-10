import os
import subprocess
import colorama
from colorama import Fore

# Define constants for directories and file paths
APK_DIR = os.path.join(os.getcwd(), "apk")
XPOSED_DIR = os.path.join(os.getcwd(), "xposed")
BIN_DIR = os.path.join(os.getcwd(), "bin")
SYSTEM_DIR = os.path.join(os.getcwd(), "system")

class Garuda:
    def __init__(self):
        self.apk_list = ['xposed.apk', 'drozer.apk', 'term.apk', 'busybox.apk', 'rootcloak.apk', 'inspeckage.apk', 'SSLunpin.apk']
        self.flashfile = ['xposed_flash.zip']
        self.server_list = ['tcpdump', 'frida_server']
        self.tools_list = ['apktool','python-pip','python3-pip', 'python-dev', 'python-twisted']
        self.py_dependencies = ['frida','frida-tools','objection','apkleaks','andriller','quark-engine']
        self.sys_tools = ['drozer.deb']
        self.DAST_tool = ['rms-runtime-mobile-security','dexcalibur']

    def welcome(self):
        banner = '''
            ██████╗  █████╗ ██████╗ ██╗   ██╗██████╗  █████╗ 
            ██╔════╝ ██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗
            ██║  ███╗███████║██████╔╝██║   ██║██║  ██║███████║
            ██║   ██║██╔══██║██╔══██╗██║   ██║██║  ██║██╔══██║
            ╚██████╔╝██║  ██║██║  ██║╚██████╔╝██████╔╝██║  ██║
             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
        '''
        print(f"\n{Fore.RED}\t WELCOME TO ALL IN ONE ANDROID PENTESTING SETUP TOOL\n")
        print(f"{Fore.GREEN}{banner}\n")
        print("      ------------------------------------------------------------------")
        print("\n\t| TOOL    :  Android Pentesting setup \t\t|")
        print("\t| AUTHOR  :  themalwarenews ( @themalwarenews)  |")      
        print("\t| VERSION :  2.0  \t\t\t\t|\n")
        print("      ------------------------------------------------------------------\n\n")
        print(f"{Fore.RED}\t NOTE: MAKE SURE YOU HAVE TURNED ON YOUR ANDROID VIRTUAL DEVICE / REAL DEVICE AND CONNECTED VIA ADB")

    def install_sys_tools(self):
        print(f"{Fore.BLUE}\n[+] Setting up the system")
        for tool in self.tools_list:
            subprocess.call(['sudo', 'apt-get', '-f', 'install', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{Fore.WHITE}\t[+] Installed {tool}")

        for dependency in self.py_dependencies:
            subprocess.call(['sudo', '-H', 'pip3', 'install', dependency], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"\t[+] Installed {dependency}")

        for dependency in self.DAST_tool:
            try:
                subprocess.check_output(['npm', '--version'])
                subprocess.call(['sudo', 'npm', 'install', '-g', dependency], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"\t[+] Installed {dependency}")  
            except subprocess.CalledProcessError:
                print(f"\t[+] install npm first")


        for sys_tool in self.sys_tools:
            subprocess.call(['sudo', 'dpkg', '-i', os.path.join(SYSTEM_DIR, sys_tool)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"\t[+] Installed {sys_tool}")

    def install_apks(self):
        print(f"{Fore.BLUE}\n[+] Installing APK Tools")
        for apk in self.apk_list:
            subprocess.Popen(['adb', 'install', '-r', os.path.join(APK_DIR, apk)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{Fore.WHITE}\n \t[+] Installed {apk}")

    def install_xposed(self):
        print(f"{Fore.BLUE}\n[+] Installing xposedframework")
        for flashfile in self.flashfile:
            subprocess.Popen(['adb', 'push', os.path.join(XPOSED_DIR, flashfile), '/sdcard/Download'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{Fore.WHITE}\n \t[+] Installed {flashfile}")

    def install_server_files(self):
        print(f"{Fore.BLUE}\n[+] Installing Binary Tools")
        for server in self.server_list:
            subprocess.Popen(['adb', 'push', os.path.join(BIN_DIR, server), '/data/local/tmp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{Fore.WHITE}\n \t[+] Installed {server}")
        os.system('adb shell "chmod 777 /data/local/tmp/frida_server"')
        os.system('adb shell "chmod 777 /data/local/tmp/tcpdump"')
        print(f"{Fore.RED}\n All the tools have been installed, Please go ahead and configure the Xposed Framework.")
        print(f"{Fore.RED}\n Watch this video to set up Xposed-framework link: https://youtu.be/Sy09edb57hg.")

    def install_go_based_tools(self):
        subprocess.check_call(['sudo','go', 'install', 'github.com/andpalmier/apkingo/cmd/apkingo@latest'])
        print("apkingo has been installed successfully.")
    
    def is_go_installed(self):
        try:
            subprocess.check_output(['go', 'version'])
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False


def main():
    ga = Garuda()
    ga.welcome()
    ga.install_sys_tools() 
    if ga.is_go_installed():
        ga.install_go_based_tools()  
    ga.install_apks()
    ga.install_xposed()
    ga.install_server_files()
    

if __name__ == '__main__':
    main()
