import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    # 定义角度范围
    theta = np.linspace(0, 10 * np.pi, 1000)
    a = 1  # 螺线初始半径
    
    # 创建螺线对象
    spiral = ArchimedeanSpiral(a, theta)
    
    # 绘制螺线
    plt.plot(spiral.x, spiral.y)
    plt.title('Archimedean Spiral (b = 0)')
    plt.axis('equal')  # 确保 x 和 y 轴比例相同
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
