from selenium import webdriver
import params 
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys
from parsel import Selector

driver =  webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin') 

user=driver.find_element_by_name('session_key')
user.send_keys(params.linkedin_username) 
sleep(1)

password=driver.find_element_by_name('session_password') 
password.send_keys(params.linkedin_password) 
sleep(1)

login_btn=driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button') 
login_btn.click()
sleep(3)

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(params.search_query)
sleep(0.5)


search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)


writer = csv.writer(open(params.file_name, 'w'))

writer.writerow(['Name','Job Title'])


for url in linkedin_urls:

	driver.get(url)

	sleep(5)

	sel = Selector(text=driver.page_source) 

	name = sel.xpath('//*[@id="ember43"]/div[2]/div[2]/div[1]/ul[1]/li[1]/text()').extract_first()

	if name:
		name = name.strip()

	job_title = sel.xpath('//*[@id="ember43"]/div[2]/div[2]/div[1]/h2/text()').extract_first()

	if job_title:
		job_title = job_title.strip()

	writer.writerow([name, job_title])



driver.quit()




