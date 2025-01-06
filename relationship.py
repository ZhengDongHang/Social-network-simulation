# 该文档目的在于模拟现实生活中各种关系，由简单到复杂逐步进行

import random
import numpy as np
random.seed(42)

class InitialRelationship:
    def __init__(self, students):
        """
        初始化 InitialRelationship 类。
        :param students: 学生列表，每个学生是一个字典，包含学生信息。
        """
        self.students = students
        self.num_students = len(students)  # 学生数量
        self.relationship_matrix = np.zeros((self.num_students, self.num_students), dtype=float)

    def simulate_relationships(self, days=30):
        """
        模拟学生之间的随机关系变化，迭代更新每一对学生的关系。
        :param days: 模拟的天数，默认 30 天。
        """
        for _ in range(days):
            for i in range(self.num_students):
                for j in range(i + 1, self.num_students):  # 遍历每一对学生，避免重复和自循环
                    # 根据天数和关系类型调整关系波动（正太分布）
                    change = random.gauss(0, 1)
                    self.relationship_matrix[i][j] += change
                    self.relationship_matrix[j][i] += change  # 确保对称性

    def get_relationship_matrix(self):
        """
        返回最终的关系矩阵。
        """
        return self.relationship_matrix

    def display_relationship_matrix(self):
        """
        打印关系矩阵，用于调试和展示。
        """
        print("Relationship Matrix:")
        print(self.relationship_matrix)


class BaseRelationship:
    def __init__(self, students):
        """
        初始化 BaseRelationship 类。
        :param students: 学生列表，每个学生是一个字典，包含学生信息。
        """
        self.students = students
        self.num_students = len(students)  # 学生数量
        self.relationship_matrix = np.zeros((self.num_students, self.num_students), dtype=float)

    def simulate_relationships(self, days=30):
        """
        模拟学生之间的随机关系变化。
        :param days: 模拟的天数，默认 30 天。
        """
        for day in range(days):
            for i in range(self.num_students):
                for j in range(i + 1, self.num_students):  # 遍历每一对学生，避免重复和自循环
                    # 根据天数和关系类型调整关系波动（正太分布）
                    change = random.gauss(0, 1)

                    # 前50天寝室相同的学生关系波动翻倍
                    if day < 50 and self.students[i]['dormitory'] == self.students[j]['dormitory']:
                        change *= 2  # 同寝室关系波动翻倍

                    # 对于兴趣相同的学生，有20%的概率增加0.02的关系
                    if self.students[i]['interest'] == self.students[j]['interest']:
                        if random.random() < 0.5:  # 生成一个0到1之间的随机数，20%的概率小于0.2
                            change += 0.02

                    self.relationship_matrix[i][j] += change
                    self.relationship_matrix[j][i] += change  # 确保对称性

    def get_relationship_matrix(self):
        """
        返回最终的关系矩阵。
        """
        return self.relationship_matrix

    def display_relationship_matrix(self):
        """
        打印关系矩阵，用于调试和展示。
        """
        print("Relationship Matrix:")
        print(self.relationship_matrix)

class StructureRelationship:
    def __init__(self, students, k=0.0015):
        """
        初始化 StructureModelRelationship 类。
        :param students: 学生列表，每个学生是一个字典，包含学生信息。
        :param k: 压力调节系数。
        """
        self.students = students
        self.num_students = len(students)  # 学生数量
        self.relationship_matrix = np.zeros((self.num_students, self.num_students), dtype=float)
        self.k = k  # 压力调节系数

    def simulate_relationships(self, days=30):
        """
        模拟学生之间的关系变化，并加入结构压力传递。
        :param days: 模拟的天数，默认 30 天。
        """
        for day in range(days):
            # 每天的关系更新
            for i in range(self.num_students):
                for j in range(i + 1, self.num_students):  # 遍历每一对学生，避免重复和自循环
                    # 根据天数和关系类型调整关系波动（正态分布）
                    change = random.gauss(0, 1)

                    # 前50天寝室相同的学生关系波动翻倍
                    if day < 50 and self.students[i]['dormitory'] == self.students[j]['dormitory']:
                        change *= 2  # 同寝室关系波动翻倍

                    # 对于兴趣相同的学生，有20%的概率增加0.02的关系
                    if self.students[i]['interest'] == self.students[j]['interest']:
                        if random.random() < 0.2:  # 20%的概率
                            change += 0.02

                    self.relationship_matrix[i][j] += change
                    self.relationship_matrix[j][i] += change  # 确保对称性

            # 创建一个新的矩阵，用于存储结构压力传递的结果
            new_relationship_matrix = np.copy(self.relationship_matrix)

            # 结构压力传递更新
            for a in range(self.num_students):
                for b in range(self.num_students):
                    if a != b:
                        pressure_sum = 0  # 初始化压力
                        for c in range(self.num_students):
                            if c != a and c != b:  # 排除自身和目标
                                pressure_sum += (
                                    self.k * self.relationship_matrix[a][c] * self.relationship_matrix[c][b]
                                )
                        new_relationship_matrix[a][b] += pressure_sum

            # 更新关系矩阵，限制其范围在[-20, 20]之间
            new_relationship_matrix = np.clip(new_relationship_matrix, -20, 20)
            # 更新关系矩阵
            self.relationship_matrix = new_relationship_matrix

    def get_relationship_matrix(self):
        """
        返回最终的关系矩阵。
        """
        return self.relationship_matrix

    def display_relationship_matrix(self):
        """
        打印关系矩阵，用于调试和展示。
        """
        print("Relationship Matrix:")
        print(self.relationship_matrix)
