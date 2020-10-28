from helper import getHTML, getSeller

def driver():
    html = getHTML("https://www.lazada.sg/products/golden-fk-jasmine-rice-5kg-i294586384-s496534981.html")
    getSeller(html)
    html = getHTML("https://www.lazada.sg/products/liziqi-mushroom-sauce-i661084440-s2005852824.html")
    getSeller(html)
    html = getHTML("https://www.lazada.sg/products/amazing-lokarb-shirataki-fettuccine-pasta-noodles-low-carb-keto-noodles-gluten-free-6-x-fettuccine-pouches-6-12-servings-low-calorie-high-fibre-suitable-for-diabetic-vegans-keto-diet-paleo-diabetes-plant-based-xndo-users-i577056540-s1648886936.html")
    getSeller(html)

if __name__ == "__main__":
    driver()