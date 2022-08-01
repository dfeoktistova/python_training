# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.fill_form(Contact(firstname="Иван", middlename="Иванов", lastname="Иванович", nickname="Ivanov_Ivan", title="q", company="w", address="e", home="555-55-55",
                                  mobile="8-921-666-66-66", work_number="911", fax="666", email="1a@ya.ru", email2="2b@mail.ru", email3="3c@rambler.com",
                                  homepage="https://ru.wikipedia.org/wiki/", bday="1", bmonth="January", byear="1980", aday="1", amonth="January", ayear="1990",
                                  address2="qwerty", phone2="555", notes="qwerty1"))
    app.return_to_home_page()
    app.session.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.fill_form(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                                  mobile="", work_number="", fax="", email="", email2="", email3="",
                                  homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                                  address2="", phone2="", notes=""))
    app.return_to_home_page()
    app.session.logout()

