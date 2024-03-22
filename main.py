import os
from pynput.mouse import Listener
import pyperclip
import random

rootDir = os.path.dirname(os.path.abspath(__file__))
while rootDir[len(rootDir) - 1] != '\\':
    rootDir = rootDir[0:len(rootDir) - 1]

DICTIONARY_PATH = rootDir + "AndroidProjectObfuscator\\src\\main\\kotlin\\dictionary\\dictionary.txt"

words = []


def read_dictionary():
    global words
    with open(DICTIONARY_PATH, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()


def generate_camel_case():
    global words
    num_words = random.randint(1, 3)
    selected_words = random.sample(words, num_words)
    camel_case = selected_words[0].lower() + ''.join(word.capitalize() for word in selected_words[1:])
    return camel_case


def on_click(x, y, button, pressed):
    if str(button) == "Button.x2" and pressed:
        variable = generate_camel_case()
        print(variable)
        pyperclip.copy(variable)


def main():
    read_dictionary()
    with Listener(on_click=on_click) as listener:
        listener.join()

main()
