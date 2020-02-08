from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import csv

csv_file = open('Filelist Tutorials', 'w')

webdriver = "/usr/local/bin/chromedriver"
driver = Chrome(webdriver)
url = "http.yyy.com"
driver.get(url)


username = driver.find_element_by_id("username")
username.clear()
username.send_keys("xxx")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("ccc")


driver.find_element_by_class_name("btn").click()

input_text = driver.find_element_by_name("search")
input_text.clear()
input_text.send_keys("Elearning")

cauta_click = driver.find_element_by_xpath("//input[@value='Caută!']")
cauta_click.click()

soup_page = BeautifulSoup(driver.page_source, 'lxml')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Packet number', 'Content'])

count = 0

def run_script():
    global count
    for i in range(0, 20):      
        try:
            cauta_document = driver.find_elements_by_xpath("//a[@title]")[i]
            cauta_document.click()
        except:
            print("No more aqua com gas found, exit!")
            break     
        # except ValueError:    
        # print("Something happend")
        soup_page = BeautifulSoup(driver.page_source, 'lxml')
        list_items = soup_page.find_all('tt')      
        tutorial_pack = soup_page.find('div', class_='cblock-header')
        for item in list_items:
            csv_writer.writerow([tutorial_pack.h4.text,item.text])
        print(list_items)
        driver.back()
        if i == 19:
            count += 1
            test1 = driver.find_element_by_xpath("//a[@href='?search=Elearning&cat=0&searchin=1&sort=2&page=" + str(count) + "']")
            test1.click()
            run_script()  
run_script()
driver.close()


def check_deeper_recursively(string, substring, index, ending, count = 0):
    if(string.find(substring, index, ending)) >= 0:
        count += 1
        return check_deeper_recursively(string, substring, string.find(substring, index, ending)+1, ending, count)    
    elif string.find(substring, index, ending) < 0:
        return count

with open('Filelist Tutorials') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_list = []
    row_count = 0
    react, css, html, java, react_native, networking, javascript, python, sql, photoshop = 0,0,0,0,0,0,0,0,0,0
    interest_list = ["REACT", "CSS", "HTML", "JAVA", "REACT NATIVE", "NETWORK", "JAVASCRIPT", "PYTHON", "SQL", "PHOTOSHOP"]
    dic_list = {"REACT": react, 
                "CSS": css,
                "HTML": html, 
                "JAVA": java, 
                "REACT NATIVE": react_native, 
                "NETWORK": networking, 
                "JAVASCRIPT": javascript, 
                "PYTHON": python,
                "SQL": sql,
                "PHOTOSHOP": photoshop  
                }
    for row in csv_reader:
        row_count += row[1].count('\n')
        for i in interest_list:
            dic_list[i] += check_deeper_recursively(row[1].replace("."," ").upper(), i, 0, 9999)

print(dic_list)

def percentage(item, row):
    return round(100 * float(item)/float(row), 2)

with open('scraping_statistics', mode='w') as scraping_statistics:
    csv_writer = csv.writer(scraping_statistics, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Type', 'Number'])
    for i in dic_list:
        if i == "JAVA":
            csv_writer.writerow([i, dic_list[i]-130])
        else:
            csv_writer.writerow([i, dic_list[i]])            
    csv_writer.writerow(['Type', 'Percentage of total'])
    for i in interest_list:
        csv_writer.writerow([i, str(percentage(dic_list[i],row_count)) + '%'])
    

# string = "jonsnow este la mare cu jonsnow si cu celalalt jonsnow, dar dupa aceea jonsnow a zis recursive: jonsnow"
# cp = 0
# if string.find("jonsnow") >= 0:
#     cp +=1
#     if string.find("jonsnow")>= 0:
#         string.find("jonsnow", 1, 100)
#         cp +=1
#         if string.find("jonsnow")>= 0:
#             string.find("jonsnow", 2, 100)
#             cp +=1
# print(cp)


# print(check_deeper_recursively(string, "jonsnow", 0, 100))