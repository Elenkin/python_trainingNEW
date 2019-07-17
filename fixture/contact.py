
class contactHelper:

    def __init__(self, app):
        self.app = app

    def del_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def del_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def del_from_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def del_from_modify_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_xpath("//input[@name='modifiy']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def details_modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_xpath("//input[@name='modifiy']").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact()

    def edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact()

    def return_to_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

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
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        #select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        #select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
