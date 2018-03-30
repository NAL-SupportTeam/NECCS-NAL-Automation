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


from conf import config
from operation import node
from operation import resource
from operation import service
from operation import settings

SET_NAL_VERSION = getattr(config, "SET_NAL_VERSION")


class NalTestMethod(object):
    def __init__(self, driver, evidence):
        self.driver = driver
        self.evidence = evidence

    # ---------------------------------------------------------------
    # Settings
    # ---------------------------------------------------------------
    def sign_in(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.sign_in()

    def change_project(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.change_project()

    def change_setting(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.change_setting()

    def sign_out(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.sign_out()

    def global_sign_in(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.global_sign_in()

    def global_change_project(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.global_change_project()

    def global_change_setting(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.global_change_setting()

    def create_user(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.create_user()

    def create_role(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.create_role()

    def create_project(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.create_project()

    def add_admin_user(self):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.add_admin_user()

    def create_network(self, input_params):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.create_network(input_params)

    def add_subnet(self, input_params):
        # create instance
        setting_instance = settings.SettingOperations(self.driver, self.evidence)
        # call operation
        setting_instance.add_subnet(input_params)

    # ---------------------------------------------------------------
    # Nodes
    # ---------------------------------------------------------------
    def node_list(self):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.check_list_node()

    def node_list_admin(self):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.check_list_node_admin()

    def node_detail(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.check_detail_node(input_params)

    def node_detail_admin(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.check_detail_node_admin(input_params)

    def node_create(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)

        # Initialization processing
        node_create_flg = node_instance.initialize_node_create(input_params)
        if node_create_flg == False:
            return

        # check operation before
        resource_instance.check_list_resource_before(input_params)
        resource_instance.check_list_resource_admin_before(input_params)

        # get firewall ip if node is LoadBalancer
        if input_params["type"] == "2":
            fw_ip_address = node_instance.get_firewall_ipaddress()
            input_params["fw_ip_address"] = fw_ip_address

        # call operation
        node_instance.list_node()
        node_instance.check_create_node(input_params)

        # check operation after
        resource_instance.check_list_resource_after(input_params)
        resource_instance.check_list_resource_admin_after(input_params)

    def node_add_interface(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)

        # Initialization processing
        node_update_flg = node_instance.initialize_add_interface(input_params)
        if node_update_flg == False:
            return

        # call operation
        node_instance.list_node()
        node_instance.detail_node(input_params)
        node_instance.check_update_node_add_interface(input_params)

    def node_delete_interface(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.list_node()
        node_instance.detail_node(input_params)
        node_instance.check_update_node_delete_interface(input_params)

    def node_add_v6_interface(self, input_params):
        if SET_NAL_VERSION < "3":
            return

        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)

        # Initialization processing
        node_update_flg = node_instance.initialize_add_v6_interface(input_params)
        if node_update_flg == False:
            return

        # get firewall ip if node is LoadBalancer
        if "fw_ip_v6_address" in input_params:
            fw_ip_v6_address = node_instance.get_firewall_v6_ipaddress()
            input_params["fw_ip_v6_address"] = fw_ip_v6_address

        # call operation
        node_instance.list_node()
        node_instance.detail_node(input_params)
        node_instance.check_update_node_add_v6_interface(input_params)

    def node_assign_license(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)

        # Initialization processing
        node_update_flg = node_instance.initialize_assign_license(input_params)
        if node_update_flg == False:
            return

        # call operation
        node_instance.list_node_admin()
        node_instance.detail_node_admin(input_params)
        node_instance.check_asign_license(input_params)

    def node_delete(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        # call operation
        node_instance.list_node()
        node_instance.check_delete_node(input_params)

    # ---------------------------------------------------------------
    # Services
    # ---------------------------------------------------------------
    def service_list(self):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.check_list_service()

    def service_list_admin(self):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.check_list_service_admin()

    def service_detail(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.check_detail_service(input_params)

    def service_detail_admin(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.check_detail_service_admin(input_params)

    def service_create(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)

        # Initialization processing
        service_create_flg = service_instance.initialize_service_create(input_params)
        if service_create_flg == False:
            return

        # check operation before
        resource_instance.check_list_resource_before(input_params)
        resource_instance.check_list_resource_admin_before(input_params)

        # get firewall ip
        fw_ip_address = node_instance.get_firewall_ipaddress()
        input_params["fw_ip_address"] = fw_ip_address

        # call operation
        service_instance.list_service()
        service_instance.check_create_service(input_params)

        # check operation after
        resource_instance.check_list_resource_after(input_params)
        resource_instance.check_list_resource_admin_after(input_params)

    def service_add_interface(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)

        # Initialization processing
        service_update_flg = service_instance.initialize_add_interface(input_params)
        if service_update_flg == False:
            return

        # call operation
        service_instance.list_service()
        service_instance.detail_service(input_params)
        service_instance.check_update_service_add_interface(input_params)

    def service_add_v6_interface(self, input_params):
        if SET_NAL_VERSION < "3":
            return

        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        service_instance = service.ServiceOperations(self.driver, self.evidence)

        # Initialization processing
        service_update_flg = service_instance.initialize_add_v6_interface(input_params)
        if service_update_flg == False:
            return

        # get firewall ip
        if "fw_ip_v6_address" in input_params:
            fw_ip_v6_address = node_instance.get_firewall_v6_ipaddress()
            input_params["fw_ip_v6_address"] = fw_ip_v6_address

        # call operation
        service_instance.list_service()
        service_instance.detail_service(input_params)
        service_instance.check_update_service_add_v6_interface(input_params)

    def service_bandwidth(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)

        # Initialization processing
        service_update_flg = service_instance.initialize_service_bandwidth(input_params)
        if service_update_flg == False:
            return

        # call operation
        service_instance.list_service()
        service_instance.detail_service(input_params)
        service_instance.check_update_service_bandwidth(input_params)

    def service_setting(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.list_service()
        service_instance.detail_service(input_params)
        service_instance.check_update_service_setting(input_params)

    def service_delete(self, input_params):
        # create instance
        service_instance = service.ServiceOperations(self.driver, self.evidence)
        # call operation
        service_instance.list_service()
        service_instance.check_delete_service(input_params)

    def service_add_member(self, input_params):
        # create instance
        node_instance = node.NodeOperations(self.driver, self.evidence)
        service_instance = service.ServiceOperations(self.driver, self.evidence)

        # get firewall ip
        fw_ip_address = node_instance.get_firewall_ipaddress()
        input_params["fw_ip_address"] = fw_ip_address

        # call operation
        service_instance.list_service()
        service_instance.check_update_service_add_member(input_params)

    # ---------------------------------------------------------------
    # Resource
    # ---------------------------------------------------------------
    def resource_list(self):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.check_list_resource()

    def resource_list_admin(self):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.check_list_resource_admin()

    def resource_detail(self, input_params):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.check_detail_resource(input_params)

    def resource_detail_admin(self, input_params):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.check_detail_resource_admin(input_params)

    def resource_create(self, input_params):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.list_resource()
        resource_instance.detail_resource(input_params)
        resource_instance.check_create_resource()

    def resource_update(self, input_params):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.list_resource()
        resource_instance.detail_resource(input_params)
        resource_instance.check_update_resource_used()
        resource_instance.check_update_resource_unused()

    def resource_delete(self, input_params):
        # create instance
        resource_instance = resource.ResourceOperations(self.driver, self.evidence)
        # call operation
        resource_instance.list_resource()
        resource_instance.detail_resource(input_params)
        resource_instance.check_delete_resource()
