# coding=utf-8

class Person(object):
    
    def __init__(self,name,age,gender,partner=None):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__partner = partner

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if not isinstance(age,int):
            raise ValueError('age must be type int')
        if age<1 or age>120:
            raise ValueError('age must be between 1 and 120')

        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self,gender):
        if gender=='男' or gender=='女':
            self.__gender = gender
        else:
            raise ValueError('sex must be 男 or 女')

    def getGender(self):
        return self.__gender

    def setPartner(self,partner):
        if partner == None:
            self.__partner = None
            return
        if not isinstance(partner,Person):
            raise ValueError('partner typpe must be Person')
        self.__partner = partner

    def getPartner(self):
        return self.__partner


    def __str__(self):
        if self.__partner !=None:
            str = '名字:%s,年龄:%d,性别:%s,配偶:%s'%(self.__name,self.__age,self.__gender,self.__partner.getName())
            return str

        else:
            str = '名字:%s,年龄:%d,性别:%s,没有结婚'%(self.__name,self.__age,self.__gender)
            return str

    def marry(self,operson):
        if self.getGender() == operson.getGender():
            print('在中国，同性暂时不能结婚')
        elif self.getGender() == '男':
            if self.getAge()<24 or operson.getAge()<22:
                print("还未到法定结婚年龄，过几年在来吧！！")
            elif self.getPartner()!=None or operson.getPartner()!=None:
                print("在中国重婚已是犯法了，不能结婚！")
            else:
                print("恭喜%s和%s新婚快乐，百年好合！！"%(self.getName(),operson.getName()))
                self.setPartner(operson)
                operson.setPartner(self)
        elif self.getGender() == '女':

            if self.getAge()<22 or operson.getAge()<24:
                print("还未到法定结婚的年龄，过几年在来吧！！")
            elif self.getPartner()!= None or operson.getPartner()!= None:
                print("在中国重婚是犯法了，不能结婚！！")
            else:
                print("恭喜%s和%s新婚快乐，百年好合！！"%(self.getName(),operson.getName()))
                self.setPartner(operson)
                operson.setPartner(self)
        else:
            print('系统出现故障了，不能结婚')

    
    def divorce(self):
        if self.getPartner() == None:
            print('醒醒吧，还没结婚呢，无法办理离婚啊！！')
        else:
            partner = self.getPartner()
            self.setPartner(None)
            partner.setPartner(None)



if __name__ == '__main__':
    p1 = Person('Pig','18','男')
    p2 = Person('杨丹','17','女')
    p1.marry(p2)

    p3 = Person('Jack','20','男',None)
    p1.marry(p2)
    print("======六年后======")
    p1.setAge(24)
    p2.setAge(23)
    p3.setAge(26)

    p4 = Person('Rose','23','女',None)
    p1.marry(p4)
