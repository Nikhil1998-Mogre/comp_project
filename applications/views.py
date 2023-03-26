# views.py
# hi nikhil
from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
import numpy as np
import time
import json
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#user input
def user_input(request):
    return render(request,'applications/job.html')



def linked_jobs(request):
    if request.method == 'GET':
        # Retrieve filter values from frontend
        location_filter = request.GET.get('location', '')
        output = find(location_filter)
    return render(request,'applications/job.html',{'a':output})



def find(location):
    from selenium import webdriver
    import time

    link = []
    # url = 'https://in.linkedin.com/jobs/jobs-in-india?keywords=&location=India&locationId=&geoId=102713980&sortBy=R&f_TPR=&f_E=2&position=1&pageNum=0'
    url = f'https://www.linkedin.com/jobs/jobs-in-india/?currentJobId=3522422225&f_E=2&keywords=&location={location}%2C%20India&originalSubdomain=in&sortBy=R'
    driver = webdriver.Chrome("C:\Chrome web =driver\chromedriver_win32\chromedriver.exe")
    driver.get(url)

    # Scroll through the page to load all job listings

    scroll_pause_time = 4  # You can set your own pause time. dont slow too slow that might not able to load more data
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    A = 1
    job_count = 0

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{A});".format(screen_height=screen_height, A=A))
        A += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * A > scroll_height or job_count >= 5:
            break

        try:
            see_more_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/button')
            see_more_button.click()
            time.sleep(scroll_pause_time)
        except:
            pass


        links = driver.find_elements('tag name','a')
        for i in links:
            link.append(i.get_attribute('href'))

        #call fun_2
        fun_2(link)


#2nd function
def fun_2(link):
    job_link = []
    for i in link:
        if 'jobs/view/' in i:
            job_link.append(i)

    fun_3(job_link)

# 3rd function
def fun_3(job_link):
    job_role = []
    company = []
    Location = []
    Posted_date = []
    JD = []

    for i in job_link:
    # for i in job_link:
        driver = webdriver.Chrome("C:\Chrome web =driver\chromedriver_win32\chromedriver.exe")
        driver.get(i)
        try:
            see_more = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]')
            see_more.click()
        except:
            pass

        try:
            job_role.append(driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1').text)
        except:
            job_role.append(np.nan)
        try:
            company.append(driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]/a').text)
        except:
            company.append(np.nan)
        try:
            Location.append(driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]').text)
        except:
            Location.append(np.nan)
        try:
            Posted_date.append(driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/span[1]').text)
        except:
            Posted_date.append(np.nan)
        try:
            JD.append(driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup').text)
        except:
            JD.append(np.nan)


    d={'job_role':job_role,'company':company,'Location':Location,'Posted_date':Posted_date,'JD':JD}

    return d
                
