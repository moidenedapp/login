import datetime

class Permission():
    name: str
    can_update: bool
    can_write: bool
    can_delete: bool
    can_read: bool


class User():
    name : str
    lastname :str
    email : str
    role : str
    password : str
    created_at : datetime
    updated_at : datetime
    permissions : [Permission] # type: ignore

    def login(self, password):
        return self.password == password
    
