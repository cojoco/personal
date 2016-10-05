#!/usr/bin/env python3

"""This is the base file for my chatbot/personal assistant"""

from response_builder import respond


def _main():
  """Sets up and starts the conversation loop"""
  # Setup
  user_string = ''
  should_exit = False

  # Print start text
  print("Hi! I'm Zura.")
  print("Can I help you with something? Or maybe you just want to talk?")

  # Begin conversation loop
  while (True and not should_exit):
    user_string = input().lower()
    should_exit = respond(user_string)
    if should_exit:
      break


if __name__ == "__main__":
  _main()
