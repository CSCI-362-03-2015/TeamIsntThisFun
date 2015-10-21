__author__ = 'todzzx'

def driver(info):
    inFuncName = info[3]
    inInputVal = info[4]

    output = getattr(ui, inFuncName)(inInputVal)
    #print(output)