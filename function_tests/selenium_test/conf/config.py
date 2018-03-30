# Base URL. Environment for testing.
# As for the URL, the last slash is unnecessary.
SET_BASE_URL = "http://10.58.70.107"
# Login user
USER_NAME = "test_user"
USER_PASSWORD = "password"
PROJECT_NAME = "nal_auto_test"
# Version set
SET_NAL_VERSION = "4.1"

# Global portal's URL
SET_GLOBAL_BASE_URL = "http://10.58.79.171"

# Admin user information
ADMIN_USER_NAME = "admin"
ADMIN_USER_PASSWORD = "admin"
ADMIN_PROJECT_NAME = "admin"

# role list for NAL create
CREATE_ROLE_LIST = ["O__DC2__Nal", "T__DC2__Nal"]

# Role list setting for test
SET_ROLE_LIST = ["O__DC2__Nal", "T__DC2__Nal", "T__DC2__ProjectMember", "O__DC2__ContractManager", "admin"]
ADMIN_ROLE_LIST = ["T__DC2__ProjectMember", "O__DC2__ContractManager", "admin"]

# Display language
SET_LANGUAGE = "en"
# Width of the window.
SET_WIDTH = 1280
# Height of the window.
SET_HEIGHT = 960
# Timeout.
SET_TIMEOUT = 5
# Capture of location.
SET_EVIDENCE = "evidence/"
# Profile path
SET_PROFILE_PATH = "/root/.mozilla/firefox/"
# Timeout setting of Create.
SET_CREATE_WAITTIME = 30
SET_CREATE_RETRYCOUNT = 120
# Timeout setting of Update.
SET_UPDATE_WAITTIME = 30
SET_UPDATE_RETRYCOUNT = 30
# Timeout setting of Delete.
SET_DELETE_WAITTIME = 30
SET_DELETE_RETRYCOUNT = 30

# Setting for environment construction
ZABBIX_VIP_IP = ""
ZABBIX_01_IP = ""
ZABBIX_02_IP = ""
DNS_PRIMARY_IP = ""
DNS_SECONDARY_IP = ""
NTP_PRAMARY_IP = ""
NTP_SECONDARY_IP = ""
INTERSEC_EXT_IPV6_ADDRESS = ""
FORTIGATEVM_524_EXT_IPV6_ADDRESS = ""
FORTIGATEVM_524_PUB_IPV6_ADDRESS = ""
PALOALTOVM_EXT_IPV6_ADDRESS = ""
PALOALTOVM_PUB_IPV6_ADDRESS = ""
INTERSECVM_PUB_IPV6_ADDRESS = ""
FORTIGATEVM_541_EXT_IPV6_ADDRESS = ""
FORTIGATEVM_541_PUB_IPV6_ADDRESS = ""
FORTIGATE_EXT_IPV6_ADDRESS = ""
FORTIGATE_PUB_IPV6_ADDRESS = ""
FORTIGATE_SHARE_EXT_IPV6_ADDRESS = ""
FORTIGATE_SHARE_PUB_IPV6_ADDRESS = ""
PALOALTO_EXT_IPV6_ADDRESS = ""
PALOALTO_PUB_IPV6_ADDRESS = ""
PALOALTO_SHARE_EXT_IPV6_ADDRESS = ""
PALOALTO_SHARE_PUB_IPV6_ADDRESS = ""
WEB_CLIENT_IP = "10.10.10.10"

NETWORK_NAME_01 = "nal_check_infra_net01"
SUBNET_NAME_01 = "nal_check_infra_sub01"
NETWORK_ADDRESS_01 = "10.58.71.0/24"

NETWORK_NAME_02 = "nal_check_infra_net02"
SUBNET_NAME_02 = "nal_check_infra_sub02"
NETWORK_ADDRESS_02 = "10.58.72.0/24"

SUBNET_NAME_03 = "nal_check_infra_sub03"
NETWORK_ADDRESS_03 = "1234::/112"

REDUNDANT_CONF_FLG_01 = "Redundancy"
REDUNDANT_CONF_FLG_02 = "Single"

