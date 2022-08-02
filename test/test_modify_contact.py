from model.contact import Contact


def test_edit_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(firstname="Иван_new"))
    app.session.logout()


def test_edit_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(middlename="Иванов_new"))
    app.session.logout()

def test_edit_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(lastname="Иванович_new"))
    app.session.logout()

def test_edit_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(nickname="Ivanov_Ivan_new"))
    app.session.logout()

def test_edit_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(title="q_new"))
    app.session.logout()

def test_edit_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(company="w_new"))
    app.session.logout()

def test_edit_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(address="e_new"))
    app.session.logout()

def test_edit_contact_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(home="555-55-551"))
    app.session.logout()

def test_edit_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(mobile="8-921-666-66-661"))
    app.session.logout()

def test_edit_contact_work_number(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(work_number="9111"))
    app.session.logout()

def test_edit_contact_fax(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(fax="6661"))
    app.session.logout()

def test_edit_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(email="1a@ya.ru1"))
    app.session.logout()


def test_edit_contact_email2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(email2="2b@mail.ru1"))
    app.session.logout()


def test_edit_contact_email3(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(email3="3c@rambler.com1"))
    app.session.logout()


def test_edit_contact_homepage(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(homepage="https://ru.wikipedia.org/wiki/1"))
    app.session.logout()


def test_edit_contact_bday(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(bday="11"))
    app.session.logout()


def test_edit_contact_bmonth(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(bmonth="April"))
    app.session.logout()


def test_edit_contact_byear(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(byear="19801"))
    app.session.logout()


def test_edit_contact_aday(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(aday="11"))
    app.session.logout()


def test_edit_contact_amonth(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(amonth="April"))
    app.session.logout()


def test_edit_contact_ayear(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(ayear="1991"))
    app.session.logout()


def test_edit_contact_address2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(address2="qwerty1"))
    app.session.logout()


def test_edit_contact_phone2(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(phone2="5551"))
    app.session.logout()


def test_edit_contact_notes(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(notes="qwerty11"))
    app.session.logout()