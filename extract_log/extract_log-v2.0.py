#!/usr/bin/env python
import datetime
import re

def makekey(line:str, CHARS=set(""" []"'""")):
    start = 0
    length = len(line)
    flag = False
    for i, char in enumerate(line):
        if char in CHARS:
            if char == '[':
                start = i + 1
                flag = True
            elif char == ']':
                flag = False
            elif char == '"':
                flag = not flag
                if flag: start = i + 1

            if flag: continue

            if start == i:
                start = i + 1
                continue

            yield line[start:i]
            start = i + 1

        else:
            if start == length:
                result.append(line[start:i])


names = ('remote', '', '', 'datetime', 'request', 'status', 'size', '', 'useragent')

ops = (None, None, None,
       lambda dstr: datetime.datetime.strptime(dstr, '%d/%b/%Y:%H:%M:%S %z'),
       lambda request: dict(zip(['method', 'url', 'protocol'], request.split())),
       int, int, None, None)

# def extract(line:str):
#     return dict(
#         map(
#             lambda triple: (triple[0], triple[1](triple[2]) if triple[1] else triple[2]),
#             zip(names, ops, makekey(line))
#         )
#     )

def extract(line:str):
    pattern = r'([\d.]{7,15}) \S+ \S+ \[(.*)\]\s+"([^"]*)" (\d+) (\d+) \S+ "([^"]+)"'
    regex = re.compile(pattern, re.S)
    matcher = regex.match(line)
    if matcher:
        print(matcher)
        print(line[matcher.start():matcher.end()])
        print(matcher.groups())

if __name__ == '__main__':

    line = '''114.249.235.230 - - [11/Apr/2017:10:49:51 +0800] "GET /path/to/file.py HTTP/1.1" 200 7635 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"'''

    # print(extract(line))
    extract(line)