SELECT_SUBNET_01 = NETWORK_NAME_01 + ": " + NETWORK_ADDRESS_01 + " (" + SUBNET_NAME_01 + ")"
SELECT_SUBNET_02 = NETWORK_NAME_02 + ": " + NETWORK_ADDRESS_02 + " (" + SUBNET_NAME_02 + ")"
SELECT_SUBNET_V6_01 = NETWORK_NAME_01 + ": " + NETWORK_ADDRESS_03 + " (" + SUBNET_NAME_03 + ")"

#----------------------------------------------------------------
# Provisioning
#----------------------------------------------------------------
PROVISIONING_CREATE_NETWORK_1_PARAMS = {
    "net_name": NETWORK_NAME_01,
    "subnet_name": SUBNET_NAME_01,
    "network_address": NETWORK_ADDRESS_01
}

PROVISIONING_CREATE_NETWORK_2_PARAMS = {
    "net_name": NETWORK_NAME_02,
    "subnet_name": SUBNET_NAME_02,
    "network_address": NETWORK_ADDRESS_02
}

PROVISIONING_ADD_SUBNET_1_PARAMS = {
    "net_name": NETWORK_NAME_01,
    "subnet_name": SUBNET_NAME_03,
    "network_address": NETWORK_ADDRESS_03
}

# ---------------------------------------------------------------
# InterSecVM SG for Ext
# ---------------------------------------------------------------
NODE_INTERSECVM_EXT_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "1",
    "device_type": "1",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testInterExt",
    "webclient_ip": WEB_CLIENT_IP,
    "zabbix_vip_ip": ZABBIX_VIP_IP,
    "zabbix_01_ip": ZABBIX_01_IP,
    "zabbix_02_ip": ZABBIX_02_IP,
    "ntp_server_primary": NTP_PRAMARY_IP
}

NODE_INTERSECVM_EXT_ADD_INTERFACE_PARAMS = {
    "host_name": "testInterExt",
    "subnet_info": SELECT_SUBNET_02
}

NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testInterExt",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1"
}
if INTERSEC_EXT_IPV6_ADDRESS != "":
    NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = INTERSEC_EXT_IPV6_ADDRESS

NODE_INTERSECVM_EXT_DELETE_PARAMS = {
    "host_name": "testInterExt"
}

# ---------------------------------------------------------------
# FortiGateVM
# ---------------------------------------------------------------
NODE_FOORTIGATEVM_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "1",
    "device_type": "2",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testFortiVM",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_FOORTIGATEVM_ADD_INTERFACE_PARAMS = {
    "host_name": "testFortiVM",
    "subnet_info": SELECT_SUBNET_02
}

NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testFortiVM",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if FORTIGATEVM_524_EXT_IPV6_ADDRESS != "":
    NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = FORTIGATEVM_524_EXT_IPV6_ADDRESS
if FORTIGATEVM_524_PUB_IPV6_ADDRESS != "":
    NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = FORTIGATEVM_524_PUB_IPV6_ADDRESS

NODE_FOORTIGATEVM_DELETE_PARAMS = {
    "host_name": "testFortiVM"
}

# ---------------------------------------------------------------
# PaloAltoVM
# ---------------------------------------------------------------
NODE_PALOALTOVM_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "1",
    "device_type": "3",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testPaloVM",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "pavm_zone_name": "zone1",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_PALOALTOVM_ASSIGN_LICENSE_PARAMS = {
    "host_name": "testPaloVM"
}

NODE_PALOALTOVM_ADD_INTERFACE_PARAMS = {
    "host_name": "testPaloVM",
    "subnet_info": SELECT_SUBNET_02,
    "pavm_zone_name": "zone1"
}

NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testPaloVM",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if PALOALTOVM_EXT_IPV6_ADDRESS != "":
    NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = PALOALTOVM_EXT_IPV6_ADDRESS
if PALOALTOVM_PUB_IPV6_ADDRESS != "":
    NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = PALOALTOVM_PUB_IPV6_ADDRESS

NODE_PALOALTOVM_DELETE_PARAMS = {
    "host_name": "testPaloVM"
}

# ---------------------------------------------------------------
# InterSecVM SG for Pub
# ---------------------------------------------------------------
NODE_INTERSECVM_PUB_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "1",
    "device_type": "4",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testInterPub",
    "webclient_ip": WEB_CLIENT_IP,
    "zabbix_vip_ip": ZABBIX_VIP_IP,
    "zabbix_01_ip": ZABBIX_01_IP,
    "zabbix_02_ip": ZABBIX_02_IP,
    "ntp_server_primary": NTP_PRAMARY_IP
}

