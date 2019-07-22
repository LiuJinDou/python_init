# coding=utf-8
import io
class Goods(object):
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price
    def __str__(self):
        info = "编号:%s\t商品名称:%s\t\t价格:%d"%(self.id,self.name,self.price)
        return info




class ShopManager(object):

    def __init__(self,path):
        self.path = path
        self.shopdic = self.readFileToDic()

    def readFileToDic(self):
        f = io.open(self.path,'r',encoding='utf-8')
        clist = f.readlines()
        f.close()
        index = 0
        shopDic = {}
        while index < len(clist):
            ctlist = clist[index].replace('\n',"").split("||")
            good = Goods(clist[0],ctlist[1],int(ctlist[2]))
            shopdic[good.id] = good
            index = index +1
        return shopdic

    def writeContentFile(self):
        str1 = ''
        for key in self.shopdic.keys():
            good = self.shopdic[key]
            ele = good.id+"|"+good.name+"|"+str(good.price)+"\n"
            str1 = str1+ele
         f = io.open(self.path,'w',encoding='utf-8')
         f.write(str1)
         f.close()

     def addGoods(self):
        id = input("请输入添加商品编号:>")
        if self.shopdic.get(id):
            printf("商品编号已存在，请重新选择！")
            return
        name = input("请输入添加商品名称:>")
        price = int(input("请输入添加商品价格:>"))
        good = Goods(id,name,price)
        self.shopdic[id] = good
        print("添加成功！")

      def deleteGoods(self):
        id = input("请输入删除商品编号:>")
        if self.shopdic.get(id):
            del self.shopdic[id]
            print("删除成功！")
        else:
            print("删除的商品不存在！")
      def showGoods(self):
        print("="*40)
        for key in self.shopdic.keys():
            good = self.shopdic[key]
            print(good)
        print("="*40)
      def adminWork(self):
        info = """
        ============欢迎进入好嗨哦购物商场==============
            输入功能编号，你可以选择一下功能：
            输入”1“：显示商品信息
            输入”2“：添加商品信息
            输入”3“：删除商品信息
            输入”4“：退出系统功能
        ================================================
        """
        print(info)
        while True:
            code = input("请输入功能编号:>")
            if code == "1":
                self.showGoods()
            elif code == "2":
                self.addGoods()
            elif code == "3":
                sef,deleteGoods()
            elif code == "4":
                print("感谢你的使用，正在退出系统！！")
            else:
                print("输入编号有误，请重新输入！！")
        def useWork(self):
            print("===============欢迎进入好嗨哦购物商城=========")
            print("您可以输入编号和购买数量选购商品，输入编号n则为结账")
            self.showGoods()
            total = 0
            while True:
                id = input("请输入购买商品编号:>")
                if id == "n":
                    print("本次购买商品共消费%d元，感谢你的光临!"%(total))
                    break
                if self.shopdic.get(id):
                    good = self.shopdic[id]
                    num = int(input("请输入购买数量:>"))
                    total = total+good.price*num
                 else:
                    print("输入商品编号有误，请核对后重新输入！")


        def login(self):
            print("==========欢迎登陆好嗨哦购物商城================")
            uname = input("请输入用户名:>")
            password = input("请输入密码:>")
            if uname = 'admin':
                if password == '123456'
                    print("欢迎你，admin管理员")
                    self.adminWork()
                else:
                    print("欢迎你，%s用户"%s(uname))
                    self.userWork()
if __name__ == '__main__':
    shopManage = ShopManager("shop.txt")
    showManage.login()
