import vlc
import os
import random
from time import sleep

# pqtran Jan 30 2018
# Provided with 24 audio samples
# A game is guarenteed a winner by pigeonhole principle

def print_header():
    os.system('clear')
    print("\t**********************************************")
    print("\t***  Chinese PinYin Bingo Extravaganza!!!  ***")
    print("\t**********************************************")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

def print_main_menu():
    print("[q] Quit  [s] Start game")

def print_game_menu():
    print("[q] Quit [p] Play [<] Navigate left [>] Navigate right [a] Show answer")

#def print_end_game_menu():
#    print("\t[q] Quit   [n] New game")

def print_draw_answer(draw_answer):
    sleep_interval = 0.4

    print("And the answer is ...")
    sleep(sleep_interval * 2)

    for x in range(3, 0, -1):
        print(str(x))
        sleep(sleep_interval)

    print(draw_answer)

def print_draw_index(pinyin_index):
    draw_index = pinyin_index + 1
    print("Draw #%s" % str(draw_index))

def get_user_choice():
    return input("Input: ")

def get_game_started():
    return game_started

#def get_game_ended():
#    return game_ended

def set_game_started(started):
    global game_started
    game_started = started

#def set_game_ended(ended):
#    global game_ended = ended

def get_pinyin_index():
    return pinyin_index

def set_pinyin_index(index):
    global pinyin_index
    pinyin_index = index

def get_pinyin_clips():
    return pinyin_clips

def set_pinyin_clips(clips):
    global pinyin_clips
    pinyin_clips = clips

def get_audio_dir():
    return audio_dir

def set_audio_dir(dir):
    global audio_dir
    audio_dir = dir

def bingo_setup():
    clips = os.listdir('./assets/audio/')
    random.shuffle(clips)
    set_pinyin_clips(clips)

    pinyin_index = 0
    set_pinyin_index(pinyin_index)

    print_header()
    print_game_menu()
    print_draw_index(pinyin_index)

def start_game():
    if get_game_started(): # and get_game_ended():
        return
    else:
        set_game_started(True)

    bingo_setup()

#def restart_game():
#    if not get_game_started() or not get_game_ended():
#        return
#    else:
#        set_game_started(True)
#        set_game_ended(False)

#    bingo_setup()

def play_sound():
    if not get_game_started():
        return

    index = get_pinyin_index()
    clips = get_pinyin_clips()

    dir = get_audio_dir()
    mp = vlc.MediaPlayer(dir + clips[index]);
    mp.play()

def prev_pinyin():
    pinyin_index = get_pinyin_index()

    if not get_game_started():
        return

    if pinyin_index == 0:
        print("At the beginning, cannot go any further :x")
    else:
        pinyin_index -= 1
        set_pinyin_index(pinyin_index)
        print_header()
        print_game_menu()
        print_draw_index(pinyin_index)

def next_pinyin():
    pinyin_index = get_pinyin_index()
    clips = get_pinyin_clips()

    if not get_game_started():
        return

    if pinyin_index == len(clips) - 1:
        print("At the end, cannot go any further :$")
    else:
        pinyin_index += 1
        set_pinyin_index(pinyin_index)
        print_header()
        print_game_menu()
        print_draw_index(pinyin_index)

# assuming the format of zzz4.mp3
def parse_pinyin_from_filename(filename):
    extension_length = 4
    pinyin = filename[0 : len(filename) - extension_length]
    return pinyin


def show_answer():
    if not get_game_started():
        return

    print_header()
    print_game_menu()

    pinyin_index = get_pinyin_index()
    print_draw_index(pinyin_index)

    clips = get_pinyin_clips()
    draw_answer = parse_pinyin_from_filename(clips[pinyin_index])

    print_draw_answer(draw_answer)

def init():
    set_game_started(False)
#    global game_ended = False
    set_audio_dir("./assets/audio/")

def main():
    init()

    print_header()
    print_main_menu()

    input=''
    while input != 'q':
        input = get_user_choice()

        if input == 'q':
            print("\nThank you for playing :>")
        elif input == 's':
            start_game()
#        elif input == 'n':
#            restart_game()
        elif input == 'p':
            play_sound()
        elif input == '<':
            prev_pinyin()
        elif input == '>':
            next_pinyin()
        elif input == 'a':
            show_answer()
        else:
            print("\nSorry, don't understand your input. Try again :<")


main()
