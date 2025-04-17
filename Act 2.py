class computer:
    def __init__(self):
        self.__mp=50000
    def sell(self):
        print("price:",self.__mp)

    def setmp(self,p):
        self.__mp=p

ob=computer()
ob.sell()
ob.__mp=70000
ob.sell()
ob.setmp(60000)
ob.sell()