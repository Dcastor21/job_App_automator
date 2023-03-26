import time
import main
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager


def apply():
    lnkdin_job_site = main.site
    user = main.email
    password = main.password
    options = Options()
    options.headless = False

    chrome_driver_path = "/Users/casto/chromedriver/chromedriver"
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install(), options=options))
    driver.get(lnkdin_job_site)

    sign_in = driver.find_element("id", "session_key")
    sign_in.click()
    email_field = driver.find_element("id", "username")
    email_field.send_keys(user)
    pwd_field = driver.find_element("id", "password")
    pwd_field.send_keys(password)
    pwd_field.send_keys(Keys.ENTER)

    all_listings = driver.find_elements("css", "job-card-Container--Clickable")

    for listing in all_listings:
        print("called")
        listing.click()
        time.sleep(2)
        try:
            apply_bttn = driver.find_element("css", ".job-s-apply button")
            apply_bttn.click()
            time.sleep(2)
            phone = driver.find_element("css", "fb-single-line-text__input")
            phone.send_keys("123456789")
            next_bttn = driver.find_element("css", "footer Button")
            if next_bttn.get_attribute("data-control-name") == "continue_unify":
                next_bttn.click()
            else:
                close_bttn = driver.find_element("class_name", "artdeco-model__dismiss")
                close_bttn.click()
                discard_buttn = driver.find_element("class_name", "artdeco-modal__comfirm-dialog-btn")
                discard_buttn.click()
                print("complex application, Skipped..")
                continue
            time.sleep(2)
            review_button = driver.find_element("clas_name", "artdeco-button--primary")
            if review_button.get_attribute("data-control-name") == "continue_unify":
                close_bttn = driver.find_element("class_name", "artdeco-model__dismiss")
                close_bttn.click()
                discard_buttn = driver.find_element("class_name", "artdeco-modal__comfirm-dialog-btn")[1]
                discard_buttn.click()
                print("complex application, Skipped..")
                continue
            else:
                review_button.click()
                time.sleep(2)
                submit_btn = driver.find_element("class_name", "artdeco-buttton--primary")
                if submit_btn.get_attribute("data-control-name") == "submit_unify":
                    submit_btn.click()
                    time.sleep(2)
                    close_bttn = driver.find_element("class_name", "artdeco-model__dismiss")
                    close_bttn.click()
                else:
                    close_bttn = driver.find_element("class_name", "artdeco-model__dismiss")
                    close_bttn.click()
                    discard_buttn = driver.find_element("class_name", "artdeco-modal__comfirm-dialog-btn")[1]
                    discard_buttn.click()
                    print("complex application, Skipped..")
                    continue
        except NoSuchElementException:
            print("No application Button, skipped.")
            continue

    # driver.close()
