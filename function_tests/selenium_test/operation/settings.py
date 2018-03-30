#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#  
#       http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
#  
#  COPYRIGHT  (C)  NEC  CORPORATION  2017
#  


import base
from conf import config
import urllib

from selenium import webdriver
from selenium.webdriver.support.ui import Select

SET_BASE_URL = getattr(config, 'SET_BASE_URL')
SET_LANGUAGE = getattr(config, "SET_LANGUAGE", "en")
USER_NAME = getattr(config, 'USER_NAME')
USER_PASSWORD = getattr(config, 'USER_PASSWORD')
PROJECT_NAME = getattr(config, 'PROJECT_NAME')
SET_GLOBAL_BASE_URL = getattr(config, 'SET_GLOBAL_BASE_URL')
ADMIN_USER_NAME = getattr(config, 'ADMIN_USER_NAME')
ADMIN_USER_PASSWORD = getattr(config, 'ADMIN_USER_PASSWORD')
ADMIN_PROJECT_NAME = getattr(config, 'ADMIN_PROJECT_NAME')
CREATE_ROLE_LIST = getattr(config, 'CREATE_ROLE_LIST')
SET_ROLE_LIST = getattr(config, 'SET_ROLE_LIST')
ADMIN_ROLE_LIST = getattr(config, 'ADMIN_ROLE_LIST')


