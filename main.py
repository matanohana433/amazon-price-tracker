import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 70
response = requests.get(url=URL)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")
soup.prettify()
product_price = float(soup.select_one('.a-price-whole').getText())
title = soup.find(id="productTitle").text.strip()


SMTP_ADDRESS=os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS=os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.environ.get("EMAIL_PASSWORD")

message = f"{title} is on sale for ${product_price}!"

if product_price < TARGET_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
        print("Email sent!")



