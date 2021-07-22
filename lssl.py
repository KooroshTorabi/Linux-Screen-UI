from os import system
from os import path
from sys import exit as exit_program
import glob
from simple_term_menu import TerminalMenu
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
log_dir = config['main']['log_dir']


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREENBACKGROUND = '\x1b[6;30;42m'
    GREENBACKGROUND1 = '\033[30;42m'


onlyfiles = [f for f in glob.glob(log_dir+"/*.log")]
choices = onlyfiles
choices = sorted(choices, reverse=True)


print(
    f"\n\r           {bcolors.GREENBACKGROUND1}                         {bcolors.ENDC}")
print(
    f"\r           {bcolors.GREENBACKGROUND1}   Linux Screen Viewer   {bcolors.ENDC}")
print(
    f"\r           {bcolors.GREENBACKGROUND1}                         {bcolors.ENDC}")
print(
    f"\r           {bcolors.GREENBACKGROUND1}                         {bcolors.ENDC}")
print(
    f"\r           {bcolors.GREENBACKGROUND1}                         {bcolors.ENDC}")
print('\n\rPlease select one:  (ctrl-c for exit)\n\r')

if (not path.isdir(log_dir)):
    print("there is no screen recorded! ")
    exit_program()

terminal_menu = TerminalMenu(
    choices, preview_command="ls -lha {}", preview_size=.75)

answer = terminal_menu.show()

if (answer != None):
    print('\n\r_______________________ start ... _________________________\n\r')
    filename = choices[answer].replace(".log", '')
    filename = filename.replace(log_dir+"/", '')

    command = " scriptreplay --timing="+log_dir+"/" + \
        filename+".timing "+log_dir+"/"+filename+".log"

    system(command)

    print('\n\r_________________________ end ... _________________________\n\r')
