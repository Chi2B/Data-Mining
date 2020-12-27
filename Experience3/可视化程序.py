# 导入所需库
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 用来正常显示中文标签（①）
plt.rcParams['font.sans-serif']=['SimHei']

# 为保证各类颜色相同，定义一个颜色数组
color = ['gold', 'blue', 'brown', 'black', 'green', 'purple']

# 导入数据（在这里改变要聚成几类，可相应改变为result2、result3、result4、result5）
data = pd.read_csv('./result2.csv')

# 初始化
k = max(data['Class'])  # k为类数
list_center = []    # 质心list
list_Class = []     # 保存各类中项的list

# 将各类中的项放到list_Class[]中，将各类质心放到list_center[]中
for i in range(k):
    temp_pd_eachClass = data[data['Class'] == (i+1)]
    list_eachClass = list(zip(temp_pd_eachClass['X'],temp_pd_eachClass['Y']))
    center = [temp_pd_eachClass.iat[0,2],temp_pd_eachClass.iat[0,3]]
    list_center.append(center)
    list_Class.append(list_eachClass)

# 定义半径
radius = np.zeros(k)
for i in range(k):
    # 如果是一个点属于一类 就令其半径为0.2
    max_dis = 0.2
    # 遍历点
    for j in range(len(list_Class[i])):
        dis_x = list_Class[i][j][0] - list_center[i][0]
        dis_y = list_Class[i][j][1] - list_center[i][1]
        # 计算欧式距离
        distance = np.sqrt(pow(dis_x, 2) + pow(dis_y, 2))
        # 更新最大半径
        if distance > max_dis:
            max_dis = distance
    # 最大值即为该类的类半径
    radius[i] = max_dis

# 画图
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
    # 给图加上图例
    plt.legend()
    # 设置X轴标签
    plt.xlabel('X')
    # 设置Y轴标签
    plt.ylabel('Y')
    # 显示散点图
    plt.show()

plot(k,list_Class,list_center)