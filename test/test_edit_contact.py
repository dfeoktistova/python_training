from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.edit_first_contact()
    app.contact.fill_form(
        Contact(firstname="Иван_new", middlename="Иванов_new", lastname="Иванович_new", nickname="Ivanov_Ivan_new",
                title="q_new",
                company="w_new", address="e_new", home="555-55-551",
                mobile="8-921-666-66-661", work_number="9111", fax="6661", email="1a@ya.ru1", email2="2b@mail.ru1",
                email3="3c@rambler.com1",
                homepage="https://ru.wikipedia.org/wiki/1", bday="11", bmonth="April", byear="19801", aday="11",
                amonth="April", ayear="1991",
                address2="qwerty1", phone2="5551", notes="qwerty11"))
    app.contact.confirm_edit_first_contact()
    app.session.logout()
