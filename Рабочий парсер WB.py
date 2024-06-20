from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import re

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--headless')  # Запуск без графического интерфейса

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

links_list = []  # сюда можно ссылки
# &nbsp позже убрать
with open("links.txt") as links_list:
    links_list = links_list.readlines()
    links_list = (i.strip() for i in links_list)

element = r'<ins class="price-block__final-price wallet">(.*?)</ins>'
element1 = r'<h1 class="product-page__title".*?>(.+?)</h1>'


def get_link(link, element, element1):
    driver.get(link)
    time.sleep(4)
    html = driver.page_source
    answer1 = re.findall(element1, html, flags=re.DOTALL)
    answer = re.findall(element, html, flags=re.DOTALL)
    if answer:
        return f"{link}:: {answer[0].replace('&nbsp;', '').replace('₽', '').strip()}:: {answer1[0]}"
    else:
        return f"{link}:: нет в наличии:: {answer1[0]}"


print("start")
with open("text.txt", "w", encoding="utf-8") as text:
    for link in links_list:
        try:
            text.write(f"{get_link(link, element, element1)}\n")
        except Exception as e:
            text.write(f"{type(e).__name__}\n")

driver.quit()
print("done")
