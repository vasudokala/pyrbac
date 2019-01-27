# @Author: Vasu Dokala


"""Testing assignment and deletion of a Role to User
"""

from pyrbac import Role, User, AccessControlLayer

default_role = Role(1, name='default')
admin_role = Role(2, name='admin')

default_user = User("vasu",roles=[default_role])
admin_user = User("ashish", roles=[admin_role, default_role])


acl = AccessControlLayer()

resource1 = '/api/v0/accounts/info'
resource2 = '/api/v0/accounts/1/'

acl.add_read_permisson(default_role, 'GET', resource1)
acl.add_delete_permisson(admin_role, 'DELETE', resource2)


class TestRoleAssignmentDeletion:

    def test_role_assignment(self):
        """Creates the roles which need to be assigned to users
        """
        assert [role.get_name() for role in default_user.get_roles()] == ['default']
        assert [role.get_name() for role in admin_user.get_roles()].sort() == ['admin', 'default'].sort()

    def test_delete_role_from_user(self):
        """Tests the function to delete a role from a user
        """
        anonymous_user = User(uid="vasu", roles=[default_role, admin_role])
        anonymous_user.remove_role(default_role)
        assert 'default' not in [role.get_name() for role in anonymous_user.get_roles()]


class TestPermissions():

    def test_read_rule_everyone(self):
        for role in default_user.get_roles():
            assert acl.is_read_allowed(role, 'GET', resource1) is True

    def test_write_rule_everyone(self):
        for role in default_user.get_roles():
            assert acl.is_write_allowed(role, 'WRITE', resource1) is False

    def test_delete_rule_admin(self):

        for role in default_user.get_roles():
            if role.get_name() == 'admin':
                assert acl.is_delete_allowed(role, 'DELETE', resource2) is True
            else:
                assert acl.is_delete_allowed(role, 'DELETE', resource2) is False
