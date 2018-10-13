import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import msvcrt as m

driver=webdriver.Chrome()
driver.get("http://play.typeracer.com/")
time.sleep(10)
#enter=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.xpath,'//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')))

enterrace = driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')

enterrace.click()

#enter=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'nhwMiddlegwt-uid-6')))
time.sleep(15)
wordlist=driver.find_element_by_id("nhwMiddlegwt-uid-6").text

wordlist+=" "+driver.find_element_by_id("nhwRightgwt-uid-8").text

#enter=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.xpath,'//*[@id="gwt-uid-11"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')))

inp=driver.find_element_by_class_name("txtInput")
wd=wordlist.split(" ")
for x in wd:
	inp.send_keys(x+" ")
	m.getch()
time.sleep(5)

while(m.kbhit()): m.getch()

input("Press enter to exit...")
driver.quit()