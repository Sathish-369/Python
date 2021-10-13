import re

def match(text):
    pattern = "[Z-X]+[z-y]+$"
    if re.search(pattern, text):
             return ('Yes')
    else:
              return ('No')

    print(match("Sat"))
    print(match("satSat"))
    print(match("sat"))