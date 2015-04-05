#! /usr/bin/python3

import hashlib, argparse

parser=argparse.ArgumentParser(description='a tool to check hash')
parser.add_argument('string',help='the string to be calculated')
parser.add_argument('-a','--algorithm',default='md5',help='the algorithm to be used, default is md5. Supported algorithms are '+str(hashlib.algorithms_available))
parser.add_argument('-f','--file',action='store_true',default=False,help='treat string as file name')
arguments=parser.parse_args()

if not arguments.algorithm in hashlib.algorithms_available:
    print('unsupported algorithm '+arguments.algorithm)
else:
    calculator=hashlib.new(arguments.algorithm)

if arguments.file :
    with open(arguments.string,'rb') as f:
        while True:
            data=f.read(10240)
            if data :
                calculator.update(data)
            else:
                break
else:
    calculator.update(arguments.string.encode())

print(calculator.hexdigest().upper())
