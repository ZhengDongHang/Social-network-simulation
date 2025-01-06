"""此目的是在于进行社会网络转化"""
import networkx as nx
import numpy as np

def convert_to_adjacency_matrix(matrix, threshold=5):
    """
    将关系矩阵转换为邻接矩阵，大于 threshold 的值转化为 1，反之为 0。

    :param matrix: 输入的二维矩阵（numpy 数组或列表）
    :param threshold: 用于判定关系强度的阈值，默认值为 10
    :return: 返回转化后的邻接矩阵
    """
    # 转化为 numpy 数组（如果输入是列表）
    matrix = np.array(matrix)

    # 创建邻接矩阵，关系大于阈值设为 1，否则设为 0
    adjacency_matrix = np.where(matrix > threshold, 1, 0)

    return adjacency_matrix


def calculate_centrality(adj_matrix):
    """
    计算图的各种中心性指标（度中心性、介数中心性、接近中心性、特征向量中心性）。

    :param adj_matrix: 输入的邻接矩阵（二维 NumPy 数组或列表）
    :return: 返回一个字典，包含四种中心性指标和节点编号
    """
    # 创建图
    G = nx.Graph()

    # 将邻接矩阵添加到图中
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 避免重复边
            if adj_matrix[i][j] == 1:  # 如果有连接
                G.add_edge(i, j)

    # 计算度中心性
    degree_centrality = nx.degree_centrality(G)

    # 计算介数中心性
    betweenness_centrality = nx.betweenness_centrality(G)

    # 计算接近中心性
    closeness_centrality = nx.closeness_centrality(G)

    # 计算特征向量中心性
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

    # 创建节点编号，从1开始
    nodes = list(range(1, num_nodes + 1))

    # 返回计算的中心性指标和节点编号
    return {
        'Node': nodes,
        "degree_centrality": [degree_centrality[node - 1] if node - 1 in degree_centrality else 0 for node in nodes],
        "betweenness_centrality": [betweenness_centrality[node - 1] if node - 1 in betweenness_centrality else 0 for
                                   node in nodes],
        "closeness_centrality": [closeness_centrality[node - 1] if node - 1 in closeness_centrality else 0 for node in
                                 nodes],
        "eigenvector_centrality": [eigenvector_centrality[node - 1] if node - 1 in eigenvector_centrality else 0 for
                                   node in nodes]
    }
