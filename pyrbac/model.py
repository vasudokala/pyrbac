# -*- coding: utf-8 -*-
# @Author: Vasu Dokala


class Role:
    """roles which are associated to permissions to access resources
    """
    def __init__(self, id, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description,

    def get_name(self):
        return self.name

    def __repr__(self):
        return '<Role %s>' % self.name


class Permisson:
    def __init__(self, role, method, resource):
        self.role = role
        self.method = method
        self.resource = resource

    def get_perm_key(self):
        return self.role.id + self.method + self.resource


class User:
    def __init__(self, uid=None, password=None, role_constraints=None, roles=[], groups =[]):
        self.uid = uid
        self.password = password
        self.role_constraints = role_constraints
        self.roles = set(roles)
        self.groups = groups

    def add_role(self, role):
        """
        Adds the role to this user
        
        """
        self.roles.add(role)

    def add_roles(self, roles):
        """Add roles to this user.
        """
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        """Returns a generator object for the roles held by the User
        """
        for role in self.roles:
            yield role

    def remove_role(self, role):
        """Remove a role assigned to a User

        """
        if role in self.roles:
            self.roles.remove(role)

    def __repr__(self):
        return '<User %s>' % self.uid
