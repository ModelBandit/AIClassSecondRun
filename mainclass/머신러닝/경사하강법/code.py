import numpy as np
import matplotlib.pyplot as plt

# w = w^0
w0 = 1.0
w1 = 1.0

learning_rate = 0.1 # 학습률
num_iterations = 100 # 반복횟수

#경사하강 반복

mlist = [[w0, w1]]
print(f"시작: w0 = {w0:.6f}, w1 = {w1:.6f}")

for t in range(num_iterations):
    w0_gradient = 4 * w1 + 6 * w0 - 6
    w1_gradient = 4 * w1 + 4 * w0 - 6

    w0 = w0 - learning_rate * w0_gradient
    w1 = w1 - learning_rate * w1_gradient

    mlist.append([w0, w1])

    print(f"iteration {t+1}: w0 = {w0:6f}, w1 = {w1:.6f}")
print(f"최종결과: w0 = {w0:.6f}, w1 = {w1:.6f}")
#print(mlist)
plt.plot(mlist)
plt.show()