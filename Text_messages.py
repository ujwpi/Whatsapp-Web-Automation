from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = options)

DRIVER_PATH = 'C:\Windows\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

ph_no = ['xxxxxxxxxx', 'yyyyyyyyyy'] #Add a list of phone numbers

for i in range(len(ph_no)):
    driver.get('https://web.whatsapp.com/send?phone=+91'+str(ph_no[i]))
    
    button = driver.find_element_by_xpath('//*[@id="action-button"]')
    driver.implicitly_wait(3)
    ActionChains(driver).move_to_element(button).click(button).perform()
    
    driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    time.sleep(16)

#Add your message here
    message = """ <drop your DM here>"""
    link = """<drop your invite link here>"""

    message += '\n'
    textBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textBox.click()
    textBox.send_keys(message)
    time.sleep(2)
    textBox.send_keys(link)
    time.sleep(2)
    textBox.send_keys('\n')
    time.sleep(2)

print('Process Complete')
