import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#if you are using linux include this line - 'chrome_path = "path of chromeDriver"'

print("Opening browser.")
driver=webdriver.Chrome()
print("Navigating to 10fastfingers.com . Please wait till the page loads.")
driver.get("https://10fastfingers.com/typing-test/english")

inp=driver.find_element_by_id("inputfield")#links the 'inp' variable to the input box 
word=[]
row=driver.find_elements_by_xpath('//div[@id="row1"]/span[@wordnr]')#locates the element storing words to be entered in the input box
print("Building Word List: ")

for x in row:#extracts the words from the located element and stores them in a list
	print(x.get_attribute('wordnr'),x.get_attribute("textContent"))
	word.append(driver.execute_script("return arguments[0].textContent",x))

print("Word List Complete. Entering words in the input box.")

for x in word:#enters the word from the list in the input box
	inp.send_keys(x+" ")

print("Process complete. Check words per minute in the website.")

ex=input("Press Enter to exit.")
driver.quit()
