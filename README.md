# Network Automation Layer (NAL) Auto Setup Tool

## Overview
This tools is Automation tools for NAL. Installation and Test.

The tool is based on Ansible and Selenium.

## Installation and Usage
The procedures described in this document will show how to setup NAL on a single DC using the NAL-Automation Tool.
In case NAL is planned to be deployed on multiple DC, please contact NAL Support Team (via community forum).

### ■ REQUIREMENTS 
1)  An Ansible Controller Node

Setup and installation of Ansible is not covered in this document.
Please prepare it in advance.

2)  10 VMs for NAL WIM-DC

Recommended VM Configuration:

![Alt text](images/vm_specs.png)
   
※Number of CPUs allocated using KVM in an environment using Hyper-Threading, two Intel Xeon processors E5-2660v3 (2.6 GHz)

3)  NAL Parameters (TODO)

■ NETWORK CONFIGURATION

![Alt text](images/configuration.png)

### ■ PREPARATION
#### 1) In the Ansible Controller Node

1-1) It is confirmed that the Ansible Controller Node is able to connect to the NAL VMs.

1-2) Download the installation tool to the ansible home directory (/home/ansible)
<pre># git clone https://github.com/NAL-SupportTeam/NECCS-NAL-Automation.git /home/ansible
# cd /home/ansible
# chown -R ansible:ansible nal</pre>

1-3) Using an editor, update the inventory source file according to NAL parameters
<pre>
# su – ansible
$ vi /home/ansible/nal/hosts.ini</pre>
  [nallbservers]<br/>
  `NAL Web-LB#1 Hostname` ansible_host=`NAL Web-LB#1 SVmng IP Address` is_first_active_node=active index=0<br/>
  `NAL Web-LB#2 Hostname` ansible_host=`NAL Web-LB#2 SVmng IP Address` is_first_active_node=standby index=1<br/>
  <br/>
  [nalwebservers]<br/>
  `NAL Web#1 Hostname` ansible_host=`NAL Web#1 SVmng IP Address` is_first_active_node=active index=0<br/>
  `NAL Web#2 Hostname` ansible_host=`NAL Web#2 SVmng IP Address` is_first_active_node=active index=1<br/>
  <br/>
  [nalapservers]<br/>
  `NAL AP#1 Hostname` ansible_host=`NAL AP#1 SVmng IP Address` is_first_active_node=active index=0<br/>
  `NAL AP#2 Hostname` ansible_host=`NAL AP#2 SVmng IP Address` is_first_active_node=standby index=1<br/>
  <br/>
  [naldbservers]<br/>
  `NAL DB#1 Hostname` ansible_host=`NAL DB#1 SVmng IP Address` is_first_active_node=active index=0<br/>
  `NAL DB#2 Hostname` ansible_host=`NAL DB#2 SVmng IP Address` is_first_active_node=standby index=1<br/>
  <br/>
  [nalfeservers]<br/>
  `NAL FE#1 Hostname` ansible_host=`NAL FE#1 SVmng IP Address` is_first_active_node=active index=0<br/>
  `NAL FE#2 Hostname` ansible_host=`NAL FE#2 SVmng IP Address` is_first_active_node=active index=1<br/>
  ...<br/>

1-4) Using an editor, update the ansible configuration file according to NAL parameters
```
# su – ansible
$ vi /home/ansible/nal/group_vars/all/common.yml
```
**TODO**

1-5) Update the initial data for NAL Database
- Copy and extract the initial data archive for NAL DB into an arbitrary directory.
```
# su – ansible
$ cp –p ~/nal/playbooks/roles/nal_initdb/files/nal-template.tar.gz /tmp/wk.tar.gz
$ cd /tmp
$ tar zxvf wk.tar.gz
```
- Update the values in the following files according to the NAL parameter sheet.
```
/tmp/template/init_NAL_*.sql
/tmp/template/init_WIM_*.sql
```
- Create an archive with the updated files and replace the initial data archive for NAL DB with this one.
```
$ cd /tmp
$ tar -zcvf nal-template.tar.gz template
$ cp –f nal-template.tar.gz ~/nal/playbooks/roles/nal_initdb/files/.
```
1-6) Replace the MSO public key 
```
# su – ansible
$ cd ~/nal/playbooks/roles/nal_nwa/files/
$ scp –p root@<MSO IP Address>:/root/.ssh/id_rsa.pub id_rsa_msa_to_intersec.pub
```
   _*NOTE*: If MSO public key does not exists, create one._
   
1-7) Get the <userID> of the Ansible User
```
# grep ansible /etc/passwd
ansible:x:1001:1001::/home/ansible:/bin/bash
```

1-8) Get the public key of the “Ansible Controller” Node
```
# cd /home/ansible/.ssh
# cat id_rsa.pub
```

#### 2. NAL Components
On each NAL Component VM, perform the following steps

2-1) Create ansible user (if not exists)
`# useradd -d /home/ansible -m ansible -u <userID>`

2-2) Add the public key of the “Ansible Controller” Node to the ansible user ssh authorized_keys
```
# su – ansible
$ mkdir ~/.ssh                    ## create if it does not exists
$ chmod 700 ~/.ssh
$ cd ~/.ssh
$ vi authorized_keys
          <append the public key of the “Ansible Controller Node”>
$ chmod 600 authorized_keys
```

2-3) Add sudo execution rights. Skip if definition already exists.
```
# vi sudo
…
ansible ALL=(ALL)       NOPASSWD:ALL               ## add this line
```

2-4) Update SSH Settings
```
# vi /etc/ssh/sshd_config
…
RSAAuthentication yes
PubkeyAuthentication yes
…
# systemctl restart sshd
```

2-5) Generate the authentication keys for each NAL component server pair. <br/>
Run the following commands on each #1 node.
```
# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):      <Press the enter key>
Enter passphrase (empty for no passphrase):                   <Press the enter key>
Enter same passphrase again:                                  <Press the enter key>
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
...
# ssh-copy-id -i ~/.ssh/id_rsa.pub root@<NAL XX#2>
```

#### 3. Check the connection
Check if SSH connection using the public key is possible

3-1) Between "Ansible Controller Node" and NAL Component VMs
```
# su - ansible
$ ssh -i ~/.ssh/id_rsa ansible@<NAL VM SVmng IP Address>
```

3-2) Between NAL Server Pairs
`# ssh -i ~/.ssh/id_rsa root@<SVmng IP Address of #2>`

_*Note:* These steps are required. A confirmation prompt is displayed during initial connection. The tool may not work properly if input is requested during operation._

### ■ Installation

1	Run the installation tool. <br/>
Login to the ansible controller node and run the tool
```
# su – ansible
$ cd /home/ansible/nal
$ sh ./setup.sh 
```

2	Check the status using ansible.
```
$ cd /home/ansible/nal
$ sh ./unittest.sh
```

Logs can be found in /home/ansible/nal/logs/ directory.
If errors are encountered during operation, please check the logs and rerun the script after fixing the cause.


