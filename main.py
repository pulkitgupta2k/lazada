from helper import getHTML, getSeller

def driver():
    html = getHTML("https://www.lazada.sg/products/golden-fk-jasmine-rice-5kg-i294586384-s496534981.html")
    getSeller(html)

if __name__ == "__main__":
    driver()