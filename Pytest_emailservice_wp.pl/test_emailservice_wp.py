# test_emailservice_wp
# Removes Spam and empties Trash in wp.pl email service.
# (this test requires an active account in the email service)

"""
To run this test with 'pytest' module:
1. Open the PyCharm terminal (ALT+F12  or  View > Tool Windows > Terminal).
2. In terminal check if correct path to 'Pytest_emailservice_wp.pl' folder is visible.
3. To run this test and receive description of the results, write in the terminal:
   pytest -v -s test_emailservice_wp.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pytest


def test_email_service():
    # Here you can select your web browser and path to its driver:
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://profil.wp.pl/login.html?zaloguj=poczta")
    driver.maximize_window()

    """Login and password"""
    textbox1 = driver.find_element_by_id("login")
    textbox1.clear()
    # Below, between quotation marks, please put your login.
    textbox1.send_keys("--------------")

    textbox2 = driver.find_element_by_id("password")
    textbox2.clear()
    # Below, between quotation marks, please put your password.
    textbox2.send_keys("--------------")

    submit_button = driver.find_element_by_class_name("notificationWrapper")
    submit_button.click()

    """Spam removal"""
    try:
        spam_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='folder-5']/span/span"))
        )
        spam_button.click()
    except NoSuchElementException:
        print("Spam removal error 1")

    try:
        spam_confirm = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/button[2]"))
        )
        spam_confirm.click()
    except NoSuchElementException:
        print("Spam removal error 2")

    """Trash removal"""
    try:
        trash_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'opróżnij')]"))
        )
        trash_button.click()
    except NoSuchElementException:
        print("Trash removal error")
    waste_confirm = driver.find_element_by_css_selector("[class='Button Button--cta']")
    waste_confirm.click()

    """Assertion: Spam folder is empty"""
    time.sleep(3)
    spam_folder = driver.find_element_by_id("folder-5")
    spam_folder.click()
    try:
        actual = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "empty-state__title"))
        )
        actual_text = actual.text
    except NoSuchElementException:
        print("Assertion_1 locator error")
    expected_text = "Folder Spam jest pusty"
    assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but Actual text: {actual_text}'

    """Assertion: Trash folder is empty"""
    waste_folder = driver.find_element_by_id("folder-3")
    waste_folder.click()
    try:
        actual2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "empty-state__title"))
        )
        actual_text2 = actual2.text
    except NoSuchElementException:
        print("Assertion_2 locator error")
    expected_txt = "Folder Kosz jest pusty"
    assert expected_txt == actual_text2, f'Error. Expected text: {expected_txt}, but Actual text: {actual_text2}'

    """Logging out"""
    logout = driver.find_element_by_id("Logout-Button").click()
    print("Test finished - OK")
    driver.close()
    driver.quit()


if __name__ == "__main__":
    pytest.main()
