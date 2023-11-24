class A:
    def show(self):
        print("A")

class A1:
    def show(self):
        print("A1")

class B(A,A1):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    def show(self):
        print("D")
        super(A,self).show()
        # super(B,self).show()


    

def main():
    d = D()
    print(D.mro())
    d.show()

if __name__=='__main__':
    main()
