def main():
    # ZeroDivisionError : PascalCase  UpperCamelCase
    # zeroDivisionError : camelCase
    # zero_division_error : snake_case
    # zero-division-error : kebab-case
    
    try:
        a = int(input("valeur de a:"))
        b = 2
        c = b/a
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
    except Exception as e:
        print("Exception")   
        print(e,type(e))
    else:
        print("pas d'erreur")
    finally:
        print("finally")
        
    print("après les erreurs")
         
if __name__=='__main__':
    main()
