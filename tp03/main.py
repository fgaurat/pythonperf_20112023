import traceback

class DivBy12Error(Exception):

    def __init__(self):
        super().__init__("Division par 12!")


def div(a,b):
    if b == 12:
        e = DivBy12Error()
        raise e
    return  a/b

def call_div(a,b):
    c=0
    
    try:
        print('open log')
        c = div(a,b)    
    finally:
        print('close log')
        
    
    
    return c


def main():
    
    try:
        a = 2
        b = 12
        c = call_div(a,b)
        print(c)
    # except ZeroDivisionError as e:
    #     print("ZeroDivisionError")   
    #     print(e,type(e))
    # except TypeError as e:
    #     print("TypeError")   
    #     print(e,type(e))
    # except ValueError as e:
    #     print("ValueError")   
    #     print(e,type(e))

    except DivBy12Error as e:
        print("DivBy12Error")   
        traceback.print_exc()
        print(e,type(e))
    except Exception as e:
        print("Exception")   
        traceback.print_exc()
        print(e,type(e))
    else:
        print("pas d'erreur")
    finally:
        print("finally")
        
    print("après les erreurs")
         
if __name__=='__main__':
    main()
