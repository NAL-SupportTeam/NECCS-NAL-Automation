from conf import config

ZABBIX_VIP_IP = getattr(config, "ZABBIX_VIP_IP")
ZABBIX_01_IP = getattr(config, "ZABBIX_01_IP")
ZABBIX_02_IP = getattr(config, "ZABBIX_02_IP")
DNS_PRIMARY_IP = getattr(config, "DNS_PRIMARY_IP")
DNS_SECONDARY_IP = getattr(config, "DNS_SECONDARY_IP")
NTP_PRAMARY_IP = getattr(config, "NTP_PRAMARY_IP")
NTP_SECONDARY_IP = getattr(config, "NTP_SECONDARY_IP")

SELECT_SUBNET_01 = getattr(config, "SELECT_SUBNET_01")
SELECT_SUBNET_02 = getattr(config, "SELECT_SUBNET_02")
SELECT_SUBNET_V6_01 = getattr(config, "SELECT_SUBNET_V6_01")

PROVISIONING_CREATE_NETWORK_1_PARAMS = getattr(config, "PROVISIONING_CREATE_NETWORK_1_PARAMS")
PROVISIONING_CREATE_NETWORK_2_PARAMS = getattr(config, "PROVISIONING_CREATE_NETWORK_2_PARAMS")
PROVISIONING_ADD_SUBNET_1_PARAMS = getattr(config, "PROVISIONING_ADD_SUBNET_1_PARAMS")
NODE_INTERSECVM_EXT_CREATE_PARAMS = getattr(config, "NODE_INTERSECVM_EXT_CREATE_PARAMS")
NODE_INTERSECVM_EXT_ADD_INTERFACE_PARAMS = getattr(config, "NODE_INTERSECVM_EXT_ADD_INTERFACE_PARAMS")
NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS")
NODE_INTERSECVM_EXT_DELETE_PARAMS = getattr(config, "NODE_INTERSECVM_EXT_DELETE_PARAMS")
NODE_FOORTIGATEVM_CREATE_PARAMS  = getattr(config, "NODE_FOORTIGATEVM_CREATE_PARAMS")
NODE_FOORTIGATEVM_ADD_INTERFACE_PARAMS = getattr(config, "NODE_FOORTIGATEVM_ADD_INTERFACE_PARAMS")
NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS")
NODE_FOORTIGATEVM_DELETE_PARAMS  = getattr(config, "NODE_FOORTIGATEVM_DELETE_PARAMS")
NODE_PALOALTOVM_CREATE_PARAMS  = getattr(config, "NODE_PALOALTOVM_CREATE_PARAMS")
NODE_PALOALTOVM_ASSIGN_LICENSE_PARAMS = getattr(config, "NODE_PALOALTOVM_ASSIGN_LICENSE_PARAMS")
NODE_PALOALTOVM_ADD_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTOVM_ADD_INTERFACE_PARAMS")
NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS")
NODE_PALOALTOVM_DELETE_PARAMS  = getattr(config, "NODE_PALOALTOVM_DELETE_PARAMS")
NODE_INTERSECVM_PUB_CREATE_PARAMS = getattr(config, "NODE_INTERSECVM_PUB_CREATE_PARAMS")
NODE_INTERSECVM_PUB_ADD_INTERFACE_PARAMS = getattr(config, "NODE_INTERSECVM_PUB_ADD_INTERFACE_PARAMS")
NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS")
NODE_INTERSECVM_PUB_DELETE_PARAMS = getattr(config, "NODE_INTERSECVM_PUB_DELETE_PARAMS")
NODE_FORTIGATEVM_541_CREATE_PARAMS = getattr(config, "NODE_FORTIGATEVM_541_CREATE_PARAMS")
NODE_FORTIGATEVM_541_ADD_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATEVM_541_ADD_INTERFACE_PARAMS")
NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS")
NODE_FORTIGATEVM_541_DELETE_PARAMS = getattr(config, "NODE_FORTIGATEVM_541_DELETE_PARAMS")
NODE_INTERSECVM_LB_CREATE_PARAMS = getattr(config, "NODE_INTERSECVM_LB_CREATE_PARAMS")
NODE_INTERSECVM_LB_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_INTERSECVM_LB_ADD_V6_INTERFACE_PARAMS")
NODE_INTERSECVM_LB_DELETE_PARAMS = getattr(config, "NODE_INTERSECVM_LB_DELETE_PARAMS")
NODE_BIGIP_VE_CREATE_PARAMS  = getattr(config, "NODE_BIGIP_VE_CREATE_PARAMS")
NODE_BIGIP_VE_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_BIGIP_VE_ADD_V6_INTERFACE_PARAMS")
NODE_BIGIP_VE_DELETE_PARAMS  = getattr(config, "NODE_BIGIP_VE_DELETE_PARAMS")
NODE_VTHUNDER_CREATE_PARAMS  = getattr(config, "NODE_VTHUNDER_CREATE_PARAMS")
NODE_VTHUNDER_ASSIGN_LICENSE_PARAMS = getattr(config, "NODE_VTHUNDER_ASSIGN_LICENSE_PARAMS")
NODE_VTHUNDER_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_VTHUNDER_ADD_V6_INTERFACE_PARAMS")
NODE_VTHUNDER_DELETE_PARAMS  = getattr(config, "NODE_VTHUNDER_DELETE_PARAMS")
NODE_VTHUNDER_411_CREATE_PARAMS  = getattr(config, "NODE_VTHUNDER_411_CREATE_PARAMS")
NODE_VTHUNDER_411_ASSIGN_LICENSE_PARAMS = getattr(config, "NODE_VTHUNDER_411_ASSIGN_LICENSE_PARAMS")
NODE_VTHUNDER_411_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_VTHUNDER_411_ADD_V6_INTERFACE_PARAMS")
NODE_VTHUNDER_411_DELETE_PARAMS  = getattr(config, "NODE_VTHUNDER_411_DELETE_PARAMS")
NODE_FORTIGATE_PNF_CREATE_PARAMS = getattr(config, "NODE_FORTIGATE_PNF_CREATE_PARAMS")
NODE_FORTIGATE_PNF_ADD_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATE_PNF_ADD_INTERFACE_PARAMS")
NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_FORTIGATE_PNF_DELETE_PARAMS = getattr(config, "NODE_FORTIGATE_PNF_DELETE_PARAMS")
NODE_FORTIGATE_SHARE_PNF_CREATE_PARAMS = getattr(config, "NODE_FORTIGATE_SHARE_PNF_CREATE_PARAMS")
NODE_FORTIGATE_SHARE_PNF_ADD_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATE_SHARE_PNF_ADD_INTERFACE_PARAMS")
NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS = getattr(config, "NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS")
NODE_PALOALTO_PNF_CREATE_PARAMS  = getattr(config, "NODE_PALOALTO_PNF_CREATE_PARAMS")
NODE_PALOALTO_PNF_ADD_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTO_PNF_ADD_INTERFACE_PARAMS")
NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_PALOALTO_PNF_DELETE_PARAMS  = getattr(config, "NODE_PALOALTO_PNF_DELETE_PARAMS")
NODE_PALOALTO_SHARE_PNF_CREATE_PARAMS  = getattr(config, "NODE_PALOALTO_SHARE_PNF_CREATE_PARAMS")
NODE_PALOALTO_SHARE_PNF_ADD_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTO_SHARE_PNF_ADD_INTERFACE_PARAMS")
NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS  = getattr(config, "NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS")
NODE_BIGIP_PNF_CREATE_PARAMS  = getattr(config, "NODE_BIGIP_PNF_CREATE_PARAMS")
NODE_BIGIP_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_BIGIP_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_BIGIP_PNF_DELETE_PARAMS  = getattr(config, "NODE_BIGIP_PNF_DELETE_PARAMS")
NODE_BIGIP_SHARE_PNF_CREATE_PARAMS = getattr(config, "NODE_BIGIP_SHARE_PNF_CREATE_PARAMS")
NODE_BIGIP_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_BIGIP_SHARE_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_BIGIP_SHARE_PNF_DELETE_PARAMS = getattr(config, "NODE_BIGIP_SHARE_PNF_DELETE_PARAMS")
NODE_THUNDER_PNF_CREATE_PARAMS  = getattr(config, "NODE_THUNDER_PNF_CREATE_PARAMS")
NODE_THUNDER_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_THUNDER_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_THUNDER_PNF_DELETE_PARAMS  = getattr(config, "NODE_THUNDER_PNF_DELETE_PARAMS")
NODE_THUNDER_SHARE_PNF_CREATE_PARAMS = getattr(config, "NODE_THUNDER_SHARE_PNF_CREATE_PARAMS")
NODE_THUNDER_SHARE_PNF_ADD_V6_INTERFACE_PARAMS = getattr(config, "NODE_THUNDER_SHARE_PNF_ADD_V6_INTERFACE_PARAMS")
NODE_THUNDER_SHARE_PNF_DELETE_PARAMS = getattr(config, "NODE_THUNDER_SHARE_PNF_DELETE_PARAMS")
SERVICE_CISCO_L2_CREATE_PARAMS  = getattr(config, "SERVICE_CISCO_L2_CREATE_PARAMS")
SERVICE_CISCO_L2_ADD_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L2_ADD_INTERFACE_PARAMS")
SERVICE_CISCO_L2_ADD_V6_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L2_ADD_V6_INTERFACE_PARAMS")
SERVICE_CISCO_L2_UPDATE_BANDWIDTH_PARAMS = getattr(config, "SERVICE_CISCO_L2_UPDATE_BANDWIDTH_PARAMS")
SERVICE_CISCO_L2_UPDATE_SETTING_PARAMS = getattr(config, "SERVICE_CISCO_L2_UPDATE_SETTING_PARAMS")
SERVICE_CISCO_L2_DELETE_PARAMS  = getattr(config, "SERVICE_CISCO_L2_DELETE_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_CREATE_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_CREATE_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_ADD_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_ADD_INTERFACE_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_ADD_V6_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_ADD_V6_INTERFACE_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_UPDATE_BANDWIDTH_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_UPDATE_BANDWIDTH_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_UPDATE_SETTING_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_UPDATE_SETTING_PARAMS")
SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS = getattr(config, "SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS")
SERVICE_CISCO_L3_PLAIN_CREATE_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_CREATE_PARAMS")
SERVICE_CISCO_L3_PLAIN_ADD_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_ADD_INTERFACE_PARAMS")
SERVICE_CISCO_L3_PLAIN_ADD_V6_INTERFACE_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_ADD_V6_INTERFACE_PARAMS")
SERVICE_CISCO_L3_PLAIN_UPDATE_BANDWIDTH_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_UPDATE_BANDWIDTH_PARAMS")
SERVICE_CISCO_L3_PLAIN_UPDATE_SETTING_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_UPDATE_SETTING_PARAMS")
SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS = getattr(config, "SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS")
SERVICE_CISCO_ADD_MEMBER_PARAMS = getattr(config, "SERVICE_CISCO_ADD_MEMBER_PARAMS")

