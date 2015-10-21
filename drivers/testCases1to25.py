__author__ = 'todzzx'
import importlib

def driverDefault(info):
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)
    componentName = importlib.import_module(info[2])

    inFuncName = info[3]
    inInputVal = info[4]

    output = getattr(componentName, inFuncName)(inInputVal)
    #print(output)


if __name__ == "__main__":
    pass