NODE_INTERSECVM_PUB_ADD_INTERFACE_PARAMS = {
    "host_name": "testInterPub",
    "subnet_info": SELECT_SUBNET_02
}

NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testInterPub",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_pub_auto_set_flg": "1"
}
if INTERSECVM_PUB_IPV6_ADDRESS != "":
    NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = INTERSECVM_PUB_IPV6_ADDRESS

NODE_INTERSECVM_PUB_DELETE_PARAMS = {
    "host_name": "testInterPub"
}

# ---------------------------------------------------------------
# FortiGateVM 5.4.1
# ---------------------------------------------------------------
NODE_FORTIGATEVM_541_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "1",
    "device_type": "5",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testFortiVM541",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_FORTIGATEVM_541_ADD_INTERFACE_PARAMS = {
    "host_name": "testFortiVM541",
    "subnet_info": SELECT_SUBNET_02
}

NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testFortiVM541",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if FORTIGATEVM_541_EXT_IPV6_ADDRESS != "":
    NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = FORTIGATEVM_541_EXT_IPV6_ADDRESS
if FORTIGATEVM_541_PUB_IPV6_ADDRESS != "":
    NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = FORTIGATEVM_541_PUB_IPV6_ADDRESS

NODE_FORTIGATEVM_541_DELETE_PARAMS = {
    "host_name": "testFortiVM541"
}

# ---------------------------------------------------------------
# InterSecVM LB
# ---------------------------------------------------------------
NODE_INTERSECVM_LB_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "2",
    "device_type": "1",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testInterLb",
    "fw_ip_address": "192.168.40.252",
    "zabbix_vip_ip": ZABBIX_VIP_IP,
    "zabbix_01_ip": ZABBIX_01_IP,
    "zabbix_02_ip": ZABBIX_02_IP,
    "ntp_server_primary": NTP_PRAMARY_IP
}

NODE_INTERSECVM_LB_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testInterLb",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_INTERSECVM_LB_DELETE_PARAMS = {
    "host_name": "testInterLb"
}

# ---------------------------------------------------------------
# BIG-IP VE
# ---------------------------------------------------------------
NODE_BIGIP_VE_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "2",
    "device_type": "2",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testBigipVe",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "fw_ip_address": "192.168.40.252",
    "domain_name": "domain01",
    "self_ip_name": "self01",
    "timezone": "Asia/Tokyo",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_BIGIP_VE_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testBigipVe",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_BIGIP_VE_DELETE_PARAMS = {
    "host_name": "testBigipVe"
}

# ---------------------------------------------------------------
# vThunder(4.0.1)
# ---------------------------------------------------------------
NODE_VTHUNDER_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "2",
    "device_type": "3",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testVthun401",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "fw_ip_address": "192.168.40.252",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_VTHUNDER_ASSIGN_LICENSE_PARAMS = {
    "host_name": "testVthun401"
}

NODE_VTHUNDER_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testVthun401",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_VTHUNDER_DELETE_PARAMS = {
    "host_name": "testVthun401"
}

# ---------------------------------------------------------------
# vThunder(4.1.1)
# ---------------------------------------------------------------
NODE_VTHUNDER_411_CREATE_PARAMS = {
    "apl_type": "1",
    "type": "2",
    "device_type": "4",
    "subnet_info": SELECT_SUBNET_01,
    "host_name": "testVthun411",
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "fw_ip_address": "192.168.40.252",
    "dns_server_primary": DNS_PRIMARY_IP,
    "dns_server_secondary": DNS_SECONDARY_IP,
    "ntp_server_primary": NTP_PRAMARY_IP,
    "ntp_server_secondary": NTP_SECONDARY_IP
}

NODE_VTHUNDER_411_ASSIGN_LICENSE_PARAMS = {
    "host_name": "testVthun411"
}

