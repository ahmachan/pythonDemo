# coding=utf-8

import lottery

class MyTest:

    myname = 'peter'
    # add a instance attribute
    def __init__(self, name):
        self.name = name

    def start(self):
        print ('the name is %s'%self.name)
        return lottery.choice_once()

    def sayhello(self):
        return "say hello to %s" % MyTest.myname
  
    def spendRmbYears(self,year):
        spendRmbData=lottery.spend_years(year)
        #元组
        pay_in,pay_out=spendRmbData
        #字典
        #pay_in = spendRmbData['in']
        #pay_out  = spendRmbData['out']
        #列表
        #pay_in = spendRmbData[0]
        #pay_out  = spendRmbData[1]
        print("a day spend 2 RMB,then %s years late, you spent %i RMB, and earn %i RMB,so you cost %i RMB " % ( year,pay_out, pay_in,pay_out-pay_in))

if __name__ == "__main__":
   test = MyTest('John')
   outStr = test.start()
   print(outStr)
  
   print(test.sayhello())
   print(test.spendRmbYears(10))
   
