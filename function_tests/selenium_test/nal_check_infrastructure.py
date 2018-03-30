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


import datetime
import os
import shutil
import subprocess
import sys
import time

from assemble import nal as nal_list
import base
from conf import config
from conf import test_scenario

from selenium import webdriver

SET_BASE_URL = getattr(config, "SET_BASE_URL")
SET_WIDTH = getattr(config, "SET_WIDTH", 1280)
SET_HEIGHT = getattr(config, "SET_HEIGHT", 1024)
SET_TIMEOUT = getattr(config, "SET_TIMEOUT", 5)
SET_PROFILE_PATH = getattr(config, "SET_PROFILE_PATH",
                           "/home/ansible/.mozilla/firefox/")


class SeleniumNalTest(base.SeleniumBase):

    def __init__(self, driver, evidence):
        super(SeleniumNalTest, self).__init__(driver, evidence)
        self.driver = driver
        self.evidence = evidence

    def main(self):

        test_scenario_name = sys.argv[1]
        test_flow = getattr(test_scenario, test_scenario_name)
        test_instance = nal_list.NalTestMethod(self.driver, self.evidence)

        self.output_log_start(test_scenario_name)
        for test_info in test_flow:
            try:
                test_method = test_info["method"]
                input_params = test_info.get("input_params", None)
                test_method_attr = getattr(test_instance, test_method)
                if input_params:
                    test_method_attr(input_params)
                else:
                    test_method_attr()
            except Exception as e:
                self.output_log_result(test_method, "NG")
                self.output_log_end()
                raise e
            self.output_log_result(test_method, "OK")

        self.output_log_end()


if __name__ == "__main__":

    # profile check
    if os.path.exists(SET_PROFILE_PATH):
        shutil.rmtree(SET_PROFILE_PATH)

    # Create Firefox Profile for test
    cmd = "firefox -CreateProfile default"
    subprocess.call(cmd.strip().split(" "))

    if not os.path.exists(SET_PROFILE_PATH):
        raise Exception("Profile does not exist")

    for folder_name in os.listdir(SET_PROFILE_PATH):
        if os.path.isdir(SET_PROFILE_PATH + folder_name):
            if folder_name.count('.default'):
                profile = SET_PROFILE_PATH + folder_name
                break
    else:
        raise Exception("Profile does not exist")

    # Authentication setting for https
    override_profile_pass = os.path.abspath(os.path.dirname(__file__))
    cert_override = override_profile_pass + "/profile/cert_override.txt"
    if os.path.exists(cert_override):
        shutil.copy(cert_override, profile)

    # Run automated test
    selenium_driver = webdriver.Firefox(firefox_profile=profile)
    selenium_driver.implicitly_wait(30)
    selenium_driver.set_window_size(SET_WIDTH, SET_HEIGHT)

    now_time = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    evidence = {"evidence_name": str(now_time)}
    try:
        selenium_test = SeleniumNalTest(selenium_driver, evidence)
        selenium_test.main()
    except Exception as e:
        print(e)

    selenium_driver.quit()

    shutil.rmtree(SET_PROFILE_PATH)
    time.sleep(5)
