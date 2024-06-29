import string
from random import randint
import random

char ='abcdefghijklmnopqrstuvwxyz1234567890'
# char = string.digits
char_list = []
char_list[:0] = char

def random_uder_id():
    id = ''
    for _ in range(6):
        id += random.choice(char_list)
    return id
print(random_uder_id())

def random_gen_id():
    char = int(input("How many characters do you want\n"))
    # num_of_id = input('How many IDs do you want to be generated\n')

    id = ''
    for _ in range(char):
        id+= random.choice(char_list)
    return id
    
print(random_gen_id())


def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return f'rgb({r},{g},{b})'
print(rgb_color_gen())