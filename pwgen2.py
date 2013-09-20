#!/usr/bin/env python
import requests
import sys
import re
import argparse
import columnize

def assword(length=12):
    try:
        num = int(length)
        if num < 8 or num > 16:
            return "Number must be between 8 and 16"
        num = str(num)
    except:
        num = "16"
    payload = {'n': num}
    r = requests.post("http://p.assword.me/", data=payload)
    assword = re.search('h2>(.*)<\/h2', r.text).group(1).replace('<span>','').replace('</span>','')
    return assword

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='(P)assword generator based off http://p.assword.me.')

    parser.add_argument('iterations', metavar='N', type=int, default=1, help='Number of passwords to generate', nargs='?')
    parser.add_argument('-s', dest='length', type=int, default=12, help='Length of each password')

    args = parser.parse_args()
    asswords = []
    for n in xrange(0, args.iterations):
       asswords.append(assword(args.length)) 

    print(columnize.columnize(asswords, displaywidth=80))
