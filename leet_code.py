from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd


options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
browser = webdriver.Chrome(options = options, service = Service("chromedriver.exe"))


browser.get("https://leetcode.com/problemset/all/")
time.sleep(5)

dif=browser.find_element(By.XPATH , "//button[contains(text(), 'Difficulty')]")
time.sleep(5)

browser.execute_script("arguments[0].scrollIntoView();",dif)
time.sleep(5)

dif.click()
time.sleep(5)

med = browser.find_element(By.XPATH , "//span[contains(text(), 'Medium')]")
med.click()
time.sleep(5)

status=browser.find_element(By.XPATH , "//button[contains(text(), 'Status')]")
status.click()
time.sleep(5)

# # # todo=browser.find_element(By.XPATH , "//span[contains(text(), 'Todo')]")
# # # print("------------")
# # # print(todo)
# # # print("------------")

todo=browser.find_element(By.XPATH , "//span[text()='Todo']")
# # #print("------------")
# # print(todo)
# # #print("------------")

todo.click()
time.sleep(5)

tags=browser.find_element(By.XPATH , "//span[text()='Tags']")
tags.click()
time.sleep(5)

kano=['Greedy','Array']

for x in kano:
    
    arr_gre=browser.find_element(By.XPATH , f"//span[@data-name='{x}']")
    arr_gre.click()
    time.sleep(5)

tags=browser.find_element(By.XPATH , "//span[text()='Tags']")
tags.click()
time.sleep(10)
# browser.get("https://leetcode.com/problemset/all/?difficulty=MEDIUM&page=1&status=NOT_STARTED&topicSlugs=greedy%2Carray")
# time.sleep(10)

#all_titles=browser.find_elements(By.XPATH,"//div[@class='flex items-center']")

#for kk in all_titles:
 #   print(kk.text)
    

#accepts=browser.find_elements(By.XPATH,"//div[@style='box-sizing:border-box;flex:100 0 auto;min-width:0px;width:100px']")
#for kk in accepts:
#    print(kk.text)


main_data=[]


while(True):

    all_items=browser.find_elements(By.XPATH,"//div[@role='row']")
    
    for x in all_items:
        
        try:
            dic={}
            all_titles=x.find_element(By.CLASS_NAME,'truncate')
            all_acceptance=x.find_element(By.TAG_NAME,'span')

            print(all_titles.text)
            print(all_acceptance.text)


            dic["title"]=all_titles.text
            dic["accept"]=all_acceptance.text
            main_data.append(dic)
        except Exception as e:
            print(e)

    next=browser.find_element(By.XPATH,"//button[@aria-label='next']")
    last_page = next.get_attribute("disabled")
    #print(last_page)

    if last_page=="true":
        break
    

    browser.execute_script("arguments[0].scrollIntoView();",next)
    next.click()

    time.sleep(10)

pd.DataFrame(main_data).to_excel("leet_code.xlsx",index=False)




browser.quit()

    
