import re

def validityChecker(user):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, user):
        return True
    else:
        return False
   
user = input()
if not validityChecker(user): # Check Vaidity till the function turns True
    print('WRONG')
else:
    print('OK')
