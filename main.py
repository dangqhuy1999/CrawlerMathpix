# selenium 4
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
def cccd():
    sleep(2)
    driver.get('https://mathpix.com/')
    sleep(5)
    login_button = driver.find_element(By.XPATH, "/html/body/main/header/div/div/a[2]").click()
    sleep(10)
    email_input = driver.find_element(By.XPATH, "/html/body/div[2]/section/section/div/div/div/div[2]/form/div[1]/div/div/span/span/input")
    email_input.send_keys("vietnamtopapp@gmail.com")  # Replace with your email
    sleep(2)
    password_input = driver.find_element(By.XPATH, "/html/body/div[2]/section/section/div/div/div/div[2]/form/div[2]/div/div/span/span/input")
    password_input.send_keys("Langnghiem04041979@2023")  # Replace with your password
    sleep(2)
    try:
    # Login process code
        submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/section/section/div/div/div/div[2]/form/button")
        submit_button.click()
        sleep(20)
    except Exception as e:
        print(f"Login error: {e}")
    note = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]").click()
    sleep(20)
    note_blank = driver.find_element(By.XPATH, "//div[@class='ant-popover custom-popover white ant-popover-placement-bottomLeft']//div[@class='ant-popover-content']//div[@role='tooltip']//div//span[@class='text-[14px] pl-2 pr-4 shrink-0 text-action-title'][normalize-space()='New blank note']").click()
    sleep(30)
    ########
    # Find the button element using its CSS selector
    upload_button = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    upload_button.send_keys(r"H:\3i-Intern\Project1\image_cccd\SelectorsHub.png")  # Type the file path
    sleep(30)
    ########


    export = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/ul[1]/li[11]/div[2]/div[1]/button[1]/*[name()='svg'][1]").click()
    sleep(3)
    latex = driver.find_element(By.XPATH, "//span[normalize-space()='LaTeX']").click()
    sleep(30)
    driver.quit()
cccd()
# from selenium import webdriver.
