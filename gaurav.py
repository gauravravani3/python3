from selenium import webdriver
driver = webdriver.Firefox(executable_path=r"/home/ubuntu/Desktop/geckodriver")
driver.get("https://google.com")
