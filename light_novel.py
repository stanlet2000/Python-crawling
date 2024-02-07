import sys
import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.lightnovel.us/series/129"

chapter = 257

path_txt = 'output/txt/'+str(chapter)+'.txt'
path_md = 'output/md/'+str(chapter)+'.md'


def write_txt(title, content):
    f = open(path_txt, 'w')
    s = ['\n' if str(sentece)=='<br/>' else str(sentece).replace('\u3000', '') for sentece in content]
    f.write(title.text+'\n')
    f.writelines(s)
    f.close()

def write_md(title, content):
    f = open(path_md, 'w')
    s = ['\\\n' if str(sentece)=='<br/>' else str(sentece) for sentece in content]
    f.write('# '+title.text+'\n')
    f.writelines(s)
    f.close()

if __name__ == "__main__":
    

    driver = webdriver.Edge()

    driver.get(url)

    driver.maximize_window()

    driver.implicitly_wait(5)

    collection = driver.find_element(By.CLASS_NAME, "collection-index")

    indices = collection.find_elements(By.CLASS_NAME, "tab-item")


    for i in indices:
        l = i.text.split("-")
        if chapter >= int(l[0]) and chapter <= int(l[1]):
            i.find_element(By.TAG_NAME, "span").click()


    chapters = collection.find_elements(By.CLASS_NAME, "item-box")

    for c in chapters:
        if f"P{str(chapter)}" == c.text:
            c.click()

    driver.implicitly_wait(5)

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    driver.implicitly_wait(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    whole_contents = soup.find("article")
    title = whole_contents.find("h2")

    content = whole_contents.find("article", id="article-main-contents")
    
    write_txt(title, content)

    write_md(title=title, content=content)

    time.sleep(3)
    driver.close()