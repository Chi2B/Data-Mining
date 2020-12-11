
# 导入pandas（*1）
import pandas as pd
from pandas import DataFrame as df

# 防止输出换行与省略
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# 导入数据源1并根据ID去重（*2）
data1 = pd.read_excel('./一.数据源1.xlsx')
data1_noDup = data1.drop_duplicates('ID').copy()

# 数据清洗
# ①校正身高，全部变为cm（*3）
# 下面两句为分解
# data1_temp1 = data1_noDup[data1_noDup["Height"] < 10]    # 查询出Height < 10的数据
# data1_temp2 = data1_temp1['Height'].values    # 以array形式返回指定column的所有取值
data1_temp2 = data1_noDup[data1_noDup["Height"] < 10]['Height'].to_numpy()    # 查询出Height < 10的数据并以array形式返回用于接下来的replace
data1_noDup["Height"] = data1_noDup["Height"].replace(data1_temp2, 100*data1_temp2)


# ②去除名字中存在的空格（*4）
data1_noDup["Name"] = data1_noDup["Name"].map(str.strip)

# ③利用正则表达式去除名字中不是字母的部分(*5)
data1_noDup["Name"] = data1_noDup.Name.str.replace('[^a-zA-Z]', '')

# ④性别统一改成boy和girl
data1_noDup["Gender"] = data1_noDup["Gender"].replace(['male', 'female'], ['boy', 'girl'])


# 导入数据源2并根据ID去重
data2 = pd.read_csv('./一.数据源2-逗号间隔.txt')
data2_noDup = data2.drop_duplicates('ID').copy()

# 数据清洗
# ①校正身高，全部变为cm
data2_temp2 = data2_noDup[data2_noDup["Height"] < 10]['Height'].to_numpy()      # 查询出Height < 10的数据并以array形式返回用于接下来的replace
data2_noDup["Height"] = data2_noDup["Height"].replace(data2_temp2, 100*data2_temp2)

# ②去除名字中存在的空格
data2_noDup["Name"] = data2_noDup["Name"].map(str.strip)

# ③利用正则表达式去除名字中不是字母的部分
data2_noDup["Name"] = data2_noDup.Name.str.replace('[^a-zA-Z]', '')

# ④性别统一改成boy和girl
data2_noDup["Gender"] = data2_noDup["Gender"].replace(['male', 'female'], ['boy', 'girl'])

# ⑤校正ID，全部变为1开始
data2_temp3 = data2_noDup['ID'].to_numpy()      # 查询出ID并以array形式返回用于接下来的replace
data2_noDup["ID"] = data2_noDup["ID"].replace(data2_temp3, data2_temp3-202000)

# 数据合并
# 找出“人无我有”的行（其实是数据源1有但是数据源2无的行，稍后会解释）（*6）
data_concat = pd.concat([data1_noDup['ID'], data2_noDup['ID']])    # 堆叠两个数据源的ID列
data_temp_noDup = data_concat.drop_duplicates(keep=False)    # 去除“你有我有”的行,keep=False代表有任何重复的行就全部删掉
temp = pd.merge(data_temp_noDup, data1_noDup['ID'], on='ID')    # 找出和数据源1中ID列的交集（只需要数据源1独有的）

temp_noDup = temp.drop_duplicates(keep=False)    # 这一步其实从结果来看没有意义，但为了规范化还是写了，可自行去除
data_temp1 = temp_noDup['ID'].to_numpy()      # 查询出ID并以array形式返回用于接下来的replace

#将数据源1独有的行堆叠到数据源2中
# print(data1_noDup.loc[data1_noDup['ID'].isin(data_temp2)])    # 查询ID为data_temp2里的数的行，因为我要行，而不是ID(isin=is in)
data2_noDup = pd.concat([data1_noDup.loc[data1_noDup['ID'].isin(data_temp1)], data2_noDup])

# 用数据源1的数据填充数据源2的缺失值（*7）
# 因为数据源1填充到数据源2到只能填充数据源2有的数据，所以前面的代码是为了先将数据源1独有的数据填到数据源2上
data3 = data2_noDup.combine_first(data1_noDup)

#去重，整理索引号，按照ID排序
data3_noDup = data3.drop_duplicates(['ID'])
data3_noDup = data3_noDup.sort_values('ID', ignore_index=True)

# 处理缺失值（*8）
data3_noDup['C10'] = data3_noDup['C10'].fillna(0)    # 将C10置0
data3_noDup['Constitution'] = data3_noDup['Constitution'].fillna(axis=0,method='ffill')    # 将Constitution缺失值用前面的一个值代替缺失值，axis=0是指用纵向的值替换后面的缺失值
data3_noDup = data3_noDup.fillna(axis=1,method='ffill')    # 用缺失值前面的一个值代替缺失值，axis=1是指用横向的前面的值替换后面的缺失值
print(data3_noDup)



# 1.	学生中家乡在Beijing的所有课程的平均成绩(*9)
res1_temp = data3_noDup[data3_noDup['City'] == 'Beijing']
def AVG(df):
    C_avg = sum(df)/len(df)
    C_avg = float('%0.1f' %C_avg)    # 设置精度
    return(C_avg)

C1 = AVG(res1_temp['C1'].to_numpy())
C2 = AVG(res1_temp['C2'].to_numpy())
C3 = AVG(res1_temp['C3'].to_numpy())
C4 = AVG(res1_temp['C4'].to_numpy())
C5 = AVG(res1_temp['C5'].to_numpy())
C6 = AVG(res1_temp['C6'].to_numpy())
C7 = AVG(res1_temp['C7'].to_numpy())
C8 = AVG(res1_temp['C8'].to_numpy())
C9 = AVG(res1_temp['C9'].to_numpy())
C10 = AVG(res1_temp['C10'])


