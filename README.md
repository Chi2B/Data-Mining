

# 实验一《多源数据集成、清洗和统计》

##  小组信息

+ 组员信息：陈泽彬（有组但单干）
+ 组员分工：陈泽彬
+ 指导老师：彭伟龙

## 作业题目和内容

### **题目**

广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在Excel中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java/Python程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

- Excel表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。
- txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。

### **参考**

一.数据源1.xlsx

| ID   | Name  | City     | Gender | Height | C1   | ...  | C10  | Constitution |
| ---- | ----- | -------- | ------ | ------ | ---- | ---- | ---- | ------------ |
| 1    | Marks | Shenzhen | boy    | 166    | 77   |      |      | general      |
| 2    | Wayne | Shenzhen | girl   | 159    | 77   |      |      | good         |
| ...  | ...   | ...      | ...    | ...    | ...  | ...  | ...  | ...          |



一.数据源2-逗号间隔.txt

ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution
202001,Marks,Shenzhen,male,1.66,77,100,84,71,91,6,7,6,8,,general

### 实验内容

两个数据源合并后读入内存，并统计：

1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

### **提示**

参考数据结构：

Student{

int id;

string id;

vector<float> data;

}



可能用到的公式：

| 均值公式             | ![img](https://github.com/Chi2B/Image/blob/main/1.jpg?raw=true) |
| :------------------- | :----------------------------------------------------------: |
| 协方差公式           | ![img](https://github.com/Chi2B/Image/blob/main/2.jpg?raw=true) |
| z-score规范化        | ![img](https://github.com/Chi2B/Image/blob/main/3.jpg?raw=true) |
| 数组A和数组B的相关性 | ![img](https://github.com/Chi2B/Image/blob/main/4.jpg?raw=true)<br/>**这里A=[a1, a2,...ak,..., an],B=[b1, b2,...bk,..., bn]<br/>mean(A)代表A中元素的平均值std是标准差，即对协方差的开平方.<br/>点乘的定义：**![img](https://github.com/Chi2B/Image/blob/main/5.jpg?raw=true) |

注意：计算部分不能调用库函数；画图/可视化显示可以用可视化API或工具实现。

## 作业环境

+ Windows10

+ Anaconda Python3.6（IDE为pycharm）

### 文件说明

+ 「main.py」是源代码

+ 「一.数据源1.xlsx」是数据源1

+ 「一.数据源2-逗号间隔.txt」是数据源2

+ 「运行结果截图.jpg」是运行结果
  + 输出合并后数据源
  + 输出学生中家乡在Beijing的所有课程的**平均成绩**
  + 输出学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的**数量**
  + 输出比较广州和上海两地女生的平均体能测试成绩并判断哪个地区的更强些
  + 输出学习成绩和体能测试成绩两者的**相关性**



运算结果截图.jpg：

![img](https://github.com/Chi2B/Image/blob/main/%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C%E6%88%AA%E5%9B%BE.jpg?raw=true)

### 函数说明

#### 平均数函数

```python
def AVG(df):
    C_avg = sum(df)/len(df)
    C_avg = float('%0.1f' %C_avg)    # 设置精度
    return(C_avg)
```

输入类型可为numpy.ndarray，结果输出float类型的一个平均数

结果不希望要那么多小数点于是设置了精度，保留一位小数

#### 标准差函数

```python
def STD(df):
    sum = 0
    for j in df:
        sum = sum + pow(j-AVG(df),2)
    return pow(sum/(len(df)-1),0.5)
```

输入类型可为numpy.ndarray，结果输出float类型的一个标准差，其中调用了AVG（df）平均数函数

#### 相关系数函数

```python
def CORRELATION(df1,df2):
    STD_df1df2 = sum([(i - AVG(df1)) * (j - AVG(df2)) for i, j in zip(df1, df2)])/(len(df1)-1)
    return STD_df1df2/(STD(df1)*STD(df2))
```

输入类型可为numpy.ndarray，结果输出float类型的一个相关系数，其中调用了AVG（df）平均数函数、STD（df）标准差函数

### 调用的函数库以及涉及哪些技术

#### 函数库

+ pandas

#### 涉及的技术

| 调用的函数                       | 函数说明                                                     |
| -------------------------------- | ------------------------------------------------------------ |
| panda.set_option                 | 用于设置dataframe的输出显示                                  |
| pandas.read_excel                | 将Excel文件读入pandas数据框                                  |
| pandas.DataFrame.drop_duplicates | 返回删除了重复行的DataFrame                                  |
| pandas.DataFrame.to_numpy        | 将DataFrame转换为NumPy数组                                   |
| pandas.DataFrame.replace         | 将DataFrame的值动态替换为其他值                              |
| pandas.Series.map                | 用于将Series中的每个值替换为可以从函数、字典或Series获取的数据 |
| pandas.read_csv                  | 将逗号分隔值（csv）文件读取到DataFrame中                     |
| pandas.DataFrame                 | 做一个复制此对象的索引和数据                                 |
| pandas.concat                    | 将pandas对象与其他轴上的可选集合逻辑连接起来                 |
| pandas.DataFrame.merge           | 使用数据库的样式联接合并DataFrame或命名的Series对象（取交集） |
| pandas.DataFrame.combine_first   | 通过将一个DataFrame中的空值与其他DataFrame中的非空值一起填充来组合两个DataFrame对象。所得DataFrame的行索引和列索引将是两者的并集 |
| pandas.DataFrame.sort_values     | 沿任一轴的值排序                                             |
| pandas.DataFrame.fillna          | 使用指定的方法填充NA /  NaN值                                |

## 难题与解决

前言：非常惭愧做本次实验基本是从0开始，除了理解实验要求不是难题，其余一切代码实现几乎都是难题，无论是简单的导入还是复杂的清洗、合并、查询，都花费了大量的时间和精力用于各种百度上，也从中收集了一些个人认为很不错的文章，同时也在源代码中做好了标记，下面会根据标记处所遇到的问题以及解决办法罗列在下方，今后一定洗心革面好好学习天天向上

### *1

#### [\# Numpy的基础知识](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402378855&idx=1&sn=77ed3c403aa00977e66a6d712b565f44&scene=21#wechat_redirect)

#### [# Panda的基础知识](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402568021&idx=1&sn=66d5234a31f2de640baa71439f856a33&scene=21#wechat_redirect)

### *2

#### [\# 数据导入](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402829681&idx=1&sn=3042132921889b2b5414fff28513b05b&scene=21#wechat_redirect)

#### [\# .drop_duplicates 用法说明](https://www.cnblogs.com/yaos/p/9837448.html)

#### [\# SettingwithCopyWarning（不加.copy()会报警告的原因）](https://blog.csdn.net/xiaofeixia666888/article/details/106807181)

### *3

#### [\# Pandas中把数据格式（df,array）的相互转换](https://blog.csdn.net/weixin_43708040/article/details/87275815)

#### [\# numpy对象折叠成一维的数组1](https://blog.csdn.net/likeyou1314918273/article/details/89735607)

#### [\# numpy对象折叠成一维的数组2](https://www.pythonheidong.com/blog/article/430164/3f1749c78e817b2d3ec0/)

#### [\# 替换异常值](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313425&idx=1&sn=72ebfbe60eb592e5b36aa0fd71c508d5&scene=21#wechat_redirect)

### *4

#### [\# 去除空格](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313491&idx=1&sn=08d3dcaf1bace4265691fa7541c05727&scene=21#wechat_redirect)

### *5

#### [\# 如何在Python中从dataframe列的字符串中删除非字母数字字符？](https://www.cnpython.com/qa/61821)

### *6

#### [# 数据合并](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313362&idx=1&sn=3d8b068493098a942241fbe8662a81b9&scene=21#wechat_redirect)

### *7

#### [\# 用一个数据源的数据填充另一个数据源的缺失值](https://www.cnblogs.com/yuxiangyang/p/11286394.html)

### *8

#### [\# 有缺失值默认给float类型](https://www.cnblogs.com/everfight/p/10855654.html)

### *9

#### [\# Pandas 查询选择数据](https://www.gairuo.com/p/pandas-selecting-data)	

### *10

#### [pandas--将字符串属性转换为int型](https://blog.csdn.net/weixin_43486780/article/details/105601526)

### *额外

#### [\# git语法](https://www.liaoxuefeng.com/wiki/896043488029600)

## 总结

本次实验所要求的内容并不复杂，难就难在代码实现上，由于没有什么基础可言，90%的时间都拿去搜索各种文档恶补相关知识去了，可谓是受益匪浅，了解到了Python中的Numpy库以及Pandas库，也在不断捣鼓的过程中摸索出了一些相通的方法，第一次将项目推到GitHub上，也开始意识到要对自己写出的代码负责，这份沉甸甸的责任感使我不断优化自身代码，虽然学习Git语法也花费了我不少时间，整个实验花费了远多于以往实验的精力和时间，但结果总归是好的，相信接下来的实验会更加有的放矢更加得心应手，期间非常感谢彭老师的悉心指导

# 实验二《数据统计和可视化》

##  小组信息

+ 组员信息：陈泽彬（有组但单干）
+ 组员分工：陈泽彬
+ 指导老师：彭伟龙

## 作业题目和内容

#### **题目**

基于**实验一**中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：

1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2. 以5分为间隔，画出课程1的成绩直方图。
3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。

#### **提示：**

计算部分不能调用库函数；画图/可视化显示可可视化工具或API实现。

## 作业环境

+ Windows10
+ Anaconda Python3.6（IDE为pycharm）

### 文件说明

+ 「main.py」是源代码

+ 「Merge Data.csv」是实验一最后数据处理过后的学生成绩单

+ 「Nearest.txt」是第五题要求输出的txt文件

+ 「直方图.jpg」

+ 「散点图.jpg」

+ 「可视化混淆矩阵.jpg」

+ 「矩阵.jpg」是第三题、第四题、第五题运行后的矩阵结果
  + 归一化数据矩阵
  + 相关矩阵
  + 100*3矩阵

  

直方图.jpg：

![直方图](https://github.com/Chi2B/Image/blob/main/%E7%9B%B4%E6%96%B9%E5%9B%BE.jpg?raw=true)

散点图.jpg：

![直方图](https://github.com/Chi2B/Image/blob/main/%E6%95%A3%E7%82%B9%E5%9B%BE.jpg?raw=true)

可视化混淆矩阵.jpg：

![直方图](https://github.com/Chi2B/Image/blob/main/%E5%8F%AF%E8%A7%86%E5%8C%96%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%98%B5.jpg?raw=true)

矩阵.jpg：

![直方图](https://github.com/Chi2B/Image/blob/main/%E7%9F%A9%E9%98%B5.jpg?raw=true)

### 函数说明

#### 平均数函数

```python
def AVG(df):
    C_avg = sum(df)/len(df)
    C_avg = float('%0.1f' %C_avg)    # 设置精度
    return(C_avg)
```

输入类型可为numpy.ndarray，结果输出float类型的一个平均数

结果不希望要那么多小数点于是设置了精度，保留一位小数

#### 标准差函数

```python
def STD(df):
    sum = 0
    for j in df:
        sum = sum + pow(j-AVG(df),2)
    return pow(sum/(len(df)-1),0.5)
```

输入类型可为numpy.ndarray，结果输出float类型的一个标准差，其中调用了AVG（df）平均数函数

#### z-score函数

```python
def z_score(df):
    score=[]
    for i in df:
        score.append((i-AVG(df))/STD(df))
    return score
```

输入类型可为numpy.ndarray，结果输出numpy.ndarray类型的数组，其中调用了AVG（df）平均数函数、STD(df)标准差函数

#### 相关系数函数

```python
def CORRELATION(df1,df2):
    STD_df1df2 = sum([(i - AVG(df1)) * (j - AVG(df2)) for i, j in zip(df1, df2)])/(len(df1)-1)
    return STD_df1df2/(STD(df1)*STD(df2))
```

输入类型可为numpy.ndarray，结果输出float类型的一个相关系数，其中调用了AVG（df）平均数函数、STD（df）标准差函数

#### 相关矩阵函数

```python
def correlation_matrix(df):
        result = np.zeros((len(df),len(df)))
        for i in range(len(df)):
            for j in range(len(df)):
                result[i][j] = CORRELATION(df[i],df[j])
        return result
```

输入类型可为numpy.ndarray，结果输出numpy.ndarray类型

#### 100*3矩阵函数

```python
def Nearest(df):
    value = [0,0,0]
    result_value = np.zeros((len(df),3))
    result_ID = np.zeros((len(df),3))
    for i in range(len(df)):
        temp = sorted(df[i])
        value[0],value[1],value[2] = temp[-2],temp[-3],temp[-4]
        result_value[i][0],result_value[i][1],result_value[i][2] = value[0],value[1],value[2]
        result_ID[i][0],result_ID[i][1],result_ID[i][2] = df[i].tolist().index(result_value[i][0]),df[i].tolist().index(result_value[i][1]),df[i].tolist().index(result_value[i][2])
    return result_ID
```

输入类型可为numpy.ndarray，结果输出numpy.ndarray类型

### 调用的函数库以及涉及哪些技术

#### 函数库

+ pandas
+ matplotlib
+ seaborn
+ numpy

#### 涉及的技术

| 调用的函数                | 函数说明                                      |
| ------------------------- | --------------------------------------------- |
| pandas.read_csv(filename) | 从CSV文件导入数据                             |
| matplotlib.rcParams       | 返回是否在每个绘图命令后重绘。                |
| matplotlib.pyplot.title   | 为坐标轴设置标题                              |
| matplotlib.pyplot.xlabel  | 设置 x 轴的标签                               |
| matplotlib.pyplot.ylabel  | 设置 y 轴的标签                               |
| matplotlib.pyplot.scatter | 用不同的标记大小和/或颜色绘制 y 与 x 的散点图 |
| matplotlib.pyplot.yticks  | 获取或设置 y 轴的当前刻度位置和标签           |
| matplotlib.pyplot.show    | 显示所有打开的图像                            |
| matplotlib.pyplot.hist    | 画一个直方图                                  |
| pandas.DataFrame          | 创建DataFrame对象                             |
| pandas.DataFrame.values   | 返回 DataFrame 的 Numpy 表示形式              |
| numpy.zeros               | 返回给定形狱和类型的新数组，并用零填充        |
| seaborn.heatmap           | 将矩形数据绘制为颜色编码矩阵。                |
| pandas.Series.str.len     | 计算Series/Index 中每个元素的长度。           |
| numpy.savetxt             | 将数组保存到文本文件中                        |

## 难题与解决

### *1

#### [\# 替换中文及显示负数异常问题](https://www.cnblogs.com/hhh5460/p/4323985.html)

#### [\# 用python绘制散点图](https://blog.csdn.net/tszupup/article/details/81037411)

#### [\# matplotlib坐标轴设置参数（刻度值、间隔）](https://blog.csdn.net/JackSparrow_sjl/article/details/81226971)

### *2

#### [\# 绘制直方图](https://www.cnblogs.com/LiErRui/articles/11588399.html)

### *3

#### [\# pandas assign添加新的列或者覆盖原有的列](https://blog.csdn.net/weixin_40161254/article/details/82852969)

### *4

#### [\# 混淆矩阵](https://blog.csdn.net/b876144622/article/details/79871331)

### *5

#### [\# ndarray类型如何用index查找元素位置](https://blog.csdn.net/huanhuaqian/article/details/78825319)

### *6

#### [\# 保存txt](https://blog.csdn.net/weixin_42394932/article/details/81126005)

## 总结

本次实验主要是进行可视化以及进行数据统计，可视化用了Python库matplotlib，里面内置了一系列所需要的图，矩阵方面主要思想是先建立Dataframe类型的格式化数据，再利用pandas.Dataframe.values函数很方便地转为矩阵类型（ndarray），混淆矩阵用热力图的方式来表示，保存txt文件利用numpy.savetxt函数，难点主要在于写计算部分的函数。

# 实验三  《k-means聚类算法》

##  小组信息

+ 组员信息：陈泽彬（组长）、李华辉、冼海俊
+ 组员分工：
  + 陈泽彬——k-means算法代码实现
  + 李华辉——可视化实现
  + 冼海俊——实验结果分析与总结
+ 指导老师：彭伟龙

## 参考Github

在实现可视化中「类半径」和「标签显示」两个内容借鉴了软件182班**吴富乐**同学的代码，吴富乐同学GitHub地址为https://github.com/Chimaeras/Data_Mining_ex

## 作业题目和内容

#### **题目**

用C++实现k-means聚类算法，

1. 对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？
2. 由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。

样例数据(x,y)数据对：



| 3.45 | 7.08 |
| :--- | ---- |
| 1.76 | 7.24 |
| 4.29 | 9.55 |
| 3.35 | 6.65 |
| 3.17 | 6.41 |
| 3.68 | 5.99 |
| 2.11 | 4.08 |
| 2.58 | 7.10 |
| 3.45 | 7.88 |
| 6.17 | 5.40 |
| 4.20 | 6.46 |
| 5.87 | 3.87 |
| 5.47 | 2.21 |
| 5.97 | 3.62 |
| 6.24 | 3.06 |
| 6.89 | 2.41 |
| 5.38 | 2.32 |
| 5.13 | 2.73 |
| 7.26 | 4.19 |
| 6.32 | 3.62 |



找到聚类中心后，判断(2,6)是属于哪一类？



#### **注意**

除文件读取外，不能使用C++基础库以外的API和库函数。

## 作业环境

+ Windows10
+ Anaconda Python3.6（IDE为pycharm）

### 文件说明

#### 题目一

- **Question1文件夹**：题目一的CPP代码

+ **归一化数据矩阵.txt**：实验二导出的归一化数据矩阵
+ **Q1结果图文件夹**：Question1结果图片截图
  + Q1聚类2.jpg
  + Q1聚类3.jpg
  + Q1聚类4.jpg
  + Q1聚类5.jpg

#### 题目二

- **Question2文件夹**：题目二的CPP代码

- **train.txt**：训练集，即上述样例数据对

- **test.txt**：测试集，即（2，6）

- **result2、3、4、5**.csv：Qusetion2中CPP代码导出的分成不同类的数据，用于可视化程序.py，数据样式如下表

  | X       | Y       | Center_X            | Center_Y            | Class      |
  | ------- | ------- | ------------------- | ------------------- | ---------- |
  | 数据的x | 数据的y | 数据所在类的质心的x | 数据所在类的质心的y | 数据所在类 |

- **可视化程序.py**：用于数据可视化
- **Q2结果图文件夹**：Question1结果图片截图
  - Q2聚类2.png
  - Q2聚类2可视化.png
  - Q2聚类3.png
  - Q2聚类3可视化.png
  - Q2聚类4.png
  - Q2聚类4可视化.png
  - Q2聚类5.png
  - Q2聚类5可视化.png



**Q1聚类2.jpg：**

![Q1聚类2](https://github.com/Chi2B/Image/blob/main/Q1%E8%81%9A%E7%B1%BB2.jpg?raw=true)



**Q1聚类3.jpg：**

![Q1聚类3](https://github.com/Chi2B/Image/blob/main/Q1%E8%81%9A%E7%B1%BB3.jpg?raw=true)



**Q1聚类4.jpg：**

![Q1聚类4](https://github.com/Chi2B/Image/blob/main/Q1%E8%81%9A%E7%B1%BB4.jpg?raw=true)



**Q1聚类5.jpg：**

![Q1聚类5](https://github.com/Chi2B/Image/blob/main/Q1%E8%81%9A%E7%B1%BB5.jpg?raw=true)



**Q2聚类2.png**：

![Q2聚类2](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB2.png?raw=true)



**Q2聚类2可视化.png**：

![Q2聚类可视化](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB2%E5%8F%AF%E8%A7%86%E5%8C%96.png?raw=true)



**Q2聚类3.png**：

![Q2聚类3](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB3.png?raw=true)



**Q2聚类3可视化.png**

![Q2聚类3可视化](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB3%E5%8F%AF%E8%A7%86%E5%8C%96.png?raw=true)



**Q2聚类4.png**

![Q2聚类4](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB4.png?raw=true)



**Q2聚类4可视化.png**

![Q2聚类4可视化](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB4%E5%8F%AF%E8%A7%86%E5%8C%96.png?raw=true)



**Q2聚类5.png**

![Q2聚类5](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB5.png?raw=true)



**Q2聚类5可视化.png**

![Q2聚类5可视化](https://github.com/Chi2B/Image/blob/main/Q2%E8%81%9A%E7%B1%BB5%E5%8F%AF%E8%A7%86%E5%8C%96.png?raw=true)

### 函数说明

#### Question1.cpp（Question2.cpp类似）

##### 读取数据函数

```c++
void CTestKMeans::LoadFeatureFile(const string strFileName, std::vector<Tuple> &lDataList)
{
	double C1, C2, C3,C4,C5,C6,C7,C8,C9,C10, Constitution;
	ifstream iFile;
	iFile.open(strFileName.c_str(), ios::in);
	if (!iFile.is_open())		//文件无法正确打开
		cout << "open file failure!" << endl;
	if (iFile.peek() == EOF)		//文件若为空
	{
		cout << "file is empty!" << endl;
		return;
	}
	while (!iFile.eof())            // 若未到文件结束一直循环
	{
		iFile >> C1 >> C2 >> C3>>C4>>C5>>C6>>C7>>C8>>C9>>C10>> Constitution;
		struct Tuple sData;
		sData.C1 = C1;
		sData.C2 = C2;
		sData.C3 = C3;
		sData.C4 = C4;
		sData.C5 = C5;
		sData.C6 = C6;
		sData.C7 = C7;
		sData.C2 = C2;
		sData.C8 = C8;
		sData.C9 = C9;
		sData.C10 = C10;
		sData.Constitution = Constitution;
		lDataList.push_back(sData);

		iFile.get();//获取之后一个字符（后面这几行代码理解为会判断到最后是否为空即可）
		//peek方法可以返回下一个却不移动指针
		if (iFile.peek() == '\n')
		{
			break;
		}
	}

	iFile.close();   //关闭文件
}
```

输入参数为文件名（即归一化数据矩阵.txt）和Tuple类型的数据容器，最终结果为将txt数据全部导入数据容器中，Tuple为结构体，结构如下

```c++
//定义结构体，包含11科成绩
struct Tuple {
	double C1;
	double C2;
	double C3;
	double C4;
	double C5;
	double C6;
	double C7;
	double C8;
	double C9;
	double C10;
	double Constitution;
};
```



##### 计算两个元组间的欧氏距离

```c++
float CTestKMeans::GetDistXY(Tuple t1, Tuple t2)
{
	return sqrt((t1.C1 - t2.C1) * (t1.C1 - t2.C1) + (t1.C2 - t2.C2) * (t1.C2 - t2.C2) + (t1.C3 - t2.C3) * (t1.C3 - t2.C3) + (t1.C4 - t2.C4) * (t1.C4 - t2.C4) + (t1.C5 - t2.C5) * (t1.C5 - t2.C5) + (t1.C6 - t2.C6) * (t1.C6 - t2.C6) + (t1.C7 - t2.C7) * (t1.C7 - t2.C7) + (t1.C8 - t2.C8) * (t1.C8 - t2.C8) + (t1.C9 - t2.C9) * (t1.C9 - t2.C9) + (t1.C10 - t2.C10) * (t1.C10 - t2.C10) + (t1.Constitution - t2.Constitution) * (t1.Constitution - t2.Constitution));
}
```

输入参数为两个Tuple类型的变量，返回两个变量之间的欧氏距离



##### 根据质心，决定当前项属于哪个类

```c++
int CTestKMeans::ClusterOfTuple(Tuple tCentroid[], Tuple vDataList)
{
	float fDistance = GetDistXY(tCentroid[0], vDataList);//当前元组与第一个质心的欧式距离
	float fTmp;
	int nLabel = 0;//标示属于哪一个簇
	for (int i = 1; i < FEATURE_DIM; i++)
	{
		fTmp = GetDistXY(tCentroid[i], vDataList);//当前元组与第i个质心的欧氏距离
		if (fTmp < fDistance)//取最近的欧氏距离
		{
			fDistance = fTmp;
			nLabel = i;
		}
	}
	return nLabel;
}
```

输入参数为各类质心位置以及当前项，结果返回一个int型整数，为当前项所属类



##### 获得给定簇集的平方误差

```c++
float CTestKMeans::GetVar(vector<Tuple> vCluster[], Tuple tCentroid[]) {
	float fVar = 0;
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		vector<Tuple> vTuple = vCluster[i];
		for (int j = 0; j < vTuple.size(); j++)
		{
			fVar += GetDistXY(vTuple[j], tCentroid[i]);
		}
	}
	return fVar;
}
```

输入参数为每类所有项以及质心位置，返回当前分类情况下的平方误差



##### 获得当前簇的均值（质心）

```c++
Tuple CTestKMeans::GetMeans(vector<Tuple> vCluster) {

	int nNum = vCluster.size();
	double dMeansC1 = 0, dMeansC2 = 0, dMeansC3 = 0, dMeansC4 = 0, dMeansC5 = 0, dMeansC6 = 0, dMeansC7 = 0, dMeansC8 = 0, dMeansC9 = 0, dMeansC10 = 0, dMeansConstitution = 0;
	Tuple tTmp;
	for (int i = 0; i < nNum; i++)
	{
		dMeansC1 += vCluster[i].C1;
		dMeansC2 += vCluster[i].C2;
		dMeansC3 += vCluster[i].C3;
		dMeansC4 += vCluster[i].C4;
		dMeansC5 += vCluster[i].C5;
		dMeansC6 += vCluster[i].C6;
		dMeansC7 += vCluster[i].C7;
		dMeansC8 += vCluster[i].C8;
		dMeansC9 += vCluster[i].C9;
		dMeansC10 += vCluster[i].C10;
		dMeansConstitution += vCluster[i].Constitution;
	}
	tTmp.C1 = dMeansC1 / nNum;
	tTmp.C2 = dMeansC2 / nNum;
	tTmp.C3 = dMeansC3 / nNum;
	tTmp.C4 = dMeansC4 / nNum;
	tTmp.C5 = dMeansC5 / nNum;
	tTmp.C6 = dMeansC6 / nNum;
	tTmp.C7 = dMeansC7 / nNum;
	tTmp.C8 = dMeansC8 / nNum;
	tTmp.C9 = dMeansC9 / nNum;
	tTmp.C10 = dMeansC10 / nNum;
	tTmp.Constitution = dMeansConstitution / nNum;
	return tTmp;
}
```

输入参数为某一类所有项，返回这一类的质心



##### 训练集进行K-means算法

```c++
void CTestKMeans::TrainData(std::vector<Tuple> &vDataList, Tuple tCentroid[FEATURE_DIM])
{	//vDataList：所有数据项	          tCentroid[FEATURE_DIM]：有FEATURE_DIM项数据，为每一类的质心位置

	vector<Tuple> vClusters[FEATURE_DIM];	//可以理解为是个二维链表，存储某一类中的所有项

	//默认一开始将前FEATURE_DIM个元组的值作为FEATURE_DIM个簇的质心
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		tCentroid[i].C1 = vDataList[i].C1;
		tCentroid[i].C2 = vDataList[i].C2;
		tCentroid[i].C3 = vDataList[i].C3;
		tCentroid[i].C4 = vDataList[i].C4;
		tCentroid[i].C5 = vDataList[i].C5;
		tCentroid[i].C6 = vDataList[i].C6;
		tCentroid[i].C7 = vDataList[i].C7;
		tCentroid[i].C8 = vDataList[i].C8;
		tCentroid[i].C9 = vDataList[i].C9;
		tCentroid[i].C10 = vDataList[i].C10;
		tCentroid[i].Constitution = vDataList[i].Constitution;
	}

	int nLable = 0;		//标注这一项为哪一类
	//根据默认的质心给簇赋值
	for (int i = 0; i < vDataList.size(); i++)
	{
		//ClusterOfTuple：返回项所属类
		nLable = ClusterOfTuple(tCentroid, vDataList[i]);
		//将此项放至对应类中
		vClusters[nLable].push_back(vDataList[i]);
	}

	float fOldVar = -1;//第一次初始化为-1确保至少迭代一次
	float fNewVar = GetVar(vClusters, tCentroid);//获得给定簇集的平方误差
	while (fabs(fNewVar - fOldVar) > 0.1) //当新旧函数值相差不到1即准则函数值不发生明显变化时，算法终止
	{
		for (int i = 0; i < FEATURE_DIM; i++) //更新每个簇的中心点
		{
			//GetMeans返回每一类的质心
			tCentroid[i] = GetMeans(vClusters[i]);
			//cout<<"means["<<i<<"]:"<<tCentroid[i].Height<<"  "<<tCentroid[i].Weight<<endl;
		}
		fOldVar = fNewVar;
		//获得给定簇集的平方误差
		fNewVar = GetVar(vClusters, tCentroid); //计算新的准则函数值
		for (int i = 0; i < FEATURE_DIM; i++) //清空每个簇
		{
			vClusters[i].clear();
		}
		//根据新的质心获得新的簇
		for (int i = 0; i < vDataList.size(); i++)
		{
			//ClusterOfTuple：返回项所属类
			nLable = ClusterOfTuple(tCentroid, vDataList[i]);
			//将此项放至对应类中
			vClusters[nLable].push_back(vDataList[i]);
		}
	}
	//打印质心位置
	for (int i = 0; i < FEATURE_DIM; i++)
	{
		cout << "tCentroid"<< i + 1 <<": "<<"("<< tCentroid[i].C1 << "," << tCentroid[i].C2 << "," << tCentroid[i].C3 << "," << tCentroid[i].C4 << "," << tCentroid[i].C5 << "," << tCentroid[i].C6 << "," << tCentroid[i].C7 << "," << tCentroid[i].C8 << "," << tCentroid[i].C9 << "," << tCentroid[i].C10 << "," << tCentroid[i].Constitution<<")" << endl;
	}
}
```

输入参数为Tuple类型的数据容器和质心的位置



##### 预测K-means后所属簇类结果

```c++
std::vector<double> CTestKMeans::Prediect(Tuple tCentroid[FEATURE_DIM], std::vector<Tuple> vTestList)
{
	//一维链表
	std::vector<double> vdResult;
	for (int i = 0; i < vTestList.size(); i++) {
		Tuple tTest;
		tTest.C1 = vTestList[i].C1;
		tTest.C2 = vTestList[i].C2;
		tTest.C3 = vTestList[i].C3;
		tTest.C4 = vTestList[i].C4;
		tTest.C5 = vTestList[i].C5;
		tTest.C6 = vTestList[i].C6;
		tTest.C7 = vTestList[i].C7;
		tTest.C8 = vTestList[i].C8;
		tTest.C9 = vTestList[i].C9;
		tTest.C10 = vTestList[i].C10;
		tTest.Constitution = vTestList[i].Constitution;
		int nRet = ClusterOfTuple(tCentroid, tTest);
		vdResult.push_back(nRet+1);//类从1开始
		std::cout <<"ID:"<<i<<"\t"<< vdResult[i] << endl;
	}

	return vdResult;
}
```

输入参数为质心位置和Tuple类型的数据容器



#### 可视化程序.py

##### 画图函数

```python
def plot(k, assignment, center):
    # 初始坐标列表
    x = []
    y = []
    for i in range(k):
        x.append([])
        y.append([])
    # 填充坐标 并绘制散点图
    for j in range(k):
        for i in range(len(assignment[j])):
            x[j].append(assignment[j][i][0])  # 横坐标填充
        for i in range(len(assignment[j])):
            y[j].append(assignment[j][i][1])  # 纵坐标填充
        plt.scatter(x[j], y[j], c=color[j],marker='o',label=("类别%d" % (j + 1)))
        if(j==(k-1)):
            plt.scatter(center[j][0], center[j][1], c='red', marker='*', label="中心点")  # 画聚类中心
        else:
            plt.scatter(center[j][0], center[j][1], c='red', marker='*')  # 画聚类中心
    # 画出类半径
    for i in range(k):
        # 定义圆心和半径
        x = list_center[i][0]
        y = list_center[i][1]
        r = radius[i]
        # 点的横坐标为a
        a = np.arange(x - r, x + r, 0.0001)
        # 点的纵坐标减掉质心的y为b
        b = np.sqrt(abs(pow(r, 2) - pow((a - x), 2)))
        # 绘制上半部分
        plt.plot(a, y + b, color=color[i], linestyle='-')
        # 绘制下半部分
        plt.plot(a, y - b, color=color[i], linestyle='-')
    plt.scatter(2, 6, c='violet', marker='x', label="(2,6)")  # 画（2，6）
    # 设置标题
    plt.title('K-means Scatter Diagram')
    #
    plt.legend()
    # 设置X轴标签
    plt.xlabel('X')
    # 设置Y轴标签
    plt.ylabel('Y')
    # 显示散点图
    plt.show()
```

### 调用的函数库以及涉及哪些技术函数库

#### 函数库

##### Question1.cpp(Question.cpp):

| include的头文件 |
| --------------- |
| fstream         |
| iostream        |
| vector          |
| math.h          |



##### 可视化程序.py

| 调用的python库 |
| -------------- |
| pandas         |
| matplotlib     |
| numpy          |

#### 涉及的技术

##### Question1.cpp(Question.cpp):

| 调用的函数        | 函数说明                           |
| ----------------- | ---------------------------------- |
| ifstream::open()  | 指定模式打开文件                   |
| istream::peek()   | 查看下一个字符                     |
| ios::eof()        | 查看是否为空                       |
| istream::get      | 从流中提取字符，作为未格式化的输入 |
| ifstream::close   | 关闭文件                           |
| vector::size      | 返回容器大小                       |
| vector::push_back | 在最后添加元素                     |
| vector::clear     | 清除内容                           |



##### 可视化程序.py

| 调用的函数                | 函数说明                                       |
| ------------------------- | :--------------------------------------------- |
| matplotlib.rcParams       | 返回是否在每个绘图命令后重绘                   |
| pandas.read_csv(filename) | 从CSV文件导入数据                              |
| dataframe.iat             | 取某列某行的值                                 |
| list.append               | 将数据添加到list尾部                           |
| matplotlib.pyplot.scatter | 用不同的标记大小和/或颜色绘制 y  与 x 的散点图 |
| matplotlib.pyplot.plot    | 将y和x绘制为线条、标记                         |
| numpy.arange              | 函数返回一个有终点和起点的固定步长的排列       |
| matplotlib.pyplot.title   | 为坐标轴设置标题                               |
| matplotlib.pyplot.xlabel  | 设置  x 轴的标签                               |
| matplotlib.pyplot.ylabel  | 设置 y 轴的标签                                |
| matplotlib.pyplot.legend  | 给图加上图例                                   |
| matplotlib.pyplot.show    | 显示所有打开的图像                             |
| numpy.zeros               | 返回给定形狱和类型的新数组，并用零填充         |

## 难题与解决

### [# string中c_str()的用法](https://blog.csdn.net/qq_41282102/article/details/82695562)

### [# string中is_open()的用法](https://blog.csdn.net/guotianqing/article/details/107138117)

### [# if (!iFile.is_open())](https://zhidao.baidu.com/question/52686747.html)

### [# ifstream.get()](https://www.cnblogs.com/batman425/p/3179520.html)

### [# peek方法可以返回下一个却不移动指针](https://blog.csdn.net/zgqxiexie/article/details/51112487)

### [# C++ 输出结果到CSV或者Excel文件中](https://zhidao.baidu.com/question/1819941753548219028.html)

### [# pandas取dataframe特定行/列](https://www.cnblogs.com/nxf-rabbit75/p/10105271.html)

### [# Python 画图常用颜色 - 单色、渐变色、混色](https://blog.csdn.net/weixin_40683253/article/details/87370127)

### [# python中数组，列表，元组的区别、定义、功能](https://www.cnblogs.com/Ycc-LearningRate/p/11517791.html)

### [# pandas取dataframe特定行/列](https://www.cnblogs.com/nxf-rabbit75/p/10105271.html#auto-id-0)

### [# 类半径（吴富乐同学的GitHub）](https://github.com/Chimaeras/Data_Mining_ex)

## 总结

本次实验主要目的是实现k-means算法及可视化，算法有c++语言完成，可视化有python语言完成，第一题训练集为实验二的z-score规范化后的学生数据，第二题有训练集以及测试集，需要训练完模型后再进行测试集的测试，题目二最终导出各聚类的情况保存到csv中，可视化程序用导出的csv文件作为数据集进行相应的可视化，难点在如何绘制出类半径，其中借鉴了吴富乐同学的python代码，特别鸣谢，由第二题的可视化图像可以看出题目所给数据集分成2类会比较合适，其他类都出现分类过多、区限不明显的问题，综合考虑我认为分成2类会更合适

