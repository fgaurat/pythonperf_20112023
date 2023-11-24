from collections import deque

def main():
    l = [10,20,30]
    print(l)
    l.append(40)
    print(l)
    last_value = l.pop()
    print(l)
    print(last_value)
    l.insert(0,0)
    print(l)
    first_value = l.pop(0)
    print(l)
    print(first_value)
    
    d = deque(l)
    print(d)
    d.append(40)
    d.appendleft(0)
    print(d)

if __name__=='__main__':
    main()
