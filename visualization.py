# 此文档的目的在于进行可视化
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False  # 防止负号显示问题

def plot_heatmap(matrix, save_path, vmin=-20, vmax=20, title="社会关系热力图"):
    """
    绘制热力图矩阵。

    :param matrix: 输入的二维数组或矩阵
    :param vmin: 热力图的最小值（默认 -20）
    :param vmax: 热力图的最大值（默认 20）
    :param title: 热力图标题（可选）
    """
    # 创建一个新的绘图窗口
    plt.figure(figsize=(8, 8))

    # 绘制热力图
    plt.imshow(matrix, cmap="coolwarm", vmin=vmin, vmax=vmax)
    plt.colorbar(label="关系强度")  # 添加颜色条

    # 添加标题
    plt.title(title, fontsize=16)

    # 添加 x 和 y 轴的标签
    plt.xlabel("学生标签", fontsize=12)
    plt.ylabel("学生标签", fontsize=12)

    # 显示网格线
    plt.grid(False)

    # 显示与存储图形
    plt.savefig(f'{save_path}/社会关系热力图.png')
    # plt.show()


def visualize_matrix_distribution(matrix, save_path):
    """
    绘制每个人的关系分布图（直方图）

    :param matrix: 输入的二维矩阵 (numpy 数组或列表)
    :param save_path: 保存图片的路径
    """
    # 创建图形
    plt.figure(figsize=(10, 6))
    num_students = len(matrix)  # 学生数量

    # 为每个学生的关系绘制直方图
    for i, row in enumerate(matrix):
        plt.hist(row, bins=20, alpha=0.6, label=f"学生 {i + 1}", density=True)

    # 添加标题和标签
    plt.title("个人关系分布图", fontsize=16)
    plt.xlabel("关系量化值", fontsize=12)
    plt.ylabel("频率", fontsize=12)

    # 显示图例
    plt.grid(alpha=0.3)

    # 保存并显示图像
    plt.tight_layout()
    plt.savefig(f'{save_path}/个人关系分布图.png')
    # plt.show()


def visualize_social_network(adj_matrix, save_path):
    """
    根据邻接矩阵绘制社会网络图，节点颜色根据度数变化。

    :param adj_matrix: 邻接矩阵，二维 NumPy 数组
    :param save_path: 保存图形的路径
    """
    # 创建一个空图
    G = nx.Graph()

    # 将邻接矩阵添加到图中
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 避免重复边
            if adj_matrix[i][j] == 1:  # 如果有连接
                G.add_edge(i, j)

    # 计算每个节点的度（即每个人的连接数）
    degrees = dict(G.degree())
    max_degree = max(degrees.values())
    min_degree = min(degrees.values())

    # 定义颜色渐变
    colors = ['#25d938', '#00a1d4']  # 从绿色到蓝色
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', colors)
    norm = plt.Normalize(min_degree, max_degree)

    # 提取节点和权重
    node_colors = [cmap(norm(degrees[node])) for node in G.nodes()]

    # 绘制图形
    fig, ax = plt.subplots(figsize=(12, 12))
    pos = nx.spring_layout(G, seed=42)  # 使用 spring 布局
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, font_size=12, font_weight='bold', edge_color='gray')

    # 添加颜色条
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, orientation='vertical', label='Degree')

    # 保存和显示图形
    plt.tight_layout()
    plt.savefig(f'{save_path}/社会网络图.png')
    # plt.show()

