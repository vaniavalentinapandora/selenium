import os

from selenium.webdriver.common.by import By

WAIT_TIME = 60
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'vaniavalentinapandora@gmail.com'
password = '***'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
driver.get("https://www.youtube.com/watch?v=D0_41NWqOxU")
driver.find_element_by_id("identifierId").send_keys(email)
driver.find_element_by_id("identifierNext").click()

#tunggu sampai password muncul
element = WebDriverWait(driver, WAIT_TIME).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)
element.send_keys(password)
driver.find_element_by_id('passwordNext').click()

#ditunggu sampai dialog Use Youtube As muncul...
element = WebDriverWait(driver, WAIT_TIME).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio'][value='117836062881483054646']"))
)
element.click()
driver.find_element_by_id('identity-prompt-confirm-button').click()

#ditunggu sampai .yt-uix-form-input-textarea.metadata-share-contacts bs diclick
element = WebDriverWait(driver, WAIT_TIME).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-uix-form-input-textarea.metadata-share-contacts'))
)
element.send_keys('edwardmichaelsetyadhi@gmail.com')
driver.find_element_by_css_selector('.yt-uix-form-input-checkbox.notify-via-email').click()
driver.find_element_by_css_selector('.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary.sharing-dialog-button.sharing-dialog-ok').click()

#ditunggu proses sampai muncul kata-kata Saved. di dalam elemen ini .yt-dialog-working-bubble .yt-dialog-waiting-content
element = WebDriverWait(driver, WAIT_TIME).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.yt-dialog-working-bubble .yt-dialog-waiting-content'), 'Saved.')
)

# SELESAI, bisa maju ke video berikutnya atau selesai
driver.quit()