from UserDAO import UserDAO


def filter_male(gen):
    for u in gen:
        if u.gender == "Male":
            yield u

def main():
    with UserDAO(r'tp08\formation.db') as dao:
    # dao  = UserDAO(r'tp08\formation.db')
        users = dao.findAll()
        male_users = filter_male(users)
        raise Exception("Erreur ")
        # print(list(male_users) )
        # print(next(users))    
        # for u in male_users:
        #     print(u)
if __name__=='__main__':
    main()
