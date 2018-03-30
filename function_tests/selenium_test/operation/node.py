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
from selenium.webdriver.support.ui import Select

SET_BASE_URL = getattr(config, "SET_BASE_URL")
SET_NAL_VERSION = getattr(config, "SET_NAL_VERSION")
PROJECT_NAME = getattr(config, "PROJECT_NAME")
SET_CREATE_WAITTIME = getattr(config, "SET_CREATE_WAITTIME")
SET_CREATE_RETRYCOUNT = getattr(config, "SET_CREATE_RETRYCOUNT")
SET_UPDATE_WAITTIME = getattr(config, "SET_UPDATE_WAITTIME")
SET_UPDATE_RETRYCOUNT = getattr(config, "SET_UPDATE_RETRYCOUNT")
SET_DELETE_WAITTIME = getattr(config, "SET_DELETE_WAITTIME")
SET_DELETE_RETRYCOUNT = getattr(config, "SET_DELETE_RETRYCOUNT")

if SET_NAL_VERSION < "3":
    TABLE_COLUMNS_MAP = {
        "node_network_list": {
            "NIC": "1",
            "IPv4 Address": "2",
            "Network Name": "3",
            "Network Type": "4",
            "Actions": "5"
        }
    }
else:
    TABLE_COLUMNS_MAP = {
        "node_network_list": {
            "NIC": "1",
            "IPv4 Address": "2",
            "IPv6 Address": "3",
            "Network Name": "4",
            "Network Type": "5",
            "Actions": "6"
        }
    }


