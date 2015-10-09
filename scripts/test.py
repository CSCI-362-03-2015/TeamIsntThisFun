#!/usr/bin/env python

import sys
from beets.ui import human_bytes

def main():
  test1 = 1023
  test2 = -1
  test3 = 0
  test4 = 2000000000 # 2 billion
  test5 = None
  
  print("test1: " + human_bytes(test1) + "\n")
  print("test2: " + human_bytes(test2) + "\n")
  print("test3: " + human_bytes(test3) + "\n")
  print("test4: " + human_bytes(test4) + "\n")
  print("test5: " + human_bytes(test5))

if __name__ == "__main__":
  main()
