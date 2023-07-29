import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/gp/bestsellers/books/?ie=UTF8&ref_=sv_books_1"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("div", {"id": "gridItemRoot"})

with open("books.txt", "w", encoding="utf-8") as file:
    for book in books:
        rank = book.find("span",{"class":"zg-bdg-text"}).get_text().strip()
        rank = rank[1:]
        name = book.find("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"}).get_text().strip()
        author = book.find("span", {"class": "a-size-small a-color-base"}).get_text().strip()
        try:
            score = book.find("span", {"class": "a-icon-alt"}).get_text().strip()
            score = score[-3:]
        except:
            score = "belirtilmemiş"

        file.write(f"{rank}.{name} - {author} - {score}\n")





