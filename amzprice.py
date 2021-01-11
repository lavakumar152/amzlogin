from requests_html import HTMLSession


def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'titel': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }

    print(product)
    return product


getPrice('https://www.amazon.com/TCL-32-720p-ROKU-Smart/dp/B088S3V3R4/ref=sr_1_2?dchild=1&keywords=tv&qid=1610298018&rnid=2528832011&s=tv&sr=1-2')
