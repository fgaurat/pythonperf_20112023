

def do_log(prefix=""):
    def wrapper_deco(func):
        print("do_log",func)
        def wrapper(*args,**kwargs):
            print(prefix,"args",args,kwargs)
            r = func(*args,**kwargs)
            print(prefix,"return",r)
            return r
        return wrapper
    return wrapper_deco

@do_log('LOG')
def say_hello(name):
    r = f"Hello {name}"
    return r

@do_log('LOG_GOODBYE')
def say_goodbye(name):
    r = f"Goodbye {name}"
    return r

def main():
    r = say_hello("Fred")
    print(r)
    r = say_goodbye("Fred")
    print(r)
    
    
    

if __name__=='__main__':
    main()
