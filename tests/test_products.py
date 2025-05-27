import pytest

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.regression
def test_product_details_flow(driver):

    driver.get("http://automationexercise.com")
    assert "Automation Exercise" in driver.title


    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()


    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'All Products')]")
        )
    )
    heading = driver.find_element(By.XPATH, "//h2[contains(text(),'All Products')]")
    assert heading.is_displayed()


    products_list = driver.find_element(By.CLASS_NAME, "features_items")
    assert products_list.is_displayed()


    #driver.find_element(By.XPATH, "(//a[contains(text(),'View Product')])[1]").click()
    btn = driver.find_element(By.XPATH, "(//a[contains(text(),'View Product')])[1]")
                                        
    driver.execute_script("arguments[0].click();", btn)

  
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-information"))
    )
    info = driver.find_element(By.CLASS_NAME, "product-information")



    name = info.find_element(By.TAG_NAME, "h2")
    assert name.is_displayed() and name.text.strip()

 
    category = info.find_element(By.XPATH, ".//p[contains(text(),'Category')]")
    assert category.is_displayed() and "Category:" in category.text


    price = info.find_element(By.XPATH, ".//span[contains(text(),'Rs.')]")
    assert price.is_displayed() and price.text.strip()


    availability = info.find_element(
        By.XPATH, ".//p[b[contains(text(),'Availability')]]"
    )
    assert availability.is_displayed() and "Availability" in availability.text


    condition = info.find_element(
        By.XPATH, ".//p[b[contains(text(),'Condition')]]"
    )
    assert condition.is_displayed() and "Condition" in condition.text


    brand = info.find_element(By.XPATH, ".//p[b[contains(text(),'Brand')]]")
    assert brand.is_displayed() and "Brand" in brand.text
