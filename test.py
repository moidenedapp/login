from data import ORM
from data.models import Users, Modules, Roles, Permissions

if __name__ == '__main__':

    module = Modules()
    module.name = 'Testing'
    module.save()

    role = Roles()
    role.name = 'Tester'
    role.save()

    permission = Permissions()
    permission.role_id = role.id
    permission.module_id = module.id
    permission.can_write = True
    permission.can_read = True
    permission.can_update = True    
    permission.can_delete = True
    permission.save()

    data = {
        'name': 'Tester',
        'lastname': 'Test lastname',
        'email': 'tester@gogo.com' , 
        'password': 'asdasdfsadff',
        'hash': 'asdasdfsadff',
        'role_id': role.id
    }

    user = Users(**data)
    user.save()
    print(user.__dict__)