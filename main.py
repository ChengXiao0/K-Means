import numpy as np
import matplotlib.pyplot as plt

# 随机生成数据
s1x = np.random.normal(1, 0.5, 50)
s1y = np.random.normal(1, 0.5, 50)
s2x = np.random.normal(3, 0.5, 50)
s2y = np.random.normal(3, 0.5, 50)
x_t = np.concatenate((s1x, s2x))
y_t = np.concatenate((s1y, s2y))
# plt.plot(x_t, y_t, 'o')
# 两个蔟，初始化质心
c1 = list()
c2 = list()
ch1 = (2, 3)
ch2 = (1, 2)
# plt.plot(ch1[0], ch1[1], 'ro')
# plt.plot(ch2[0], ch2[1], 'ro')
# plt.show()
# 迭代1000次
for i in range(1000):
    c1.clear()
    c2.clear()
    c1.append(ch1)
    c2.append(ch2)
    for j in range(len(x_t)):
        dj1 = (x_t[j] - ch1[0]) ** 2 + (y_t[j] - ch1[1]) ** 2
        dj2 = (x_t[j] - ch2[0]) ** 2 + (y_t[j] - ch2[1]) ** 2
        if dj1 < dj2:
            c1.append((x_t[j], y_t[j]))
        else:
            c2.append((x_t[j], y_t[j]))
    # 重新计算质心
    # 质心1：
    sumx1 = 0
    sumy1 = 0
    for k in range(len(c1)):
        temp = c1[k]
        sumx1 += temp[0]
        sumy1 += temp[1]
    sumx1 /= len(c1)
    sumy1 /= len(c1)
    # 质心2：
    sumx2 = 0
    sumy2 = 0
    for k in range(len(c2)):
        temp = c2[k]
        sumx2 += temp[0]
        sumy2 += temp[1]
    sumx2 /= len(c1)
    sumy2 /= len(c1)
    # 更新质心
    if ch1 != (sumx1, sumy1) or ch2 != (sumx2, sumy2):
        ch1 = (sumx1, sumy1)
        ch2 = (sumx2, sumy2)
    else:
        break
    print(i)

for i in range(len(c1)):
    temp = c1[i]
    plt.plot(temp[0], temp[1], 'bo')

for i in range(len(c2)):
    temp = c2[i]
    plt.plot(temp[0], temp[1], 'ro')
plt.savefig('2class.jpg')
plt.show()

