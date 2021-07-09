from selenium import webdriver
import urllib.request
import os

PATH = "E:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

linkList = [
    "https://www.pinterest.com/search/pins/?rs=ac&len=2&q=jacket%20outfit%20women&eq=jacket%20out&etslf=12412&term_meta[]=jacket%7Cautocomplete%7C1&term_meta[]=outfit%7Cautocomplete%7C1&term_meta[]=women%7Cautocomplete%7C1",
    "https://www.pinterest.com/search/pins/?rs=ac&len=2&q=summer%20outfits%20men&eq=summer%20ou&etslf=6675&term_meta[]=summer%7Cautocomplete%7C2&term_meta[]=outfits%7Cautocomplete%7C2&term_meta[]=men%7Cautocomplete%7C2",
    "https://www.pinterest.com/search/pins/?q=jacket%20men%20outfit&rs=typed&term_meta[]=jacket%7Ctyped&term_meta[]=men%7Ctyped&term_meta[]=outfit%7Ctyped"
]
folderName = [ "jacket_woman", "summer_outfit_man", "jacket_men"]

imgNumber = 1
folderIndex = 0
for link in linkList :
    driver.get(link)
    i = 1
    while i <= 150:
        for item in driver.find_elements_by_tag_name("img"):
            print(item.get_attribute("src"))
            fullfileName = os.path.join("C:\CollegeMadeProgram\S2\Phyton\Pinterest Scrapping\scrappedimg\\batch2\\" +folderName[folderIndex]  + "\\" + "batch2_" + folderName[folderIndex] + "_" + str(imgNumber) + ".png")
            urllib.request.urlretrieve(item.get_attribute("src"), fullfileName)
            i = i + 1
            imgNumber = imgNumber + 1
    folderIndex = folderIndex + 1
