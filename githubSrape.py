from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

scrape = input("enter a page to scrape")
service = Service()
driver = webdriver.Firefox(service=service,)
driver.get(f"{scrape}")
repo = "https://github.com/Berkan-dev"
res = driver.find_elements(By.CLASS_NAME, "repo")

links = []
fLink = []


def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "Box-sc-g0xbh4-0")
    raw.click()
    time.sleep(3)
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"found password {second_page}")


def loop(net_page):
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in res2:
        pass
    if "py" in a.text:
        second_page = f"{net_page}/blob/main/{a.text}"
        going_for_raw(second_page)
        time.sleep(3)


for i in res:
    links.append(i.text)
    # print(links)

for l in links:
    next_page = f"{repo}/{l}"
    fLink.append(next_page)
    loop(next_page)
    # print(fLink)
driver.quit()
