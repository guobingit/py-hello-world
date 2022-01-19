#斐波纳契数列
a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b
print()

#条件控制
c = 100
if c==1:
    print(1)
elif c==2:
    print(2)
else:
    print(4)

#循环语句
n = 1
while n < 100:
    n +=1
    print(n, end=",")
print()

#迭代器
list = [1,2,3,4]
it = iter(list)
print(next(it), end=',')
print(next(it))


