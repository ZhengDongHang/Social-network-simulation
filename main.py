from freshman import *
from relationship import *
from visualization import *
from network import *
import pandas as pd

def InitialModel():
    """
    最基础的模型，新生属性只有编号
    """
    # InitialModel，模拟新生入学
    freshman_group = InitialFreshman(30) # 生成 30 个新生
    students = freshman_group.get_students()  # 获取新生列表
    # print(students) #输出新生列表

    # 创建 InitialRelationship 实例，模拟新生交互
    relationships = InitialRelationship(students)
    relationships.simulate_relationships(days=20) # 模拟 30 天的关系变化
    relationship_matrix = relationships.get_relationship_matrix() # 获取 30 天后的情绪矩阵
    # print(relationship_matrix) #输出情绪矩阵

    # 进行可视化
    plot_heatmap(relationship_matrix,'./charts/InitialCharts')
    visualize_matrix_distribution(relationship_matrix, './charts/InitialCharts')

    # 转化为邻接矩阵进行社会网络分析
    adjacency_matrix = convert_to_adjacency_matrix(relationship_matrix)
    visualize_social_network(adjacency_matrix, './charts/InitialCharts')

    # 计算中心性指标
    centrality_metrics = calculate_centrality(adjacency_matrix)
    centrality_metrics_df = pd.DataFrame(centrality_metrics)
    centrality_metrics_df.to_excel('./output/InitialOutput/中心性指标.xlsx', index=False)
    visualize_network_with_centrality(adjacency_matrix,'./charts/InitialCharts')

def BaseModel():
    """
    最基础的模型，新生属性有(学号，寝室，兴趣爱好)、
    """
    # 创建BaseFreshman实例，模拟新生入学
    freshman_group = BaseFreshman(30) # 生成 30 个新生
    students = freshman_group.get_students()  # 获取新生列表
    # print(students) #输出新生列表

    # 创建 BaseRelationship 实例，模拟新生交互
    relationships = BaseRelationship(students)
    relationships.simulate_relationships(days=30) # 模拟 30 天的关系变化
    relationship_matrix = relationships.get_relationship_matrix() # 获取 30 天后的情绪矩阵
    # print(relationship_matrix) #输出情绪矩阵

    # 进行可视化
    plot_heatmap(relationship_matrix,'./charts/BaseCharts')
    visualize_matrix_distribution(relationship_matrix, './charts/BaseCharts')

    # 转化为邻接矩阵进行社会网络分析
    adjacency_matrix = convert_to_adjacency_matrix(relationship_matrix)
    visualize_social_network(adjacency_matrix, './charts/BaseCharts')

    # 计算中心性指标
    centrality_metrics = calculate_centrality(adjacency_matrix)
    centrality_metrics_df = pd.DataFrame(centrality_metrics)
    centrality_metrics_df.to_excel('./output/BaseOutput/中心性指标.xlsx', index=False)
    visualize_network_with_centrality(adjacency_matrix, './charts/BaseCharts')

    # 观察属性和小世界的关系
    visualize_social_network_attribute(adjacency_matrix, students, './charts/BaseCharts')

def StructureModel():
    """
    增加结构平衡的模型，新生属性有(学号，寝室，兴趣爱好)，并使用压力传递算法来
    模拟小团体的加剧现象
    """
    # 创建BaseFreshman实例，模拟新生入学（这里仍然可以使用创建BaseFreshman实例）
    freshman_group = BaseFreshman(30) # 生成 30 个新生
    students = freshman_group.get_students()  # 获取新生列表
    # print(students) #输出新生列表

    # 创建 StructureRelationship 实例，模拟结构平衡
    relationships = StructureRelationship(students)
    relationships.simulate_relationships(days=30) # 模拟 30 天的关系变化
    relationship_matrix = relationships.get_relationship_matrix() # 获取 30 天后的情绪矩阵
    # print(relationship_matrix) #输出情绪矩阵

    # 进行可视化
    plot_heatmap(relationship_matrix,'./charts/StructureCharts')
    visualize_matrix_distribution(relationship_matrix, './charts/StructureCharts')

    # 转化为邻接矩阵进行社会网络分析
    adjacency_matrix = convert_to_adjacency_matrix(relationship_matrix)
    visualize_social_network(adjacency_matrix, './charts/StructureCharts')

    # 计算中心性指标
    centrality_metrics = calculate_centrality(adjacency_matrix)
    centrality_metrics_df = pd.DataFrame(centrality_metrics)
    centrality_metrics_df.to_excel('./output/StructureOutput/中心性指标.xlsx', index=False)
    visualize_network_with_centrality(adjacency_matrix, './charts/StructureCharts')

    # 观察属性和小世界的关系
    visualize_social_network_attribute(adjacency_matrix, students, './charts/StructureCharts')
if __name__ == '__main__':
    StructureModel()