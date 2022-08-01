from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.group.fill_form(Group(name="qw_new", header="wq_new"))
    app.group.confirm_edit_first_group()
    app.group.return_to_groups_page()
    app.session.logout()
