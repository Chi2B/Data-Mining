#  小组信息

+ 组员信息：陈泽彬（有组但单干）
+ 组员分工：陈泽彬
+ 指导老师：彭伟龙

# 实验一**《多源数据集成、清洗和统计》**

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

| 均值公式             | ![img](https://github.com/Chi2B/Image/blob/main/%E8%9C%82%E8%9C%9C%E6%B5%8F%E8%A7%88%E5%99%A8_1.jpg?raw=true) |
| :------------------- | :----------------------------------------------------------: |
| 协方差公式           | ![img](https://github.com/Chi2B/Image/blob/main/%E8%9C%82%E8%9C%9C%E6%B5%8F%E8%A7%88%E5%99%A8_2.jpg?raw=true) |
| z-score规范化        | ![img](https://github.com/Chi2B/Image/blob/main/%E8%9C%82%E8%9C%9C%E6%B5%8F%E8%A7%88%E5%99%A8_3.jpg?raw=true) |
| 数组A和数组B的相关性 | ![img](https://github.com/Chi2B/Image/blob/main/%E8%9C%82%E8%9C%9C%E6%B5%8F%E8%A7%88%E5%99%A8_4.jpg?raw=true)<br/>**这里A=[a1, a2,...ak,..., an],B=[b1, b2,...bk,..., bn]<br/>mean(A)代表A中元素的平均值std是标准差，即对协方差的开平方.<br/>点乘的定义：**![img](https://github.com/Chi2B/Image/blob/main/%E8%9C%82%E8%9C%9C%E6%B5%8F%E8%A7%88%E5%99%A8_5.jpg?raw=true) |

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

# 实验二**《数据统计和可视化》**

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

+ 「矩阵.jpg」是第三题、第四题、第五题运行后的矩阵结果
  + 归一化数据矩阵
  + 相关矩阵
  + 100*3矩阵

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

