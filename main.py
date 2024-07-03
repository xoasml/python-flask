from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

# .launch(headless=True) 가 디폴트이며 True일때 백그라운드에서 작업 된다.
# False 일 때는 실제로 브라우저가 작동 하는걸 볼수 있다.
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

time.sleep(2)

for x in range(5):
    page.keyboard.down("End")
    time.sleep(1)

time.sleep(3)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(["title", "company", "url"])

for job in jobs:
    url = job.find("a")["href"]
    title = job.find("strong", class_="JobCard_title__HBpZf")
    company = job.find("span", class_="JobCard_companyName__N1YrF")

    data = {
        "title": title.text,
        "company": company.text,
        "url": f"https://www.wanted.co.kr{url}",
    }

    writer.writerow(data.values())

file.close()