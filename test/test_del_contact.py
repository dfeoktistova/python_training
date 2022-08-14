# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_delele_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # удаляем из старого списка все элементы с 0 по 1 (правая граница не включается, т.е только элемент 0)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
