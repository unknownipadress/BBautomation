from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import requests
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import pause
def fun(period,driver,day):
 '''searching for the element'''
 looking_for_element = True
 ldmore = ''

 while looking_for_element:
  elements = driver.find_elements_by_link_text(period)
#element is found

  if len(elements) > 0:
   ldmore = elements[0]
   looking_for_element = False
  else:
   body = driver.find_element_by_css_selector('body')
   body.send_keys(Keys.TAB)#clicking tab until the element is found
 time.sleep(5)
 periods=driver.find_element_by_link_text(period)#clicking the element
 periods.click()
#opening the course outline
 time.sleep(5)
 period2=driver.find_element_by_xpath('//*[@class="blue-link" and @bb-translate="course.outline.collab.ultraCollabContent.roomEnabled"]')
 period2.click()
 time.sleep(2)
 joinclass=driver.find_element_by_partial_link_text(day)
 joinclass.click()
#after joining the class
 newURl = driver.window_handles[1]
 oldurl = driver.window_handles[0]
 driver.switch_to.window(newURl)
 time.sleep(20)
 driver.maximize_window()
 #giving mic rights
 driver.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
 #time spent for a class
 if (period=="APTITUDE"or period=="SOFT SKILLS" ):
  time.sleep(7200)#softskills 2 hrs
 else:
  time.sleep(3600)#3600=1hr
 driver.close()
 driver.switch_to.window(oldurl)
 #openeing the second class
 closing_old_period=driver.find_element_by_class_name('bb-close')
 closing_old_period.click()
 time.sleep(2)
#function ends here
#change the date here everyday
#format is yyyy,mm,dd,hr(24-hourformat),min,sec,millisec
#always set the time to 9:46 AM only
#only change the date
dt = datetime.datetime(2021, 2, 24, 15, 54, 34, 383752)
pause.until(dt)
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(executable_path='drivers/chromedriver',chrome_options=chrome_options)

driver.get('https://cuchd.blackboard.com/webapps/login/')
cookie=driver.find_element_by_id('agree_button')
cookie.click()

username = driver.find_element_by_id('user_id')
password = driver.find_element_by_id('password')
#change your username and pass here
username.send_keys('18bcs4118')
password.send_keys('Phani@123')


login = driver.find_element_by_xpath('//*[@id="entry-login"]') # Login
login.click()
time.sleep(5)

#chnage the time table here
#change the time table everyday
period=["NETWORK OPERATING SYSTEM","APTITUDE","Lunch", "THEORY OF COMPUTATION", "Empty","TECHNICAL TRAINING"]
#change the day here use the first three leters (first letter capital"
#change the day everyday
day="Mon"

for i in period:
 if i=="Lunch":
     print("this lunch")
     time.sleep(27)

     continue
 elif i=="Empty":
  print("this is empty")
  time.sleep(10)

  continue
 else:
  print("going in the classs hold on tight ")
  fun(i,driver,day)
