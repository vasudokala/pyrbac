# -*- coding: utf-8 -*-
# @Author: Vasu Dokala

from pyrbac import Permisson


class AccessControlLayer:
    """
    Defines the detailed access control rules
    
    If a role is not given an explicit resource authorisation, it's rejected by default. Rule of Least privileges.
    """

    def __init__(self):
        self._read_perm = []
        self._write_perm = []
        self._delete_perm = []

    def add_read_permisson(self, role, method, resource):
        permission = Permisson(role, method, resource)
        if permission not in self._read_perm:
            self._read_perm.append(permission.get_perm_key())

    def add_write_permisson(self, role, method, resource):
        permission = Permisson(role, method, resource)
        if permission not in self._read_perm:
            self._read_perm.append(permission.get_perm_key())

    def add_delete_permisson(self, role, method, resource):
        permission = Permisson(role, method, resource)
        if permission not in self._read_perm:
            self._read_perm.append(permission.get_perm_key())

    def is_read_allowed(self, role, method, resource):
        permission = Permisson(role, method, resource)
        return permission.get_perm_key() in self._read_perm

    def is_write_allowed(self, role, method, resource):
        permission = Permisson(role, method, resource)
        return permission.get_perm_key() in self._write_perm

    def is_delete_allowed(self, role, method, resource):
        permission = Permisson(role, method, resource)
        return permission.get_perm_key() in self._delete_perm
