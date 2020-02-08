from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

csv_file = open('cristiano_fb_info', 'w')
csv_writer = csv.writer(csv_file)

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

from bs4 import BeautifulSoup

webdriver = "/usr/local/bin/chromedriver"
driver = Chrome(webdriver, options=option)
url = "https://www.facebook.com/"
driver.get(url)

username = driver.find_element_by_name("email")
username.clear()
username.send_keys("facebook-sucks")

password = driver.find_element_by_id("pass")
password.clear()
password.send_keys("facebook-sucks")


driver.find_element_by_id("loginbutton").click()

cristiano = driver.find_element_by_xpath("//a[@href='https://www.facebook.com/messages/t/100002968423241']")

cristiano.click()
driver.implicitly_wait(3)

cristiano_profile = driver.find_elements_by_xpath("//a[@href='https://www.facebook.com/CristianBoboi.Ro']")[1]
cristiano_profile.click()

cristiano_about = driver.find_element_by_xpath("//a[@data-tab-key='about']")
cristiano_about.click()

cristiano_work = driver.find_element_by_xpath("//a[@label='Work and Education']")
cristiano_work.click()

cristiano_page = BeautifulSoup(driver.page_source, 'lxml')
cristiano_overview = cristiano_page.find_all('a', class_="profileLink")

interest_info = ['Lucreaza', 'Stai','','', 'Studiat']
for g in range(0,5):
    print(g)
    print(cristiano_overview[g].text)
    csv_writer.writerow([interest_info[g], cristiano_overview[g].text])


interest_list = ['movies', 'sports', 'music', 'map']

for i in interest_list:
    cristiano_1 = driver.find_element_by_xpath("//a[@class='_9ry _p']")
    cristiano_1.click()
    cristiano_likes = driver.find_element_by_xpath("//li[@data-tab-key='" + i + "']")
    cristiano_likes.click()
    driver.implicitly_wait(2)
    cristiano_page2 = BeautifulSoup(driver.page_source, 'lxml')
    cristiano_test = cristiano_page2.find_all('a', class_='_gx7')
    try:
        for x in range(0,13):
            print(cristiano_test[x].text) 
            csv_writer.writerow([i, cristiano_test[x].text])                
    except:
        pass

cristiano_profile_back = driver.find_element_by_xpath("//a[@title='Go to Facebook Home']")
cristiano_profile_back.click()

cristiano_chat = driver.find_element_by_xpath("//a[@href='https://www.facebook.com/messages/t/100002968423241']")
cristiano_chat.click()

csv_file.close()

with open('cristiano_fb_info') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    text_input = driver.find_element_by_xpath("//div[@contenteditable='true']")
    for row in csv_reader:
        print(row)
        if row[0] == 'movies':
            print(text_input)
            text_input.clear()
            text_input.send_keys("Ai vazut urmatoarele filme bomba la kapatos: " + row[1])
            send_text = driver.find_element_by_xpath("//a[@data-tooltip-content='Press Enter to send']")
            send_text.click()
        if row[0] == 'sports':
            text_input = driver.find_element_by_xpath("//div[@contenteditable='true']")
            text_input.clear()
            text_input.send_keys("Urmaresti cele mai bastane cluburi: " + row[1])
            send_text = driver.find_element_by_xpath("//a[@data-tooltip-content='Press Enter to send']")
            send_text.click()
        if row[0] == 'map':
            text_input.clear()
            text_input.send_keys("Ai studiat la cel mai tare liceu din Arad: " + row[1])
            send_text = driver.find_element_by_xpath("//a[@data-tooltip-content='Press Enter to send']")
            send_text.click()
        text_input.clear()
        text_input.send_keys("Simplu din fisier -> ", row)
        send_text = driver.find_element_by_xpath("//a[@data-tooltip-content='Press Enter to send']")
        send_text.click()

driver.close()


