def add(*l):
    print(l)
    r=0
    for i in l:
        r+=i
    return r        
    
def hello(**data):
    print(data)
    print("hello",data['name'],data['firstname'])

def hello2(*,name,firstname):
    print(data)
    print("hello",name,firstname)


def the_function():
    a = 2
    b = 3
    return a,b


def mult2(l):
    result = [i*2 for i in l]
    # for i in l:
    #     result.append(i*2)
    
    return result


def map_malt2(i):
    return i*2   
    
def main():
    l = [10,20,30]
    r = add(*l) #60
    r = add(10,20,30) #60
    print(r)
    
    l = [10,20,30,40,50,60]
    a,b,c,*lereste = l
    print(a,b,c,lereste)
    
    
    hello(name="GAURAT",firstname="Fred")
    
    d = {
        "name":"GAURAT",
        "firstname":"Fred"
    }
    
    hello(**d)
    
    print(50*'-')
    
    a,b=1,2
    print(a,b)
    d,e = the_function()
    print(d,e)
    print(50*'-')
    l = [10,20,30]
    # l2 = mult2(l) 
# def map_malt2(i):
#     return i*2    
    
    m2 = lambda i:i*2   
    l2 = list(map(m2, l))
    i = m2(5)
    print(type(m2))
    print(l2) # [20 40 60]
    dirty_l = ["   value 1","value 2    ","   value 3   "]
    clean_l = [i.strip() for i in dirty_l]
    print(dirty_l)
    print(clean_l)
    
if __name__=='__main__':
    main()
