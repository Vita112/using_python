## Basics
* 标识符
* 关键字：不可用于其他对象的标识符
```python
import keyword
print(keyword.kwlist)

```
* 表达式expression
    * 算数运算符：**幂运算，%取余数, //取整数商
    * 位运算符：~取反，&与，或|， <<左移，>>右移
    * 比较运算符：==， !=
    * 逻辑运算符:not非，and与，或or
```python
num = 123
num // 10  # 12
res = num//10%10  # 2
# 字符串比较：按照ASCII码值大小比较
3<4<7            # True
'abc' == 'xyz'   # False
4<3<7 != 2<7     # False
4<5<7 != 2<7     # False
# 位运算符
3-2 << 4   # 16



```
* 赋值语句assignment statement
    * 增量赋值：+=，%=
    * 链式赋值
    * 多重赋值

```python
x=3.5
z=3.5
z is x # False
c = 256
d = 257 
c is d #  True。因在python中相同的若干小整数 (-5,256)会被分配同一内存空间
y = x
y is x  # True
id(x)    # 2649498111248
id(z)   # 2649497472752
id(y)   # 2649498111248
```
* 语句和表达式
    * 语句：完成一个任务
    * 表达式：任务中一个具体的组成部分
* python 标准数据类型
    * 字符串
    * (长)整型；浮点型：数学中的实数，可用科学计数法表示；复数型
    * 布尔型
    * 列表，元组;字典:映射类型，类似于哈希表的键值对
```python
x=3+6j
x.real  # 实部
x.imag

```
* python中的函数、模块和包
    * 函数：完成一个特定功能的一段代码。
        * 内建函数。例如：abs();type();dir();open()
        * 标注库函数，导入模块即可使用
        * 第三方库 (包)，先安装库，再导入使用
        * 用户自定义函数
```python
dir(__builtins__)

# 导入包
# package:一个有层次的文件目录结构，定义了一个 由子包和模块组成的python应用程序执行环境
from torch.nn.functional import softmax
softmax()

# 导入模块
# 使用非内建函数，实现将 已有模块中函数的、类等的重用到其他代码块中；一个完整的.py文件即是一个模块。
import math   
dir(math)      # 查看模块中包含的函数
math.pi        # 输出pi值

# 提供与操作系统交互的函数
import os 
os.getcwd()     # 获取当前工作目录
os.chdir(path='./test')    # 更改当前工作目录



# 库(library):一组具有相关功能的模块的集合

```

* while循环和for循环
    * while expression
    * for iter_var in iterable_object:
        * iterable_object: string,list, tuple, dict, file; 
        * iterator是一种特殊的可迭代对象，在迭代到某个元素时才计算该元素。
        * range()返回一个iterable_object,string 也是一个iterable_object.
        * 判断对象是否为iterator 或者 iterable_object
    * break:终止整个循环，执行循环之后的语句
    * continue:停止当前该轮循环，重新进入循环
      
   
```python
from collections.abc import Iterator, Iterable
isinstance(range(10), Iterator)  # False
isinstance(iter(range(10)), Iterator)  # True
isinstance(range(10),Iterable)   # True

cnt = 0
i, j, k = 0, 0, 0
for i in range(21):
    for j in range(51):
        k = 100 - i*5 - j*2
        if k >= 0 :
            cnt += 1

print('counts=' , cnt)    

# break语句
sum_a = 0
i = 1
while True:
    sum_a += i
    i += 1
    if sum_a > 10:
        break 
# 输出2~100之间的素数: while循环
from math import sqrt
j = 2
while j <= 100:
    i = 2
    k = sqrt(j)
    while i <= k:
        if j%i ==0:
            break
        i += 1
    if i > k:
        print(j, end=' ')
    j += 1
    
# 输出2~100之间的素数: for循环
for j in range(2, 101):
    flag = 1
    k = int(sqrt(j))
    for i in range(2, k+1):
        if j%i == 0:
            flag = 0    # 用于标识能够被整除，即不是素数
            break
    if flag :              # 若flag=1，则为素数，输出素数
        print(j, end=' ')   
  
# 猜数字游戏
from random import randint

x = randint(0, 300)     
go = 'y'
while go == 'y':
    guess = int(input('Please input a number between 0~300: '))
    if guess == x:
        print('Bingo!')
        break
    elif guess < x:
        print('Too small, please try again.')
    else:
        print('Too large, please try again.')
    print('Input y if you want to continue.')
    go = input()
    print(go)
# 循环中的else的用法：若循环代码从break处终止，则跳出循环；
# 若正常结束循环==猜对，则执行else中的代码。
else:
    print('Goodbye')

```
* 自定义函数
    * 默认参数：需放在参数列表最后
    * 位置参数：按位置顺序赋值
    * 关键字参数: 允许调用者改变参数列表中的参数顺序。要么都显式使用关键字，要么都不用；否则会报错。
    * 传递函数：函数可以像 参数一样传递给另一个函数
    * lambda函数
```python
def add_me2me(x):
    return x+x
def self(f, y):
    print(f(y))

self(add_me2me, 2.2)

```
* 递归 
    * 逐层递归调用，逐层返回调用直到最初层
 ```python
def func(n):
    if n >= 2:
        func(n//2)
    print(n%2, end=' ')
 
 func(8)  # 1 0 0 0
 func(9)  # 1 0 0 1
```

* 变量作用域
    * 全局变量：位于程序代码主体部分
    * 局部变量：位于函数内部
若全局变量和局部变量同名，遵循**内层屏蔽外层**；程序设计时有个原则：模块内部聚合性强，与其他模块耦合性弱。



* 异常exception
python中每一个异常都是类的实例，使用异常对象exception object表示异常情况

```python
# 捕捉、处理异常，避免程序因为异常而终止运行。
# try-except  ->  外层套上循环  -> 接finally子句
while True:
    try:
        num1 = int(input('please enter the first number: '))
        num2 = int(input('please enter the second number: '))
        print(num1/num2)
        
    except ValueError:
        print("Input should be a digit!")
    except ZeroDivisionError:
        print('Second number cannot be zero!')
    
    else:          # 若无异常发生，则执行else子句
        break 
    # 或者选用接finally子句
    finally:
        print('It\'s over.')


```
* 通过 with语句使用 上下文管理器(context manager) 
定义和控制代码块执行前的准备动作，及执行后的收尾动作
