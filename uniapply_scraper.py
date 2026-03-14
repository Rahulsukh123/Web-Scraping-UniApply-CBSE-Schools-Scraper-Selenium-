from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def scrape_schools():
    url = "https://www.uniapply.com/schools/cbse-schools-in-nagpur/"
    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    
    schools = []
    for container in driver.find_elements(By.CLASS_NAME, "item-list"):
        try:
            name = container.find_element(By.CSS_SELECTOR, ".item-title h4 a").text
            address = container.find_element(By.CSS_SELECTOR, ".item-title small").text
            fees = container.find_element(By.CSS_SELECTOR, ".list-info-item:nth-child(2) .item-val").text
            classes = container.find_element(By.CSS_SELECTOR, ".list-info-item:nth-child(1) .item-val").text
            board = container.find_element(By.CSS_SELECTOR, ".list-info-item:nth-child(3) .item-val").text
            link = container.find_element(By.CSS_SELECTOR, ".item-title h4 a").get_attribute('href')
            
            schools.append([name, address, fees, classes, board, link])
        except:
            continue
    
    with open('nagpur_cbse_schools_new.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['School Name', 'Address', 'Monthly Fees', 'Classes', 'Board', 'Link'])
        writer.writerows(schools)
    
    print(f"Scraped {len(schools)} schools")
    driver.quit()

if __name__ == "__main__":
    scrape_schools()
