# WP.POCZTA
# Usuwa spam i opróżnia kosz w poczcie wp.pl.(wymagane aktywne konto w poczcie).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://profil.wp.pl/login.html?zaloguj=poczta")

"""Maksymalizacja okna w Chrome"""
driver.maximize_window()

"""Logowanie"""
textbox1 = driver.find_element_by_id("login")
textbox1.clear()
textbox1.send_keys("______")

textbox2 = driver.find_element_by_id("password")
textbox2.clear()
textbox2.send_keys("______")

submit_Button = driver.find_element_by_class_name("notificationWrapper")
submit_Button.click()

"""Usunięcie Spamu"""
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

"""Opróżnienie Kosza"""
try:
    waste_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'opróżnij')]"))
    )
    waste_button.click()
finally:
    print()

waste_confirm = driver.find_element_by_css_selector("[class='Button Button--cta']")
waste_confirm.click()

"""Asercja opróżnienia folderu Spam"""
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

"""Asercja opróżnienia folderu Kosz"""
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


