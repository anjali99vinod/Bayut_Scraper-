import scrapy
from bs4 import BeautifulSoup as bs


class Bayut1Spider(scrapy.Spider):
    name = "Bayut1"
    allowed_domains = ["www.bayut.com"]
    start_urls = ["https://www.bayut.com/property/details-10398969.html"]

    def start_requests(self):
        for property_id in range(9941202, 9942202):
            url = f"https://www.bayut.com/property/details-{property_id}.html"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = bs(response.text, 'html.parser')


        property_id = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(2) > ul > li:nth-of-type(3) > span:nth-of-type(2)'))
        property_url = response.url
        purpose = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(2) > ul > li:nth-of-type(2) > span:nth-of-type(2)'))
        type = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(2) > ul > li:nth-of-type(1) > span:nth-of-type(2)'))
        added_on = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(2) > ul > li:nth-of-type(6) > span:nth-of-type(2)'))
        furnishing = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(3) > div:nth-of-type(1) > div > div:nth-of-type(2) > ul > li:nth-of-type(4) > span:nth-of-type(2)'))
        price = self.extract_price(self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2) > span')))
        location = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2)'))
        bed_bath_size_element = soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(3)')
        bed_bath_size_text = self.get_text(bed_bath_size_element)
        bed_bath_size_parts = bed_bath_size_text.split() if bed_bath_size_text else []
        bed_bath_size = {
            'beds': bed_bath_size_parts[0] if bed_bath_size_parts and bed_bath_size_parts[0].isdigit() else '',
            'baths': ''.join(filter(str.isdigit, bed_bath_size_parts[1])) if len(bed_bath_size_parts) > 1 else '',
            'sqft': ''.join(filter(str.isdigit, bed_bath_size_parts[-2])) if len(bed_bath_size_parts) > 3 else ''
        }        
        permit_number = self.get_text(soup.select_one('html>body>div:nth-child(1)>main>div:nth-child(2)>div:nth-child(4)>div:nth-child(3)>div:nth-child(1)>div>div:nth-child(2)>ul>li:nth-child(3)>span:nth-child(2)'))
        agent_name = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(5) > div:nth-of-type(1) > div > div:nth-of-type(1) > div > div:nth-of-type(2) > span > a'))
        primary_image_url = self.get_image_url(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(1) > div > div > picture > img'))
        breadcrumbs = self.get_text(soup.select_one('html>body>div:nth-of-type(1)>main>div:nth-of-type(1)>div>div>a:nth-of-type(1)>span'))
        amenities = self.get_text(soup.select_one('html > body > div:nth-of-type(1) > main > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > div > h2'))
        description = self.get_text(soup.select_one('html>body>div:nth-of-type(1)>main>div:nth-of-type(2)>div:nth-of-type(4)>div:nth-of-type(3)>div:nth-of-type(1)>div>div:nth-of-type(1)>div:nth-of-type(1)'))
        property_image_urls = self.get_image_urls(soup.select_one('html>body>div:nth-of-type(1)>main>div:nth-of-type(2)>div:nth-of-type(2)>div'))
        
