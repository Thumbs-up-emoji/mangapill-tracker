#if url- store, if number- update using new url, if blank- check all from db
import sys
from urllib.parse import urlparse
from url import parse_url,update
from next import next_check

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg.isdigit():
        # Code to handle when the argument is a number
        print("Enter last read url")
        url=input()
        if urlparse(url).scheme:
        # The input is a URL
            update(url, 'db.csv')
        else:
            print("Error: Enter a valid URL.")
        # chapter number as input
    elif urlparse(arg).scheme:
        # Code to handle when the argument is a URL
        parse_url(arg, 'db.csv')
    else:
        # Code to handle when the argument is neither a number nor a URL
        print("Error: Enter valid URL or manga no.")
else:
    # Code to handle when no argument is provided
    next_check('db.csv')
    pass