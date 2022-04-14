
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import glob

import gensim



#code to ignore browser notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


from selenium.webdriver.support.wait import WebDriverWait


# chrome driver
driver = webdriver.Chrome('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\chromedriver.exe',chrome_options=chrome_options)



content_list=[]
name_list=[]
time_list=[]




#log in + navigate to a group of choice on facebook

driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
email = driver.find_element(By.XPATH, "//input[@id='email' or @name='email']")
email.send_keys('YOUR EMAIL GOES HERE!!!')     #ENETER YOUR EMAIL HERE
print("email entered...")
password = driver.find_element(By.XPATH, "//input[@id='pass']")
password.send_keys('YOUR PASSWORD GOES HERE!!!') #ENETER YOUR PASSWORD HERE
print("Password entered...")
button = driver.find_element( By.XPATH, "//button[@id='loginbutton']")
button.click()
sleep(3)
print("facebook opened")

print('go to group page')

driver.get('https://www.facebook.com/kolzchut') # GROUPS' URL GOES HERE
y=1000





while True:
            soup=BeautifulSoup(driver.page_source,"html.parser")
            #grab all posts on loaded group page
            all_posts=soup.find_all("div",{"class":"du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})

            #read the chosen divs and crape the text from them
            for post in all_posts:
                try:
                    name=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"})
                    strips_name = list(name.stripped_strings)
                    strips_name= ' '.join(strips_name)


                except:
                    strips_name="not found"
                print(strips_name)
                try:
                    content=post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"})
                    strips_content = list(content.stripped_strings)
                    strips_content= ' '.join(strips_content)

                except:
                    strips_content="not found"
                print(strips_content)
                try:
                    time=post.find("span",{"class":"t5a262vz aenfhxwr b6zbclly l9j0dhe7 sdhka5h4"})
                    strips_time = list(time.stripped_strings)
                    strips_time= ' '.join(strips_time)
                except:
                    strips_time="not found"
                print(strips_time)


                #translate the posts to english
                from googletrans import Translator         #pip install googletrans==3.1.0a0 to avoid API errors
                translator = Translator()  # initalize the Translator object
                strips_content = translator.translate(strips_content, dest='en') # translate 
                strips_name = translator.translate(strips_name, dest='en') # translate 
                strips_content = strips_content.text
               
                #append translated posts to lists
                content_list.append(strips_content)
                time_list.append(strips_time)
                name_list.append(strips_name.text)

                #send to DF and remove duplicates
                df=pd.DataFrame({"name":name_list,"content":content_list,"time":time_list})
                df.drop_duplicates(subset="content",keep="first",inplace=True)
                if df.shape[0]>1000:
                    break


                #write translated posts to CSV
                df.to_csv("testData123.csv")
                

                #scroll down to load more posts
                driver.execute_script("window.scrollTo(0,"+str(y)+")")
                y+=500
                sleep(3)
 


            #sleep(5)
            #y=1000
            #for timer in range(0,4):
            #    driver.execute_script("window.scrollTo(0,"+str(y)+")")
            #    y+=500
            #    sleep(3)

                    


    

