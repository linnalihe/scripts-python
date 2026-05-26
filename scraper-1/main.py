import scrapy

class HackernewsSpiderSpider(scrapy.Spider):

    name = 'hackernews_spider'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    def parse(self, response):
        articles = response.css('tr.athing')
        for article in articles:
            yield {
                "URL": article. css(".titleline a::attr(href)").get(),
                "title": article.css(".titleline a::text").get(),
                "rank": article.css(".rank::text").get().replace(".", "")
            }

            print({
                "URL": article. css(".titleline a::attr(href)").get(),
                "title": article.css(".titleline a::text").get(),
                "rank": article.css(".rank::text").get().replace(".", "")
            })

HackernewsSpiderSpider.parse(self)


# import asyncio

# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.firefox.launch(headless=False)
#         page = await browser.new_page()

#         await page.goto("https://www.amazon.com/Hitchhikers-Guide-Galaxy/dp/B0009JKV9W/ref=sr_1_2?crid=2V2GGNZBMJZ6I&dib=eyJ2IjoiMSJ9.wb7EHnUj9gmaRGl8cK24x15H1fyqeae9MyzM7NuXZekEt1vf6GgMCA8ytmUAOShvvL--K0pSflJmAo_KIouynK8Vx_7uhGJvhn7YCmPNdjl8Mij_xTb3qxnbRaz2LasELD2HEV0aMBxP1kLYUDxFtSF6NR_sVMJpz2p7DBLdRib4f-ygprJVB4t7BlQFBOQZJYMD28fRI-s8aSgfK0Dycxs07JJ330VA8qb25-vygY4.b-nn-hGw5Bx4juiG25uHiB3b3gtkwnkG1AbOVrO00J0&dib_tag=se&keywords=douglas+adams+hitchhiker%27s+guide+to+the+galaxy&qid=1760126107&sprefix=douglas+adams+hi%2Caps%2C116&sr=8-2")

#         selectors = ['#productTitle', 'span.author a', '#productSubtitle', ]

#         book_data = await asyncio.gather(*(page.query_selector(sel) for sel in selectors))

#         book = {}

#         book["book_title"], book["author"], book["edition"], book["price"] = [await elem.inner_text() for elem in book_data if elem]


#         print("this is the book:")
#         print(book)


# asyncio.run(main())

# print("hello world")



# from bs4 import BeautifulSoup

# import httpx

# response = httpx.get("https://news.ycombinator.com/news")

# print("Hello world")
# print(response)

# res_content = response.content

# print(res_content)

# soup = BeautifulSoup(res_content)

# articles = soup.find_all(class_="athing")

# for article in articles:
#     data = {

#         "URL": article.find(class_="titleline").find("a").get('href'),
#         "title": article.find(class_="titleline").getText(),
#         "rank": article.find(class_="rank").getText().replace(".", "")
#     }

#     print(data)