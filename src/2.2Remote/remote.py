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

def remote(command):
    global HOST, user, password
    logging.basicConfig(filename='log.log',filemode='w',level=logging.INFO)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    logging.info("Command executed: "+command)

    tn.write(command+'\n')
    time.sleep(1)
    output = tn.read_very_eager()
    output = output.split(':~$ ')[-2]
    #print output
    logging.info("Output: "+output)
    tn.write("exit\n")

def csv_reader(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

def main():
    lst = csv_reader('file.csv')
    print lst
    for i in lst[0]:
        remote(i)

if __name__ == '__main__':
    main()
