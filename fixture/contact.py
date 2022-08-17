from model.contact import Contact
from selenium.webdriver.support.select import Select
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_1_value("bday", contact.bday)
        self.change_field_1_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_1_value("aday", contact.aday)
        self.change_field_1_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_1_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # open modification contact form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def edit_first_contact(self):
        wd = self.app.wd
        # select edit button
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_add_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    # находим количество контактов
    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                lastname = td[1].text
                firstname = td[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = td[3].text
                all_mails = td[4].text
                all_phones = td[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_mails_from_home_page=all_mails))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile,
                       work_number=work_number, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work_number=work_number, phone2=phone2)

