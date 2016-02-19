import paramiko
import csv
import time
import logging
import getpass
import sys
import telnetlib
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("params.ini")
HOST = str(Config.get('Section1', 'HOST'))
user = str(Config.get('Section1', 'user'))
password = str(Config.get('Section1', 'password'))

def remote(commands):
    global HOST, user, password
    logging.basicConfig(filename='log.log',filemode='w',level=logging.INFO)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    for command in commands:
        #print command
        logging.info("Command executed: "+command)
        tn.write(command+'\n')
        time.sleep(1)
        output = tn.read_very_eager()
        output = output.split(command)[-1]
        logging.info("Output: "+ output.replace('\n', '  ').replace('\r', '  ') + "\n")
    tn.write("exit\n")

def csv_reader(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list[0]

def main():
    lst = csv_reader('file.csv')
    remote(lst)

if __name__ == '__main__':
    main()
