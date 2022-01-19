#生成器
import sys


def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, count = 0, 1, 0
    while True:
        if (count > n) :
            return
        yield a
        a, b = b, a + b
        count += 1

f = fibonacci(10)

while True:
    try:
        print(next(f), end= ' ')
    except StopIteration:
        sys.exit()