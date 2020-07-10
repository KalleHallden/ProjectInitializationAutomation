import sys
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from dotenv import load_dotenv

browser=webdriver.Edge(r"PATH TO THE WEBDRIVER FILE") #Replace Edge with the name of the browser you mostly use. Also, type in the path of the webdriver file
browser.get("https://github.com/login") 

load_dotenv()

password = os.getenv("PASSWORD")
username = "YOUR USERNAME HERE"#Type in your GitHub username
reponame=sys.argv[1]
path = os.getenv("FILEPATH")

def delete():				
	browser.find_elements_by_xpath("//*[@id='login_field']")[0].send_keys(str(username))
	browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(password)
	browser.find_elements_by_xpath("//*[@id='login']/form/div[4]/input[9]")[0].click()
	browser.get("https://github.com/YOURUSERNAME/"+reponame+"/settings")#Replace  YOURUSERNAME with your actual GitHub username
	browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/summary")[0].click()
	browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input")[0].send_keys(username+"/"+reponame)
	browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button")[0].click()	
	print("The repository {} has been deleted successfully".format(reponame))
	browser.quit()	
	


if	__name__ == "__main__":
	delete()