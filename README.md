# Network Automation Layer (NAL) Auto Setup Tool

## Overview
This is the automation tool for NAL installation and testing.

This tool is based on Ansible and Selenium.

## Installation
This guide will cover the installation and configuration of NAL using the NAL-Automation Tool.

### ■ REQUIREMENTS 
#### (1)  An Ansible Controller Node

Setup and installation of **Ansible** are not covered in this document.
</br>Please prepare it in advance.

#### (2) An NFS Server 

Setup and installation of the **NFS Server** are not covered in this document.
</br>Please prepare it in advance.

#### (3) OpenMSA 

Setup and installation of the **OpenMSA** are not covered in this document. Please refer to the [OpenMSA Installation Guide](https://www.openmsa.co/documentation/getting-started-with-the-openmsa-freeware/).
</br>Please prepare it in advance.

#### (4) 10 VMs for the NAL Components

Recommended VM Configuration:

![Alt text](images/vm_specs.png)

※ `NAL Portal` is installed in a machine where OpenStack Horizon exists. Please install and configure OpenStack Horizon beforehand.
   
   
■ NETWORK CONFIGURATION

![Alt text](images/network_configuration.png)

**Notes:**
</br> - This guide covers the automated installation and configuration of the components in ![Alt text](images/box.png) using ansible.
</br> - For networks, a single or multiple networks can be used for each network connection.

### ■ PREPARATION
#### (1) An Ansible Controller Node, already configured and connected to the `SVmng` network.
#### (2) An NFS Server, already configured and connected to the `storage` network.
#### (3) An OpenMSA, already configured and connected to the `SVmng` network.
#### (4) In the Ansible Controller Node, perform the following.
4-1 Download the NAL-Automation tool to the `ansible` home directory (/home/ansible)
```
# git clone https://github.com/NAL-SupportTeam/NECCS-NAL-Automation.git /home/ansible
# cd /home/ansible
# chown -R ansible:ansible nal
```

4-2 Switch to `ansible` user.
```
# su - ansible
```

4-3 Update the inventory source file according to the target configuration.
```
$ vi /home/ansible/nal/hosts.ini
```
```ini
[nallbservers]
<NAL Web-LB #1 Hostname> ansible_host=<NAL Web-LB #1 IP Address for SVmng> is_first_active_node=active  index=0
<NAL Web-LB #2 Hostname> ansible_host=<NAL Web-LB #2 IP Address for SVmng> is_first_active_node=standby index=1

[nalwebservers]
<NAL Web #1 Hostname> ansible_host=<NAL Web #1 IP Address for SVmng> is_first_active_node=active  index=0
<NAL Web #2 Hostname> ansible_host=<NAL Web #2 IP Address for SVmng> is_first_active_node=active  index=1

[nalapservers]
<NAL AP #1 Hostname> ansible_host=<NAL AP #1 IP Address for SVmng> is_first_active_node=active  index=0
<NAL AP #2 Hostname> ansible_host=<NAL AP #2 IP Address for SVmng> is_first_active_node=standby index=1

[naldbservers]
<NAL DB #1 Hostname> ansible_host=<NAL DB #1 IP Address for SVmng> is_first_active_node=active  index=0
<NAL DB #2 Hostname> ansible_host=<NAL DB #2 IP Address for SVmng> is_first_active_node=standby index=1

[nalfeservers]
<NAL Portal #1 Hostname> ansible_host=<NAL Portal #1 IP Address for SVmng>  is_first_active_node=active  index=0
<NAL Portal #2 Hostname> ansible_host=<NAL Portal #2 IP Address for SVmng>  is_first_active_node=active  index=1
...
  ```
4-4 Update the ansible configuration file according to the target configuration settings.
```
$ vi /home/ansible/nal/group_vars/all/common.yml
```

4-5 Update the initial data for NAL DB.

4-5-1 Copy and extract the initial data archive for NAL DB into an arbitrary directory.
```
$ cp –p ~/nal/playbooks/roles/nal_initdb/files/nal-template.tar.gz /tmp/wk.tar.gz
$ cd /tmp
$ tar zxvf wk.tar.gz
```
4-5-2 Update the values in the following files according to the target configuration settings.
```
/tmp/template/init_NAL_*.sql
/tmp/template/init_WIM_*.sql
```
4-5-3 Create an archive with the updated files and replace the initial data archive for NAL DB with this one.
```
$ cd /tmp
$ tar -zcvf nal-template.tar.gz template
$ cp –f nal-template.tar.gz ~/nal/playbooks/roles/nal_initdb/files/.
```

4-6 Replace the public key file for OpenMSA.
```
$ cd ~/nal/playbooks/roles/nal_nwa/files/
$ scp –p root@<OpenMSA IP Address>:/root/.ssh/id_rsa.pub id_rsa_msa_to_intersec.pub
```
   _**NOTE**: If the OpenMSA public key does not exist, please create one._
   
4-7 Get the `<userID>` (UID) of the Ansible User.
```
$ grep ansible /etc/passwd
ansible:x:1001:1001::/home/ansible:/bin/bash
```
The response is delimited by a colon `:`. It is the 3rd value from the left.

4-8 Get the public key of the "Ansible Controller Node".
```
$ cd /home/ansible/.ssh
$ cat id_rsa.pub
```

#### (5) In each NAL Component VM, perform the following.
5-1 Login as root and create the `ansible` user (_if it does not exist yet_)
```
# useradd -d /home/ansible -m ansible -u <userID>
```

**NOTE:** `<userID>` is the value retrieved from step 4-7.

5-2 Append the public key of the "Ansible Controller Node" to the ssh authorized_keys of the `ansible` user.
```
# su – ansible
$ mkdir ~/.ssh                                                     ## create if it does not exist yet
$ chmod 700 ~/.ssh
$ cd ~/.ssh
$ vi authorized_keys
          <append the public key of the "Ansible Controller Node">
$ chmod 600 authorized_keys
$ exit
```
5-3 Add `sudo` execution rights. Skip if the definition already exists.
```
# visudo
...
ansible ALL=(ALL)       NOPASSWD:ALL                               ## add this line
```
5-4 Update the SSH Settings as shown below.
```
# vi /etc/ssh/sshd_config
...
RSAAuthentication yes
PubkeyAuthentication yes
...
# systemctl restart sshd
```
5-5 Generate the authentication key for each NAL component server pair. 

Run the following commands on each `VM#1` node then copy the public key to the pair node - `VM#2`.
```
# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):           ##Press the enter key
Enter passphrase (empty for no passphrase):                        ##Press the enter key
Enter same passphrase again:                                       ##Press the enter key
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
...
# ssh-copy-id -i ~/.ssh/id_rsa.pub root@<NAL XX#2>
```

#### (6) Check the connection between VMs.
Check if SSH connection using the public key is possible.

6-1 Login to the "Ansible Controller Node" and check the connection to each of the NAL Component VMs.
```
# su - ansible
$ ssh -i ~/.ssh/id_rsa ansible@<NAL VM SVmng IP Address>
```
6-2 For each NAL Component, login to NAL #1 VM and check the connection to NAL #2 VM.
```
# ssh -i ~/.ssh/id_rsa root@<SVmng IP Address of #2>
```

_**Note:** The tool connects to each target host via SSH using an authentication key. Since a confirmation prompt is displayed during SSH initial connection, make sure to run these steps. The tool may not work properly if in case input is requested during installation operation._


### ■ INSTALLATION
#### (1)	Run the installation tool.
Login to the "Ansible Controller Node" and run the tool
```
# su – ansible
$ cd /home/ansible/nal
$ sh ./setup.sh 
```
#### (2)	Check the status by running the following script.
```
$ cd /home/ansible/nal
$ sh ./unittest.sh
```

If errors are encountered during operation, make sure that all preparatory steps were performed.</br>
Check the logs and rerun the script after fixing the cause.</br>
Logs can be found in `/home/ansible/nal/logs/` directory.
