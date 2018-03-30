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


import inspect

import base
from conf import config

from selenium.common import exceptions as selenium_except
from selenium import webdriver
from selenium.webdriver.support.ui import Select

SET_BASE_URL = getattr(config, 'SET_BASE_URL')
RESOURCE_LIST = {
    "Global IP": "Global IP",
    'InterSecVM/SG(Ext)': 'InterSecVM/SG',
    'FortiGateVM(5.2.4)': 'FortiGateVM',
    'PaloAltoVM': 'PaloAltoVM',
    'InterSecVM/SG(Pub)': 'InterSecVM/SG',
    'FortiGateVM(5.4.1)': 'FortiGateVM',
    'InterSecVM/LB': 'InterSecVM/LB',
    'BIG-IP VE': 'BIG-IP VE',
    'vThunder(4.0.1)': 'vThunder',
    'vThunder(4.1.1)': 'vThunder',
    'Firefly': 'Firefly',
    'CSR1000v': 'Cisco',
    'CSR1000v (Encrypted)': 'Cisco',
    'CSR1000v (Unencrypted)': 'Cisco',
}

class ResourceOperations(base.SeleniumBase):
    def __init__(self, driver, evidence):
        super(ResourceOperations, self).__init__(driver, evidence)
        self.driver = driver
        self.evidence = evidence

    def check_list_resource(self):
        driver = self.driver

        # Show resource list
        self.list_resource()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_list_resource_before(self, input_params):
        driver = self.driver

        # Get filter key
        search_key = self._get_search_key(input_params)

        # Show resource list
        self.list_resource()
        driver.find_element_by_name("resource__filter__q").clear()
        driver.find_element_by_name("resource__filter__q").send_keys(search_key)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "resource_list", "before")

    def check_list_resource_after(self, input_params):
        driver = self.driver

        # Get filter key
        search_key = self._get_search_key(input_params)

        # Show resource list
        self.list_resource()
        driver.find_element_by_name("resource__filter__q").clear()
        driver.find_element_by_name("resource__filter__q").send_keys(search_key)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "resource_list", "after")

    def check_detail_resource(self, input_params):
        driver = self.driver

        # Show resource list
        self.detail_resource(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_list_resource_admin(self):
        driver = self.driver

        # Show resource list
        self.list_resource_admin()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_list_resource_admin_before(self, input_params):
        driver = self.driver

        # Get filter key
        search_key = self._get_search_key(input_params)

        # Show resource list
        self.list_resource_admin()
        driver.find_element_by_name("resource__filter__q").clear()
        driver.find_element_by_name("resource__filter__q").send_keys(search_key)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "admin_resource_list", "before")

    def check_list_resource_admin_after(self, input_params):
        driver = self.driver

        # Get filter key
        search_key = self._get_search_key(input_params)

        # Show resource list
        self.list_resource_admin()
        driver.find_element_by_name("resource__filter__q").clear()
        driver.find_element_by_name("resource__filter__q").send_keys(search_key)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "admin_resource_list", "after")

    def check_detail_resource_admin(self, input_params):
        driver = self.driver

        # Show resource list
        self.detail_resource_admin(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_create_resource(self):
        driver = self.driver

        # Check before change globalip status
        globalip_line = 0
        for num in range(1, 10):
            try:
                status = self.get_data_from_line(str(num), "1")
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "not_exist_globalip")
                raise Exception("There is no global IP that can be payout")
            if self.check_status(status, "Unacquired"):
                globalip_line = num
                break
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "not_exist_globalip")
            raise Exception("There is no global IP that can be payout")

        # Payout globalip operation
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "globalip_list", "before")
        driver.find_element_by_id("resource_globalip__action_create").click()
        self.sleep_time()
        driver.find_element_by_id("id_count").clear()
        driver.find_element_by_id("id_count").send_keys(1)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time()

        # Check result globalip list
        status = self.get_data_from_line(str(globalip_line), "1")
        if self.check_status(status, "Unused"):
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list", "after")
            pass
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list", "after")
            raise Exception("Status is invalid after payout of global IP")

    def check_update_resource_used(self):
        driver = self.driver

        # Check before change globalip status
        globalip_line = 0
        for num in range(1, 10):
            try:
                status = self.get_data_from_line(str(num), "1")
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "not_exist_globalip")
                raise Exception("There is no global IP that can be update status")
            if self.check_status(status, "Unused"):
                globalip_line = num
                break
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "not_exist_globalip")
            raise Exception("There is no global IP that can be update status")

        # Update globalip operation
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "globalip_list_unused_to_used", "before")
        driver.find_element_by_xpath("//tr[" + str(globalip_line) + "]/td[4]/div/a").click()
        self.sleep_time()
        Select(driver.find_element_by_id("status")).select_by_value("2")
        try:
            Select(driver.find_element_by_id("node_id")).select_by_index(0)
        except:
            driver.find_element_by_css_selector("input.btn.btn-primary").click()
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "input_params_unused_to_used_error")
            raise Exception("Parameter of change global IP is incorrect")

        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params_unused_to_used")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time()

        # Check result globalip list
        status = self.get_data_from_line(str(globalip_line), "1")
        if self.check_status(status, "Used"):
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list_unused_to_used", "after")
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list_unused_to_used", "after")
            raise Exception("Status is invalid after change global IP")

    def check_update_resource_unused(self):
        driver = self.driver

        # Check before change globalip status
        globalip_line = 0
        for num in range(1, 10):
            try:
                status = self.get_data_from_line(str(num), "1")
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "not_exist_globalip")
                raise Exception("There is no global IP that can be update status")
            if self.check_status(status, "Used"):
                globalip_line = num
                break
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "not_exist_globalip")
            raise Exception("There is no global IP that can be update status")

        # Update globalip operation
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "globalip_list_used_to_unused", "before")
        driver.find_element_by_xpath("//tr[" + str(globalip_line) + "]/td[4]/a").click()
        self.sleep_time()
        Select(driver.find_element_by_id("status")).select_by_value("0")
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params_used_to_unused")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time()

        # Check result globalip list
        status = self.get_data_from_line(str(globalip_line), "1")
        if self.check_status(status, "Unused"):
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list_used_to_unused", "after")
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list_used_to_unused", "after")
            raise Exception("Status is invalid after change global IP")

    def check_delete_resource(self):
        driver = self.driver

        # Check before change globalip status
        globalip_line = 0
        for num in range(1, 10):
            try:
                status = self.get_data_from_line(str(num), "1")
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "not_exist_globalip")
                raise Exception("There is no global IP that can be refund")
            if self.check_status(status, "Unused"):
                globalip_line = num
                break
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "not_exist_globalip")
            raise Exception("There is no global IP that can be refund")

        # Return globalip operation
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "globalip_list", "before")
        driver.find_element_by_xpath("//tr[" + str(globalip_line) + "]/td[4]/div/a[2]").click()
        driver.find_element_by_xpath("//li/button").click()
        self.sleep_time()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_link_text("Delete Resource").click()
        self.sleep_time(10)

        driver.refresh()
        # Check result globalip list
        status = self.get_data_from_line(str(globalip_line), "1")
        if self.check_status(status, "Unacquired"):
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list", "after")
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "globalip_list", "after")
            raise Exception("Status is invalid after refund global IP")

    def list_resource(self):
        # Show resource list
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/project/resource/")
        self.sleep_time()

    def list_resource_admin(self):
        # Show resource list for admin
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/admin/resource/")
        self.sleep_time()

    def detail_resource(self, input_params):
        # Show resource detail
        driver = self.driver
        self.list_resource()
        driver.find_element_by_link_text(input_params["resource_name"]).click()
        self.sleep_time()

    def detail_resource_admin(self, input_params):
        # Show resource detail for admin
        driver = self.driver
        self.list_resource_admin()
        driver.find_element_by_link_text(input_params["resource_name"]).click()
        self.sleep_time()

    def _get_search_key(self, input_params):
        # Get keywords to search in resource list
        search_key = ""
        if "device_type" in input_params:
            search_key = input_params["device_type"]
        elif "service_type" in input_params:
            search_key = input_params["service_type"]

        return RESOURCE_LIST.get(search_key, "")
