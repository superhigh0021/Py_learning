import re


class StudentInfo:
    def __init__(self, str) -> None:
        self.info_list = str.split(' ')
        self.ID = self.info_list[0]
        self.name = self.info_list[1]
        self.gender = self.info_list[2]
        self.Class = self.info_list[3]
        self.grade = dict()
        self.grade_init()

    def grade_init(self):
        for i in range(4, len(self.info_list)):
            subject = re.findall('.+(?=:)', self.info_list[i])
            grade = re.findall('(?<=:).+', self.info_list[i])
            if self.grade.get(subject[0], 0) == 0:
                self.grade[subject[0]] = int(grade[0])
        self.aver = int(sum(self.grade.values()) / len(self.grade))

    def grade_modify(self):
        choose = input("If you want to modify/add a subject,input y: ")
        if choose == 'y':
            str = input('Please input the subject you want to add/modify: ')
            grade = int(input("Please input the grade of that subject: "))
            if self.grade.get(str, 0) != 0:
                #right here
                self.grade[str] = grade
            else:
                #add a subject
                self.grade[str] = grade
        else:
            str = input('Please input the subject you want to delete: ')
            del self.grade[str]
        print(self.grade)

    def print(self, rank):
        print('{} {} {} {} {} 平均分:{} 排名:{}'.format(self.ID, self.name,
                                                   self.gender, self.Class,
                                                   self.grade, self.aver,
                                                   rank))


def rank_student(list):
    list.sort(key=lambda x: x.aver, reverse=True)


fp = open(input("Please input your filename: "), 'r', encoding='utf-8')
student_info_line = fp.readlines()
student_list = list()

for i in range(len(student_info_line)):
    student_list.append(StudentInfo(student_info_line[i]))
while input("modify the grade,type 'y':") == 'y':
    name = input("input the name who you want to modify his grade: ")
    for item in student_list:
        if item.name == name:
            item.grade_modify()
            break
    else:
        print("The guy is nowhere to be found.")

rank_student(student_list)

rank = 1
for item in student_list:
    item.print(rank)
    rank += 1