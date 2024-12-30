import pytest
from data import Users, Modules, Roles, Permissions


def test_user_flow():
    module = Modules()
    module.name = 'Testing'
    module.save()

    assert type(module.id) is int
    
    role = Roles()
    role.name = 'Tester'
    role.save()

    assert type(role.id) is int
   

    permission = Permissions()
    permission.role_id = role.id
    permission.module_id = module.id
    permission.can_write = True
    permission.can_read = True
    permission.can_update = True    
    permission.can_delete = True
    permission.save()

    assert type(permission.id) is int
   

    data = {
        'name': 'Tester',
        'lastname': 'Test lastname',
        'email': 'lllllll@gogo.com' , 
        'password': 'asdasdfsadff',
        'hash': 'asdasdfsadff',
        'role_id': role.id
    }

    user = Users(**data)
    user.save()

    assert type(user.id) is int
    print(user.__dict__)

    user.delete()
    permission.delete()
    role.delete()
    module.delete()