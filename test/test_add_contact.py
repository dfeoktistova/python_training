from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                    company="", address="", home="", mobile="", work_number="", fax="", email="", email2="",
                    email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5", amonth="July", ayear="2022",
                    address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 5),
          lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
          title=random_string("title", 5), address=random_string("address", 5),
          home=random_string("home", 5), mobile=random_string("mobile", 5),
          work_number=random_string("work_number", 5), fax=random_string("fax", 5), email=random_string("email", 5),
          email2=random_string("email2", 5), email3=random_string("email3", 5), homepage=random_string("homepage", 5),
          bday="20", bmonth="July", byear="2022", aday="5", amonth="July", ayear="2022",
          address2=random_string("address2", 5), phone2=random_string("phone2", 5),
          notes=random_string("notes", 5))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

