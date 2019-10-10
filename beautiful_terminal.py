# print(Fore.LIGHTBLUE_EX + '   _____                         _     ____ ', file=stream)
# print(Fore.LIGHTBLUE_EX + '  |_   _|__  _ __ _ __ ___ _ __ | |_  / ___|  ___ _ __ __ _ _ __   ___ _ __         ', file=stream)
# print(Fore.LIGHTBLUE_EX + '    | |/ _ \| \'__| \'__/ _ \ \'_ \| __| \___ \ / __| \'__/ _` | \'_ \ / _ \ \'__|', file=stream)
# print(Fore.LIGHTBLUE_EX + '    | | (_) | |  | | |  __/ | | | |_   ___) | (__| | | (_| | |_) |  __/ |    ', file=stream)
# print(Fore.LIGHTBLUE_EX + '    |_|\___/|_|  |_|  \___|_| |_|\__| |____/ \___|_|  \__,_| .__/ \___|_|         ', file=stream)
# print(Fore.LIGHTBLUE_EX + '                                                           |_|' + Fore.RESET, file=stream)

# print(Fore.LIGHTBLUE_EX + '                  _ ', file=stream)
# print(Fore.LIGHTBLUE_EX + '   /\  /\__ _ ___| |__  _ __   ___ _ __ ', file=stream)
# print(Fore.LIGHTBLUE_EX + '  / /_/ / _` / __| \'_ \| \'_ \ / _ \ \'__|', file=stream)
# print(Fore.LIGHTBLUE_EX + ' / __  / (_| \__ \ | | | |_) |  __/ |', file=stream)
# print(Fore.LIGHTBLUE_EX + ' \/ /_/ \__,_|___/_| |_| .__/ \___|_|', file=stream)
# print(Fore.LIGHTBLUE_EX + '                       |_| ', file=stream)

# print(" " + Fore.LIGHTRED_EX + " .-----." + "                  " + Fore.YELLOW + " _   __                 _",
#       file=stream)
# print(" " + Fore.LIGHTRED_EX + "/      |" + Fore.YELLOW + "\_______________  " + "| | / /                | |",
#       file=stream)
# print(
#     " " + Fore.LIGHTRED_EX + "|(#)   |" + Fore.YELLOW + " ___   _   _   _) " + "| |/ / _ __   ___   ___| | _____ _ __",
#     file=stream)
# print(
#     " " + Fore.LIGHTRED_EX + "\      |" + Fore.YELLOW + "/   \"-\" | | | |  " + " " + "|    \| '_ \ / _ \ / __| |/ / _ \ '__|",
#     file=stream)
# print(
#     " " + Fore.LIGHTRED_EX + " `-----\'        " + Fore.YELLOW + "| | \"-\"  " + " " + "| |\  \ | | | (_) | (__|   <  __/ |",
#     file=stream)
# print(" " + Fore.YELLOW + "                \"-\"" + "      " + " \_| \_/_| |_|\___/ \___|_|\_\___|_|", file=stream)
# print_information('Version', '0.0.0a')
# print(Fore.LIGHTBLUE_EX + ' {0}'.format('===========' * 7) + Fore.LIGHTBLUE_EX + Fore.RESET, file=stream)

from os import system, name
from main import launch
import time
import threading
import sys
from colorama import init, AnsiToWin32, Fore

# Font Color Configuration
init(autoreset=True)

# Header
hashper_header = [
    '                  _ ',
    '   /\  /\__ _ ___| |__  _ __   ___ _ __ ',
    '  / /_/ / _` / __| \'_ \| \'_ \ / _ \ \'__|',
    ' / __  / (_| \__ \ | | | |_) |  __/ |',
    ' \/ /_/ \__,_|___/_| |_| .__/ \___|_|',
    '                       |_| '
]

trackers = ['ExtraTorrent', 'KickassTorrent', 'MejorTorrent', 'ThePirateBay']

color_scheme = {
    'fst_color': Fore.LIGHTBLUE_EX,
    'snd_color': '',
    'failure': {'text': 'FAILURE', 'color': Fore.LIGHTRED_EX },
    'querying': {'text': 'QUERYNG', 'color': Fore.LIGHTYELLOW_EX },
    'success': {'text': 'SUCCESS', 'color': Fore.LIGHTGREEN_EX }
}

acepted_trackers = ['https://proxtpb.art', 'https://247prox.link', 'https://unblocktheship.org', 'https://proxy247.art']


def print_information(text, data='', subheader=False):
    print(Fore.LIGHTBLUE_EX + ' [ ' + Fore.RESET + text + Fore.LIGHTBLUE_EX + ' ]:' + Fore.RESET + ' {0} '.format(data) + Fore.LIGHTBLUE_EX)
    if subheader:
        print(Fore.LIGHTBLUE_EX + ' {0}'.format('===========' * 7) + Fore.LIGHTBLUE_EX)


def print_header(version='0.5.1'):
    for hline in hashper_header:
        print(Fore.LIGHTBLUE_EX + '{0}'.format(hline))
    print_information('Version', version)
    print(Fore.LIGHTBLUE_EX + ' {0}'.format('===========' * 7) + Fore.LIGHTBLUE_EX)


def print_brackets(text, sub_text, filler='=', multiplier=77, subheader=False, color=Fore.LIGHTBLUE_EX):
    print(color + ' [ ' + Fore.RESET + ' {0} '.format(text) + color + ' ]:' + Fore.RESET + ' {0} '.format(sub_text) + Fore.LIGHTBLUE_EX)
    if subheader:
        print(Fore.LIGHTBLUE_EX + ' {0}'.format(filler * multiplier) + Fore.LIGHTBLUE_EX)


def animated_loading():
    chars = [' /', ' —', ' \\', ' |']
    _chars = ['   ', '.  ', '.. ', '...']


    for char in _chars:
        print('\r ' + color_scheme['fst_color'] + '[' + Fore.RESET + '{0:^5}'.format(char) + color_scheme['fst_color'] + ']', end='')
        #print('\r{0:^5}'.format(char), end='')
        time.sleep(.150)
    print('\r', flush=True, end='')


def update_checker():
    the_process = threading.Thread(target=launch)
    the_process.start()

    while the_process.isAlive():
        animated_loading()
    print('\r', flush=True, end='')

import sys
import os

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def main():
    print()
    print_header()
    print_information('Validating TrackerEndPoints')

    print('{0:^30}{1:^76}'.format('Trackers',' Status'), flush=True)
    print(Fore.LIGHTBLUE_EX + ' {0}'.format('===========' * 7) + Fore.LIGHTBLUE_EX, flush=True)
    update_checker()

    # print_information('Building Tor Circuits')
    # update_checker()
    # os.get_terminal_size()

class Manager(object):
    def new_thread(self):
        return TrackerEndPointManager(parent=self)

    def on_tracker_end_point_checked(self, thread, data):
        print(thread, data)

class TrackerEndPointManager(threading.Thread):

    def __init__(self, parent=None):
        self.parent = parent
        super(TrackerEndPointManager, self).__init__()

    def run(self):
        main()


def move_down(n):
    return "\033[{0}B".format(n)


def move_up(n):
    return "\033[{0}A".format(n)

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == '__main__':
    clear()
    hide_cursor()

    # main()
    mgr = Manager()
    thread = mgr.new_thread()
    thread.start()



    #print_summary(trackers)
    # print_brackets('coco1', 'coco2', subheader=True)
    # def move(y, x):
    #     print("\033[%d;%dH" % (y, x))
