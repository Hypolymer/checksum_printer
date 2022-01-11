import glob
import hashlib
import csv
import sys
import os

from datetime import datetime
today = datetime.today().strftime('%Y%m%d' + '_' + '%H%M%S')
counter = 0

# To run this script, type:  python3.7 checksum_printer.py [directory of folder]

# This is the path to the directory:
input_path = sys.argv[1] + "/*"
# IMPORTANT: When you paste in the directory name in Terminal as the second argument, you need to make sure you escape whitespace with a backslash for the directory name.
# This means that '/Users/jonesw/Desktop/MP3 Audio Merged Kimball' turns into '/Users/jonesw/Desktop/MP3\ Audio\ Merged\ Kimball'
# If it's a longer directory name, you can just wrap it in double quotes like "/Users/jonesw/Desktop/MP3 Audio Merged Kimball"

print("Starting MD5 checksum scan of directory: " + input_path)

#https://stackoverflow.com/questions/36099331/how-to-grab-all-files-in-a-folder-and-get-their-md5-hash-in-python?noredirect=1&lq=1

filenames = glob.glob(input_path)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

with open('md5_checksum_' + today + '.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for filename in filenames:
        print(filename, md5(filename))
        spamwriter.writerow([filename,os.path.basename(filename), md5(filename)])
        counter = counter + 1
print("Success!")
print("MD5 Checksums produced for " + f"{counter:,}" + " records!")