#----------------------------------------------------------------
# Provisioning
#----------------------------------------------------------------
provisioning_for_auto_test = [
    {
        "method": "global_sign_in",
    },
    {
        "method": "global_change_setting",
    },
    {
        "method": "global_change_project",
    },
    {
        "method": "create_user",
    },
    {
        "method": "create_role",
    },
    {
        "method": "create_project",
    },
    {
        "method": "add_admin_user",
    },
    {
        "method": "sign_out",
    },
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "create_network",
        "input_params": PROVISIONING_CREATE_NETWORK_1_PARAMS
    },
    {
        "method": "add_subnet",
        "input_params": PROVISIONING_ADD_SUBNET_1_PARAMS
    },
    {
        "method": "sign_out",
    }
]

# ---------------------------------------------------------------
# InterSecVM SG for Ext
# ---------------------------------------------------------------
node_intersecvm_sg_for_ext_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_INTERSECVM_EXT_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_INTERSECVM_EXT_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_INTERSECVM_EXT_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_ext_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_INTERSECVM_EXT_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_ext_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_INTERSECVM_EXT_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_ext_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_INTERSECVM_EXT_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_ext_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_INTERSECVM_EXT_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# FortiGateVM
# ---------------------------------------------------------------
node_fortigatevm_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_FOORTIGATEVM_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_FOORTIGATEVM_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_FOORTIGATEVM_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_FOORTIGATEVM_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_FOORTIGATEVM_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_FOORTIGATEVM_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# PaloAltoVM
# ---------------------------------------------------------------
node_paloaltovm_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_PALOALTOVM_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_PALOALTOVM_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_PALOALTOVM_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloaltovm_assign_license = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_assign_license",
        "input_params": NODE_PALOALTOVM_ASSIGN_LICENSE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloaltovm_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_PALOALTOVM_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloaltovm_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_PALOALTOVM_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloaltovm_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_PALOALTOVM_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# InterSecVM SG for Pub