def visualize_social_network_attribute(adj_matrix, attribute, save_path):
    """
    根据邻接矩阵绘制社会网络图，节点颜色根据 dormitory 属性变化，节点名称为 interest。

    :param adj_matrix: 邻接矩阵，二维 NumPy 数组
    :param attribute: 学生属性列表，与邻接矩阵的顺序一致，每个属性是一个字典
                      示例：{'student_number': 1, 'dormitory': 2, 'interest': '网游'}
    :param save_path: 保存图形的路径
    """
    # 创建一个空图
    G = nx.Graph()

    # 将邻接矩阵添加到图中
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 避免重复边
            if adj_matrix[i][j] == 1:  # 如果有连接
                G.add_edge(i, j)

    # 提取 dormitory 属性并为每个节点定义颜色
    dormitory_colors = {attr['dormitory'] for attr in attribute}  # 提取所有不同的 dormitory 值
    color_map = {dorm: plt.cm.tab10(idx) for idx, dorm in enumerate(dormitory_colors)}  # 生成颜色映射
    node_colors = [color_map[attr['dormitory']] for attr in attribute]  # 根据 dormitory 赋予颜色

    # 提取 interest 属性作为节点标签
    node_labels = {i: attr['interest'] for i, attr in enumerate(attribute)}

    # 绘制图形
    fig, ax = plt.subplots(figsize=(12, 12))
    pos = nx.spring_layout(G, seed=42)  # 使用 spring 布局
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)  # 绘制边
    nx.draw_networkx_nodes(
        G, pos, node_size=3000, node_color=node_colors, edgecolors='black', cmap=plt.cm.tab10
    )  # 绘制节点
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight='bold')  # 添加标签

    # 添加图例
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=f"Dormitory {dorm}")
        for dorm, color in color_map.items()
    ]
    ax.legend(handles=legend_elements, loc='upper right', title="Dormitory")

    # 保存和显示图形
    plt.tight_layout()
    plt.savefig(f'{save_path}/社会网络图_属性.png')
    # plt.show()


def visualize_network_with_centrality(adj_matrix, save_path):
    """
    可视化基于邻接矩阵的社会网络，并为每个节点绘制多种中心性指标的颜色。

    :param adj_matrix: 邻接矩阵（NumPy 数组或二维列表）
    """
    # 创建图
    G = nx.Graph()
    num_nodes = len(adj_matrix)

    # 将邻接矩阵添加到图中
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 避免重复边
            if adj_matrix[i][j] == 1:  # 如果有连接
                G.add_edge(i, j)

    # 计算各类中心性
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

    # 提取每种中心性最高的5个节点
    top_5_degree = set(sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:5])
    top_5_betweenness = set(sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5])
    top_5_closeness = set(sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:5])
    top_5_eigenvector = set(sorted(eigenvector_centrality, key=eigenvector_centrality.get, reverse=True)[:5])

    # 定义颜色
    colors = {
        'degree': 'red',
        'betweenness': 'blue',
        'closeness': 'yellow',
        'eigenvector': 'green'
    }

    # 获取节点的颜色
    def get_node_color(node):
        segments = []
        if node in top_5_degree:
            segments.append(colors['degree'])
        if node in top_5_betweenness:
            segments.append(colors['betweenness'])
        if node in top_5_closeness:
            segments.append(colors['closeness'])
        if node in top_5_eigenvector:
            segments.append(colors['eigenvector'])

        if segments:
            return segments
        else:
            return ['gray']

    # 绘制图形
    fig, ax = plt.subplots(figsize=(16, 16))
    pos = nx.spring_layout(G, seed=42)  # 布局算法

    # 绘制网络边
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')

    # 绘制节点
    for node, (x, y) in pos.items():
        segments = get_node_color(node)
        if len(segments) > 1:
            # 计算角度
            num_segments = len(segments)
            angles = np.linspace(0, 2 * np.pi, num_segments + 1)
            wedge_radius = 0.06  # 调整饼图的大小
            for i in range(num_segments):
                wedge = patches.Wedge(center=(x, y), r=wedge_radius, theta1=np.degrees(angles[i]),
                                      theta2=np.degrees(angles[i + 1]), color=segments[i], ec='black')
                ax.add_patch(wedge)
        else:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=segments[0], node_size=3000)

    # 绘制节点标签
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # 添加图例
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Degree Centrality', markersize=10, markerfacecolor='red'),
        Line2D([0], [0], marker='o', color='w', label='Betweenness Centrality', markersize=10, markerfacecolor='blue'),
        Line2D([0], [0], marker='o', color='w', label='Closeness Centrality', markersize=10, markerfacecolor='yellow'),
        Line2D([0], [0], marker='o', color='w', label='Eigenvector Centrality', markersize=10, markerfacecolor='green'),
        Line2D([0], [0], marker='o', color='w', label='Other Nodes', markersize=10, markerfacecolor='gray'),
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    # 显示并保存图片
    plt.savefig(f'{save_path}/社会网络图_中心性分析.png')
    # plt.show()