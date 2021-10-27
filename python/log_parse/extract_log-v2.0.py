#!/usr/bin/env python
import datetime
import re
from user_agents import parse


ops = {
    'datetime':lambda dstr: datetime.datetime.strptime(dstr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int, 'size':int
}

def extract(line:str):
    pattern = r'(?P<remote>[\d.]{7,15}) \S+ \S+ \[(?P<datetime>.*)\]\s+"(?P<method>[^" ]*) (?P<url>[^" ]*) (?P<protocol>[^" ]*)" ' \
              r'(?P<status>\d+) (?P<size>\d+) \S+ "(?P<useragent>[^"]+)"'
    regex = re.compile(pattern, re.S)
    matcher = regex.match(line)
    if matcher:
        # print(matcher)
        # print(line[matcher.start():matcher.end()])
        # print(matcher.groups())
        # print(matcher.groupdict())
        return {k:ops.get(k, lambda x:x)(v) for k, v in matcher.groupdict().items()}
    else:
        return line

def load(filename:str):
    with open(filename, encoding='utf8') as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('No match: {}'.format(fields))

if __name__ == '__main__':

    line = '''114.249.235.230 - - [11/Apr/2017:10:49:51 +0800] "GET /path/to/file.py HTTP/1.1" 200 7635 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"'''

    # print(extract(line))
    # extract(line)
    # for x in load('test.log'):
    #     print(x)

    uastr = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    print(uastr)

    ua = parse(uastr)
    print(ua, type(ua))
    print(ua.browser)
    print(ua.browser.family, ua.browser.version_string)