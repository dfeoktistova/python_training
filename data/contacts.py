from model.contacts import Contact
# import random
# import string


testdata = [
    Contact(firstname="", middlename="", lastname="", nickname="", title="",
                    company="", address="", home="", mobile="", work_number="", fax="", email="", email2="",
                    email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5", amonth="July",
                    ayear="2022", address2="", phone2="", notes="")] + [
    Contact(firstname=("firstname", 10), middlename=("middlename", 10), lastname=("lastname", 10),
            nickname=("nickname", 10), title=("title", 10), company=("company", 10), address=("address", 10),
            home=("home_number", 10), mobile=("mobile_number", 10),
            work_number=("work_number", 10), fax=("fax", 10), email=("email", 10), email2=("email2",20),
            email3=("email3", 10), homepage=("homepage", 10), bday="10", bmonth="July", byear="2022",
            aday="10", amonth="July", ayear="2022", address2=("address2", 10), phone2=("phone2", 10),
            notes=("notes", 10))
    for i in range(5)
]