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
        * 第三方库，先安装库，再导入使用
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
math.pi

# 库(library):一组具有相关功能的模块的集合





```