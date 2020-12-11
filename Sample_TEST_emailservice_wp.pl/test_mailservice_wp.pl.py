# test_mailservice_wp.pl
# Removes spam and empties the trash in wp.pl email service.
# (this test requires an active account in the email service)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Here you can select your web browser and path to its driver.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://profil.wp.pl/login.html?zaloguj=poczta")
driver.maximize_window()

"""Login"""
textbox1 = driver.find_element_by_id("login")
textbox1.clear()
# Below, between quotation marks, please put your login.
textbox1.send_keys("_____")

textbox2 = driver.find_element_by_id("password")
textbox2.clear()
# Below, between quotation marks, please put your password.
textbox2.send_keys("_____")

submit_Button = driver.find_element_by_class_name("notificationWrapper")
submit_Button.click()

"""Spam removal"""
try:
    spam_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'usuń')]"))
    )
    spam_button.click()
finally:
    print()
try:
    spam_confirm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/button[2]"))
    )
    spam_confirm.click()
finally:
    print()

"""Trash removal"""
try:
    trash_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'opróżnij')]"))
    )
    trash_button.click()
finally:
    print()
waste_confirm = driver.find_element_by_css_selector("[class='Button Button--cta']")
waste_confirm.click()

"""Assertion - the Spam folder is empty"""
time.sleep(5)
spam_folder = driver.find_element_by_id("folder-5")
spam_folder.click()
try:
    actual = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "empty-state__title"))
    )
    actual_text = actual.text
finally:
    print()
expected_text = "Folder Spam jest pusty"
assert expected_text == actual.text, f'Error. Expected text: {expected_text}, but Actual text: {actual_text}'

"""Assertion - the Trash folder is empty"""
time.sleep(3)
waste_folder = driver.find_element_by_id("folder-3")
waste_folder.click()
try:
    actual2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "empty-state__title"))
    )
    actual_text2 = actual2.text
finally:
   print()
expected_txt = "Folder Kosz jest pusty"
assert expected_txt == actual_text2, f'Error. Expected text: {expected_txt}, but Actual text: {actual_text2}'

"""Wylogowanie"""
logout = driver.find_element_by_id("Logout-Button").click()
driver.quit()