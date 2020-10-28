from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

def get_items():
    driver.get("https://www.lazada.sg/gourmet-food-and-gifts/?spm=a2o42.home.cate_6_3.1.191646b5JfWlaR")
    items = driver.find_elements_by_xpath("//div[@data-tracking='product-card']")
    for item in items:
        print(item.text)
        link = item.find_elements_by_xpath("//a")[0]
        print(link.get_attribute("href"))
    
if __name__ == "__main__":
    get_items()