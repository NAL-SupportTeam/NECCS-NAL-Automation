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
import time

from conf import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

SET_BASE_URL = getattr(config, 'SET_BASE_URL')
SET_WIDTH = getattr(config, 'SET_WIDTH', 1280)
SET_HEIGHT = getattr(config, 'SET_HEIGHT', 1024)
SET_TIMEOUT = getattr(config, 'SET_TIMEOUT', 5)
SET_EVIDENCE = getattr(config, 'SET_EVIDENCE', 'evidence/')
SET_NAL_VERSION = getattr(config, "SET_NAL_VERSION")


class SeleniumBase(object):
    def __init__(self, driver, evidence):
        self.driver = driver
        self.evidence = evidence

    def sleep_time(self, wait_time=SET_TIMEOUT):
        time.sleep(wait_time)

    def output_log_start(self, test_name):
        # Make log message
        output_text = "--------------------Test Start--------------------"
        self.output_log(output_text)
        output_text = "[TestName]" + test_name
        self.output_log(output_text)

    def output_log_result(self, process_name, result):
        # Make log message
        output_text = "[Time]" + str(datetime.datetime.today()) \
                      + " [ProcessName]" + process_name + " [Result]" + result
        self.output_log(output_text)

    def output_log_end(self):
        # Make log message
        output_text = "--------------------Test End--------------------"
        self.output_log(output_text)
        self.output_log("")

    def output_log(self, output_text):
        # Make directory.
        filepath = SET_EVIDENCE + self.evidence["evidence_name"] + "/logs"
        if not os.path.isdir(filepath):
            os.makedirs(filepath)

        # Make file.
        filename = "nal_auto_test.log"
        if not os.path.isfile(filepath + "/" + filename):
            f = open(filepath + "/" + filename, "w")
        else:
            f = open(filepath + "/" + filename, "a")
        f.write(output_text)
        f.write('\n')

    def get_screenshot(self, method_name, process_name, situation=''):
        # Save a screenshot
        driver = self.driver
        filepath = SET_EVIDENCE + self.evidence["evidence_name"] + "/screenshots"
        # Make directory.
        if not os.path.isdir(filepath):
            os.makedirs(filepath)

        if situation:
            filename = method_name + "__" + process_name + "__" + situation + ".png"
        else:
            filename = method_name + "__" + process_name + ".png"


        if process_name == "input_params":
            if SET_NAL_VERSION >= "4":
                client_height = driver.execute_script('return document.getElementsByClassName("modal-body")[0].clientHeight;')
                scroll_height = driver.execute_script('return document.getElementsByClassName("modal-body")[0].scrollHeight;')
            else:
                client_height = driver.execute_script('return document.getElementsByClassName("modal")[0].clientHeight;')
                scroll_height = driver.execute_script('return document.getElementsByClassName("modal")[0].scrollHeight;')
            if scroll_height > client_height:
                pg_filename = filename.replace(".png", "__1.png")
                if SET_NAL_VERSION >= "4":
                    driver.execute_script('document.getElementsByClassName("modal-body")[0].scrollTop = 0;')
                else:
                    driver.execute_script('document.getElementsByClassName("modal")[0].scrollTop = 0;')
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + pg_filename)

                pg_filename = filename.replace(".png", "__2.png")
                if SET_NAL_VERSION >= "4":
                    driver.execute_script('document.getElementsByClassName("modal-body")[0].scrollTop = ' + str(scroll_height) + ';')
                else:
                    driver.execute_script('document.getElementsByClassName("modal")[0].scrollTop = ' + str(scroll_height) + ';')
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + pg_filename)
            else:
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + filename)

        else:
            client_height = driver.execute_script('return document.documentElement.clientHeight;')
            scroll_height = driver.execute_script('return document.documentElement.scrollHeight;')
            if scroll_height > client_height:
                pg_filename = filename.replace(".png", "__1.png")
                driver.execute_script("window.scrollTo(0, 0);")
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + pg_filename)

                pg_filename = filename.replace(".png", "__2.png")
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + pg_filename)
            else:
                self.sleep_time(2)
                driver.get_screenshot_as_file(filepath + "/" + filename)

    def param_input(self, key, value):
        driver = self.driver
        driver.find_element_by_name(key).clear()
        driver.find_element_by_name(key).send_keys(value)

    def param_select(self, key, value):
        driver = self.driver
        Select(driver.find_element_by_name(key)).select_by_visible_text(value)

    def param_select_id(self, key, value):
        driver = self.driver
        Select(driver.find_element_by_name(key)).select_by_value(value)

    def get_line_from_list(self, target_name, target_column="1"):
        driver = self.driver
        for num in range(1, 30):
            oneline_name = driver.find_element_by_xpath("//tr[" + str(num) + "]/td[" + target_column + "]").text
            if target_name in oneline_name:
                target_line = str(num)
                break
        return target_line

    def get_data_from_line(self, target_line, target_column):
        driver = self.driver
        return driver.find_element_by_xpath("//tr[" + target_line + "]/td[" + target_column + "]").text

    def check_status(self, target_status, right_status):
        if target_status == right_status:
            return True
        else:
            return False