# ---------------------------------------------------------------
node_intersecvm_sg_for_pub_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_INTERSECVM_PUB_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_INTERSECVM_PUB_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_INTERSECVM_PUB_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_pub_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_INTERSECVM_PUB_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_pub_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_INTERSECVM_PUB_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_pub_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_INTERSECVM_PUB_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_sg_for_pub_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_INTERSECVM_PUB_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# FortiGateVM 5.4.1
# ---------------------------------------------------------------
node_fortigatevm_541_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_FORTIGATEVM_541_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_FORTIGATEVM_541_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_FORTIGATEVM_541_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_541_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_FORTIGATEVM_541_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_541_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_FORTIGATEVM_541_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigatevm_541_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_FORTIGATEVM_541_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# InterSecVM LB
# ---------------------------------------------------------------
node_intersecvm_lb_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_INTERSECVM_LB_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_INTERSECVM_LB_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_INTERSECVM_LB_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_lb_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_INTERSECVM_LB_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_intersecvm_lb_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_INTERSECVM_LB_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# BIG-IP VE
# ---------------------------------------------------------------
node_bigip_ve_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_BIGIP_VE_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_BIGIP_VE_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_BIGIP_VE_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_ve_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_BIGIP_VE_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_ve_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_BIGIP_VE_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# vThunder(4.0.1)
# ---------------------------------------------------------------
node_vthunder_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_VTHUNDER_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_VTHUNDER_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_VTHUNDER_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_assign_license = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_assign_license",
        "input_params": NODE_VTHUNDER_ASSIGN_LICENSE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_VTHUNDER_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_VTHUNDER_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# vThunder(4.1.1)
