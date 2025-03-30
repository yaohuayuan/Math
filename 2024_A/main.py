import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve



class ArchimedeanSpiral:
    def __init__(self, a: float, theta: np.ndarray):
        """
        构造函数，定义等距螺线属性
        :param a: 螺线初始半径
        :param theta: 螺线的角度数组 (弧度制)
        b 始终为 0
        """
        self.a = a  # 初始半径
        self.b = 0  # 在本题中 b 始终为 0
        self.theta = theta  # 角度数组
        self.r = self.a + self.b * theta  # 极径
        self.x = self.r * np.cos(theta)  # x 坐标
        self.y = self.r * np.sin(theta)  # y 坐标


class BenchDragon:
    def __init__(self, a, v0):
        self.bodyTheta = None
        self.HeadX = None
        self.HeadY = None
        self.HeadRho = None
        self.HeadTheta = None
        self.a = a
        self.v0 = v0
        self.bodyCounter = 223
        self.headLength = 3.41
        self.bodyLength = 2.20

    def funcDragonHeadPosition(self, x, theta0, t):
        # print(t)
        return self.a / (4 * np.pi) * (x*np.sqrt(1 + x ** 2) + np.log(x + np.sqrt(1 + x ** 2))
                                       - theta0*np.sqrt(1 + theta0 ** 2) - np.log(theta0 + np.sqrt(1 + theta0 ** 2))) \
            + self.v0 * t

    def solveDragonHeadTPosition(self, t, theta0):
        initial_guess = 32 * np.pi  # 初始猜测值
        solution = fsolve(self.funcDragonHeadPosition, initial_guess, args=(theta0, t))
        return solution[0]

    def solveDragonHeadPosition(self, t, theta0):
        ansList = []
        for i in range(t):
            ans = self.solveDragonHeadTPosition(i, theta0)
            ansList.append(ans)
        self.HeadTheta = np.array(ansList)
        self.HeadRho = a/(2*np.pi)*self.HeadTheta
        self.HeadX = self.HeadRho*np.cos(self.HeadTheta)
        self.HeadY = self.HeadRho*np.sin(self.HeadTheta)
    def funcDragonBodyPosition(self,theta1,theta0,l):
        return l**2 - self.a**2/(4*np.pi**2)*\
            (theta1**2+theta0**2-2*theta1*theta0*np.cos(theta1-theta0))

    def solveDragonBodyPosition(self,t):
        initial_guess = 32 * np.pi
        for i in range(self.bodyCounter+1):
            theta0 = self.HeadTheta[i]
            l = self.headLength - 2*27.5
            ans = []
            for i in range(t):
                solution = fsolve(self.funcDragonBodyPosition,initial_guess,args=(theta0,l))
                l = self.bodyLength - 27.5
                theta0 = solution[0]
                ans.append(solution[0])
            self.bodyTheta.append(ans)




if __name__ == "__main__":
    a = 0.55
    v0 = 1
    theta0 = 32 * np.pi
    dragon = BenchDragon(a, v0)
    dragon.solveDragonHeadPosition(300, theta0)
    plt.figure(figsize=(10, 6))
    plt.plot(dragon.HeadX, dragon.HeadY)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Dragon Head Trajectory')
    plt.axis("equal")
    plt.grid(True)
    plt.show()