class SettingOperations(base.SeleniumBase):
    def __init__(self, driver, evidence):
        super(SettingOperations, self).__init__(driver, evidence)
        self.driver = driver
        self.evidence = evidence

    def sign_in(self):
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/auth/login/?next=/dashboard/")
        self.sleep_time()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(USER_NAME)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(USER_PASSWORD)
        driver.find_element_by_id("loginBtn").click()
        self.sleep_time()

    def global_sign_in(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/auth/login/?next=/dashboard/")
        self.sleep_time()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(ADMIN_USER_NAME)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(ADMIN_USER_PASSWORD)
        driver.find_element_by_id("loginBtn").click()
        self.sleep_time()

    def change_project(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "//a[contains(@href, '#')]").click()
        self.sleep_time()
        driver.find_element_by_link_text(PROJECT_NAME).click()
        self.sleep_time()

    def global_change_project(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "//a[contains(@href, '#')]").click()
        self.sleep_time()
        driver.find_element_by_link_text(ADMIN_PROJECT_NAME).click()
        self.sleep_time()

    def change_setting(self):
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/settings/")
        self.sleep_time()
        Select(driver.find_element_by_id(
            'id_language')).select_by_value(SET_LANGUAGE)
        driver.find_element_by_css_selector("input[type=submit]").click()
        self.sleep_time()

    def global_change_setting(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/settings/")
        self.sleep_time()
        Select(driver.find_element_by_id(
            'id_language')).select_by_value(SET_LANGUAGE)
        driver.find_element_by_css_selector("input[type=submit]").click()
        self.sleep_time()

    def create_user(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/identity/users/")
        self.sleep_time()
        driver.find_element_by_id("users__action_create").click()
        self.sleep_time()

        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(USER_PASSWORD)
        driver.find_element_by_id("id_confirm_password").clear()
        driver.find_element_by_id("id_confirm_password").send_keys(USER_PASSWORD)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(USER_NAME)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time()

    def create_role(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/identity/roles/")
        self.sleep_time()
        for role in CREATE_ROLE_LIST:
            driver.find_element_by_id("roles__action_create").click()
            self.sleep_time()
            driver.find_element_by_id("id_name").clear()
            driver.find_element_by_id("id_name").send_keys(role)
            driver.find_element_by_css_selector("input.btn.btn-primary").click()
            self.sleep_time()

    def create_project(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/identity/")
        self.sleep_time()
        driver.find_element_by_id("tenants__action_create").click()
        self.sleep_time()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(PROJECT_NAME)
        driver.find_element_by_link_text("Project Members").click()
        self.sleep_time()

        for user_count in range(1, 100):
            disp_user = driver.find_element_by_xpath(
                "//div[@id='available_update_members']/ul/ul[" + str(user_count) + "]/li[1]/span").text
            if USER_NAME == disp_user:
                driver.find_element_by_xpath("(//a[contains(text(), '+')])[" + str(user_count) + "]").click()
                self.sleep_time()
                break

        driver.find_element_by_xpath("//div[@id='update_members_members']/ul/ul/li[3]/a").click()

        role_set_count = len(SET_ROLE_LIST)
        for role_count in range(1, 30):
            disp_role = driver.find_element_by_xpath(
                "//div[@id='update_members_members']/ul/ul/li[3]/ul/li[" + str(role_count) + "]").text

            if role_count == 16:
                client_height = driver.execute_script('return document.getElementsByClassName("update_members_filterable")[1].clientHeight;')
                scroll_height = driver.execute_script('return document.getElementsByClassName("update_members_filterable")[1].scrollHeight;')
                if scroll_height > client_height:
                    driver.execute_script('document.getElementsByClassName("update_members_filterable")[1].scrollTop = ' + str(scroll_height) + ';')

            if disp_role in SET_ROLE_LIST:
                driver.find_element_by_xpath(
                    "//div[@id='update_members_members']/ul/ul/li[3]/ul/li[" + str(role_count) + "]").click()
                self.sleep_time()
                role_set_count = role_set_count - 1
                if role_set_count == 0:
                    break

        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(15)

    def add_admin_user(self):
        driver = self.driver
        driver.get(SET_GLOBAL_BASE_URL + "/dashboard/identity/")
        self.sleep_time()

        for num in range(1, 100):
            project_name = self.get_data_from_line(str(num), "2")
            if project_name == PROJECT_NAME:
                break
        project_count = num

        # Add admin user to project
        try:
            driver.find_element_by_xpath("//tr[" + str(project_count) + "]/td[7]/a[1]").click()
        except:
            driver.find_element_by_xpath("//tr[" + str(project_count) + "]/td[7]/div/a[1]").click()
        self.sleep_time()

        for user_count in range(1, 100):
            disp_user = driver.find_element_by_xpath(
                "//div[@id='available_update_members']/ul/ul[" + str(user_count) + "]/li[1]/span").text
            if ADMIN_USER_NAME == disp_user:
                driver.find_element_by_xpath("(//a[contains(text(), '+')])[" + str(user_count) + "]").click()
                self.sleep_time()
                break

        driver.find_element_by_xpath("//div[@id='update_members_members']/ul/ul[2]/li[3]/a").click()
        self.sleep_time()

        role_set_count = len(ADMIN_ROLE_LIST)
        for role_count in range(1, 30):
            disp_role = driver.find_element_by_xpath(
                "//div[@id='update_members_members']/ul/ul[2]/li[3]/ul/li[" + str(role_count) + "]").text

            if role_count == 16:
                client_height = driver.execute_script('return document.getElementsByClassName("update_members_filterable")[1].clientHeight;')
                scroll_height = driver.execute_script('return document.getElementsByClassName("update_members_filterable")[1].scrollHeight;')
                if scroll_height > client_height:
                    driver.execute_script('document.getElementsByClassName("update_members_filterable")[1].scrollTop = ' + str(scroll_height) + ';')

            if disp_role in ADMIN_ROLE_LIST:
                driver.find_element_by_xpath(
                    "//div[@id='update_members_members']/ul/ul[2]/li[3]/ul/li[" + str(role_count) + "]").click()
                self.sleep_time()
                role_set_count = role_set_count - 1
                if role_set_count == 0:
                    break

        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(15)

    def create_network(self, input_params):
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/project/networks/")
        self.sleep_time()
        driver.find_element_by_id("networks__action_create").click()
        self.sleep_time()
        driver.find_element_by_name("net_name").clear()
        driver.find_element_by_name("net_name").send_keys(input_params['net_name'])
        driver.find_element_by_link_text("Subnet").click()
        self.sleep_time()
        driver.find_element_by_name("subnet_name").clear()
        driver.find_element_by_name("subnet_name").send_keys(input_params['subnet_name'])
        driver.find_element_by_name("cidr").clear()
        driver.find_element_by_name("cidr").send_keys(input_params['network_address'])
        driver.find_element_by_xpath("//button[2]").click()
        self.sleep_time()
        driver.find_element_by_xpath("//button[3]").click()
        self.sleep_time()

    def add_subnet(self, input_params):
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/project/networks/")
        self.sleep_time()
        driver.find_element_by_link_text(input_params['net_name']).click()
        self.sleep_time()
        try:
            driver.find_element_by_link_text("Subnets").click()
        except:
            pass
        driver.find_element_by_link_text("Create Subnet").click()
        self.sleep_time()
        driver.find_element_by_name("subnet_name").clear()
        driver.find_element_by_name("subnet_name").send_keys(input_params['subnet_name'])
        driver.find_element_by_name("cidr").clear()
        driver.find_element_by_name("cidr").send_keys(input_params['network_address'])
        self.param_select("ip_version", "IPv6")
        self.sleep_time()
        driver.find_element_by_xpath("//button[2]").click()
        self.sleep_time()
        driver.find_element_by_xpath("//button[3]").click()
        self.sleep_time()

    def sign_out(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "//div[@id='navbar-collapse']/ul[2]/li/a/span[2]").click()
        self.sleep_time()
        driver.find_element_by_link_text("Sign Out").click()
        self.sleep_time()
