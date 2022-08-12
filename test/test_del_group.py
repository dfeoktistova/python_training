# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # удаляем из старого списка все элементы с 0 по 1 (правая граница не включается, т.е только элемент 0)
    old_groups[0:1] = []
    assert old_groups == new_groups
