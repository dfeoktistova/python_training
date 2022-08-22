# -*- coding: utf-8 -*-
import random

from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test_group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # удаляем из старого списка все элементы с 0 по 1 (правая граница не включается, т.е только элемент 0)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)
