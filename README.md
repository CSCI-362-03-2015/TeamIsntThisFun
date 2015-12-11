# TeamIsntThisFun

Team IsntThisFun is working on project which is a collaborative effort to design and build an automated testing framework for our chosen Open Source Software project.

Malcolm Byrd- Programming / Design / Scripting

Zachary Davis - Linux and Scripting authority / Programming / Design

Kaitlyn Fulford - Testing / QA / Documentation / Programming / Design

Adam Sugmarman - Programming / Design / Scripting


###How-To Documentation

Prerequisites: Python 2.7+, Git, Ubuntu/Linux, pip

If pip is not installed, use the following commands:
>>>sudo apt-get install python-pip python-dev build-essential

>>>sudo pip install --upgrade pip

>>>sudo pip install --upgrade virtualenv


1.) The first step is to clone the TeamIsntThisFun repository. This is done by typing the command:  
>>>git clone https://github.com/CSCI-362-03-2015/TeamIsntThisFun.git

2.) Afterwards, the next step is to navigate to the top-level directory in the cloned repository /TeamIsntThisFun and then clone the repository located at Beets Github into the /project/src folder in the cloned TeamIsntThisFun repository. These steps are done by typing the commands:  
>>>cd TeamIsntThisFun/testAutomation/project/src

>>>git clone https://github.com/sampsyo/beets.git

3.) Then the files must be added to the python site packages folder. In order to do this, use the following command.

>>>sudo pip install beets

and then navigate to the /TeamIsntThisFun/testAutomation directory using the command
>>>cd ..

until the current directory is /TeamIsntThisFun/testAutomation. Then use the commands:
>>>pwd

This is PATH1.
>>>python

>>>import site

>>>site.getsitepackages()[0] 

This is PATH2.

and replace PATH1 and PATH2 in the next command with the returned paths.
>>>sudo cp -r PATH1/scripts PATH2

>>>sudo cp -r PATH1/drivers PATH2

>>>sudo cp -r PATH1/project/src/beets/beets PATH2

PATH2 may need to be given permissions in order to be copied into.

4.) To run the automated testing framework use the commands:   
>>>chmod +x ./scripts/runAllTests.py

>>>./scripts/runAllTests.py

The testing framework should execute automatically and output a test report in a web browser.

5.) In order to test the faults, use these commands:
copy /TeamIsntThisFun/docs/__init__.py to /TeamIsntThisFun/project/src/beets/beets/ui and /TeamIsntThisFun/docs/hooks.py to /TeamIsntThisFun/project/src/beets/beets/autotag. These files in the docs directory have the faults in them, therefore once the files are copied into the correct directory (overwriting the other copies), the script may simply be ran as normal.
