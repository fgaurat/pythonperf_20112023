def main():
    for i in range(10):
        print(i)
        if i == 5:
            print("ok")
            continue
        print('la suite',i)
    else:
        print("pas trouvé")
if __name__=='__main__':
    main()