NODE_VTHUNDER_411_ADD_V6_INTERFACE_PARAMS = {
    "host_name": "testVthun411",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_VTHUNDER_411_DELETE_PARAMS = {
    "host_name": "testVthun411"
}

# ---------------------------------------------------------------
# Fortigate
# ---------------------------------------------------------------
NODE_FORTIGATE_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "1",
    "device_type": "1",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "vdom_name": "testForti",
    "admin_prof_name": "admin_name",
    "user_account_id": "account_id",
    "account_password": "account_pw"
}

NODE_FORTIGATE_PNF_ADD_INTERFACE_PARAMS = {
    "vdom_name": "testForti",
    "subnet_info": SELECT_SUBNET_02
}

NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS = {
    "vdom_name": "testForti",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if FORTIGATE_EXT_IPV6_ADDRESS != "":
    NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = FORTIGATE_EXT_IPV6_ADDRESS
if FORTIGATE_PUB_IPV6_ADDRESS != "":
    NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = FORTIGATE_PUB_IPV6_ADDRESS

NODE_FORTIGATE_PNF_DELETE_PARAMS = {
    "vdom_name": "testForti"
}

# ---------------------------------------------------------------
# Fortigate Share
# ---------------------------------------------------------------
NODE_FORTIGATE_SHARE_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "1",
    "device_type": "3",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "vdom_name": "testFortSh",
    "admin_prof_name": "admin_name",
    "user_account_id": "account_id",
    "account_password": "account_pw"
}

NODE_FORTIGATE_SHARE_PNF_ADD_INTERFACE_PARAMS = {
    "vdom_name": "testFortSh",
    "subnet_info": SELECT_SUBNET_02
}

NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = {
    "vdom_name": "testFortSh",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if FORTIGATE_SHARE_EXT_IPV6_ADDRESS != "":
    NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = FORTIGATE_SHARE_EXT_IPV6_ADDRESS
if FORTIGATE_SHARE_PUB_IPV6_ADDRESS != "":
    NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = FORTIGATE_SHARE_PUB_IPV6_ADDRESS

NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS = {
    "vdom_name": "testFortSh"
}

# ---------------------------------------------------------------
# Paloalto
# ---------------------------------------------------------------
NODE_PALOALTO_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "1",
    "device_type": "2",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "vsys_name": "testPalo",
    "zone_name": "zone1"
}

NODE_PALOALTO_PNF_ADD_INTERFACE_PARAMS = {
    "vsys_name": "testPalo",
    "subnet_info": SELECT_SUBNET_02,
    "zone_name": "zone1"
}

NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS = {
    "vsys_name": "testPalo",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if PALOALTO_EXT_IPV6_ADDRESS != "":
    NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = PALOALTO_EXT_IPV6_ADDRESS
if PALOALTO_PUB_IPV6_ADDRESS != "":
    NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = PALOALTO_PUB_IPV6_ADDRESS

NODE_PALOALTO_PNF_DELETE_PARAMS = {
    "vsys_name": "testPalo"
}

# ---------------------------------------------------------------
# Paloalto Share
# ---------------------------------------------------------------
NODE_PALOALTO_SHARE_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "1",
    "device_type": "4",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "admin_id": "nalid",
    "admin_pw": "nalpw",
    "vsys_name": "paloSh",
    "zone_name": "zone1"
}

NODE_PALOALTO_SHARE_PNF_ADD_INTERFACE_PARAMS = {
    "vsys_name": "paloSh",
    "subnet_info": SELECT_SUBNET_02,
    "zone_name": "zone1"
}

NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = {
    "vsys_name": "paloSh",
    "subnet_info": SELECT_SUBNET_V6_01,
    "ip_v6_ext_auto_set_flg": "1",
    "ip_v6_pub_auto_set_flg": "1"
}
if PALOALTO_SHARE_EXT_IPV6_ADDRESS != "":
    NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_ext_auto_set_flg"] = "0"
    NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_ext"] = PALOALTO_SHARE_EXT_IPV6_ADDRESS
if PALOALTO_SHARE_PUB_IPV6_ADDRESS != "":
    NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["ip_v6_pub_auto_set_flg"] = "0"
    NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS["fixed_ip_v6_pub"] = PALOALTO_SHARE_PUB_IPV6_ADDRESS

NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS = {
    "vsys_name": "paloSh"
}

