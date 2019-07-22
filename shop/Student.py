#coding=utf-8
"""
学生信息管理系统功能
1.欢迎用户使用学生信息管理系统，提示用户输入用户名和密码完成登录功能。   admin  123456
登录功能有3次机会，如果3次内成功，用户可登录享有其他功能，否则用户不能登录，退出系统
3.登录成功后提示用户输入编号，选择功能
   学生信息管理系统功能
    1.添加学生信息功能（输入学号，学生名称，班级）
    2.搜索学生功能（输入学生学号，得到姓名和班级）
    3.删除功能（输入学号，可对于对应学生进行删除操作）
    4.显示所有学生信息的功能
    5.退出系统功能
"""
class Student(object):
    def __init__(self,id,name,classNo):
        self.id = id
        self.name = name
        self.classNo = classNo
    def __str__(self):
        str = '学生学号:%s\t姓名:%s\t班级:%s'%(self.id,self.name,self.classNo)
        return str

class StudentManager(object):
    def __init__(self):
        #创建字典，作为存放学生信息的容器，
        # 字典的key为学号，value为学生对象
        self.studic = {}

    def addStudent(self):
        # 1.添加学生信息功能（输入学号，学生名称，班级）
        id = input("请输入添加学生学号:>")
        if self.studic.get(id):
            print('此学号已存在，请重新操作！')
            return
        name = input("请输入添加学生姓名:>")
        classNo = input("请输入添加学生班级:>")
        stu = Student(id,name,classNo)
        self.studic[id] = stu
        print("添加成功！")

    def queryStudent(self):
        # 2.搜索学生功能（输入学生学号，得到姓名和班级）
        id = input("请输入搜索学生学号:>")
        # 判断是否存在此学生
        if self.studic.get(id):
            stu = self.studic[id]
            print("您查找的学生信息为:",end='')
            print(stu)
        else:
            print('此学号不存在，请重新操作！')

    def deleteStudent(self):
        # 3.删除功能（输入学号，可对于对应学生进行删除操作）
        id = input("请输入删除学生学号:>")
        if self.studic.get(id):
            del self.studic[id]
            print("删除成功！")
        else:
            print('此学号不存在，请重新操作！')

    def getAllStudent(self):
        #4.显示所有学生信息的功能
        print("="*20)
        for key in self.studic.keys():
            print(self.studic[key])
        print("="*20)


    def work(self):
        info ="""
        ==================学生信息管理系统==================
        输入“1”:添加学生信息功能（输入学号，学生名称，班级）
        输入“2”:搜索学生功能（输入学生学号，得到姓名和班级）
        输入“3”:删除功能（输入学号，可对于学生进行删除操作）
        输入“4”:显示所有学生信息的功能（学号，学生名，班级）
        输入“5”:感谢用户使用，退出学生信息管理系统
        ====================================================
        """
        print(info)
        while True:
            num = input("请根据提示，输入对应功能编号:>")
            if num == "1":
                self.addStudent()
            elif num == "2":
                self.queryStudent()
            elif num == "3":
                self.deleteStudent()
            elif num == "4":
                self.getAllStudent()
            elif num == "5":
                print("正在退出系統，感謝您的使用！！")
                break
            else:
                print("輸入編碼有誤，請核對後重新輸入！")

    def login(self):
        print("----------请先登录学生信息管理系统----------")
        num = 1
        while num < 4:
            uname = input('请输入用户名:>')
            password = input('请输入密码:>')
            if uname == 'admin' and password == '123456':
                print('登录成功，欢迎进入该系统')
                #登录成功，开始执行相关操作
                self.work()
                return
            else:
                if num != 3:
                    print('登录失败，用户名或者密码有误，您还有%d次机会，请核对后重新输入' % (3 - num))
                else:
                    print('没有权限进入系统')
            num = num + 1


if __name__ == '__main__':
    stuManager = StudentManager()
    stuManager.login()
