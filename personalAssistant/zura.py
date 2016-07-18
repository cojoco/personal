#!/usr/bin/env python3

"""This is the base file for my chatbot/personal assistant"""

user_string = ''
EXIT_STRINGS = ['exit', 'goodbye', 'good bye', 'bye', 'see you', 'see ya']

print("Hi! I'm Zura.\nCan I help you with something? Or maybe you just want to talk?")

while (True and user_string.lower() not in EXIT_STRINGS):
    user_string = input()
    print("User string gotten!")

print("Alright, see you later!")
