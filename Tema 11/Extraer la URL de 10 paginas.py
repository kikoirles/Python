import bs4
import requests
import lxml


url_base = "https://books.toscrape.com/catalogue/page-{}.html"
# cambir el numero de pagina por el URL
print(url_base.format('15'))

for n in range(1, 11):
    print(url_base.format(n))
