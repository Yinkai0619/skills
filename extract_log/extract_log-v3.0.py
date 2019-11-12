#!/usr/bin/env python
import re
import time
import datetime
import random
from queue import Queue
import threading

# 模拟数据生成者
def source(seconds=1):
    '''
    :param seconds:
    :return: 返回时间与一个随机数字
    '''
    while True:
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))), 'value': random.randint(1, 100)}
        time.sleep(seconds)


# 数据处理函数
def avg_handler(iterable):
    '''
    计算平均值
    :param iterable:
    :return:
    '''
    return sum(map(lambda item: item['value'], iterable)) / len(iterable)


# 滑动窗口控制器
def window(q:Queue, handler, width:int, interval:int):
    buffer = list()
    current = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    # start = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    start = current
    delta = datetime.timedelta(seconds = width - interval)
    while True:
        data = q.get() #next(iterator)
        if data:
            buffer.append(data)
            current = data['datetime']
        print(current, start)

        if (current - start).total_seconds() > interval:
            print('='*60)
            print('Average: {:.2f}'.format(handler(buffer)))
            print(threading.current_thread())
            start = current

        # 清除过期数据
        # print('length of buffer: ', len(buffer))
        buffer = [x for x in buffer if x['datetime'] > current - delta]


# 注册和分发器，决定着数据的调度
def dispatcher(src):
    queues = list()
    threads = list()

    def reg(handler, width, interval):
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))

        queues.append(q)
        threads.append(t)

    def run():
        for t in threads:
            t.start()

        while True:
            data = next(src)
            for q in queues:
                q.put(data)

    return reg, run

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
        return {k:ops.get(k, lambda x:x)(v) for k, v in matcher.groupdict().items()}
    else:
        return line

# 装载数据
def load(filename:str):
    with open(filename, encoding='utf8') as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('No match: {}'.format(fields))

if __name__ == '__main__':

    s = source()
    reg, run = dispatcher(s)
    reg(avg_handler, 10, 5)
    print(threading.current_thread())
    run()
    line = '''114.249.235.230 - - [11/Apr/2017:10:49:51 +0800] "GET /path/to/file.py HTTP/1.1" 200 7635 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"'''

    # print(extract(line))
    # extract(line)
    for x in load('test.log'):
        print(x)
