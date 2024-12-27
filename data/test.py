from models import Users




class User(ORM):
    pass

class Modules(ORM):
    pass

if __name__ == '__main__':
    user = User.find(id=1)
    #print(user.__dict__)
    user.name = 'Juan'
    user.save()

    data = {
        'name': 'Test',
        'lastname': 'Test lastname',
        'email': 't@t.com',
        'password': '123',
        'role_id': '6',

    }

    #user = User(**data)
    #user.save()
    #print(user.__dict__)


