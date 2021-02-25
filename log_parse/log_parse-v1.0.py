#!/usr/bin/env python
import re
import time
import datetime
import random
from queue import Queue
import threading
from pathlib import Path

from user_agents import parse


# 模拟数据生成者
def source(seconds=1):
    '''
    :param seconds:
    :return: 返回时间与一个随机数字
    '''
    while True:
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
               'value': random.randint(1, 100)}
        time.sleep(seconds)


# 数据处理函数
def avg_handler(iterable):
    '''
    计算平均值
    :param iterable:
    :return:
    '''
    return sum(map(lambda item: item['value'], iterable)) / len(iterable)

# 测试函数
def donothing_handler(iterable):
    return iterable

# 状态码分析
def status_handler(iterable:list): # 指一段时间内的数据
    status = dict()
    for item in iterable:
        key = item['status']
        status[key] = status.get(key, 0) + 1
    total = len(iterable)
    return {k:v/total for k, v in status.items()}


# 浏览器分析
all_browser = dict()
def browser_handler(iterable:list):
    browsers = {}
    for item in iterable:
        uastr = item['useragent']
        ua = parse(uastr)

        key = ua.browser.family, ua.browser.version_string
        browsers[key] = browsers.get(key, 0) + 1
        all_browser[key] = all_browser.get(key, 0) + 1

    return browsers


# 滑动窗口控制器
def window(q: Queue, handler, width: int, interval: int):
    buffer = list()
    current = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    # start = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    start = current
    delta = datetime.timedelta(seconds=width - interval)
    while True:
        data = q.get()  # next(iterator)
        if data:
            buffer.append(data)
            current = data['datetime']
        # print(current, start)

        if (current - start).total_seconds() > interval:
            # print('=' * 60)
            # print('Average: {:.2f}'.format(handler(buffer)))
            print('{}'.format(handler(buffer)))
            # print(threading.current_thread())
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
            # data = next(src)
            for data in src:
                for q in queues:
                    q.put(data)

            print('='*60)

            while True:
                cmd = input('>>>')
                if cmd == 'plot':
                    print(all_browser)

                    new_all_browser = {}
                    for (k, ver), val in all_browser.items():
                        new_all_browser[k] = new_all_browser.get(k, 0) + val

                    # print(sorted(new_all_browser.items(), key=lambda item: item[1], reverse=True))

                    from pandas import Series
                    import matplotlib


                    s = Series(new_all_browser)
                    s = s.sort_values(ascending=False)
                    print(s)
                    # s.plot()    # 画图
                    # matplotlib.pyplot.show()


    return reg, run


ops = {
    'datetime': lambda dstr: datetime.datetime.strptime(dstr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int, 'size': int
}


def extract(line: str):
    pattern = r'(?P<remote>[\d.]{7,15}) \S+ \S+ \[(?P<datetime>.*)\]\s+"(?P<method>[^" ]*) (?P<url>[^" ]*) (?P<protocol>[^" ]*)" ' \
              r'(?P<status>\d+) (?P<size>\d+) \S+ "(?P<useragent>[^"]+)"'
    regex = re.compile(pattern, re.S)
    matcher = regex.match(line)
    # return matcher
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
    else:
        return line


# 装载数据
def load_file(filename, encoding='utf-8'):
    # filename = str(filename)
    # with open(filename, encoding=encoding, newline=newline) as f:
    with filename.open(encoding=encoding) as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('No match: {}'.format(fields))


def load(*paths, ext='*.log,*.txt', recursion=False):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            if isinstance(ext, str):
                ext = ext.split(',')
                # print(ext)
            for e in ext:
                files = path.rglob(e) if recursion else path.glob(e)
                for file in files:
                    yield from load_file(file.absolute())
        elif path.is_file():
            yield from load_file(path.absolute())
        else:
            print('File error!')


if __name__ == '__main__':

    src = load('.')
    # print(type(src))
    # for x in src:
    #     print(x)
    reg, run = dispatcher(src)
    # reg(donothing_handler, 10, 5) # 注册处理函数
    reg(status_handler, 10, 5) # 注册处理函数
    reg(browser_handler, 10, 10) # 注册处理函数
    run()   # 运行
    # print(all_browser)

    # reg(donothing_handler, 10, 5) # 注册处理函数