#if url- store, if number- update using new url, if blank- check all from db
import sys
from urllib.parse import urlparse
import os
from url import update
from next import next_check
from print import print_all

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'db.csv')

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if urlparse(arg).scheme:
        # Code to handle when the argument is a URL
        update(arg, db_path)
    elif arg=='p':    
        print_all(db_path)
    else:
        # Code to handle when the argument is neither a number nor a URL
        print("Error: Enter valid URL or manga no.")
else:
    # Code to handle when no argument is provided
    next_check(db_path)
    pass