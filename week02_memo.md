# 1. 本地文件操作

```python
import  os
import shutil

def count_lines(file):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print(f'{file} is not found.')

path = '.'
for file in os.listdir(path):
    if file.endswith('.txt'):
        print(file)
        file_path = os.path.join(path, file)
        print(file_path)
        count_lines(file_path)
        
        if os.path.exists('test'):
            shutil.rmtree('test')
            os.mkdir('test_mk')

```

# 2. 获取网页内容
* 抓取数据，使用Requests第三方库
* 解析
    * 使用BeautifulSoup库，一个可以从HTML或XML文件中提取数据的python库。有4种对象：
        * Tag: e.g. <b>some strings</b>
        * NavigatableString: Tag中的字符串
        * BeautifulSoup
        * Comment: Navigatable的一个子类
    * re模块，处理正则表达式。测试网站:regex101.com。pycharm中的txt阅读器也支持
    

```python
import requests

re = requests.get('https://www.coursera.org/learn/hipython/lecture/TUHOm/1-ben-di-shu-ju-huo-qu')
re.status_code    # 200:抓取成功; 

# 418:该网站添加了反爬虫程序识别，爬取未成功，为此，在请求头中加入一些信息,代码如下：
url = 'https://book.douban.com/subject/1084336/comments/'
# 浏览器中输入 about:version
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
response = requests.get(url=url, headers=head)

from bs4 import BeautifulSoup
import lxml

markup = '<p class="title"><b>The Little Prince</b></p>'
soup = BeautifulSoup(markup, 'lxml')

# 提取网页中的评论信息：
soup_text = BeautifulSoup(response.text, 'lxml')
pattern = soup_text.find_all('span','short')
for item in pattern:
    print(item.string)

```
# 3. 数据表示
* python中有6种序列：string，list，tuple，tList;序列对象可迭代；索引与切片

常见函数：enumerate(), reversed(), sorted(), sum(), zip()
* string

常用方法：format(), isalpha(), join(), find(), strip(), replace(), split(), startswith()
* list

常用方法：append(), copy(), count(), extend(), insert(), pop(), sort()
    
    可扩展的容器对象，和字典一起构成python的两大主要容器。
    * 列表元素可更改。list1.extend(list2):合并两个list中的元素
    * num_list.sort(reverse=True): 逆序排列；str_list.sort(key=len):按照字符长度进行升序排列
    
* tuple: not support item assignment 

```python
[x**2 for x in range(10) if x**2 < 50]
[(x+1, y+2) for x in range(10) for y in range(10)]

def clean_list(list):
    cleaned_list = []
    for item in list:
        for c in item:            
            if c.isalpha() != True:  # 非字母
                item = item.replace(c,'')
        cleaned_list.append(item)
    return cleaned_list                
raw_list = ['32Latte', '_Americano30', '/34Cappuccino','Mocha35']
res = clean_list(raw_list)
for k, v in zip(range(1, len(res)+1), res):
    print(k, v)
    
    
```
# 4. 函数式编程主要由 3个基本函数 + 1个算子operator构成
* map()：接收一个函数和list，将函数逐一映射到list中的每个元素上
* reduce()
* filter()
* lambda

```python
from functools import reduce

lst = [2, 3, 4, 5, 6]
list(map(lambda x: x**2, lst))
list(filter(lambda x: x%2 == 0, lst))    #返回满足lambda函数的元素 
reduce(lambda x, y: x+y,lst)    # 20 == 元素之和
lst_str = ['abc', 'xyz']
list(map(lambda char:char.upper(), lst_str))

```

# 5. 可变可迭代对象修改问题解释
* python中的浅拷贝，在使用第三方库时需要注意，关系到是否会修改原始对象，或原始对象中的某些对象
```python
x = [1,2,3,4,5,6]
y = x
y[0] = 10   
# 此时x[0]也会被修改，因为y和x使用的是 同一块内存空间，再看如下一个例子：
lst = [1,3,4,6,8,7]
for num in lst:
    if num%2 == 0:
        lst.remove(num)
print(lst)   # [1,3,6,7]，6被留下来是由于指针移动造成的，当remove 4时，6会向前移动，索引也由原来的3变为2，但for循环的索引是3
# 解决方案：使用浅拷贝，如 lst[:] or lst.copy()
# 但是浅拷贝只复制了一级对象，二级对象仍然指向了原来的内存空间，因而会被同时修改，以下是例子：
x = [1,2,[3,4]]
z = x.copy()
z[0], z[2][0] = 9,9 
print(x)   #[1, 2, [9, 4]]

# 引入copy模块
import copy
z = copy.deepcopy(x)
z[0],z[2][0] = 8, 8
print(z)  # [8, 2, [8, 4]]
print(x)  # [1, 2, [9, 4]]



```