import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.data_reader import load_test_data


user = load_test_data('signup_data.json')[0]

@pytest.mark.regression
def test_user_signup_flow(driver):

    driver.get("http://automationexercise.com")
    assert "Automation Exercise" in driver.title


    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    assert driver.find_element(
        By.XPATH, "//h2[contains(text(),'New User Signup')]"
    ).is_displayed()


    driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys(user["name"])
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(user["email"])
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()


    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
        )
    )

 
    if user["title"] == "Mr":
        driver.find_element(By.ID, "id_gender1").click()
    else:
        driver.find_element(By.ID, "id_gender2").click()
    driver.find_element(By.ID, "password").send_keys(user["password"])
    Select(driver.find_element(By.ID, "days")).select_by_value(user["dob"]["day"])
    Select(driver.find_element(By.ID, "months")).select_by_value(user["dob"]["month"])
    Select(driver.find_element(By.ID, "years")).select_by_value(user["dob"]["year"])
    #driver.find_element(By.ID, "newsletter").click()
    #driver.find_element(By.ID, "optin").click()


    driver.find_element(By.XPATH, "//input[@data-qa='first_name']").send_keys(user["first_name"])
    driver.find_element(By.XPATH, "//input[@data-qa='last_name']").send_keys(user["last_name"])
    driver.find_element(By.XPATH, "//input[@data-qa='company']").send_keys(user["company"])
    driver.find_element(By.XPATH, "//input[@data-qa='address']").send_keys(user["address"])
    driver.find_element(By.XPATH, "//input[@data-qa='address2']").send_keys(user["address2"])
    Select(driver.find_element(By.XPATH, "//select[@data-qa='country']")).select_by_visible_text(user["country"])
    driver.find_element(By.XPATH, "//input[@data-qa='state']").send_keys(user["state"])
    driver.find_element(By.XPATH, "//input[@data-qa='city']").send_keys(user["city"])
    driver.find_element(By.XPATH, "//input[@data-qa='zipcode']").send_keys(user["zipcode"])
    driver.find_element(By.XPATH, "//input[@data-qa='mobile_number']").send_keys(user["mobile_number"])

    btn = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    driver.execute_script("arguments[0].click();", btn)

    assert driver.find_element(
        By.XPATH, "//b[contains(text(),'Account Created')]"
    ).is_displayed()

    btn = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
                                        
    driver.execute_script("arguments[0].click();", btn)
    assert driver.find_element(
        By.XPATH, "//a[contains(text(),'Logged in as')]"
    ).is_displayed()
    btn = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
                                        
    driver.execute_script("arguments[0].click();", btn)

    assert driver.find_element(By.XPATH, "//b[contains(text(),'Account Deleted!')]").is_displayed()