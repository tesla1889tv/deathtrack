# MIT License
# Copyright (c) 2022 terribletable
# See [LICENSE](https://raw.githubusercontent.com/tesla1889tv/deathtrack/main/LICENSE) for details


# run 'python3' in command prompt, install python3, and run 'pip install keyboard' in command prompt prior to using this tool
# to run, navigate to the script in your files, single click on it, shift-right-click on it, select 'Copy as path', open a command prompt, type 'python3 ' (with the space), right-click, and enter
# only tested on windows platforms


from os import name, system
from re import fullmatch
from time import sleep
import keyboard, sys


table = []
longest = 0
highest = 0


def get_name(elem):
    return elem[0]


def add_player(player):
    global table
    global longest
    if len(table) == 9:
        return
    if len(player) > longest:
        longest = len(player)
    table = table + [[player, 0]]


def get_bar():
    global longest
    global highest
    width = longest + len(str(highest)) + 9
    if width < 20:
        width = 20
    bar = '-' * width
    return '+' + bar + '+'


def print_table():
    global table
    global longest
    global highest
    bar = get_bar()
    print(bar)
    i = 0
    for i in range(len(table)):
        line = '| %d | %s ' % ((i + 1), table[i][0])
        while len(line) < (longest + 7):
            line = line + ' '
        line = line + ('| %s ' % (table[i][1],))
        while len(line) < (len(bar) - 1):
            line = line + ' '
        print(line + '|')
        print(bar)


def print_full():
    print_table()
    bar = get_bar()
    prompt = '| 0 | (edit players) '
    while len(prompt) < (len(bar) - 1):
        prompt = prompt + ' '
    print(prompt + '|')
    prompt = '| q | (quit) '
    while len(prompt) < (len(bar) - 1):
        prompt = prompt + ' '
    print(prompt + '|')
    print(bar)


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def add_players():
    keyboard.press_and_release('\b')
    players = input('comma-separated list > ').split(',')
    players = [s.strip() for s in players]
    if (len(players) == 1) and (players[0] == ''):
        return
    for player in players:
        add_player(player)


def edit_manual():
    while True:
        clear_screen()
        print_table()
        keyboard.press_and_release('\b')
        event = keyboard.read_event()
        keyboard.press_and_release('\b')
        if event.name == 'enter':
            continue
        if event.name == 'q':
            return
        try:
            idx = int(event.name)
            if (idx > 0) and (idx <= len(table)):
                idx = idx - 1
                clear_screen()
                val = input('%s at %d (#/q) > ' % (table[idx][0], table[idx][1])).strip()
                if val == 'q':
                    return
                if fullmatch(r'^\d+$', val):
                    table[idx][1] = int(val)
                    return
        finally:
            pass


def remove_player():
    while True:
        clear_screen()
        print_table()
        keyboard.press_and_release('\b')
        event = keyboard.read_event()
        keyboard.press_and_release('\b')
        if event.name == 'enter':
            continue
        elif event.name == 'q':
            return
        try:
            idx = int(event.name)
            if (idx > 0) and (idx <= len(table)):
                del table[idx - 1]
                return
        finally:
            pass


def edit_players():
    while True:
        clear_screen()
        print('1. add player(s) (comma-separated list)')
        print('2. edit player manually')
        print('3. remove player')
        print('q. exit to menu')
        keyboard.press_and_release('\b')
        event = keyboard.read_event()
        if event.name == 'q':
            return
        elif event.name == '1':
            add_players()
            break
        elif event.name == '2':
            keyboard.press_and_release('\b')
            edit_manual()
            break
        elif event.name == '3':
            remove_player()
            break



def no_remorse():
    for i in range(10000):
        keyboard.press_and_release('\b')
    sys.exit(0)


if __name__ == '__main__':
    clear_screen()
    print('input players:')
    add_players()
    while True:
        clear_screen()
        print_full()
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '0':
                edit_players()
            elif event.name == 'q':
                keyboard.press_and_release('\b')
                clear_screen()
                if len(table) > 0:
                    print('==== final tally ====')
                    print_table()
                    print('(to copy results, select the text above and right-click)')
                keyboard.press_and_release('\b')
                no_remorse()
            for i in range(len(table)):
                if event.name == str(i + 1):
                    table[i][1] = table[i][1] + 1
    for i in range(10000):
        keyboard.press_and_release('\b')
