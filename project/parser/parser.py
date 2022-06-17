from project.chromedriver.driver import driver_init
from project.parser.definitions import change_url, space_rep
from requests_html import HTML
import json

def get_data(category):
    page = 1
    pagination = 1
    product_list = []
    driver = driver_init()
    change_url(driver, 'https://www.wildberries.ru')

    while pagination != None:
        if page == 2: break
        # change_url(driver, f'https://www.wildberries.ru/catalog/0/search.aspx?page={page}&sort=popular&search={category}')
        change_url(driver, f'https://www.wildberries.ru/catalog/0/search.aspx?page={page}&sort=popular&search={category}')

        with open(f'index{page}.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

        with open(f'index{page}.html', 'r', encoding='utf-8') as file:
            doc = file.read()

        html = HTML(html=doc)
        pagination = html.xpath(f"//a[contains(text(), '{page+1}')]/@href", first=True)
        
        card_tags = html.xpath("//div[contains(@class, 'product-card j-card-item')]")

        for tag in card_tags:

            html = HTML(html=tag.html)
            href = html.xpath("//a[contains(@class, 'j-card-link')]/@href", first=True)
            image = html.xpath("//img[contains(@class, 'j-thumbnail')]/@src", first=True)
            lower_price = html.xpath("//*[contains(@class, 'lower-price')]/text()", first=True)
            brand_name = html.xpath("//strong/text()", first=True)
            goods_name = html.xpath("//span[contains(@class, 'goods-name')]/text()", first=True)
            old_price = html.xpath("//del/text()", first=True)
            discount = html.xpath("//span[contains(@class, 'product-card__sale')]/text()", first=True)

            product_list.append(
                {
                    "link": href,
                    "image": "https:" + image,
                    "lower_price": space_rep(lower_price),
                    "old_price": space_rep(old_price),
                    "discount": discount,
                    "brand_name": brand_name,
                    "goods_name": goods_name
                }
            )
        page += 1

    with open('products.json', 'a', encoding='utf-8') as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)

    driver.quit()
    driver.close()
