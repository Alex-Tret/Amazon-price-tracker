import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import data

TARGET_PRICE = 200.0
MY_EMAIL = data.MY_EMAIL
MY_PASSWORD = data.MY_PASSWORD
TO_MAIL = "4alextret@gmail.com"

URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8?ref_=ast_sto_dp&th=1"

header = {
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Defined"
}
"""Scraping Amazon page"""
response = requests.get(URL, headers=header)
amazon_page = response.text

soup = BeautifulSoup(amazon_page,"lxml")
price_block = soup.find("span", id="priceblock_dealprice")
price = float(price_block.getText()[1::])
product_title = soup.find("span", id="productTitle").getText().strip()

"""Sending mail notification"""
if price <= TARGET_PRICE:
	with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
		connection.starttls()
		connection.login(user=MY_EMAIL, password=MY_PASSWORD)
		connection.sendmail(from_addr= MY_EMAIL,
							to_addrs= TO_MAIL,
							msg=f"Subject:Amazon price alert\n\n{product_title}\nCurrent price is $ {price}\n{URL}")
