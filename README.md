# TeamIsntThisFun

Team IsntThisFun is working on project which is a collaborative effort to design and build an automated testing framework for our chosen Open Source Software project.

Malcolm Byrd- Programming / Design / Scripting

Zachary Davis - Linux and Scripting authority / Programming / Design

Kaitlyn Fulford - Testing / QA / Documentation / Programming / Design

Adam Sugmarman - Programming / Design / Scripting


###How-To Documentation

Prerequisites: Python 2.7+

1.) The first step is to clone the TeamIsntThisFun repository. This is done by typing the command:  
   "git clone https://github.com/CSCI-362-03-2015/TeamIsntThisFun.git" enter  
  
2.) You will need to add the scripts and reports modules to your Python site packages. To do this, type:   
Python  
Import site  
>>>site.getsitepackages()[0]  
>>>This is the directory the modules go in   
You may need to edit permissions for this folder using Sudo chmod in order to add these files.
  
3.) Afterwards, the next step is to navigate to the top-level directory in the cloned repository /TeamIsntThisFun and then clone the repository located at Beets Github into the /project/src folder in the cloned TeamIsntThisFun repository. This is done by typing the commands:
"cd TeamIsntThisFun"  enter  
"cd testAutomation"  enter  
"cd project"  enter  
"cd src"  enter  
"git clone https://github.com/sampsyo/beets.git"  enter  
"cd"  enter  

4.) To run the automated testing framework navigate to the top-level directory in /TeamIsntThisFun:   
"cd TeamIsntThisFun"  
"cd testAutomation"  

5.) Then, type: “./scripts/runAllTests.py”, the testing framework should execute automatically and output a test report in a web browser.

6.) In order to test the faults, copy /TeamIsntThisFun/docs/__init__.py to /TeamIsntThisFun/project/src/beets/beets/ui and /TeamIsntThisFun/docs/hooks.py to /TeamIsntThisFun/project/src/beets/beets/autotag. These files in the docs directory have the faults in them, therefore once the files are copied into the correct directory (overwriting the other copies), the script may simply be ran as normal.