# 建立Series输出
res1 = pd.Series([C1,C2,C3,C4,C5,C6,C7,C8,C9,C10],index=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'])
print('\n科目\t 平均成绩')
print(res1)


# 2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。
res2 = data3_noDup.loc[(data3_noDup['City'] == 'Guangzhou') & (data3_noDup['C1'] > 80) & (data3_noDup['C9'] > 9) & (data3_noDup['Gender'] == 'boy')].count()
print("\n\t人数")
print(res2[:1])

# 3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
# 设定差为60分，一般为70分，良好为80分，优秀为90分(*10)
data3_noDup_Copy=data3_noDup.copy()
map_class =  {'bad':60, 'general':70, 'good':80, 'excellent':90}
data3_noDup_Copy["Constitution"] = data3_noDup_Copy["Constitution"].map(map_class)

data3_GZ_temp = data3_noDup_Copy["Constitution"].loc[(data3_noDup_Copy['City'] == 'Guangzhou') &  (data3_noDup_Copy['Gender'] == 'girl')]
data3_GZ = AVG(data3_GZ_temp)

data3_SH_temp = data3_noDup_Copy["Constitution"].loc[(data3_noDup_Copy['City'] == 'Shanghai') &  (data3_noDup_Copy['Gender'] == 'girl')]
data3_SH = AVG(data3_SH_temp)
print('\n广州女生平均体能测试成绩平均成绩为:',data3_GZ)
print('上海女生平均体能测试成绩平均成绩为:',data3_SH)
if data3_GZ < data3_SH:
    print('上海地区女生的平均体能测试成绩更强')
elif data3_GZ > data3_SH:
    print('广州地区女生的平均体能测试成绩更强')
elif data3_GZ == data3_SH:
    print('两个地区女生的平均体能测试成绩旗鼓相当')

# 4.	学习成绩和体能测试成绩，两者的相关性是多少？
# 将C6-C9成绩乘以10
data3_noDup_Copy_temp1 = data3_noDup_Copy['C6'].to_numpy()    # 查询出ID并以array形式返回用于接下来的replace
data3_noDup_Copy["C6"] = data3_noDup_Copy["C6"].replace(data3_noDup_Copy_temp1, 10*data3_noDup_Copy_temp1)
data3_noDup_Copy_temp2 = data3_noDup_Copy['C7'].to_numpy()    # 查询出ID并以array形式返回用于接下来的replace
data3_noDup_Copy["C7"] = data3_noDup_Copy["C7"].replace(data3_noDup_Copy_temp2, 10*data3_noDup_Copy_temp2)
data3_noDup_Copy_temp3 = data3_noDup_Copy['C8'].to_numpy()    # 查询出ID并以array形式返回用于接下来的replace
data3_noDup_Copy["C8"] = data3_noDup_Copy["C8"].replace(data3_noDup_Copy_temp3, 10*data3_noDup_Copy_temp3)
data3_noDup_Copy_temp4 = data3_noDup_Copy['C9'].to_numpy()    # 查询出ID并以array形式返回用于接下来的replace
data3_noDup_Copy["C9"] = data3_noDup_Copy["C9"].replace(data3_noDup_Copy_temp4, 10*data3_noDup_Copy_temp4)

# 以array形式提取各列成绩
A_C1 = data3_noDup['C1'].to_numpy()
A_C2 = data3_noDup['C2'].to_numpy()
A_C3 = data3_noDup['C3'].to_numpy()
A_C4 = data3_noDup['C4'].to_numpy()
A_C5 = data3_noDup['C5'].to_numpy()
A_C6 = data3_noDup_Copy['C6'].to_numpy()
A_C7 = data3_noDup_Copy['C7'].to_numpy()
A_C8 = data3_noDup_Copy['C8'].to_numpy()
A_C9 = data3_noDup_Copy['C9'].to_numpy()
A_Constitution = data3_noDup_Copy['Constitution'].to_numpy()

# 标准差函数
def STD(df):
    sum = 0
    for j in df:
        sum = sum + pow(j-AVG(df),2)
    return pow(sum/(len(df)-1),0.5)

# 相关系数函数
def CORRELATION(df1,df2):
    STD_df1df2 = sum([(i - AVG(df1)) * (j - AVG(df2)) for i, j in zip(df1, df2)])/(len(df1)-1)
    return STD_df1df2/(STD(df1)*STD(df2))

# 建立Series输出
res4 = pd.Series([CORRELATION(A_C1,A_Constitution),CORRELATION(A_C2,A_Constitution),CORRELATION(A_C3,A_Constitution),\
                  CORRELATION(A_C4,A_Constitution),CORRELATION(A_C5,A_Constitution),CORRELATION(A_C6,A_Constitution),\
                  CORRELATION(A_C7,A_Constitution),CORRELATION(A_C8,A_Constitution),CORRELATION(A_C9,A_Constitution)],\
                 index=['C1','C2','C3','C4','C5','C6','C7','C8','C9'])
print('\n科目\t\t相关系数')
print(res4)

# # data3_noDup.to_csv("./Merge Data.csv")    # 导出一份数据
# data3_noDup_Copy.to_csv("./Merge Data.csv")    # 导出一份数据
