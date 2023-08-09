import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def fill_form(location_params, price_params, link_params):
    input_fields = driver.find_elements(By.CLASS_NAME, value="zHQkBf")
    input_field_1 = input_fields[0]
    input_field_2 = input_fields[1]
    input_field_3 = input_fields[2]
    submit_input = driver.find_element(By.CLASS_NAME, value="RveJvd")
    time.sleep(2)
    input_field_1.send_keys(location_params)
    input_field_2.send_keys(price_params)
    input_field_3.send_keys(link_params)
    submit_input.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSczXfsIJMggkOQlgLQ02KuFt8doQkqp2K8bLNoTEqMIkUBYwQ/viewform?usp=sf_link"
zillow_link = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.64383227656958%2C%22north%22%3A37.90651729386%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
"Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
response = requests.get(url=zillow_link, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
all_prices = []
for price in soup.find_all(name="span", class_="iMKTKr"):
    if "+" in price.text:
        new = price.text.split("+")
        all_prices.append(new[0])
    elif "/" in price.text:
        new = price.text.split("/")
        all_prices.append(new[0])
    else:
        all_prices.append(price.text)
print(all_prices)
all_locations = []
for location in soup.find_all(name="address"):
    all_locations.append(location.text)
all_links = []
num = 1
for i in soup.find_all(name="a", class_="carousel-photo"):
    if num%3==0:
        if "https://www.zillow.com" not in i['href']:
            new_i = "https://www.zillow.com" + i['href']
            all_links.append(new_i)
        else:
            all_links.append(i['href'])
    num += 1
print(all_prices)
print(all_locations)
print(all_links)


s = Service(executable_path="F:\python projects\chrome developer\chromedriver.exe")

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSczXfsIJMggkOQlgLQ02KuFt8doQkqp2K8bLNoTEqMIkUBYwQ/viewform?usp=sf_link"
driver = webdriver.Chrome(service=s)
driver.get(url=form_link)
time.sleep(10)

for i in range(len(all_links)):
    fill_form(all_locations[i], all_prices[i], all_links[i])

