#!/usr/bin/env python3
import sys
import urllib
import urllib.request
import re
from collections import Counter,OrderedDict



def help():
    """
    Display usage
    """
    print("Usage is: ./Mashael_Alabbad_hw6.py <file Input>")



def check():
    """
    Check for the file
    if there is no file call help function
    """
    if len(sys.argv) == 1:
        help()
        exit(1)
    else:
        url = sys.argv[1]
        return url



def getError(url):
    """
    Get all errors from URL
    """
    sourceFile = urllib.request.urlopen(url)
    content = sourceFile.read().decode()

    theList = re.findall(r'(?:\[.*?\]) (?:\[error\]) (?:\[.*?\]) (.*)', content)
    #Find the top 25 errors
    errors =OrderedDict(Counter(theList).most_common(25))

    print("*** Top 25 page errors ***")
    for page, value in errors.items():
        print('Count: {} Page: {}'.format(value, page))

    



# Main Function
def main():
    """
    Test Function.
    """
    url = check()
    getError(url)

# "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
