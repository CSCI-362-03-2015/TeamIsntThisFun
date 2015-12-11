# TeamIsntThisFun

Team IsntThisFun is working on project which is a collaborative effort to design and build an automated testing framework for our chosen Open Source Software project.

Malcolm Byrd- Programming / Design / Scripting

Zachary Davis - Linux and Scripting authority / Programming / Design

Kaitlyn Fulford - Testing / QA / Documentation / Programming / Design

Adam Sugmarman - Programming / Design / Scripting


###How-To Documentation

Prerequisites: Python 2.7+

The first step is to clone the TeamIsntThisFun repository. This is done using the command:

  “git clone https://github.com/CSCI-362-03-2015/TeamIsntThisFun.git“
  
You will need to add the scripts and reports modules to your Python site packages. To do this, open the terminal and type:   Python  
Import site  
>>>site.getsitepackages()[0]  
>>>This is the directory the modules go in   
You may need to edit permissions for this folder using Sudo chmod in order to add these files.
  
Afterwards, navigate to the top-level directory in the cloned repository /TeamIsntThisFun. The next step is to clone the repository located at Beets Github into the /project/src folder in the cloned TeamIsntThisFun repository. This is done using the command:

  “sudo git clone https://github.com/sampsyo/beets.git /project/src“

To run the automated testing framework navigate to the top-level directory /TeamIsntThisFun. (cd TeamIsntThisFun)

With these commands, “chmod +x ./scripts/runAllTests.py” and “./scripts/runAllTests.py”, the testing framework should execute automatically and output a test report in a web browser.

In order to test the faults, copy /TeamIsntThisFun/docs/__init__.py to /TeamIsntThisFun/project/src/beets/beets/ui and /TeamIsntThisFun/docs/hooks.py to /TeamIsntThisFun/project/src/beets/beets/autotag. These files in the docs directory have the faults in them, therefore once the files are copied into the correct directory (overwriting the other copies), the script may simply be ran as normal.
