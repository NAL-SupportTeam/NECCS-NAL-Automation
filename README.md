# Network Automation Layer (NAL) Auto Setup Tool

## Overview
This tools is Automation tools for NAL. Installation and Test.

The tool is based on Ansible and Selenium.

## Installation and Usage
The procedures described in this document will show how to setup NAL on a single DC using the NAL-Automation Tool.
In case NAL is planned to be deployed on multiple DC, please contact NAL Support Team (via community forum).

■ REQUIREMENTS 
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

■ PREPARATION
1) In the Ansible Controller Node

1-1) It is confirmed that the Ansible Controller Node is able to connect to the NAL VMs.

1-2) Download the installation tool to the ansible home directory (/home/ansible)

`# git clone https://github.com/NAL-SupportTeam/NECCS-NAL-Automation.git /home/ansible`
`# cd /home/ansible`
`# chown -R ansible:ansible nal`
