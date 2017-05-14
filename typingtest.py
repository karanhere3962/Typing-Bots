import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#if you are using linux include this line 'chrome_path = "path of chromeDriver"'
driver=webdriver.Chrome()
driver.get("https://10fastfingers.com/typing-test/english")

inp=driver.find_element_by_id("inputfield")
word=[]
row=driver.find_elements_by_xpath('//div[@id="row1"]/span[@wordnr]')
print("Building Word List: ")

for x in row:
	print(x.get_attribute('wordnr'),x.get_attribute("textContent"))
	word.append(driver.execute_script("return arguments[0].textContent",x))

print("Word List Complete. Entering words in the input box.")

for x in word:
	inp.send_keys(x+" ")

print("Process complete. Check words per minute in the website.")

ex=input("Press Enter to exit.")
driver.quit()
