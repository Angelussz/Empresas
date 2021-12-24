from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1 = "https://tiendasishop.com/pe/iphone-12-64gb-negro-gratis-funda-gear4-transparente-y-protector-de-pantalla-belkin-ultra"
source2 = "https://catalogo.entel.pe/iphone-12"
source3 = "https://www.linio.com.pe/p/apple-iphone-12-64gb-libre-entrega-inmediata-funda-negro-ootvew?qid=fcdc6f25f75fa1c387215db4f80a51c8&oid=AP032EL1489TGLPE&position=3&sku=AP032EL1489TGLPE"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('excludeSwitches', ['enable-logging'])
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r'D:\UNSA\anios\IV\VIII_SEMESTRE\Empresarial\Prototipo\chromedriver.exe',options=CO)
print ("*************************************************************************** \n")
print("                     Comparando Precios ..... \n")

print ("Connecting to Entel")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath( "/html/body/div[2]/main/div[2]/div/div[1]/div[2]/div/span[1]/span/span/span" )
pr_name = wd.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div[1]/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print (" ---> Successfully retrieved the price from Entel \n")
time.sleep(2)



print("Connectando a Entel")
wd.get(source2)
wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
a_price = wd.find_element_by_xpath("/html/body/div[4]/div[2]/section[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/span")
raw_p = a_price.text
# print (raw_p[2:8])
print (" ---> Successfully retrieved the price from Entel \n")
time.sleep(2)

print("Conectando a Linio")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element_by_xpath("/html/body/div[3]/main/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div/span")
raw_c = c_price.text
# print (raw_c[1:7])
print (" ---> Successfully retrieved the price from Linio\n")
time.sleep(2)

# Final display
print ("#------------------------------------------------------------------------#")
print ("Precios del Apple Iphone 12 64gb  PEN \n".format(product))
print("Price available at Tiendas I Shop is: "+r_price[0:])
print("  Price available at Entel is: "+raw_p[0:])
print("   Price available at Linio is: "+raw_c[0:])