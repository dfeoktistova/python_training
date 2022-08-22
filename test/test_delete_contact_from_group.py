import random
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group


database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_some_contact_from_group(app, db):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='1', header='2'))

    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts = database.get_contacts_in_group(group)

    if len(db.get_contact_list()) == 0 or len(old_contacts) == 0:
        app.contact.create(Contact(firstname="Test", middlename="", lastname="", nickname="", title="", company="",
                                   address="", home="", mobile="", work_number="", fax="", email="", email2="",
                                   email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                                   amonth="July", ayear="2022", address2="", phone2="", notes=""))
        old_contacts = database.get_contacts_in_group(group)

    contacts = [contact for contact in database.get_contacts_in_group(group)
                if contact in old_contacts]

    contact = random.choice(contacts)

    app.contact.remove_contact_from_group(group_name=group.group_name, contact_id=contact.contact_id)
    new_contacts = database.get_contacts_in_group(group)

    assert contact not in new_contacts
    assert len(old_contacts) - 1 == len(new_contacts)