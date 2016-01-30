import paramiko
import csv
import logging
import getpass
import sys
import telnetlib

def remote(command):
    HOST = "10.28.3.113"
    user = 'bon'
    password = 'chupamela'

    tn = telnetlib.Telnet(HOST)

    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    command = command+'\n'
    tn.write(command)
    tn.write("exit\n")

    logging.basicConfig(filename='example.log',level=logging.WARNING)
    logging.warning(tn.read_all())

def csv_reader(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

def remote_con(host, user, passw, command):
    print "Acces digitalocean UBUNTU"
    #command = raw_input("Enter command")
    #passw = raw_input("Enter password")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passw)
    stdin, stdout, stderr = ssh.exec_command(command)
    # with open("log.log", 'w') as f:
    #     text = str(stdout.readlines())
    #     f.write(text)
    logging.basicConfig(filename='example.log',level=logging.WARNING)
    logging.warning(stdout.readlines())
    logging.warning('NEXT')
    logging.warning(stderr.readlines())
    #print 'This is error =',stderr.readlines()
    ssh.close()

def main():
    lst = csv_reader('file.csv')
    print lst
    for i in lst[0]:
        print i
        remote(i)
        #remote(i)

if __name__ == '__main__':
    main()
