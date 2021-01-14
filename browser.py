import argparse
import os
import collections
import requests
from bs4 import BeautifulSoup
import colorama

colorama.init()
parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()


if(args.dir in os.listdir()):
    os.chdir(args.dir)
    for i in os.listdir():
        os.remove(i)
    os.chdir(os.path.dirname(os.getcwd()))
    os.rmdir(args.dir)
try:
    os.mkdir(args.dir)
except FileExistsError:
    pass

os.chdir(args.dir)

my_stack = collections.deque()



# write your code here
state = 1
while(state):

    address = input()

    # retriving downloaded file
    if (address + '.txt' in os.listdir(os.getcwd())):
        with open((address + '.txt'),'r') as f1:
            print(f1.read())

    elif(address == 'back'):

        if(bool(my_stack) == False):
            pass
        else:
            my_stack.pop()
            if (bool(my_stack) == False):
                pass
            else:
                print(my_stack.pop())



    elif(address == 'exit'):
        os.chdir(os.path.dirname(os.getcwd()))
        colorama.deinit()
        state = 0

    elif (not ("." in address)):
        print("error")


    elif('www.' not in address):


        try:
            r = requests.get('http://www.' + address)
        except requests.exceptions.ConnectionError :
            r = requests.get('http://' + address)

        soup = BeautifulSoup(r.content, 'html.parser')
        paragraph = soup.find_all(['p', 'title'])
        link = soup.find_all('a')
        t1 = soup.find_all('ul')
        t2 = soup.find_all('ol')
        t3 = soup.find_all('li')
        a = address.rstrip('.')
        with open(a  + '.txt', 'a') as file:
            for i in paragraph:
                file.write(i.text + '\n')
            for i in link:
                file.write(colorama.Fore.BLUE + str(i.get('href')))
                file.write(('\n'))

        with open(a  + '.txt', 'r') as rfile:
            print(rfile.read())




    elif('www.'  in address):
        r = requests.get('http://' + address)

        soup = BeautifulSoup(r.content, 'html.parser')
        paragraph = soup.find_all(['p', 'title'])
        link = soup.find_all('a')
        t1 = soup.find_all('ul')
        t2 = soup.find_all('ol')
        t3 = soup.find_all('li')

        #addr = address[8:]
        c,a,b =address.split('.')

        with open(a + '.txt', 'a') as file:
            for i in paragraph:
                file.write(i.text + '\n')
            for i in link:
                file.write(colorama.Fore.BLUE + str(i.get('href')))
                file.write('\n')
        with open(a + '.txt', 'r') as rfile:
            print(rfile.read())





    else:
        print("error")

