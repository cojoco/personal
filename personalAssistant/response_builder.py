#! /usr/bin/env python3

"""Builds Zura's response"""



def respond(user_string):
  # Setup
  EXIT_STRINGS = ['exit', 'bye']
  should_exit = False

  # Search for the correct response
  if any(exit_string in user_string for exit_string in EXIT_STRINGS):
    print("Alright, bye!")
    should_exit = True
  elif "help" in user_string:
    print("What can I help with?")
  else:
    print("Sorry, I didn't understand. Can you say that another way?")
  return should_exit
