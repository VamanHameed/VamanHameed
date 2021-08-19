# def extracttext():
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/hamee/chromedriver.exe")
driver.get('https://quran.com/114')
print(driver.title)
for j in range(2,4):
    for i in range(1,12,2):
#         print(f'/html/body/main/div[2]/div/div[1]/div[2]/div/div[{i}]/div[2]/div[{j}]/p[1]')
        path = (f'/html/body/main/div[2]/div/div[1]/div[2]/div/div[{i}]/div[2]/div[{j}]/p[1]')
        translation = driver.find_element_by_xpath(path)
        print(f'{translation.text}\n')




