import random
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from model.contact_in_group import ContactInGroup

database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header"))
    group_ = db.get_group_list()
    group = random.choice(group_)
    old_contacts = database.get_contacts_in_group(group)
    contacts = [contact for contact in database.get_contacts_not_in_group(group)
                if contact not in old_contacts]
    if len(db.get_contact_list()) == 0 or len(contacts) == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", nickname="", title="", company="",
                                   address="", home="", mobile="", work_number="", fax="", email="", email2="",
                                   email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                                   amonth="July", ayear="2022", address2="", phone2="", notes=""))
        contacts = database.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(group_name=group.name, contact_id=contact.id)
    new_contacts = database.get_contacts_in_group(group)
    assert sorted(old_contacts, key=ContactInGroup.id_max) == sorted(new_contacts, key=ContactInGroup.id_max)