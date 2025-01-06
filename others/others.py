import numpy as np
import matplotlib.pyplot as plt
# 设置全局字体
plt.rcParams['font.family'] = 'SimHei'  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def plot_normal_distribution(mu=0, sigma=1, size=1000):
    """
    绘制正态分布图。

    :param mu: 正态分布的均值，默认为 0。
    :param sigma: 正态分布的标准差，默认为 1。
    :param size: 随机生成的样本数，默认为 1000。
    """
    # 生成正态分布的随机数据
    data = np.random.normal(loc=mu, scale=sigma, size=size)

    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', label="Histogram")

    # 绘制正态分布的概率密度函数 (PDF)
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    pdf = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    plt.plot(x, pdf, 'r-', lw=2, label=f"Normal PDF (μ={mu}, σ={sigma})")

    # 添加标题和标签
    plt.title("正态分布", fontsize=16)
    plt.xlabel("值", fontsize=12)
    plt.ylabel("分布", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)
    plt.savefig('正态分布')
    plt.show()


# 调用函数
plot_normal_distribution(mu=0, sigma=1, size=1000)
