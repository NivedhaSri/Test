from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time 

for i in range(20): 
    # Create an instance of the Chrome WebDriver
    driver = webdriver.Chrome() 
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&") 

    # Find the element where we have to enter the XPath
    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('9080197972')
    
    # Find the element and click continue
    driver.find_element(By.XPATH, '//*[@id="continue"]').click() 
    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Nivedha@10') 
    
    # Try to find and click the forgot password link
   # try:
        # Wait until the element is clickable
       # element = WebDriverWait(driver, 10).until(
       #     EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-fpp-link-bottom"]'))
       # )
        # Click the element
       # element.click()
    #except Exception as e:
       # print(e)
    #finally:
      #  time.sleep(4) 
    # Find and click the continue button again
    driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click() 
    

    # Set the interval to send each SMS 
    time.sleep(20) 
    bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('smart appliances')
    enter_buton = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
    drop= driver.find_element(By.XPATH,'//*[@id="icp-nav-flyout"]/span/span[2]/span[2]').click()
    #element = driver.find_element(By.XPATH, "//a[@id='icp-touch-link-language']//span[2]")
    #dropdown = Select(driver.find_element(By.XPATH,"(//a[@id='icp-touch-link-language']//span)[2]"))
    #dropdown.select_by_visible_text("हिंदी")
    #actions = ActionChains(driver)
    #actions.move_to_element(element).click().perform()

    #driver.execute_script("arguments[0].scrollIntoView()", element )
    time.sleep(40) 
    # Close the browser 
    driver.close()
