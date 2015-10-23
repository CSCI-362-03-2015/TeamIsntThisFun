import sys
import os
import importlib
from beets import ui

# from drivers.driverDefault import driverDefault

# from beets.ui import human_bytes

# Full script plan:
#   Read file (populate array) -> Parse file -> Sent to driver, calls functions from parse
#   -> Output to report function -> Html

contents1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Isn't This Fun?</title>
</head>
<body>'''

contents2 = '''<table name="mytable" id="mytable" border="1" style="width:90%">
                <tr> 
                    <td>Test #</td>
                    <td>Req. Tested</td>
                    <td>Component Tested</td> 
                    <td>Method Tested</td>
                    <td>Test Inputs</td>
                    <td>Expected Outcome</td>
                    <td>Actual Outcome</td>
                    <td>Pass or Fail</td>
                </tr>'''

contents3 = '''</table>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script>
            function sortTable( jQuery ){
              var rows = $('#mytable tbody  tr').get();

              rows.sort(function(a, b) {

              var A = $(a).children('td').eq(0).text().toUpperCase();
              var B = $(b).children('td').eq(0).text().toUpperCase();

              if(A < B) {
                return -1;
              }

              if(A > B) {
                return 1;
              }

              return 0;

              });

              $.each(rows, function(index, row) {
                $('#mytable').children('tbody').append(row);
              });
            }
            $( document ).ready( sortTable );
        </script></body></html>'''

def main():
    # todo: import 5 beets functions or all of beets if necessary
    # todo: write 4 helper functions: open file, run the method, compare results, write to html output

    # by this point we have imported all beets function necessary

    # walk the tree
    readFiles()

import importlib

def driverDefault(info):
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)
    # componentName = importlib.import_module(info[2])

    try:
        inFuncName = info[3]
    except: 
        inFuncName = "human_bytes"
    try:
        inInputVal = info[4]
    except:
        inInputVal = 1.0


    try:
        output = getattr(ui, inFuncName)(inInputVal)
    except TypeError as e:
        output = "TypeError"
    #except InputError:
    #    output = "InputError"
    except:
        output = "Error"
    return output


def readFiles():
    rootDir = '../testCases/'
    count = 0

    contents2 = '''<table border="1" style="width:100%"> 
            <tr> 
            <td>Test #</td>
                <td>Req. Tested</td>
                <td>Component Tested</td> 
                <td>Method Tested</td>
                <td>Test Inputs</td>
                <td>Expected Outcome</td>
                <td>Actual Outcome</td>
                <td>Pass</td>
            </tr>'''
    
    for filename in os.listdir(rootDir):
        infoLines = [0, 1, 2, 3, 4, 5, 6]
        N = 7
        f = open("../testCases/" + filename)
        for i in range(N):
            line = f.next().strip()
            infoLines[i] = line
            # print line
        infoList = parseFiles(infoLines)
        output = driverDefault(infoList)
        try:
            output = str(output)
        except:
            pass
        contents2 = report(infoList, contents2, output)
        f.close()
        
    browseLocal(contents1 + contents2 + contents3)    


       

    # for filename in os.listdir(rootDir):
    #    with open(os.path.join(rootDir, filename), "r") as f:
            # infoLines is an array populated by the first six lines of the testCase file
    #        infoLines = f.readlines()[0:7]
    #        infoLines = list(map(str.strip, infoLines))

    #        infoList = parseFiles(infoLines)
            # driverName = importlib.import_module(infoLines[6])
            # outputVal = getattr(drivers, driverName)(infoList)
    #        output = driverDefault(infoLines)
    #        f.close()


def parseFiles(inLineArray):
    # 1. test number or ID
    # 2. requirement being tested
    # 3. component being tested
    # 4. method being tested
    # 5. test input(s) including command-line argument(s)
    # 6. expected outcome(s)

    paren = '('
    comm = '#'
    quote = '"'
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
        inputVal = inLineArray[4]
        
    if '#' in inLineArray[5]:
        head, mid, tail = inLineArray[5].partition(comm)
    else:
        head = inLineArray[5]
    
    try:
        expectedVal = head.replace(quote, "")
        expectedVal = expectedVal.strip()
    except:
        print(head)
        expectedVal = "Test"

    try:
        driverName = inLineArray[6]
    except:
        driverName = defaultDriver

    returnVal = [inLineArray[0], inLineArray[1], componentName, funcName, inputVal, expectedVal, driverName]
    return returnVal


def compare(oracle, actualOutput):
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
    
    contents2 = contents2 + '''<tr> 
                    <td>''' + str(returnVal[0]) + '''</td>
                    <td>''' + str(returnVal[1]) + '''</td>
                    <td>''' + str(returnVal[2]) + '''</td> 
                    <td>''' + str(returnVal[3]) + '''</td>
                    <td>''' + str(returnVal[4]) + '''</td>
                    <td>''' + str(returnVal[5]) + '''</td>
                    <td>''' + str(outputVal) + '''</td>
                    <td>''' + str(compare(returnVal[5], outputVal)) + '''</td>
                </tr>'''
    return contents2

if __name__ == "__main__":
    main()
