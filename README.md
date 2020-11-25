#  小组信息

+ 组员信息：陈泽彬（有组但单干）

+ 组员分工：陈泽彬
+ 指导老师：彭伟龙

# 作业题目和内容

## **题目**

广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在Excel中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java/Python程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

- Excel表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。
- txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。

## **参考**

一.数据源1.xlsx

| ID   | Name  | City     | Gender | Height | C1   | ...  | C10  | Constitution |
| ---- | ----- | -------- | ------ | ------ | ---- | ---- | ---- | ------------ |
| 1    | Marks | Shenzhen | boy    | 166    | 77   |      |      | general      |
| 2    | Wayne | Shenzhen | girl   | 159    | 77   |      |      | good         |
| ...  | ...   | ...      | ...    | ...    | ...  | ...  | ...  | ...          |



一.数据源2-逗号间隔.txt

ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution
202001,Marks,Shenzhen,male,1.66,77,100,84,71,91,6,7,6,8,,general

## 实验内容

两个数据源合并后读入内存，并统计：

1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

## **提示**

参考数据结构：

Student{

int id;

string id;

vector<float> data;

}



可能用到的公式：

| 均值公式             | ![img](https://gitee.com/chi2b/pic-clound/raw/master/img/MZxvju9kaLGQm3PWf8OsgA) |
| :------------------- | :----------------------------------------------------------: |
| 协方差公式           | ![img](https://gitee.com/chi2b/pic-clound/raw/master/img/WzKGNUBrrSKwDAJURyVRQA) |
| z-score规范化        | ![img](https://gitee.com/chi2b/pic-clound/raw/master/img/DREX3MFPw-d3hZhtAkyp4g) |
| 数组A和数组B的相关性 | ![img](https://gitee.com/chi2b/pic-clound/raw/master/img/XwYEh8-AUcIxFt2zVQ-sEg)<br/>**这里A=[a1, a2,...ak,..., an],B=[b1, b2,...bk,..., bn]<br/>mean(A)代表A中元素的平均值std是标准差，即对协方差的开平方.<br/>点乘的定义：**![img](https://gitee.com/chi2b/pic-clound/raw/master/img/odNr0YyX8NwtmlJUDvD2lQ) |

注意：计算部分不能调用库函数；画图/可视化显示可以用可视化API或工具实现。

# 作业环境

+ Windows10

+ Anaconda Python3.6（IDE为pycharm）

## 文件说明

+ 「main.py」是源代码

+ 「一.数据源1.xlsx」是数据源1

+ 「一.数据源2-逗号间隔.txt」是数据源2

+ 「运行结果截图.jpg」是运行结果
  + 输出合并后数据源
  + 输出学生中家乡在Beijing的所有课程的**平均成绩**
  + 输出学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的**数量**
  + 输出比较广州和上海两地女生的平均体能测试成绩并判断哪个地区的更强些
  + 输出学习成绩和体能测试成绩两者的**相关性**

## 函数说明

### 平均数函数

```python
def AVG(df):
    C_avg = sum(df)/len(df)
    C_avg = float('%0.1f' %C_avg)    # 设置精度
    return(C_avg)
```

输入类型可为numpy.ndarray，结果输出float类型的一个平均数

结果不希望要那么多小数点于是设置了精度，保留一位小数

### 标准差函数

```python
def STD(df):
    sum = 0
    for j in df:
        sum = sum + pow(j-AVG(df),2)
    return pow(sum/(len(df)-1),0.5)
```

输入类型可为numpy.ndarray，结果输出float类型的一个标准差，其中调用了AVG（df）平均数函数

### 相关系数函数

```python
def CORRELATION(df1,df2):
    STD_df1df2 = sum([(i - AVG(df1)) * (j - AVG(df2)) for i, j in zip(df1, df2)])/(len(df1)-1)
    return STD_df1df2/(STD(df1)*STD(df2))
```

输入类型可为numpy.ndarray，结果输出float类型的一个相关系数，其中调用了AVG（df）平均数函数、STD（df）标准差函数

## 调用的函数库以及涉及哪些技术

### 函数库

+ pandas

### 涉及的技术

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

# 难题与解决

前言：非常惭愧做本次实验基本是从0开始，除了理解实验要求不是难题，其余一切代码实现几乎都是难题，无论是简单的导入还是复杂的清洗、合并、查询，都花费了大量的时间和精力用于各种百度上，也从中收集了一些个人认为很不错的文章，同时也在源代码中做好了标记，下面会根据标记处所遇到的问题以及解决办法罗列在下方，今后一定洗心革面好好学习天天向上

## *1

### [\# Numpy的基础知识](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402378855&idx=1&sn=77ed3c403aa00977e66a6d712b565f44&scene=21#wechat_redirect)

### [# Panda的基础知识](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402568021&idx=1&sn=66d5234a31f2de640baa71439f856a33&scene=21#wechat_redirect)

## *2

### [\# 数据导入](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=402829681&idx=1&sn=3042132921889b2b5414fff28513b05b&scene=21#wechat_redirect)

### [\# .drop_duplicates 用法说明](https://www.cnblogs.com/yaos/p/9837448.html)

### [\# SettingwithCopyWarning（不加.copy()会报警告的原因）](https://blog.csdn.net/xiaofeixia666888/article/details/106807181)

## *3

### [\# Pandas中把数据格式（df,array）的相互转换](https://blog.csdn.net/weixin_43708040/article/details/87275815)

### [\# numpy对象折叠成一维的数组1](https://blog.csdn.net/likeyou1314918273/article/details/89735607)

### [\# numpy对象折叠成一维的数组2](https://www.pythonheidong.com/blog/article/430164/3f1749c78e817b2d3ec0/)

### [\# 替换异常值](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313425&idx=1&sn=72ebfbe60eb592e5b36aa0fd71c508d5&scene=21#wechat_redirect)

## *4

### [\# 去除空格](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313491&idx=1&sn=08d3dcaf1bace4265691fa7541c05727&scene=21#wechat_redirect)

## *5

### [\# 如何在Python中从dataframe列的字符串中删除非字母数字字符？](https://www.cnpython.com/qa/61821)

## *6

### [# 数据合并](https://mp.weixin.qq.com/s?__biz=MjM5MDEzNDAyNQ==&mid=2650313362&idx=1&sn=3d8b068493098a942241fbe8662a81b9&scene=21#wechat_redirect)

## *7

### [\# 用一个数据源的数据填充另一个数据源的缺失值](https://www.cnblogs.com/yuxiangyang/p/11286394.html)

## *8

### [\# 有缺失值默认给float类型](https://www.cnblogs.com/everfight/p/10855654.html)

## *9

### [\# Pandas 查询选择数据](https://www.gairuo.com/p/pandas-selecting-data)	

## *10

### [pandas--将字符串属性转换为int型](https://blog.csdn.net/weixin_43486780/article/details/105601526)

## *额外

### [\# git语法](https://www.liaoxuefeng.com/wiki/896043488029600)

# 总结

本次实验所要求的内容并不复杂，难就难在代码实现上，由于没有什么基础可言，90%的时间都拿去搜索各种文档恶补相关知识去了，可谓是受益匪浅，了解到了Python中的Numpy库以及Pandas库，也在不断捣鼓的过程中摸索出了一些相通的方法，第一次将项目推到GitHub上，也开始意识到要对自己写出的代码负责，这份沉甸甸的责任感使我不断优化自身代码，虽然学习Git语法也花费了我不少时间，整个实验花费了远多于以往实验的精力和时间，但结果总归是好的，相信接下来的实验会更加有的放矢更加得心应手，期间非常感谢彭老师的悉心指导。