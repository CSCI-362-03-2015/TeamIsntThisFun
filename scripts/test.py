import sys
import os
import importlib
import drivers
from drivers import driverDefault

# from beets.ui import human_bytes

# Full script plan:
#   Read file (populate array) -> Parse file -> Sent to driver, calls functions from parse
#   -> Output to report function -> Html

def main():
    # todo: import 5 beets functions or all of beets if necessary
    # todo: write 4 helper functions: open file, run the method, compare results, write to html output

    # by this point we have imported all beets function necessary

    # walk the tree
    readFiles()


def readFiles():
    rootDir = '../testCases/'
    count = 0

    for filename in os.listdir(rootDir):
        with open(os.path.join(rootDir, filename), "r") as f:
            # infoLines is an array populated by the first six lines of the testCase file
            infoLines = f.readlines()[0:7]
            infoLines = list(map(str.strip, infoLines))

            infoList = parseFiles(infoLines)
            #driverName = importlib.import_module(infoLines[6])
            #outputVal = getattr(drivers, driverName)(infoList)
            output = driverDefault(infoLines)
            return 0


def parseFiles(inLineArray):
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)

    paren = '('
    comm = '#'
    defaultDriver = "driver"

    componentName = inLineArray[2]

    head, mid, tail = inLineArray[3].partition(paren)
    funcName = head

    # print(inLineArray[4])
    if '#' in inLineArray[4]:
        head, mid, tail = inLineArray[4].partition(comm)
    else:
        head = inLineArray[4]

    try:
        inputVal = float(head.strip())
    except:
        print(head)
        inputVal = 1.0

    try:
        driverName = inLineArray[6]
    except:
        driverName = defaultDriver

    returnVal = [inLineArray[0], inLineArray[1], componentName, funcName, inputVal, inLineArray[5], driverName]
    return returnVal


def compare(oracle, actualOutput):
    if oracle == actualOutput:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
