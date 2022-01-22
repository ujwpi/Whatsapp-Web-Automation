from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = options)

DRIVER_PATH = 'C:\Windows\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

file_path = "C:/Users/hp/OneDrive/Desktop/progs/whatsapp/xxx.jpg" #file path
ph_no = ['9704666396']

for i in range(len(ph_no)):
    driver.get('https://web.whatsapp.com/send?phone=+91'+str(ph_no[i]))
###########Edit Option Available Above###############
    time.sleep(6)

    attachment_section = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_section.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(file_path)
    time.sleep(3)
    send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()

print('Process Complete')