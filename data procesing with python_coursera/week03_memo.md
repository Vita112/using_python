# why need dictionary?
建立对象之间的映射关系，key-value对
* 创建字典
```python
dic = {}.fromkeys(('Wangdachui', 'Zhangsan','Lisi'), 3000)   # 设置默认值均为3000

dict(zip(lst1, lst2))   # 从列表中生成字典

```

* 使用字典

键值查找、vulue重新赋值、键值对添加、key是否存在、删除

字典内建函数和方法
```python
dic['wangdachui']=4000
dic['fuyun']=1000
'mayun' in dic
del dic['fuyun']

dic.keys()
dic.values()
for k,v in dic.items():
    print(k,v)

dic.get('a_key')   # key不存在时，返回None
# 删除字典
a_dict = {"AXP":78.5, "BA": 184.1}
b_dict = a_dict
a_dict.clear()  # b_dict将同时被清空

# 字典通过key来确定成员
a_dict.pop('AXP')


# 将json加载为字典
import json
data = json.load(file_path)

```
# set:  无序不重复元素
* set 和 frozenset
* 集合比较
```python
a_set = set('sunrise')
b_set = set('sunset')

a_set < b_set  # False
a_set & b_set  # 's', 'u', 'n', 'e'
a_set - b_set  # 'i', 'r'  属于a不属于b   == a_set.difference(b_set)
a_set ^ b_set  # 'i', 'r' , 't'  a, b中出去交的元素

```
# 字典、集合编程示例
```python
# 1 统计英文单词词频
text = 'Life can be good, Life can be sad, Life is mostly cheerful, But sometimes sad.'

words = text.split()
freq_dict = dict()
for item in words:
    if item[-1] in ",.\?'":
        item = item[:-1]
    freq_dict[item] = freq_dict.get(item, 0) + 1  
    # 若word在dict中第一次出现，则返回0+1；若已存在于dict中，则返回dict中对应的值，并+1.
    
# 2 各班级参加运动会人数统计排序
def func(lst):
    info_dict = {}
    for line in lst:
        cls,stu_num = line.split('_')[0], line.split('_')[1].strip()
        if cls not in info_dict:
            info_dict[cls] = [stu_num]
        else:
            info_dict[cls] += [stu_num]
    # 基于值的个数逆序排列
    sorted(info_dict.items(), key=lambda info_dict: len(info_dict[1]), reverse=True)
    return info_dict 


if __name__ == '__main__':
    try:
        with open(file) as f:
            info_list = f.readlines()
    except FileNotFoundError:
        print('file not found!')
    else:
        result = func(info_list)
        for cls, num in result.items():
            print(cls, "->", num)
'''
A1 -> ['12', '13', '30']
A2 -> ['01', '10']
A4 -> ['09', '12', '15', '12']
A3 -> ['12']
'''   

# 3 生成符合要求的学号
# 给定data={"A001":34, "A002":47, "B001":35, "B001":42}, 编写函数func随机选择班级，并生成一个学号 (学号不可以超过总人数)；
# 在__main__模块中给定data，调用func()生成10个不重复学生学号
import random

def func(data):
    cls_no = random.choice(list(data.keys()))
    stu_no = random.randint(1, data[cls_no])
    return f'{cls_no} {stu_no:02}'
    



if __name__ == "__main__":
    data={"A001":34, "A002":47, "B001":35, "B001":42}
    result = set()
    while len(result) < 10:
        result.add(func(data))
    print(result)

```

      
