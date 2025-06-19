#if url- store, if number- update using new url, if blank- check all from db
import sys
from urllib.parse import urlparse
from url import update
from next import next_check
from print import print_all

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if urlparse(arg).scheme:
        # Code to handle when the argument is a URL
        update(arg, 'db.csv')
    elif arg=='p':    
        print_all('db.csv')
    else:
        # Code to handle when the argument is neither a number nor a URL
        print("Error: Enter valid URL or manga no.")
else:
    # Code to handle when no argument is provided
    next_check('db.csv')
    pass