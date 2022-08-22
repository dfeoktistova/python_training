import random
from model.contact import Contact
from model.group import Group


def test_delete_some_contact_from_group(app, db, json_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test_group"))
    old_contacts = db.get_groups_with_contacts()
    group = random.choice(old_contacts)
    contact_in_group = get_groups_with_contacts(group)
    contact = random.choice(contact_in_group)
    app.contact.delete_contact_from_group(contact.id, group)
    new_list_contact_in_group = orm.get_contacts_in_group(group)
    contact_in_group.remove(contact)
    assert user_in_group == new_list_contact_in_group