# ---------------------------------------------------------------
node_vthunder_411_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_VTHUNDER_411_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_VTHUNDER_411_DELETE_PARAMS
    },
    {
        "method": "node_list_admin",
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_VTHUNDER_411_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_411_assign_license = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_assign_license",
        "input_params": NODE_VTHUNDER_411_ASSIGN_LICENSE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_411_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_VTHUNDER_411_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_vthunder_411_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_VTHUNDER_411_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Fortigate
# ---------------------------------------------------------------
node_fortigate_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_FORTIGATE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_FORTIGATE_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_FORTIGATE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_pnf_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_FORTIGATE_PNF_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_FORTIGATE_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_pnf_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_FORTIGATE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_FORTIGATE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Fortigate Share
# ---------------------------------------------------------------
node_fortigate_share_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_FORTIGATE_SHARE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_share_pnf_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_FORTIGATE_SHARE_PNF_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_share_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_FORTIGATE_SHARE_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_share_pnf_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_fortigate_share_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_FORTIGATE_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Paloalto
# ---------------------------------------------------------------
node_paloalto_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_PALOALTO_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_PALOALTO_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_PALOALTO_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_pnf_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_PALOALTO_PNF_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_PALOALTO_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_pnf_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_PALOALTO_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_PALOALTO_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Paloalto Share
# ---------------------------------------------------------------
node_paloalto_share_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_PALOALTO_SHARE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_PALOALTO_SHARE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_share_pnf_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_interface",
        "input_params": NODE_PALOALTO_SHARE_PNF_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_share_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_PALOALTO_SHARE_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_share_pnf_delete_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete_interface",
        "input_params": NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_paloalto_share_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_PALOALTO_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# BIG-IP
# ---------------------------------------------------------------
node_bigip_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_BIGIP_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_BIGIP_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_BIGIP_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_BIGIP_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_BIGIP_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# BIG-IP Share
# ---------------------------------------------------------------
node_bigip_share_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_BIGIP_SHARE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_BIGIP_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_BIGIP_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_share_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_BIGIP_SHARE_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_bigip_share_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_BIGIP_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Thunder
# ---------------------------------------------------------------
node_thunder_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_THUNDER_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_THUNDER_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_THUNDER_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_thunder_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_THUNDER_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_thunder_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_THUNDER_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Thunder Share
# ---------------------------------------------------------------
node_thunder_share_pnf_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_create",
        "input_params": NODE_THUNDER_SHARE_PNF_CREATE_PARAMS
    },
    {
        "method": "node_list",
    },
    {
        "method": "node_detail",
        "input_params": NODE_THUNDER_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "node_list_admin"
    },
    {
        "method": "node_detail_admin",
        "input_params": NODE_THUNDER_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_thunder_share_pnf_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_add_v6_interface",
        "input_params": NODE_THUNDER_SHARE_PNF_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

node_thunder_share_pnf_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "node_delete",
        "input_params": NODE_THUNDER_SHARE_PNF_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# CSR1000v
# ---------------------------------------------------------------
service_cisco_l2_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_create",
        "input_params": SERVICE_CISCO_L2_CREATE_PARAMS
    },
    {
        "method": "service_list"
    },
    {
        "method": "service_detail",
        "input_params": SERVICE_CISCO_L2_DELETE_PARAMS
    },
    {
        "method": "service_list_admin"
    },
    {
        "method": "service_detail_admin",
        "input_params": SERVICE_CISCO_L2_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l2_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_interface",
        "input_params": SERVICE_CISCO_L2_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l2_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_v6_interface",
        "input_params": SERVICE_CISCO_L2_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l2_update_bandwidth = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_bandwidth",
        "input_params": SERVICE_CISCO_L2_UPDATE_BANDWIDTH_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l2_update_setting = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_setting",
        "input_params": SERVICE_CISCO_L2_UPDATE_SETTING_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l2_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_delete",
        "input_params": SERVICE_CISCO_L2_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# CSR1000v (Encrypted)
# ---------------------------------------------------------------
service_cisco_l3_encrypted_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_create",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_CREATE_PARAMS
    },
    {
        "method": "service_list"
    },
    {
        "method": "service_detail",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS
    },
    {
        "method": "service_list_admin"
    },
    {
        "method": "service_detail_admin",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_encrypted_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_interface",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_encrypted_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_v6_interface",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_encrypted_update_bandwidth = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_bandwidth",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_UPDATE_BANDWIDTH_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_encrypted_update_setting = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_setting",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_UPDATE_SETTING_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_encrypted_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_delete",
        "input_params": SERVICE_CISCO_L3_ENCRYPTED_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# CSR1000v (Unencrypted)
# ---------------------------------------------------------------
service_cisco_l3_plain_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_create",
        "input_params": SERVICE_CISCO_L3_PLAIN_CREATE_PARAMS
    },
    {
        "method": "service_list"
    },
    {
        "method": "service_detail",
        "input_params": SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS
    },
    {
        "method": "service_list_admin"
    },
    {
        "method": "service_detail_admin",
        "input_params": SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_plain_add_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_interface",
        "input_params": SERVICE_CISCO_L3_PLAIN_ADD_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_plain_add_v6_interface = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_v6_interface",
        "input_params": SERVICE_CISCO_L3_PLAIN_ADD_V6_INTERFACE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_plain_update_bandwidth = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_bandwidth",
        "input_params": SERVICE_CISCO_L3_PLAIN_UPDATE_BANDWIDTH_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_plain_update_setting = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_setting",
        "input_params": SERVICE_CISCO_L3_PLAIN_UPDATE_SETTING_PARAMS
    },
    {
        "method": "sign_out"
    }
]

