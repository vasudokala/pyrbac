# pyrbac
Rule based access control
## Demo

### Role creation and assignment of role to a User

```python
from pyrbac import Role, User


default_role = Role(1, name='default')
admin_role = Role(2, name='admin')

default_user = User("vasu",roles=[default_role])
admin_user = User("ashish", roles=[admin_role, default_role])
```

### User resource access permissions

```python
from pyrbac import AccessControlLayer, User, Role

acl = AccessControlLayer()

resource1 = '/api/v0/accounts/info'
resource2 = '/api/v0/accounts/1/'

acl.add_read_permisson(default_role, 'GET', resource1)
acl.add_delete_permisson(admin_role, 'DELETE', resource2)


# checking READ operation on resource for user `default_user`
for role in default_user.get_roles():
  assert acl.is_read_allowed(role, 'GET', resource1) is True


# checking WRITE operation on resource for user `everyone_user`
for role in default_user.get_roles():
  assert acl.is_write_allowed(role, 'WRITE', resource1) is False
