
from selenium import webdriver


driver = webdriver.Chrome(executable_path="")
driver.get('https://quran.com/114')
print(driver.title)
for j in range(2,4):
    for i in range(1,12,2):
        path = (f'/html/body/main/div[2]/div/div[1]/div[2]/div/div[{i}]/div[2]/div[{j}]/p[1]')
        translation = driver.find_element_by_xpath(path)
        print(f'{translation.text}\n')