service_cisco_l3_plain_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_delete",
        "input_params": SERVICE_CISCO_L3_PLAIN_DELETE_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# CSR1000v Add Member
# ---------------------------------------------------------------
service_cisco_add_member = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "service_add_member",
        "input_params": SERVICE_CISCO_ADD_MEMBER_PARAMS
    },
    {
        "method": "sign_out"
    }
]

# ---------------------------------------------------------------
# Global IP
# ---------------------------------------------------------------
resource_globalip_create = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "resource_create",
        "input_params": {
            "resource_name": "Global IP"
        }
    },
    {
        "method": "resource_list",
    },
    {
        "method": "resource_detail",
        "input_params": {
            "resource_name": "Global IP"
        }
    },
    {
        "method": "resource_list_admin"
    },
    {
        "method": "resource_detail_admin",
        "input_params": {
            "resource_name": "Global IP"
        }
    },
    {
        "method": "sign_out"
    }
]

resource_globalip_update = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "resource_update",
        "input_params": {
            "resource_name": "Global IP"
        }
    },
    {
        "method": "sign_out"
    }
]

resource_globalip_delete = [
    {
        "method": "sign_in",
    },
    {
        "method": "change_setting",
    },
    {
        "method": "change_project",
    },
    {
        "method": "resource_delete",
        "input_params": {
            "resource_name": "Global IP"
        }
    },
    {
        "method": "sign_out"
    }
]