# ---------------------------------------------------------------
# BIG-IP
# ---------------------------------------------------------------
NODE_BIGIP_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "2",
    "device_type": "1",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "fw_ip_address": "",
    "partition_id": "testBigip",
    "route_domain_id": "10000",
    "mng_user_account_id": "mng_account_id",
    "mng_account_password": "mng_account_password",
    "certificate_user_account_id": "pro_account_id",
    "certificate_account_password": "pro_account_password"
}

NODE_BIGIP_PNF_ADD_V6_INTERFACE_PARAMS = {
    "partition_id": "testBigip",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_BIGIP_PNF_DELETE_PARAMS = {
    "partition_id": "testBigip"
}

# ---------------------------------------------------------------
# BIG-IP Share
# ---------------------------------------------------------------
NODE_BIGIP_SHARE_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "2",
    "device_type": "3",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "fw_ip_address": "",
    "partition_id": "testBigSh",
    "route_domain_id": "10000",
    "mng_user_account_id": "mng_account_id",
    "mng_account_password": "mng_account_password",
    "certificate_user_account_id": "pro_account_id",
    "certificate_account_password": "pro_account_password"
}

NODE_BIGIP_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = {
    "partition_id": "testBigSh",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_BIGIP_SHARE_PNF_DELETE_PARAMS = {
    "partition_id": "testBigSh"
}

# ---------------------------------------------------------------
# Thunder
# ---------------------------------------------------------------
NODE_THUNDER_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "2",
    "device_type": "2",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "fw_ip_address": "",
    "partition_name": "testThun",
    "user_account_id": "account_id",
    "account_password": "account_pw"
}

