from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_group"))
    app.group.modify_first_group(Group(name="Test_group1"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_group"))
    app.group.modify_first_group(Group(header="Test_group1"))
