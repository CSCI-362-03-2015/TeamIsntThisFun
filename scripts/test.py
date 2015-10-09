import sys
import os

def main():
  # todo: import 5 beets functions or all of beets if necessary
  # todo: write 4 helper functions: open file, run the method, compare results, write to html output

  # by this point we have imported all beets function necessary

  # walk the tree
  rootDir = '../testCases/'

  for filename in os.listdir(rootDir):

    with open(os.path.join(rootDir, filename), "r") as f:
      print(filename);
      for line in f:
        # helper function here to populate an array of the 6 lines
        print(line);

        # helper function here to call the beets function with input

        # helper function to compare results

        # helper function to pass output to html file


if __name__ == "__main__":
  main()
