# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delele_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
