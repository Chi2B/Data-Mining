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
plt.plot(x, h)
plt.axvline(0.0, color='k')  # 坐标轴上加一条竖直的线（0位置）
plt.axhline(y=0.5, ls='dotted', color='k') # 坐标轴上加一条横向的线（0.5位置）
plt.yticks([0.0, 0.5, 1.0])  # y轴标度
plt.ylim(-0.1, 1.1)  # y轴范围
plt.show()


# 3、加载数据
data = pd.read_csv('./result2.csv')
X_train = np.array(list(zip(data['X'].to_numpy(),data['Y'].to_numpy())))
y_train = data['Class'].to_numpy()
X_test = [[2,6]]


# 4.标准化特征值
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)


# 5. 训练逻辑回归模型
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X_train, y_train)


# 6. 预测
prepro = logreg.predict_proba(X_test_std)
np.set_printoptions(suppress=True)
np.set_printoptions(precision=8)
print(prepro)

