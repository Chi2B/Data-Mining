# 1、导入包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# 2、画出sigmoid函数
def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-10, 10, 0.1)
h = Sigmoid(x)  # Sigmoid函数
plt.plot(x, h) # 将y和x绘制为线条、标记
plt.axvline(0.0, color='k')  # 坐标轴上加一条竖直的线（0位置）
plt.axhline(y=0.5, ls='dotted', color='k') # 坐标轴上加一条横向的线（0.5位置）
plt.yticks([0.0, 0.5, 1.0])  # y轴标度
plt.ylim(-0.1, 1.1)  # y轴范围
plt.show()


# 3、加载数据
data = pd.read_csv('./result2.csv')
X_train = np.array(list(zip(data['X'].to_numpy(),data['Y'].to_numpy()))) # zip的结果是元组，我需要数组所以最后转了一下arrary
y_train = data['Class'].to_numpy()
X_test = [[2,6]]


# 4.标准化特征值
sc = StandardScaler()
sc.fit(X_train) # 用于计算训练数据的均值和方差
X_train_std = sc.transform(X_train) # 进行转换，把训练数据转换成标准的正态分布
X_test_std = sc.transform(X_test) # 进行转换，把训练数据转换成标准的正态分布


# 5. 训练逻辑回归模型
logreg = linear_model.LogisticRegression(C=1e5) # 根据现有数据对分类边界线建立回归公式，以此进行分类
logreg.fit(X_train, y_train) # 根据给出的训练数据来训练模型。


# 6. 预测
prepro = logreg.predict_proba(X_test_std) # 概率估计
np.set_printoptions(suppress=True) # 取消科学计数法表示
np.set_printoptions(precision=8) # 设定输出小数精度
print(prepro)

