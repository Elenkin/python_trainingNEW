from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.group import Group
import re

class contactHelper:

    def __init__(self, app):
        self.app = app

    def del_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def select_group_from_dropdown(self, group_id):
        wd = self.app.wd
        select = Select(wd.find_element_by_css_selector("[name='group']"))
        select.select_by_value("%s" % group_id)

    def del_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_from_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def del_from_modify_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_xpath("//input[@name='modifiy']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def details_modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_xpath("//input[@name='modifiy']").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact()
        self.contact_cache = None

    def details_modify_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_modify(index)
        wd.find_element_by_xpath("//input[@name='modifiy']").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact()
        self.contact_cache = None

    def select_contact_by_modify(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact()
        self.contact_cache = None

    def return_to_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contact()
        self.contact_cache = None

    def fill_form_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

    def count_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_page(self):
        wd = self.app.wd
        #if not ((wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_css_selector('[id="MassCB"]')) > 0):
            #return
        wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_elements_by_tag_name("td")[5].text
                address = element.find_elements_by_tag_name("td")[3].text
                all_email = element.find_elements_by_tag_name("td")[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, all_phones_from_home_page=all_phones,
                                                  address=address, all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        #fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work)

    def add_contact_in_group(self, contact_id, group_name):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        group_list = wd.find_element_by_name("to_group")
        select = Select(group_list)
        select.select_by_visible_text(group_name)
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def del_contact_from_group(self, contact_id, group):
        wd = self.app.wd
        group_list = wd.find_element_by_name("group")
        select = Select(group_list)
        select.select_by_visible_text(group)
        self.select_contact_by_id(contact_id)
        wd.implicitly_wait(10)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()
        self.contact_cache = None

    def get_contacts_in_group(self, group):
        wd = self.app.wd
        contacts_list = []
        group_list = wd.find_element_by_name("group")
        select = Select(group_list)
        select.select_by_visible_text(group)
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            contacts_list.append(Contact(id=id))
        return list(contacts_list)















