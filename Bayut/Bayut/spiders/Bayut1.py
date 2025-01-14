import scrapy


class Bayut1Spider(scrapy.Spider):
    name = "Bayut1"
    allowed_domains = ["www.bayut.com"]
    start_urls = ["https://www.bayut.com/property/details-10398969.html"]

    def start_requests(self):
        for property_id in range(9941202,9942202):
            url = f"https://www.bayut.com/property/details-{property_id}.html"
            yield scrapy.Request(url=url, callback=self.parse)

    
        
