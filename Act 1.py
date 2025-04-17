class c1:
    __pvar=50
    def __method(self):
        print("inside class method")
    
    def f1(self):
        print("Private variable:",c1.__pvar)

ob=c1()
ob.f1()