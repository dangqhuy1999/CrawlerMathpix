from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import json
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver class for your browser
sleep(1)
driver.get("https://mathpix.com/")
sleep(2)