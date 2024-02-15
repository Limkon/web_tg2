from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.binary_location = '/usr/bin/google-chrome'
browser = webdriver.Chrome(options=options)

browser.get('https://web.telegram.org/')

user_nput = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page_wrap > div > div.login_page > div.login_form_wrap > form > div.login_phone_groups_wrap.clearfix > div.md-input-group.login_phone_num_input_group.md-input-animated > input"))
        )
user_nput.send_keys("13551753935")
time.sleep(5)

country_nput = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page_wrap > div > div.login_page > div.login_form_wrap > form > div.login_phone_groups_wrap.clearfix > div.md-input-group.login_phone_code_input_group.md-input-has-value.md-input-animated > input"))
        )
country_nput.clear()
country_nput.send_keys("+86")

next_sub = browser.find_element_by_css_selector("body > div.page_wrap > div > div.login_page > div.login_head_wrap.clearfix > div > a")

next_sub.click()
ok_click = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.modal.fade.confirm_modal_window.in > div.modal-dialog > div > div > div.md_simple_modal_footer > button.btn.btn-md.btn-md-primary > span"))
        )
ok_click.click()
code_nput = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page_wrap > div > div.login_page > div.login_form_wrap > form > div.md-input-group.md-input-group-centered.md-input-animated > input"))
        )
code = input("请输入验证码：")
code_nput.send_keys(code)

li_nput = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page_wrap > div.im_page_wrap.clearfix.im_page_peer_not_selected > div > div.im_dialogs_col_wrap.noselect > div.im_dialogs_col > div > div.im_dialogs_scrollable_wrap.nano-content > ul > li:nth-child(3)"))
        )
li_nput.click()
