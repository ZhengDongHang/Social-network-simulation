# 该文档的目的在于生成不同属性的新生，由简单到复杂逐步进行
import random
class InitialFreshman:
    def __init__(self, n):
        """
        初始化 BaseFreshman 类，并生成 n 个新生。
        每个新生有一个唯一的学号。

        :param n: 要生成的新生数量
        """
        self.students = []  # 用于存储生成的新生
        self.generate_students(n)

    def generate_students(self, n):
        """
        生成 n 个新生，每个新生分配一个唯一的学号。
        学号从 1 开始递增。
        """
        for i in range(1, n + 1):
            student = {"student_number": i}  # 用字典表示新生，以便存储更多的属性
            self.students.append(student)
    def get_students(self):
        """
        返回生成的新生列表。
        :return: 学生列表
        """
        return self.students


class BaseFreshman:
    def __init__(self, n):
        """
        初始化 BaseFreshman 类，并生成 n 个新生。
        每个新生有(学号，寝室，兴趣爱好)。

        :param n: 要生成的新生数量
        """
        self.students = []  # 用于存储生成的新生
        self.dormitories = []  # 存储寝室信息
        self.interests = ["网游", "历史", "桌游", "手游", "追剧"]  # 5大类兴趣爱好
        self.generate_students(n)

    def generate_students(self, n):
        """
        生成 n 个新生，分配学号、寝室和兴趣爱好。
        学号从 1 开始递增，寝室随机分配，兴趣爱好随机分配。
        """
        # 生成学号和兴趣爱好
        for i in range(1, n + 1):
            student = {
                "student_number": i,
                "dormitory": None,  # 待分配的寝室
                "interest": random.choice(self.interests)  # 随机选择兴趣爱好
            }
            self.students.append(student)

        # 随机打乱学生顺序
        random.shuffle(self.students)
        # 随机分配寝室，每个寝室最多 4 人
        dormitory_number = 1
        for i in range(0, n, 4):  # 每次处理最多 4 个学生
            dorm = self.students[i:i + 4]
            for student in dorm:
                student["dormitory"] = dormitory_number  # 将寝室号分配给学生
            dormitory_number += 1  # 增加下一个寝室号
        self.students = sorted(self.students, key=lambda x: list(x.values())[0])

    def get_students(self):
        """
        返回生成的新生列表。
        :return: 学生列表
        """
        return self.students

if __name__ == '__main__':  # 检验代码
    freshman_group = BaseFreshman(10)  # 生成 10 个新生
    students = freshman_group.get_students()  # 获取新生列表
    print(students)  # 打印新生列表
