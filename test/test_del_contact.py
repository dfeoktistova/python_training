# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delele_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    app.contact.delete_first_contact()
