from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
# driver.get("https://www.slazzer.com/upload")
driver.get("https://www.remove.bg/upload")
pic="G:/U-2-Net-master/test_data/test_human_images/images.jpeg"
# driver.find_element(By.ID,"input_user_image_upload").send_keys(pic)
driver.find_element(By.XPATH,'//*[@id="page-content"]/div[1]/div/div/div[1]/div/div[1]/div[2]').send_keys(pic)
time.sleep(15)
button = driver.find_element_by_link_text("Download")
button.click()
time.sleep(15)
driver.find_element(By.XPATH,'//*[@title="Close"]').click()
time.sleep(10)