class NodeOperations(base.SeleniumBase):
    def __init__(self, driver, evidence):
        super(NodeOperations, self).__init__(driver, evidence)
        self.driver = driver
        self.evidence = evidence

    def check_list_node(self):
        driver = self.driver

        # Show node list
        self.list_node()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_detail_node(self, input_params):
        driver = self.driver

        # Show node detail
        self.detail_node(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_list_node_admin(self):
        driver = self.driver

        # Show node list
        self.list_node_admin()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_detail_node_admin(self, input_params):
        driver = self.driver

        # Show node detail
        self.detail_node_admin(input_params)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "check_data")

    def check_create_node(self, input_params):
        # Create operation
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_list", "before")
        driver.find_element_by_id("node__action_create").click()
        self.sleep_time()
        create_params = copy.deepcopy(input_params)
        apl_type = create_params.pop("apl_type")
        type = create_params.pop("type")
        self.param_select_id("apl_type", apl_type)
        self.param_select_id("type", type)
        self.param_select_id("device_type-" + apl_type + "-" + type,
                             create_params.pop("device_type"))
        self.param_select("subnet", create_params.pop("subnet_info"))
        if "redundant_configuration_flg" in create_params:
            self.param_select("redundant_configuration_flg",
                              create_params.pop("redundant_configuration_flg"))
        for input_key, input_value in create_params.iteritems():
            self.param_input(input_key, input_value)
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(10)

        driver.refresh()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_creating")
        self.sleep_time()

        try:
            # Check that node creation is complete
            node_name = self._get_create_node_name(input_params)
            target_line = self.get_line_from_list(node_name)
        except:
            raise Exception("A node has not been created.")

        for num in range(1, SET_CREATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "5")
            # Check result status
            if self.check_status(status, "Active") or \
                    self.check_status(status, "No License"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_list", "after")
                break
            elif self.check_status(status, "Error"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_list", "after")
                raise Exception("Status is invalid after node creation")
            else:
                self.sleep_time(SET_CREATE_WAITTIME)
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_list", "after")
            raise Exception("The node creation process did not end")

    def check_update_node_add_interface(self, input_params):
        # Check before network list
        network_count = 0
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        for num in range(1, 10):
            try:
                add_tenant_lan = self.get_data_from_line(str(num), net_type_num)
            except selenium_except.NoSuchElementException:
                break

            network_count = num

        # Add interface to node
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_detail", "before")
        driver.find_element_by_link_text("Connect Interface").click()
        self.sleep_time()

        upadte_params = copy.deepcopy(input_params)

        if "host_name" in upadte_params:
            upadte_params.pop("host_name")
        elif "vdom_name" in upadte_params:
            upadte_params.pop("vdom_name")
        elif "partition_name" in upadte_params:
            upadte_params.pop("partition_name")
        elif "vsys_name" in upadte_params:
            upadte_params.pop("vsys_name")
        elif "partition_id" in upadte_params:
            upadte_params.pop("partition_id")
        else:
            pass

        self.param_select("subnet", upadte_params.pop("subnet_info"))
        for input_key, input_value in upadte_params.iteritems():
            self.param_input(input_key, input_value)

        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(5)

        try:
            result = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable fade in']/p").text
            if result == "Success: Job of port creation is running.":
                pass
            else:
                raise
        except:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("Parameter of interface addition is incorrect")

        self.sleep_time(10)

        # Check result network list
        self.list_node()
        self.sleep_time()

        node_name = self._get_create_node_name(input_params)
        target_line = self.get_line_from_list(node_name)
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "5")
            if self.check_status(status, "Active"):
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                raise Exception("Status is invalid after interface addition")

        else:
            self.detail_node(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("The interface addition process did not end")

    def check_update_node_delete_interface(self, input_params):

        # Check before network list
        network_count = 0
        for num in range(1, 10):
            try:
                add_tenant_lan = self.get_data_from_line(str(num), "4")
            except selenium_except.NoSuchElementException:
                break

            network_count = num

        # Designate the network to delete
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_detail", "before")
        delete_port_num = network_count

        actions_num = TABLE_COLUMNS_MAP["node_network_list"]["Actions"]
        try:
            driver.find_element_by_xpath("//tr[" + str(delete_port_num) + "]/td[" + actions_num +"]/button").click()
        except selenium_except.NoSuchElementException:
            driver.find_element_by_xpath("//tr[" + str(delete_port_num) + "]/td[" + actions_num +"]/div/a[2]").click()
            driver.find_element_by_xpath("//tr[" + str(delete_port_num) + "]/td[" + actions_num +"]/div/ul/li/button").click()

        self.sleep_time()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_link_text("Delete Network").click()
        self.sleep_time(15)

        # Check result network list
        self.list_node()
        self.sleep_time()

        node_name = self._get_create_node_name(input_params)
        target_line = self.get_line_from_list(node_name)
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "5")
            if self.check_status(status, "Active"):
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                raise Exception("Status is invalid after interface deletion")

        else:
            self.detail_node(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("The interface deletion process did not end")

    def check_update_node_add_v6_interface(self, input_params):
        # Check before network list
        network_count = 0
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        ipv6_num = TABLE_COLUMNS_MAP["node_network_list"]["IPv6 Address"]

        for num in range(1, 10):
            network_type = self.get_data_from_line(str(num), net_type_num)
            ipv6_address = self.get_data_from_line(str(num), ipv6_num)
            if network_type == "Tenant" and ipv6_address == "-":
                break

        network_count = num

        # Add interface to node
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_detail", "before")
        actions_num = TABLE_COLUMNS_MAP["node_network_list"]["Actions"]
        try:
            driver.find_element_by_xpath("//tr[" + str(network_count) + "]/td[" + actions_num + "]/a[1]").click()
        except:
            driver.find_element_by_xpath("//tr[" + str(network_count) + "]/td[" + actions_num + "]/div/a[1]").click()
        self.sleep_time()

        try:
            driver.find_element_by_css_selector("input.btn.btn-primary")
        except:
            raise Exception("Please create ipv6 subnet")

        update_params = copy.deepcopy(input_params)

        if "host_name" in update_params:
            update_params.pop("host_name")
        elif "vdom_name" in update_params:
            update_params.pop("vdom_name")
        elif "partition_name" in update_params:
            update_params.pop("partition_name")
        elif "vsys_name" in update_params:
            update_params.pop("vsys_name")
        elif "partition_id" in update_params:
            update_params.pop("partition_id")
        else:
            pass

        self.param_select("subnet", update_params.pop("subnet_info"))

        if "ip_v6_ext_auto_set_flg" in update_params:
            if update_params.pop("ip_v6_ext_auto_set_flg") == "1":
                driver.execute_script(
                    'document.getElementById("id_ip_v6_ext_auto_set_flg").click();')
        if "ip_v6_pub_auto_set_flg" in update_params:
            if update_params.pop("ip_v6_pub_auto_set_flg") == "1":
                driver.execute_script(
                    'document.getElementById("id_ip_v6_pub_auto_set_flg").click();')

        for input_key, input_value in update_params.iteritems():
            self.param_input(input_key, input_value)

        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(5)

        try:
            result = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable fade in']/p").text
            if result == "Success: Job of port creation is running.":
                pass
            else:
                raise
        except:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("Parameter of ipv6 interface addition is incorrect")

        self.sleep_time(10)

        # Check result network list
        self.list_node()
        self.sleep_time()

        node_name = self._get_create_node_name(input_params)
        target_line = self.get_line_from_list(node_name)
        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(target_line, "5")
            if self.check_status(status, "Active"):
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_node(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                raise Exception("Status is invalid after ipv6 interface addition")

        else:
            self.detail_node(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("The ipv6 interface addition process did not end")

    def check_asign_license(self, input_params):
        # Assign license to node
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_detail", "before")

        # Click Create License button
        driver.find_element_by_link_text("Create License").click()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.sleep_time(15)

        # Check result status
        self.list_node_admin()
        self.sleep_time()

        # Search node_name and tenant_name
        target_node_name = self._get_create_node_name(input_params)
        for line in range(1, 100):
            line_node_name = self.get_data_from_line(str(line), "2")
            line_tanant_name = self.get_data_from_line(str(line), "1")
            if line_node_name == target_node_name \
                    and line_tanant_name == PROJECT_NAME:
                break
        node_count = line

        for num in range(1, SET_UPDATE_RETRYCOUNT):
            status = self.get_data_from_line(node_count, "6")
            if self.check_status(status, "Active"):
                self.detail_node_admin(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                break

            elif status == "Build":
                self.sleep_time(SET_UPDATE_WAITTIME)
                continue

            else:
                self.detail_node_admin(input_params)
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_detail", "after")
                raise Exception("Status is invalid after licensing")

        else:
            self.detail_node_admin(input_params)
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_detail", "after")
            raise Exception("The licensing process did not end")

    def check_delete_node(self, input_params):

        # get uuid
        driver = self.driver
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "node_list", "before")

        node_name = self._get_create_node_name(input_params)
        link = driver.find_element_by_partial_link_text(node_name)
        decode_link = urllib.unquote(link.get_attribute("href"))
        uuid = decode_link.split("/")[6]

        # Delete operation
        try:
            driver.find_element_by_id("node__row_" + uuid + "__action_delete").click()
        except selenium_except.ElementNotVisibleException:
            driver.find_element_by_xpath("//tr[@id='node__row__" + uuid + "']/td[7]/div/a[2]").click()
            driver.find_element_by_id("node__row_" + uuid + "__action_delete").click()
        self.sleep_time()
        self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                            "input_params")
        driver.find_element_by_link_text("Delete Node").click()
        self.sleep_time(5)

        # Check result node list
        for num in range(1, SET_DELETE_RETRYCOUNT):
            driver.refresh()
            self.sleep_time()
            try:
                status = driver.find_element_by_xpath(
                    "//tr[@id='node__row__" + uuid + "']/td[5]").text
            except selenium_except.NoSuchElementException:
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_list", "after")
                break

            if self.check_status(status, "Error"):
                self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                    "node_list", "after")
                raise Exception("Status is invalid after node deletion")
            else:
                self.sleep_time(SET_DELETE_WAITTIME)
                continue
        else:
            self.get_screenshot(inspect.currentframe().f_back.f_code.co_name,
                                "node_list", "after")
            raise Exception("The node deletion process did not end")

    def list_node(self):
        # Show node list
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/project/node/")
        self.sleep_time()

    def detail_node(self, input_params):
        # Show node detail
        driver = self.driver
        node_name = self._get_create_node_name(input_params)
        driver.find_element_by_partial_link_text(node_name).click()
        self.sleep_time()

    def list_node_admin(self):
        # Show node list for admin
        driver = self.driver
        driver.get(SET_BASE_URL + "/dashboard/admin/node/")
        self.sleep_time()

    def detail_node_admin(self, input_params):
        driver = self.driver
        target_node_name = self._get_create_node_name(input_params)

        # Search node_name and tenant_name
        for num in range(1, 100):
            line_node_name = self.get_data_from_line(str(num), "2")
            line_tanant_name = self.get_data_from_line(str(num), "1")
            if line_node_name == target_node_name \
                    and line_tanant_name == PROJECT_NAME:
                break
        node_count = num

        # Show node detail for admin
        driver.find_element_by_xpath("//tr[" + str(node_count) + "]/td[2]/a[1]").click()
        self.sleep_time()

    def get_firewall_ipaddress(self):
        # Get firewall info
        driver = self.driver
        self.list_node()

        firewall_line = 0
        for num in range(1, 30):
            try:
                type = self.get_data_from_line(str(num), "3")
                status = self.get_data_from_line(str(num), "5")
            except selenium_except.NoSuchElementException:
                raise Exception("Please create a firewall first")
            if self.check_status(type, "Firewall") and self.check_status(status, "Active"):
                firewall_line = num
                break
        else:
            raise Exception("Please create a firewall first")

        driver.find_element_by_xpath("//tr[" + str(firewall_line) + "]/td/a").click()
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        ipv4_num = TABLE_COLUMNS_MAP["node_network_list"]["IPv4 Address"]
        self.sleep_time()
        for num in range(1, 10):
            network_type = self.get_data_from_line(str(num), net_type_num)
            if self.check_status(network_type, "Tenant"):
                fw_ip_address = self.get_data_from_line(str(num), ipv4_num)
                break

        return fw_ip_address

    def get_firewall_v6_ipaddress(self):
        # Get firewall info
        driver = self.driver
        self.list_node()

        firewall_line = 0
        for num in range(1, 30):
            try:
                type = self.get_data_from_line(str(num), "3")
                status = self.get_data_from_line(str(num), "5")
            except selenium_except.NoSuchElementException:
                raise Exception("Please create a firewall first")
            if self.check_status(type, "Firewall") and self.check_status(status, "Active"):
                firewall_line = num
                break
        else:
            raise Exception("Please create a firewall first")

        driver.find_element_by_xpath("//tr[" + str(firewall_line) + "]/td/a").click()
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        ipv6_num = TABLE_COLUMNS_MAP["node_network_list"]["IPv6 Address"]
        self.sleep_time()
        for num in range(1, 10):
            network_type = self.get_data_from_line(str(num), net_type_num)
            if self.check_status(network_type, "Tenant"):
                fw_ip_address = self.get_data_from_line(str(num), ipv6_num)
                if fw_ip_address == "-":
                    continue
                else:
                    break

        return fw_ip_address

    def initialize_node_create(self, input_params):
        # Get firewall info
        driver = self.driver
        self.list_node()

        try:
            node_name = self._get_create_node_name(input_params)
            link = driver.find_element_by_partial_link_text(node_name)
            decode_link = urllib.unquote(link.get_attribute("href"))
            uuid = decode_link.split("/")[6]
        except:
            return True

        # Get node status
        node_status = driver.find_element_by_xpath(
            "//tr[@id='node__row__" + uuid + "']/td[5]").text

        if self.check_status(node_status, "Active") or \
                self.check_status(node_status, "No License"):
            return False

        elif self.check_status(node_status, "Error"):
            # Delete operation
            driver.find_element_by_id("node__row_" + uuid + "__action_delete").click()
            self.sleep_time()
            driver.find_element_by_link_text("Delete Node").click()
            self.sleep_time(5)

            # Check result node list
            for num in range(1, 10):
                driver.refresh()
                try:
                    status = driver.find_element_by_xpath(
                        "//tr[@id='node__row__" + uuid + "']/td[5]").text
                except selenium_except.NoSuchElementException:
                    break

                self.sleep_time(30)
                continue

            else:
                raise Exception("The node deletion process did not end")

            return True

    def initialize_add_interface(self, input_params):
        # Get firewall info
        driver = self.driver
        self.list_node()
        self.detail_node(input_params)

        # Check before network list
        tenant_lan_count = 0
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        for num in range(1, 10):
            try:
                network_type = self.get_data_from_line(str(num), net_type_num)
                if network_type == "Tenant":
                    tenant_lan_count = tenant_lan_count + 1
            except selenium_except.NoSuchElementException:
                break

        if tenant_lan_count >= 2:
            return False
        return True

    def initialize_add_v6_interface(self, input_params):
        # Get firewall info
        driver = self.driver
        self.list_node()
        self.detail_node(input_params)

        # Check before network list
        tenant_lan_count = 0
        net_type_num = TABLE_COLUMNS_MAP["node_network_list"]["Network Type"]
        ipv6_num = TABLE_COLUMNS_MAP["node_network_list"]["IPv6 Address"]
        for num in range(1, 10):
            try:
                network_type = self.get_data_from_line(str(num), net_type_num)
                ipv6_address = self.get_data_from_line(str(num), ipv6_num)
                if network_type == "Tenant" and ipv6_address != "-":
                    return False
            except selenium_except.NoSuchElementException:
                break

        return True

    def initialize_assign_license(self, input_params):
        # Get firewall info
        driver = self.driver
        self.list_node_admin()

        target_node_name = self._get_create_node_name(input_params)

        # Search node_name and tenant_name
        for num in range(1, 100):
            line_node_name = self.get_data_from_line(str(num), "2")
            line_tanant_name = self.get_data_from_line(str(num), "1")
            if line_node_name == target_node_name \
                    and line_tanant_name == PROJECT_NAME:
                break
        node_count = num

        # Get node status
        node_status = driver.find_element_by_xpath(
            "//tr[" + str(node_count) + "]/td[6]").text

        if self.check_status(node_status, "Active"):
            return False
        return True

    def _get_create_node_name(self, input_params):
        # Get create node name
        if "host_name" in input_params:
            node_name = input_params["host_name"]
        elif "vdom_name" in input_params:
            node_name = input_params["vdom_name"]
        elif "partition_name" in input_params:
            node_name = input_params["partition_name"]
        elif "vsys_name" in input_params:
            node_name = input_params["vsys_name"]
        else:
            node_name = input_params["partition_id"]
        return node_name
