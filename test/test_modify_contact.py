from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.modify_first_contact(
        Contact(firstname="Иван_new"))


def test_edit_contact_middlename(app):
    app.contact.modify_first_contact(
        Contact(middlename="Иванов_new"))

def test_edit_contact_lastname(app):
    app.contact.modify_first_contact(
        Contact(lastname="Иванович_new"))

def test_edit_contact_nickname(app):
    app.contact.modify_first_contact(
        Contact(nickname="Ivanov_Ivan_new"))

def test_edit_contact_title(app):
    app.contact.modify_first_contact(
        Contact(title="q_new"))

def test_edit_contact_company(app):
    app.contact.modify_first_contact(
        Contact(company="w_new"))

def test_edit_contact_address(app):
    app.contact.modify_first_contact(
        Contact(address="e_new"))

def test_edit_contact_home(app):
    app.contact.modify_first_contact(
        Contact(home="555-55-551"))

def test_edit_contact_mobile(app):
    app.contact.modify_first_contact(
        Contact(mobile="8-921-666-66-661"))

def test_edit_contact_work_number(app):
    app.contact.modify_first_contact(
        Contact(work_number="9111"))

def test_edit_contact_fax(app):
    app.contact.modify_first_contact(
        Contact(fax="6661"))

def test_edit_contact_email(app):
    app.contact.modify_first_contact(
        Contact(email="1a@ya.ru1"))


def test_edit_contact_email2(app):
    app.contact.modify_first_contact(
        Contact(email2="2b@mail.ru1"))


def test_edit_contact_email3(app):
    app.contact.modify_first_contact(
        Contact(email3="3c@rambler.com1"))


def test_edit_contact_homepage(app):
    app.contact.modify_first_contact(
        Contact(homepage="https://ru.wikipedia.org/wiki/1"))


def test_edit_contact_bday(app):
    app.contact.modify_first_contact(
        Contact(bday="11"))


def test_edit_contact_bmonth(app):
    app.contact.modify_first_contact(
        Contact(bmonth="April"))


def test_edit_contact_byear(app):
    app.contact.modify_first_contact(
        Contact(byear="19801"))


def test_edit_contact_aday(app):
    app.contact.modify_first_contact(
        Contact(aday="11"))


def test_edit_contact_amonth(app):
    app.contact.modify_first_contact(
        Contact(amonth="April"))


def test_edit_contact_ayear(app):
    app.contact.modify_first_contact(
        Contact(ayear="1991"))


def test_edit_contact_address2(app):
    app.contact.modify_first_contact(
        Contact(address2="qwerty1"))


def test_edit_contact_phone2(app):
    app.contact.modify_first_contact(
        Contact(phone2="5551"))


def test_edit_contact_notes(app):
    app.contact.modify_first_contact(
        Contact(notes="qwerty11"))