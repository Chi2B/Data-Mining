# 导入所需库
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn    # 混淆矩阵
import numpy as np

# 防止输出换行与省略
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# np.set_printoptions(threshold=np.inf)

# 1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
# 导入数据
data = pd.read_csv('./Merge Data.csv')  # 导入数据
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签（①）

# 添加x轴数据和y轴数据
x = data['C1']
y = data['Constitution']

# 添加标题和x轴、y轴标签
plt.title("课程1成绩和体能成绩散点图")    # 标题
plt.xlabel("课程1成绩") # x轴标签
plt.ylabel("体能成绩")  # y轴标签

# 绘制散点图
plt.scatter(x, y,s=30,c='b',marker='*') # s代表点的大小，c代表点的颜色，marker代表点的样式（①）

# 设置y轴间隔
plt.yticks(np.arange(60,100,10))     #重新设置y轴间隔和刻度值（①）

# 显示图形
plt.show()




# 2. 以5分为间隔，画出课程1的成绩直方图。
# 添加标题和x轴、y轴标签
plt.title("课程1成绩直方图")    # 标题
plt.xlabel("课程1成绩") # x轴标签
plt.ylabel("频数")  # y轴标签

# 绘制直方图（②）
plt.hist(x = data['C1'], # 指定绘图数据
         bins = 10, # 指定直方图中条块的个数
         color = 'steelblue', # 指定直方图的填充色
     edgecolor = 'black', # 指定直方图的边框色
          )

# 显示图形
plt.show()




# 3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
# 平均数函数
def AVG(df):
    C_avg = sum(df)/len(df)
    C_avg = float('%0.1f' %C_avg)    # 设置精度
    return(C_avg)

# 标准差函数
def STD(df):
    sum = 0
    for j in df:
        sum = sum + pow(j-AVG(df),2)
    return pow(sum/(len(df)-1),0.5)

# z-score函数
def z_score(df):
    score=[]
    for i in df:
        score.append((i-AVG(df))/STD(df))
    return score

# 构造数据矩阵(③)
df=pd.DataFrame({'C1':z_score(data['C1']),'C2':z_score(data['C2']),\
                 'C3':z_score(data['C3']),'C4':z_score(data['C4']),\
                 'C5':z_score(data['C5']),'C6':z_score(data['C6']),\
                 'C7':z_score(data['C7']),'C8':z_score(data['C8']),\
                 'C9':z_score(data['C9']),'C10':data['C10']\
                    ,'Constitution':z_score(data['Constitution'])})

# Dataframe转矩阵
df1=df.values

# 输出归一化数据矩阵
print('归一化数据矩阵:')
print(df1)




# 4. 计算出100x100的相关矩阵，并可视化出混淆矩阵。（④）
# 生成Datafram类型
df2=pd.DataFrame({'C1':data['C1'],'C2':data['C2'],'C3':data['C3'],'C4':data['C4'],\
                 'C5':data['C5'],'C6':data['C6'],'C7':data['C7'],'C8':data['C8'],\
                 'C9':data['C9'],'C10':data['C10'],'Constitution':data['Constitution']})

# Dataframe转矩阵
df3=df2.values

# 相关系数函数
def CORRELATION(df1,df2):
    STD_df1df2 = sum([(i - AVG(df1)) * (j - AVG(df2)) for i, j in zip(df1, df2)])/(len(df1)-1)
    return STD_df1df2/(STD(df1)*STD(df2))

# 相关矩阵函数
def correlation_matrix(df):
        result = np.zeros((len(df),len(df)))
        for i in range(len(df)):
            for j in range(len(df)):
                result[i][j] = CORRELATION(df[i],df[j])
        return result

# 输出相关矩阵
corr_result = correlation_matrix(df3)
print('\n\n\n\n相关矩阵:')
print(corr_result)

# 可视化混淆矩阵
df_cm = pd.DataFrame(corr_result)   # 矩阵转DataFrame
sn.heatmap(df_cm)   # 生成混淆矩阵（用热力图方式展示）

# 输出图像
plt.show()



# 5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。
# 100*3矩阵函数（⑤）
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

# 输出矩阵
print('\n\n\n\n100x3矩阵:')
print(Nearest(corr_result))

# 保存txt文件（⑥）
np.savetxt('Nearest.txt', Nearest(corr_result), fmt='%d', delimiter="\t")