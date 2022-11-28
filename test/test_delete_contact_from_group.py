import random
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from model.contact_in_group import ContactInGroup

database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='1', header='2'))
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", nickname="", title="", company="",
                                   address="", home="", mobile="", work_number="", fax="", email="", email2="",
                                   email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                                   amonth="July", ayear="2022", address2="", phone2="", notes=""))
    old_list_contact = database.get_groups_with_contacts()
    group = random.choice(old_list_contact)
    contact_in_group = database.get_contacts_in_group(group)
    contact = random.choice(contact_in_group)
    app.contact.delete_contact_from_group(contact.id, group)
    new_list_contact_in_group = database.get_contacts_in_group(group)
    contact_in_group.remove(contact)
    assert contact_in_group == new_list_contact_in_group