import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_integer():
    integer = f'{random.randint(100000, 999999)}'
    return integer