NODE_THUNDER_PNF_ADD_V6_INTERFACE_PARAMS = {
    "partition_name": "testThun",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_THUNDER_PNF_DELETE_PARAMS = {
    "partition_name": "testThun"
}

# ---------------------------------------------------------------
# Thunder Share
# ---------------------------------------------------------------
NODE_THUNDER_SHARE_PNF_CREATE_PARAMS = {
    "apl_type": "2",
    "type": "2",
    "device_type": "4",
    "subnet_info": SELECT_SUBNET_01,
    "redundant_configuration_flg": REDUNDANT_CONF_FLG_02,
    "fw_ip_address": "",
    "partition_name": "testThunSh",
    "user_account_id": "account_id",
    "account_password": "account_pw"
}

NODE_THUNDER_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = {
    "partition_name": "testThunSh",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

NODE_THUNDER_SHARE_PNF_DELETE_PARAMS = {
    "partition_name": "testThunSh"
}

# ---------------------------------------------------------------
# CSR1000v
# ---------------------------------------------------------------
SERVICE_CISCO_L2_CREATE_PARAMS = {
    "service_name": "testCiscoL2",
    "service_type": "2",
    "subnet_info": SELECT_SUBNET_01,
    "bandwidth": "10MB",
    "dns_server_ip_address": "10.58.70.11",
    "ntp_server_ip_address": "10.58.70.12",
    "snmp_server_ip_address": "10.58.70.13",
    "syslog_server_ip_address": "10.58.70.14"
}

SERVICE_CISCO_L2_ADD_INTERFACE_PARAMS = {
    "service_name": "testCiscoL2",
    "subnet_info": SELECT_SUBNET_02
}

SERVICE_CISCO_L2_ADD_V6_INTERFACE_PARAMS = {
    "service_name": "testCiscoL2",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

SERVICE_CISCO_L2_UPDATE_BANDWIDTH_PARAMS = {
    "service_name": "testCiscoL2",
    "bandwidth": "50MB"
}

SERVICE_CISCO_L2_UPDATE_SETTING_PARAMS = {
    "service_name": "testCiscoL2",
    "dns_server_ip_address": "10.58.70.21",
    "ntp_server_ip_address": "10.58.70.22",
    "ntp_server_interface": SELECT_SUBNET_01,
    "snmp_server_ip_address": "10.58.70.23",
    "snmp_server_interface": SELECT_SUBNET_01,
    "snmp_server_delete_flg": "",
    "syslog_server_ip_address": "10.58.70.24",
    "syslog_server_interface": SELECT_SUBNET_01,
    "syslog_server_delete_flg": ""
}

SERVICE_CISCO_L2_DELETE_PARAMS = {
    "service_name": "testCiscoL2",
}

# ---------------------------------------------------------------
# CSR1000v (Encrypted)
# ---------------------------------------------------------------
SERVICE_CISCO_L3_ENCRYPTED_CREATE_PARAMS = {
    "service_name": "testCiscoL3Enc",
    "service_type": "3",
    "subnet_info": SELECT_SUBNET_01,
    "bandwidth": "10MB",
    "dns_server_ip_address": "10.58.70.11",
    "ntp_server_ip_address": "10.58.70.12",
    "snmp_server_ip_address": "10.58.70.13",
    "syslog_server_ip_address": "10.58.70.14"
}

SERVICE_CISCO_L3_ENCRYPTED_ADD_INTERFACE_PARAMS = {
    "service_name": "testCiscoL3Enc",
    "subnet_info": SELECT_SUBNET_02
}

SERVICE_CISCO_L3_ENCRYPTED_ADD_V6_INTERFACE_PARAMS = {
    "service_name": "testCiscoL3Enc",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

SERVICE_CISCO_L3_ENCRYPTED_UPDATE_BANDWIDTH_PARAMS = {
    "service_name": "testCiscoL3Enc",
    "bandwidth": "50MB"
}

SERVICE_CISCO_L3_ENCRYPTED_UPDATE_SETTING_PARAMS = {
    "service_name": "testCiscoL3Enc",
    "dns_server_ip_address": "10.58.70.21",
    "ntp_server_ip_address": "10.58.70.22",
    "ntp_server_interface": SELECT_SUBNET_01,
    "snmp_server_ip_address": "10.58.70.23",
    "snmp_server_interface": SELECT_SUBNET_01,
    "snmp_server_delete_flg": "",
    "syslog_server_ip_address": "10.58.70.24",
    "syslog_server_interface": SELECT_SUBNET_01,
    "syslog_server_delete_flg": ""
}

SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS = {
    "service_name": "testCiscoL3Enc",
}

# ---------------------------------------------------------------
# CSR1000v (Unencrypted)
# ---------------------------------------------------------------
SERVICE_CISCO_L3_PLAIN_CREATE_PARAMS = {
    "service_name": "testCiscoL3Pla",
    "service_type": "4",
    "subnet_info": SELECT_SUBNET_01,
    "bandwidth": "10MB",
    "dns_server_ip_address": "10.58.70.11",
    "ntp_server_ip_address": "10.58.70.12",
    "snmp_server_ip_address": "10.58.70.13",
    "syslog_server_ip_address": "10.58.70.14"
}

SERVICE_CISCO_L3_PLAIN_ADD_INTERFACE_PARAMS = {
    "service_name": "testCiscoL3Pla",
    "subnet_info": SELECT_SUBNET_02
}

SERVICE_CISCO_L3_PLAIN_ADD_V6_INTERFACE_PARAMS = {
    "service_name": "testCiscoL3Pla",
    "subnet_info": SELECT_SUBNET_V6_01,
    "fw_ip_v6_address": ""
}

SERVICE_CISCO_L3_PLAIN_UPDATE_BANDWIDTH_PARAMS = {
    "service_name": "testCiscoL3Pla",
    "bandwidth": "50MB"
}

SERVICE_CISCO_L3_PLAIN_UPDATE_SETTING_PARAMS = {
    "service_name": "testCiscoL3Pla",
    "dns_server_ip_address": "10.58.70.21",
    "ntp_server_ip_address": "10.58.70.22",
    "ntp_server_interface": SELECT_SUBNET_01,
    "snmp_server_ip_address": "10.58.70.23",
    "snmp_server_interface": SELECT_SUBNET_01,
    "snmp_server_delete_flg": "",
    "syslog_server_ip_address": "10.58.70.24",
    "syslog_server_interface": SELECT_SUBNET_01,
    "syslog_server_delete_flg": ""
}

SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS = {
    "service_name": "testCiscoL3Pla",
}

# ---------------------------------------------------------------
# CSR1000v Add Member
# ---------------------------------------------------------------
SERVICE_CISCO_ADD_MEMBER_PARAMS = {
    "subnet_info": SELECT_SUBNET_01,
    "fw_ip_address": ""
}
