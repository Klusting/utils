#! /usr/bin/python3

import sys

string=sys.argv[1]
for ch in string:
    print(ch)
    print(ch.encode('utf8'))
    for i in ch.encode('utf8'):
        print(oct(i))
