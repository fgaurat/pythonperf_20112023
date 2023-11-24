import copy
import mon_module as mm
from mon_module import hello as h
from mon_module import *
import mon_package.autre_module

def hello(name):
    print("main")
    
a="tutu"
def main():
    global a
    b = "toto"
    # b[0] = "T"
    print(b)
    
    c=3
    d=3
    print("c",c,hex(id(c)))
    print("d",d,hex(id(d)))
    
    c=4
    print(c,hex(id(c)))
    print(50*'-')   
    d = "valeur de c : "+str(c)
    print(d)
    l = [10,20,30,40,50]
    l1 = l[1:4] # [1:4[
    l1 = l[:3]
    l1 = l[3:]
    l1 = l[:]
    print(l)
    print(l1)
    l1 = l[:]
    l[0] = 1000
    print(l)
    print(l1)
    print(50*'-')  
    l =[
        [10,20],
        [40,40],
        [50,60],
    ] 
    l1 = l[:] # shallow copy
    # l1 = l.copy() # shallow copy
    # l1 = copy.copy(l) # shallow copy
    
    # import copy
    l1 = copy.deepcopy(l)
    
    l[0][0] = 1000
    print(l)
    print(l1)

    # import mon_module as mm
    # mon_module.hello("fred")
    # mm.hello("fred")
    # from  mon_module import hello
    hello("fred")
    mon_package.autre_module.hello("name")
if __name__=='__main__':
    main()
