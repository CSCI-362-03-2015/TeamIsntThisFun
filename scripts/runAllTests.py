#!/usr/bin/python
## Written by Team IsntThisFun:
##  Zachary Davis
##  Ben Byrd
##  Adam Sugarman
##  Katelyn Fulford
##
## CSCI 362-03
## Due: December 01, 2015

import os
#import sys; print(sys.executable)
#import os; print(os.getcwd())
#import sys; print(sys.path)
#import sys; sys.path.append(os.getcwd().index('TeamIsntThisFun')); print(sys.path)
#import sys; sys.path.append('home/todzzx/TeamIsntThisFun.git/TeamIsntThisFun')
#import sys; print(sys.path)

#sys.path.insert(0, 'TeamIsntThisFun')
from TeamIsntThisFun.drivers import driverDefault

# Full script plan:
#   Read file (populate array) -> Parse file -> Sent to driver, calls functions from parse
#   -> Output to report function -> Html

def main():
    
    #clear temp folder of old/unneeded reports and begin browsing/parsing test cases
    clearTemp()
    readFiles()

def readFiles():
    """Reads in the lines from the test case specification file, passes them to parse, passes parsed list to driver specified
    by the test case specification file, and then calls the report function to handle building and displaying the results of
    the test in an HTML page."""
    rootDir = '../testCases/'
    testCaseLines = 8

    ## readFiles() will build the String contents2 with test case data to be later displayed on an HTML page
    contents2 = '''<table border="1" style="width:100%"> 
            <tr> 
            <td>Test #</td>
                <td>Req. Tested</td>
                <td>Component Tested</td> 
                <td>Method Tested</td>
                <td>Test Inputs</td>
                <td>Expected Outcome</td>
                <td>Actual Outcome</td>
                <td width="10%">Outcome</td>
            </tr>'''
    
    for filename in sorted(os.listdir(rootDir)):
        infoLines = [0] * testCaseLines
        N = testCaseLines
        f = open("../testCases/" + filename)
        for i in range(N):
            line = f.next().strip()
            infoLines[i] = line
            # print line
        infoList = parseFiles(infoLines)
        output = driverDefault.driverDefaultFunc(infoList)
        try:
            output = str(output)
        except:
            pass
        contents2 = report(infoList, contents2, output)
        f.close()
        
    ## Predefined header for HTML report
    contents1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
                    <html>
                    <head>
                      <meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
                      <title>Isn't This Fun?</title>
                    </head>
                    <body>
                        <h1>Beets Automated Test Suite</h1></br></br>'''

    ## Predefined footer for HTML report
    contents3 = '''</table></body></html>'''
        
    
    # write to file
    save_path = '../temp'
    fileName = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    completeName = os.path.join(save_path, fileName)
    htmlReport = open(completeName, "w")
    htmlReport.write(contents1 + contents2 + contents3)
    htmlReport.close()
    
    ## Build HTML page and generate it in a browser window
    browseLocal(contents1 + contents2 + contents3)
   

def parseFiles(inLineArray):
    """Parse the list of lines from the test case specification file to put these lines in the correct format."""
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)
    # 7. driver name
    # 8. input type

    paren = '('
    comm = '#'
    quote = '"'
    defaultDriver = "driverDefault"
    inputList = []


    componentName = inLineArray[2]

    head, mid, tail = inLineArray[3].partition(paren)
    funcName = head
    inputType = inLineArray[7]

    if '#' in inLineArray[4]:
        head, mid, tail = inLineArray[4].partition(comm)
    else:
        head = inLineArray[4]

    inputType = inLineArray[7].split(',')
    splitInputs = head.split(',')

    if (len(inputType) != len(splitInputs)):
        pass    ###########################Add here
    else:
        for i in range(len(splitInputs)):
            if (inputType[i].strip() == "string"):
                try:
                    inputList.append(splitInputs[i].strip())
                except:
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "int"):
                try:
                    inputList.append(int(splitInputs[i].strip()))
                except:
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "float"):
                try:
                    inputList.append(float(splitInputs[i].strip()))
                except:
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "char"):
                try:
                    inputList.append(chr(splitInputs[i].strip()))
                except:
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "NoneType"):
                try:
                    inputList.append(None)
                except:
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "bool"):
                try:
                    if (splitInputs[i].strip() == "True"):
                        inputList.append(bool(splitInputs[i].strip()))
                    if (splitInputs[i].strip() == "False"):
                        inputList.append(bool(""))
                except:
                    print(inLineArray[0] + "    boolfail")
                    inputList.append(inLineArray[4])
            elif (inputType[i].strip() == "unicode"):
                try:
                    inputList.append(unicode(splitInputs[i].strip()))
                except:
                    inputList.append(inLineArray[4])
            else:
                inputList.append(inLineArray[4])

    if '#' in inLineArray[5]:
        head, mid, tail = inLineArray[5].partition(comm)
    else:
        head = inLineArray[5]
    
    try:
        expectedVal = head.replace(quote, "")
        expectedVal = expectedVal.strip()
    except:
        print(head)
        expectedVal = ["Test"]

    try:
        driverName = inLineArray[6]
    except:
        driverName = defaultDriver

    returnVal = [inLineArray[0], inLineArray[1], componentName, funcName, inputList, expectedVal, driverName]
    return returnVal


def compare(oracle, actualOutput):
    """Test whether the expected value from the test case specification file equals the actual output from the function."""
    if oracle == actualOutput:
        return '''<font color='green'>Pass</font>'''
    else:
        return '''<font color='red'>Fail</font>'''
    
         
    
def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename, "w")
    output.write(text)
    output.close()
    
def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))  # elaborated for Mac
    
def report(returnVal, contents2, outputVal):
    """ Write results of test to HTML file """
    """ returnVal = infoList, outputVal = output from driver """

    inputLen = len(returnVal[4])
    inputVal = str(returnVal[4][0])
    for i in range(inputLen-1):
        inputVal += ", " + str(returnVal[4][i])

    contents2 = contents2 + '''<tr> 
                    <td>''' + str(returnVal[0]) + '''</td>
                    <td>''' + str(returnVal[1]) + '''</td>
                    <td>''' + str(returnVal[2]) + '''</td> 
                    <td>''' + str(returnVal[3]) + '''</td>
                    <td>''' + inputVal          + '''</td>
                    <td>''' + str(returnVal[5]) + '''</td>
                    <td>''' + str(outputVal)    + '''</td>
                    <td>''' + str(compare(str(returnVal[5]), str(outputVal))) + '''</td>
                </tr>'''
    return contents2

from TeamIsntThisFun.project.src.beets.beets import autotag
from TeamIsntThisFun.project.src.beets.beets import ui
from beets.autotag import hooks
import beets

def driverDefaultFunc(info):
    """Calls the function specified in the test case specification file with the specified inputs, then returns the output."""
    # info[2]. component being tested
    # info[3]. method being tested
    # info[4]. test input(s) including command-line argument(s)
    #componentName = importlib.import_module(beets)

    try:
        inFuncName = info[3]
    except:
        inFuncName = "human_bytes"
    try:
        inInputVal = info[4]
    except:
        pass

    if (len(inInputVal) == 1):
        try:
            output = getattr(ui, inFuncName)(inInputVal[0])
        except TypeError as e:
            output = "TypeError"
        #except InputError:
        #    output = "InputError"
        except:
            output = "Error"
    elif (len(inInputVal) == 2):
        if (info[2] == "autotag"):
            #print(info[0] + "   rrr1")
            try:
                output = getattr(autotag.hooks, inFuncName)(inInputVal[0], inInputVal[1])
            except TypeError as e:
                output = "TypeError"
            #except InputError:
            #    output = "InputError"
            except AssertionError as e:
                output = "AssertionError"
            except Exception, e:
                print(str(e))
                print(repr(e))
                output = "Errorrr"
        elif (info[2] == "ui"):
            #print(info[0] + "   rrr2")
            try:
                #output = getattr(ui, "human_bytes")(None)

                output = getattr(ui, inFuncName)(inInputVal[0], inInputVal[1])
            except TypeError as e:
                output = "TypeError"
            #except InputError:
            #    output = "InputError"
            except AssertionError as e:
                output = "AssertionError"
            except Exception, e:
                print(str(e))
                print(repr(e))
                output = "Errorrr2"
    else:
        output = "Some Error"

    return output
    
def clearTemp():
    folder = '../temp/'
    for item in os.listdir(folder):
        file_path = os.path.join(folder, item)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e


if __name__ == "__main__":
    """Call main if the module is run and not if imported."""
    main()
