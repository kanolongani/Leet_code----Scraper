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


def choice_(difficulty_ , status_):

    diff = browser.find_element(By.XPATH , "//button[contains(text(), 'Difficulty')]")

    browser.execute_script("arguments[0].scrollIntoView();",diff)
    diff.click()
    time.sleep(5)

    type_of_diff = browser.find_element(By.XPATH , f"//span[contains(text(), '{difficulty_}')]")
    type_of_diff.click()
    time.sleep(5)

    # difficulty_ = "Medium" , "Easy" , "Hard" .

    status = browser.find_element(By.XPATH , "//button[contains(text(), 'Status')]")
    status.click()
    time.sleep(5)

    type_of_status_ = browser.find_element(By.XPATH , f"//span[text()='{status_}']")
    type_of_status_.click()
    time.sleep(5)

    # status_ = "Todo" , "Solved" , "Attempted" .

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
    time.sleep(5)



def data_(file_name):
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

        next = browser.find_element(By.XPATH,"//button[@aria-label='next']")
        last_page = next.get_attribute("disabled")
        #print(last_page)

        if last_page=="true":
            break
    

        browser.execute_script("arguments[0].scrollIntoView();",next)
        next.click()

        time.sleep(10)

    # file_name = give a name of your file name
    pd.DataFrame(main_data).to_excel(f"{file_name}.xlsx",index=False)
    

algorithms_ = browser.find_element(By.XPATH , "//div[contains(text(), 'Algorithms')]")
algorithms_.click()
time.sleep(5)

choice_('Easy' , 'Todo')
data_('algorithms_')


database_ = browser.find_element(By.XPATH , "//div[contains(text(), 'Database')]")
database_.click()
time.sleep(5)

choice_('Easy' , 'Todo')
data_('database_')


shell_ = browser.find_element(By.XPATH , "//div[contains(text(), 'Shell')]")
shell_.click()
time.sleep(5)

choice_('Easy' , 'Todo')
data_('shell_')

Concurrency_ = browser.find_element(By.XPATH , "//div[contains(text(), 'Concurrency')]")
Concurrency_.click()
time.sleep(5)

choice_('Easy' , 'Todo')
data_('Concurrency')










