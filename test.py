from data import ORM

class Users(ORM):
    pass

class Modules(ORM) :
    pass


if __name__ == '__main__':
    user = Users.find(id=8)
    user.delete()

    data = {
        'name': 'Test',
        'lastname': 'Test lastname',
        'email': 'gogo@gogo.com' , 
        'password': 'asdasdfsadff',
        'hash': 'asdasdfsadff',
        'role_id':6
    }

    # user = Users(**data)
    # user.save()
    # print(user.__dict__)

