import sys
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal

class Human(QObject):
    nameChange=pyqtSignal(str)
    ageChange=pyqtSignal([int],[str])
    def __init__(self, name='Mike',age=10,parent=None):
        super().__init__(parent=parent)
        self.setAge(age)
        self.setName(name)
    def setAge(self,age):
        self.__age=age
        self.ageChange.emit(self.__age)
        if age<=18:
            ageInfo='youngster'
        elif 18<age<=35:
            ageInfo='young adult'
        elif (35<age<=55):
            ageInfo='adult'
        elif (age>55):
            ageInfo='elder'
        self.ageChange[str].emit(ageInfo)
    def setName(self,name):
        self.__name=name
        self.nameChange.emit(self.__name)

class Responsor(QObject):
    @pyqtSlot(int)
    def do_agechange_int(self,age):
        print('age:',str(age))
    @pyqtSlot(str)
    def do_agechange_str(self,ageInfo):
        print(ageInfo)
    @pyqtSlot(str)
    def do_nameChanged(self,name):
        print("Hello,"+str(name))

if __name__=="__main__":
    print('create objective...')
    boy=Human('Boy',16)
    resp=Responsor()
    boy.nameChange.connect(resp.do_nameChanged)

    #overload signal
    boy.ageChange[int].connect(resp.do_agechange_int)
    boy.ageChange[str].connect(resp.do_agechange_str)

    print('building relation...')
    boy.setAge(35)
    boy.setName('Jack')

    boy.ageChange[str].disconnect(resp.do_agechange_str)
    print('break relation...')
    
    boy.setAge(10)




