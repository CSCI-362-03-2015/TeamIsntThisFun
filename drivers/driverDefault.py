from beets import ui
from beets import autotag
import beets

def driverDefaultFunc(info):
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)
    #componentName = importlib.import_module(beets)

    try:
        inFuncName = info[3]
    except: 
        inFuncName = "human_bytes"
    try:
        inInputVal = info[4]
    except:
        pass

    if (info[2] == "ui"):
        try:
            output = getattr(ui, inFuncName)(inInputVal[0])
        except TypeError as e:
            output = "TypeError"
        #except InputError:
        #    output = "InputError"
        except:
            output = "Error"

     #elif (info[2] == "autotag"):
     #   try:
     #       output = getattr(autotag, inFuncName)(inInputVal[0])
     #   except TypeError as e:
     #       output = "TypeError"
     #   #except InputError:
     #   #    output = "InputError"
     #   except:
     #       output = "Error"

    return output