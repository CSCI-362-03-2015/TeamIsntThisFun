# Team 'Isn't This Fun' 
# Zach Davis, Ben Byrd, Kaitlyn Fulford, Adam Sugarman

# This script lists the contents in its containing directory in an HTML file in the browser.

ls > directoryOutput.html           #list top level-directory contents and redirect the to a html file directoryOutput.html
xdg-open directoryOutput.html &     #open the directoryOutput.html file (without causing the terminal to wait)
