import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://finance.yahoo.com"
target = "SPY"
date1 = "2000-09-11"




if __name__ == "__main__":
    driver = webdriver.Safari()

    driver.get(url)

    driver.maximize_window()

    driver.implicitly_wait(5)

    search_bar = driver.find_element(By.ID, "yfin-usr-qry")
    search_bar.send_keys(target)
    driver.implicitly_wait(10)
    search_bar.send_keys(Keys.ENTER)

    # locator = (By.CSS_SELECTOR, "#Nav-0-DesktopNav-0-DesktopNav > div > div.nr-applet-title.Fl\(start\).Pend\(navPaddings\).Bxz\(bb\).Ov\(h\).H\(navHeight\).Pstart\(10px\).Mstart\(-10px\)\!.H\(itemHeight_uhMagDesign\)\!.Pend\(30px\)\! > div > a")

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator), "找不到指定的元素")

    # locator = (By.CSS_SELECTOR, "#quote-nav > ul > li:nth-child(4) > a")
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator), "can't find element")
    time.sleep(5)
    # driver.implicitly_wait(5)


    historical_button = driver.find_element(By.CSS_SELECTOR, "#quote-nav > ul > li:nth-child(4) > a")

    historical_button.click()

    # time.sleep(5)
    locator = (By.CSS_SELECTOR, "#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\) > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div:nth-child(1) > div")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))

    period = driver.find_element(By.CSS_SELECTOR, "#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\) > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div:nth-child(1) > div")
    period.click()

    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)

    start_date = driver.find_element(By.NAME, "startDate")
    driver.execute_script("arguments[0].setAttribute('value', '2021-06-30')", start_date)

    # start_date.send_keys("2000")
    # time.sleep(1)
    # start_date.send_keys("/")
    # time.sleep(1)
    # start_date.send_keys("09")
    # start_date.send_keys(date1)

    time.sleep(5)

    driver.close()