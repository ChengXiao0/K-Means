import numpy as np
import matplotlib.pyplot as plt


# 计算质心
def jszx(c):
    sumx = 0
    sumy = 0
    for k in range(len(c)):
        jszx_temp = c[k]
        sumx += jszx_temp[0]
        sumy += jszx_temp[1]
    sumx /= len(c)
    sumy /= len(c)
    return sumx, sumy


# 打印簇
def print_c(c):
    for print_i in range(len(3)):
        temp = c[print_i]
        plt.plot(temp[0], temp[1], 'g+')


# 随机生成数据
s1x = np.random.normal(0, 0.5, 50)
s1y = np.random.normal(0, 0.5, 50)
s2x = np.random.normal(3, 0.5, 50)
s2y = np.random.normal(3, 0.5, 50)
s3x = np.random.normal(3, 0.5, 50)
s3y = np.random.normal(-3, 0.5, 50)
x_t = np.concatenate((s1x, s2x, s3x))
y_t = np.concatenate((s1y, s2y, s3y))
# plt.plot(x_t, y_t, 'o')
# 3个蔟，初始化质心
c1 = list()
c2 = list()
c3 = list()
ch1 = (1, 1)
ch2 = (3, 3)
ch3 = (2, -5)
# plt.plot(ch1[0], ch1[1], 'ro')
# plt.plot(ch2[0], ch2[1], 'ro')
# plt.show()
# 迭代1000次
for i in range(1000):
    c1.clear()
    c2.clear()
    c3.clear()
    c1.append(ch1)
    c2.append(ch2)
    c3.append(ch3)
    for j in range(len(x_t)):
        dj1 = (x_t[j] - ch1[0]) ** 2 + (y_t[j] - ch1[1]) ** 2
        dj2 = (x_t[j] - ch2[0]) ** 2 + (y_t[j] - ch2[1]) ** 2
        dj3 = (x_t[j] - ch3[0]) ** 2 + (y_t[j] - ch3[1]) ** 2
        if dj1 == min(dj2, dj3, dj1):
            c1.append((x_t[j], y_t[j]))
        elif dj2 == min(dj2, dj3, dj1):
            c2.append((x_t[j], y_t[j]))
        elif dj3 == min(dj2, dj3, dj1):
            c3.append((x_t[j], y_t[j]))
    # 重新计算质心
    temp_ch1 = jszx(c1)
    temp_ch2 = jszx(c2)
    temp_ch3 = jszx(c3)
    # 更新质心
    if ch1 != temp_ch1 or ch2 != temp_ch2 or ch3 != temp_ch3:
        ch1 = temp_ch1
        ch2 = temp_ch2
        ch3 = temp_ch3
    else:
        break
    print(i)

# 查看效果
for i in range(len(c1)):
    temp = c1[i]
    plt.plot(temp[0], temp[1], 'bo')

for i in range(len(c2)):
    temp = c2[i]
    plt.plot(temp[0], temp[1], 'r*')

for i in range(len(c3)):
    temp = c3[i]
    plt.plot(temp[0], temp[1], 'g+')
plt.savefig('3class.jpg')
plt.show()
