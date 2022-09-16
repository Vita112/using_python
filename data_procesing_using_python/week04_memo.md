# 1. Python便捷数据获取与预处理
## 1.1 便捷数据获取
* 从网页下载数据，比如yahoo财经网站中下载股票历史数据
利用 一般统计分析方法，或机器学习模型
```python
import pandas as pd
# 读取csv文件为DataFrame
df_test = pd.read_csv('AXP.csv')
# read_excel(sheet_name=)

# 读取excel文件内容为dataframe，添加字段sum= python_score + math_score
# 将更新后的df写入students.xlsx文件的scores工作表中。
df = pd.read_excel('week04_practice.xlsx')

```
* 利用API获取已清洗过的数据，而不是网页源代码

使用pandas-datareader进行remote data access

```python
import pandas_datareader.data as web

f = web.DataReader('^DJI', 'stooq')
f.head(5)

```

* 使用机器学习库中自带的数据集和语料

    * sklearn

    * nltk中包含 gutenberg，reuters，brown等
```python
from sklearn import datasets

dir(datasets)
iris = datasets.load_iris()
iris.data
iris.feature_names
iris.data.shape


# 下载nltk中的语料库
from nltk.corpus import gutenberg
import nltk

nltk.download('gutenberg')

print(gutenberg.fileids())

```
## 1.2 Python绘图基础
* pyplot模块是用于绘图的API。著名的Python绘图库有Matplotlib，用于二维绘图
```python
import matplotlib.pyplot as plt

# list_x, list_y
plt.plot([3,4,7,6,2,8,9])  # 此处list_x被省略
plt.savefig('image.jpg')
plt.show()

# 绘制多组数据
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 4., 0.1)
# 多组数据的折线图
plt.plot(t,t,t,t+2,t,t**2)   # 三条曲线在同一个图中
# 绘制散点图和柱状图
plt.scatter(range(7),[2,4,3,7,4,6,9])
plt.bar(range(7), [2,4,3,7,4,6,9])


# 设置统计图的颜色、线型和标记
plt.figure(figsize=(8,6), dpi=100)
plt.plot(t,t,'r--', label='line1')   # 红色虚线
plt.plot(t,t+3, color='green', linestyle='',marker='*',linewidth=3,label='line2')
plt.plot(t,t**2, color='blue', marker='+',label='line3')
plt.legend(loc='upper left')   # 图例显示位置，显示内容为labels

```
* 绘制子图：plt.subplot()
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi,300)
plt.figure(1)
plt.subplot(211)      # 子图为两行一列，第一个图
plt.plot(x, np.sin(x), color='r')
plt.subplot(212)       # 第二个图
plt.plot(x, np.cos(x), color='g')
plt.show()

```
* pandas 绘图
```python
import pandas as pd

df = pd.DataFrame(data)
ax = df.loc[:9,['column1', 'column4']].plot(kind='bar',x='',y='',color='')   # index从0到9的 第1列和第4列的数据
ax.set(ylable='', title='')

```

* 其他绘图工具：seaborn

## 1.3 数据预处理：探索和清洗
检查数据错误，了解数据分布特征和内在规律。

一般直接采集到的数据有如下问题：**不完整，某项缺失；噪声；维数太高；单位不统一**
* 缺失值和异常值处理
    * 缺失值如何处理？--> 
    删除，填充：固定值、均值、中位数或众数、缺失值上下的数据、插值函数、最近邻或回归方法建模计算最可能的值
    * 异常值如何观察？ --> 
    数值明显偏离其他观测值的点。可通过简单统计、绘图、基于密度/最近邻和/聚类等方法进行观察
    * 异常值如何处理？-->
    方法可参考缺失值处理方法；局部均值方法 (分箱)；不处理
```python
import pandas as pd

df = pd.read_csv('data_procesing_using_python/AXP.csv',index_col='Date')   # index_col:指定某列为列索引
df.isnull()  # NaN显示为True
df.fillna(df.mean(), inplace=True)  # 缺失值填充，直接在df上更改
df.dropna()  # 删除缺失值，默认按行删除，只要该行中存在NaN即删除。

# 观察异常值
df.describe()   #描述数据统计信息
df.loc['2022/9/15'] = [6,200,2,35,4]  # 手动增加一行异常值
df.drop('Adj Close','Volume', axis=1).boxplot()   # 使用箱型图进行异常值点的判断
df[abs(df-df.mean()) > 3*df.std()]   # 3σ方法：若该值小于μ-3σ，或大于μ+3σ，称其是异常值。使用dataframe的bool索引来筛选数据


```
* 数据集成 Data Integration

* 数据变换 Data Transformation

* 数据规约 Data Reduction


# 2. Python数据统计挖掘与应用

