from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import params 

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

jobs_btn = driver.find_element_by_xpath('//*[@id="jobs-nav-item"]')
jobs_btn.click()
sleep(2)


#note xpath of search box and search btn are changing if breaks in between change the



#as xpath and dynamically changing we are giving manually 

xpath_search_box = input("enter xpath for box:   ")
search_box = driver.find_element_by_xpath(xpath_search_box)
search_box.send_keys(params.job_role)
sleep(1)


search_btn = driver.find_element_by_class_name('jobs-search-box__submit-button')
search_btn.click()
sleep(1)
i  = 0
j = 0

writer = csv.writer(open(params.file_name, 'w'))

writer.writerow(['Job_Title','Job_Description', 'company', 'location ', 'Industry', 'Employment_type', 'Job Function', 'Experence_Level'])

# current_Url = driver.current_url
# driver.get('https://www.linkedin.com/jobs/search/?keywords=data%20scientist'+ '&start=' + i)
# this can be useful as i increses by 25 as you go for next page  write a while loop or (for loop range a big number)


# all complted except which fields you want to take

current_url = driver.current_url
print(current_url)


while(j < 1500):

# do this in the while or for loop mentioned above &&&&&&&&&&&&&&&&&&&&&&&&& Start &&&&&&&&&&&&&&&&&&&&&&&&&&

	driver.get(driver.current_url + '&start=' + str(i))


	ActionChains(driver).move_to_element(driver.find_element_by_class_name('search-results-pagination-section')).perform()

	jobs = driver.find_elements_by_class_name('job-card-search--two-pane')

	for job in jobs:
		job.click()

		try:
			company_name = driver.find_elements_by_class_name('jobs-details-top-card__company-url')
			company_name = company_name[0].text

			if company_name:
				company_name = company_name.strip()
		except:
			company_name = None


		try:
			job_name = driver.find_elements_by_class_name('jobs-details-top-card__job-title')
			job_name = job_name[0].text

			if job_name:
				job_name = job_name.strip()
		except:
			job_name = None

		try:	
			job_description = driver.find_element_by_xpath('//*[@id="job-details"]')
			job_description = job_description.text

			if job_description:
				job_description = job_description.strip()
		except:
			job_description = None

		try:	
			employement_type = driver.find_element_by_class_name('js-formatted-employment-status-body')
			employement_type = employement_type.text

			if employement_type:
				employement_type = employement_type.strip()
		except:
			employement_type = None

		try:
			industry = driver.find_elements_by_class_name('jobs-box__list-item')
			industry = [ind.text for ind in industry]
			industry = ','.join(industry)

			if industry:
				industry = industry.strip()
		except:
			industry = None

		try:	
			location= driver.find_element_by_class_name('jobs-details-top-card__bullet')  
			location = location.text

			if location:
				location = location.strip() 
		except:
			location = None

		try:
			job_funtion = driver.find_element_by_class_name('jobs-box__list-item')
			job_funtion = job_funtion.text

			if job_funtion:
				job_funtion = job_funtion.strip()
		except:
			job_funtion = None



		writer.writerow([job_name, job_description, company_name, location,  industry, employement_type, job_funtion])
		sleep(2)

	i = i+25

	j= j + 12


 # &&&&&&&&&&&&&&&&&&&&&&&&& end &&&&&&&&&&&&&&&&&&&&&&&&&&


driver.quit()



	


# driver.get('https:www.google.com')
# sleep(3)

# search_query = driver.find_element_by_name('q')
# search_query.send_keys(params.search_query)
# sleep(0.5)


# search_query.send_keys(Keys.RETURN)
# sleep(3)

# linkedin_urls = driver.find_elements_by_class_name('iUh30')
# linkedin_urls = [url.text for url in linkedin_urls]
# sleep(0.5)


# writer = csv.writer(open(params.file_name, 'w'))

# writer.writerow(['Name','Job Title'])


# for url in linkedin_urls:

# 	driver.get(url)

# 	sleep(5)

# 	sel = Selector(text=driver.page_source) 

# 	name = sel.xpath('//*[@id="ember43"]/div[2]/div[2]/div[1]/ul[1]/li[1]/text()').extract_first()

# 	if name:
# 		name = name.strip()

# 	job_title = sel.xpath('//*[@id="ember43"]/div[2]/div[2]/div[1]/h2/text()').extract_first()

# 	if job_title:
# 		job_title = job_title.strip()

# 	writer.writerow([name, job_title])






