# -*- coding: utf-8 -*-
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


import copy
import inspect

import base
from conf import config
import urllib

from selenium.common import exceptions as selenium_except
from selenium import webdriver
from selenium.webdriver.support.ui import Select

SET_BASE_URL = getattr(config, 'SET_BASE_URL')
SET_CREATE_WAITTIME = getattr(config, "SET_CREATE_WAITTIME")
SET_CREATE_RETRYCOUNT = getattr(config, "SET_CREATE_RETRYCOUNT")
SET_UPDATE_WAITTIME = getattr(config, "SET_UPDATE_WAITTIME")
SET_UPDATE_RETRYCOUNT = getattr(config, "SET_UPDATE_RETRYCOUNT")
SET_DELETE_WAITTIME = getattr(config, "SET_DELETE_WAITTIME")
SET_DELETE_RETRYCOUNT = getattr(config, "SET_DELETE_RETRYCOUNT")


class ServiceOperations(base.SeleniumBase):
    def __init__(self, driver, evidence):
        super(ServiceOperations, self).__init__(driver, evidence)
        self.driver = driver
        self.evidence = evidence

    def check_list_service(self):
        # Show service list
        self.list_service()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_list_service_admin(self):
        # Show service list for admin
        self.list_service_admin()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_detail_service(self, input_params):
        # Show service detail
        self.detail_service(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_detail_service_admin(self, input_params):
        # Show service detail for admin
        self.detail_service_admin(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_create_service(self, input_params):

        # Create operation
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_list", "before")

        driver.find_element_by_id("service__action_create").click()
        self.sleep_time()
        create_params = copy.deepcopy(input_params)
        self.param_select_id("service_type", create_params.pop("service_type"))
        self.param_select("IaaS_subnet_id", create_params.pop("subnet_info"))
        self.param_select("bandwidth", create_params.pop("bandwidth"))
        for input_key, input_value in create_params.iteritems():
            self.param_input(input_key, input_value)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(30)

        driver.refresh()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_creating")
        self.sleep_time()

        try:
            # Check that service creation is complete
            target_line = self.get_line_from_list(input_params["service_name"])
        except:
            raise Exception("A service has not been created.")

        for num in range(1, SET_CREATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "3")
            # Check result status
            if self.check_status(status, "Active"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                break
            elif self.check_status(status, "Error"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                raise Exception("Status is invalid after service creation")
            else:
                self.sleep_time(SET_CREATE_WAITTIME)
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_list", "after")
            raise Exception("The service creation process did not end")

    def check_update_service_add_interface(self, input_params):
        # Check before network list
        driver = self.driver

        # Add interface to service
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_detail", "before")
        driver.find_element_by_link_text("Connect Interface").click()
        self.sleep_time()
        self.param_select("IaaS_subnet_id", input_params["subnet_info"])
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(20)

        # Check result network list
        self.list_service()
        target_line = self.get_line_from_list(input_params["service_name"])
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "3")
            if self.check_status(status, "Active"):
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                break

            elif self.check_status(status, "Build"):
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                raise Exception("Status is invalid after interface addition")

        else:
            self.detail_service(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_detail", "after")
            raise Exception("The interface addition process did not end")

    def check_update_service_add_v6_interface(self, input_params):
        # Check before network list
        driver = self.driver

        network_count = 0
        for num in range(1, 10):
            ipv6_address = driver.find_element_by_xpath("//table[@id='network']/tbody/tr[" + str(num) + "]/td[4]").text
            if ipv6_address == "-":
                break

        network_count = num

        # Add interface to service
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_detail", "before")
        driver.find_element_by_xpath("//table[@id='network']/tbody/tr[" + str(network_count) + "]/td[6]/a").click()
        self.sleep_time()
        self.param_select("IaaS_subnet_id_v6", input_params["subnet_info"])
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        self.param_input("fw_ip_v6_address", input_params["fw_ip_v6_address"])

        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(20)

        # Check result network list
        self.list_service()
        target_line = self.get_line_from_list(input_params["service_name"])
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "3")
            if self.check_status(status, "Active"):
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                break

            elif self.check_status(status, "Build"):
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                raise Exception("Status is invalid after ipv6 interface addition")

        else:
            self.detail_service(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_detail", "after")
            raise Exception("The ipv6 interface addition process did not end")

    def check_update_service_bandwidth(self, input_params):
        # Check before update bandwidth
        driver = self.driver

        # Update bandwidth for service
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_detail", "before")
        driver.find_element_by_link_text("Update Bandwidth").click()
        self.sleep_time()
        self.param_select("bandwidth", input_params["bandwidth"])
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(20)

        # Check result member list
        self.list_service()
        self.sleep_time()
        target_line = self.get_line_from_list(input_params["service_name"])
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "3")
            if self.check_status(status, "Active"):
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                raise Exception("Status is invalid after changing the bandwidth")

        else:
            self.detail_service(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_detail", "after")
            raise Exception("The changing the bandwidth process did not end")

    def check_update_service_setting(self, input_params):
        # Check before update service setting
        driver = self.driver

        # Update setting for service
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_detail", "before")
        driver.find_element_by_xpath("//table[@id='member']/tbody/tr[1]/td[4]/div/a[2]").click()
        self.sleep_time()
        driver.find_element_by_link_text("Update Setting").click()
        self.sleep_time()

        # Input params
        self.param_input("dns_server_ip_address", input_params.get("dns_server_ip_address", ""))
        self.param_input("ntp_server_ip_address", input_params.get("ntp_server_ip_address", ""))
        self.param_select("ntp_server_interface", input_params.get("ntp_server_interface", ""))
        if input_params.get("snmp_server_delete_flg", "") == "1":
            driver.execute_script(
                'document.getElementById("id_snmp_server_delete_flg").click();')
        else:
            self.param_input("snmp_server_ip_address", input_params.get("snmp_server_ip_address", ""))
            self.param_select("snmp_server_interface", input_params.get("snmp_server_interface", ""))
        if input_params.get("syslog_server_delete_flg", "") == "1":
            driver.execute_script(
                'document.getElementById("id_syslog_server_delete_flg").click();')
        else:
            self.param_input("syslog_server_ip_address", input_params.get("syslog_server_ip_address", ""))
            self.param_select("syslog_server_interface", input_params.get("syslog_server_interface", ""))

        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(5)

        try:
            result = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable fade in']/p").text
            if result == "Success: Job of update service setting is running.":
                pass
            else:
                raise
        except:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "input_param_error")
            raise Exception("Parameter of changing the setting is incorrect")

        self.sleep_time(15)

        # Check result service detail
        self.list_service()
        target_line = self.get_line_from_list(input_params["service_name"])
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "3")
            if self.check_status(status, "Active"):
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_service(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_detail", "after")
                raise Exception("Status is invalid after changing the setting")

        else:
            self.detail_service(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_detail", "after")
            raise Exception("The changing the setting process did not end")

    def check_delete_service(self, input_params):
        # Get uuid
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_list", "before")

        link = driver.find_element_by_link_text(input_params["service_name"])
        decode_link = urllib.unquote(link.get_attribute("href"))
        uuid = decode_link.split("/")[6]

        # Delete operation
        try:
            driver.find_element_by_id("service__row_" + uuid + "__action_delete").click()
        except selenium_except.ElementNotVisibleException:
            driver.find_element_by_xpath("//tr[@id='service__row__" + uuid + "']/td[5]/div/a[2]").click()
            driver.find_element_by_id("service__row_" + uuid + "__action_delete").click()
        self.sleep_time()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_link_text("Delete Service").click()
        self.sleep_time(20)

        # Check result service list
        for num in range(1, SET_DELETE_RETRYCOUNT):
            driver.refresh()
            try:
                status = driver.find_element_by_xpath(
                    "//tr[@id='service__row__" + uuid + "']/td[3]").text
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                break

            if self.check_status(status, "Error"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                raise Exception("Status is invalid after service deletion")
            else:
                self.sleep_time(SET_DELETE_WAITTIME)
                continue

        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_list", "after")
            raise Exception("The service deletion process did not end")

    def check_update_service_add_member(self, input_params):
        # Create operation
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "service_list", "before")

        driver.find_element_by_link_text("Add Member").click()
        self.sleep_time()
        create_params = copy.deepcopy(input_params)
        self.param_select("IaaS_subnet_id", input_params.pop("subnet_info"))
        for input_key, input_value in input_params.iteritems():
            self.param_input(input_key, input_value)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(30)

        self.list_service()
        self.sleep_time()

        for num in range(1, SET_CREATE_RETRYCOUNT):
            status = self.get_data_from_line("1", "3")
            # Check result status
            if self.check_status(status, "Active"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                break
            elif self.check_status(status, "Error"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "service_list", "after")
                raise Exception("Status is invalid after service creation")
            else:
                self.sleep_time(SET_CREATE_WAITTIME)
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "service_list", "after")
            raise Exception("The service creation process did not end")

    def list_service(self):
        # Show service list
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/project/service/")
        self.sleep_time()

    def detail_service(self, input_params):
        # Show service detail
        driver = self.driver
        driver.find_element_by_link_text(input_params["service_name"]).click()
        self.sleep_time()

    def list_service_admin(self):
        # Show service list for admin
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/admin/service/")
        self.sleep_time()

    def detail_service_admin(self, input_params):
        # Show service detail for admin
        driver = self.driver
        driver.find_element_by_link_text(input_params["service_name"]).click()
        self.sleep_time()

    def initialize_service_create(self, input_params):
        # Get service info
        driver = self.driver
        self.list_service()

        try:
            link = driver.find_element_by_link_text(input_params["service_name"])
            decode_link = urllib.unquote(link.get_attribute("href"))
            uuid = decode_link.split("/")[6]
        except:
            return True

        # Get service status
        service_status = driver.find_element_by_xpath(
            "//tr[@id='service__row__" + uuid + "']/td[3]").text

        if self.check_status(service_status, "Active"):
            return False

        elif self.check_status(service_status, "Error"):
            # Delete operation
            driver.find_element_by_id("service__row_" + uuid + "__action_delete").click()
            self.sleep_time()
            driver.find_element_by_link_text("Delete Service").click()
            self.sleep_time(5)

            # Check result service list
            for num in range(1, 10):
                driver.refresh()
                self.sleep_time()
                try:
                    service_status = driver.find_element_by_xpath(
                        "//tr[@id='service__row__" + uuid + "']/td[3]").text
                except selenium_except.NoSuchElementException:
                    break

                self.sleep_time(30)
                continue

            else:
                raise Exception("The services deletion process did not end")

            return True

    def initialize_add_interface(self, input_params):
        # Get service info
        driver = self.driver
        self.list_service()
        self.detail_service(input_params)

        # Check before network list
        tenant_lan_count = 0
        for num in range(1, 10):
            try:
                network = driver.find_element_by_xpath(
                    "//table[@id='network']/tbody/tr[" + str(num) + "]/td[1]").text
                tenant_lan_count = tenant_lan_count + 1
            except selenium_except.NoSuchElementException:
                break

        if tenant_lan_count >= 2:
            return False
        return True

    def initialize_add_v6_interface(self, input_params):
        # Get service info
        driver = self.driver
        self.list_service()
        self.detail_service(input_params)

        # Check before network list
        tenant_lan_count = 0
        for num in range(1, 10):
            try:
                ipv6_address = driver.find_element_by_xpath(
                    "//table[@id='network']/tbody/tr[" + str(num) + "]/td[4]").text
                if ipv6_address != "-":
                    return False
            except selenium_except.NoSuchElementException:
                break

        return True

    def initialize_service_bandwidth(self, input_params):
        # Get service info
        driver = self.driver
        self.list_service()
        self.detail_service(input_params)

        # Check before bandwidth
        bandwidth = driver.find_element_by_xpath(
            "//table[@id='member']/tbody/tr[1]/td[2]").text

        if bandwidth == input_params["bandwidth"]:
            return False
        return True
