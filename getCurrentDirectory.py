import os
from pathlib import Path

def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"


def getCurDir1():
  print("Path at terminal when executing this file")
  print(os.getcwd() + "\n")

def getCurDir2():
  print("This file path, relative to os.getcwd()")
  print(__file__ + "\n")

def getCurDir3():
  full_path = os.path.realpath(__file__)
  print("This file directory only")
  print(os.path.dirname(full_path))

def getCurDir4():
  #full_path = os.path.realpath(__file__)
  print(Path(__file__).resolve())  # /home/sk  
  print(Path(__file__).resolve().parent)  # /home/sk  

# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# print("This file directory only")
# print(os.path.dirname(full_path))