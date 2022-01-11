# checksum_printer

Written by Bill Jones (December 2021)  
License:  CC-BY-NC  

This repository contains a Python script that allows you to get the checksums for files in a directory.  The script will print out the checksums in Terminal as well as produce a spreadsheet of filenames and checksum values.

Notice:  This script was tested on Python 3.7.9.  It may or may not work with older versions of Python.  You need to have Python installed in order to run this script.  To download Python, please visit [https://www.python.org/downloads/](https://www.python.org/downloads/).  You can check which version of Python you have installed by typing this into Terminal:

python -v

**Instructions:**

1. Download the checksum_printer.py file, or copy and paste the text into a text editor and save the file as checksum_printer.py
2. Open Terminal (on Mac) and navigate to the directory where you have the checksum_printer.py file saved
3. Locate the path of the directory that contains the file(s) that you want to have the checksum_printer.py act upon
4. Type the following in Terminal to run the script:

python3.7 checksum_printer.py "directory_of_file(s)_to_check"

Please note the use of double quotes around the directory in the line above.  The quotes allow for easy entry of a directory without having to escape whitespace typically found in directory paths.

After you press the Enter key, you will be presented with a message in Terminal letting you know that the process has started.  Terminal will then print out each filename and each associated checksum.  You will receive a confirmation message after the job is complete and a new .csv file will be made in the same directory as the checksum_printer.py file.  You can either retrieve the data from the spreadsheet, or you can copy and paste the checksum data from Terminal.

**Basic Linux Directory Navigation Hints:**

In Terminal, navigate to the folder that you want to check.  Use these commands to navigate (press Enter after typing command):
| Command | Description |
| :---------- | :------------------- |
| ls | List directory files |
| cd folder_name | Change Directory |
| cd ~/ | Start at user home directory |
| cd / | Start at root directory |
| cd .. | Go up a folder in current directory |
| pwd | Print working directory (this gives you your current directory) |

Use the TAB key to auto-complete filenames and directories
