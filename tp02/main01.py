

def make_incrementor(inc):
    
    def inc_value(value_to_inc):
        return inc+value_to_inc

    def mult_value(value_to_inc):
        return inc*value_to_inc
    
    return inc_value,mult_value

def main():
    inc,mult = make_incrementor(10)
    a = inc(5)
    b = mult(5)
    print(a) # 15
    print(b) # 50

if __name__=='__main__':
    main()
