from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test_contact", middlename="", lastname="", nickname="", title="",
                                   company="", address="", home="", mobile="", work_number="", fax="", email="",
                                   email2="", email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                                   amonth="July", ayear="2022", address2="", phone2="", notes=""))
    app.contact.open_contact_page()
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Test_contact", middlename="", lastname="", nickname="", title="",
                      company="", address="", home="", mobile="", work_number="", fax="", email="",
                      email2="", email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                      amonth="July", ayear="2022", address2="", phone2="", notes="")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    app.contact.open_contact_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


"""def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="Иванов_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Иванович_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(nickname="Ivanov_Ivan_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title="q_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(company="w_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address="e_new"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_home(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact( Contact(home="555-55-551"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact( Contact(mobile="8-921-666-66-661"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_work_number(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(work_number="9111"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_fax(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(fax="6661"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email="1a@ya.ru1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email2="2b@mail.ru1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_email3(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email3="3c@rambler.com1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(homepage="https://ru.wikipedia.org/wiki/1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(bday="11"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_bmonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact( Contact(bmonth="April"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_byear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact( Contact(byear="19801"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(aday="11"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(amonth="April"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_ayear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(ayear="1991"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_address2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address2="qwerty1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_phone2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(phone2="5551"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_notes(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(notes="qwerty11"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)"""
