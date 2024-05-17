from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import re

options = ChromeOptions()
options.add_argument("--start-maximized")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

links_list = [
    "https://www.wildberries.ru/catalog/160104584/detail.aspx",
    "https://www.wildberries.ru/catalog/169796718/detail.aspx",
    "https://www.wildberries.ru/catalog/160104590/detail.aspx",
    "https://www.wildberries.ru/catalog/160104622/detail.aspx",
    "https://www.wildberries.ru/catalog/160104695/detail.aspx",
    "https://www.wildberries.ru/catalog/214097596/detail.aspx",
    "https://www.wildberries.ru/catalog/198410835/detail.aspx",
    "https://www.wildberries.ru/catalog/160104559/detail.aspx",
    "https://www.wildberries.ru/catalog/160104601/detail.aspx",
    "https://www.wildberries.ru/catalog/160104625/detail.aspx",
    "https://www.wildberries.ru/catalog/187378832/detail.aspx",
    "https://www.wildberries.ru/catalog/159933028/detail.aspx",
    "https://www.wildberries.ru/catalog/208515968/detail.aspx",
    "https://www.wildberries.ru/catalog/160104553/detail.aspx",
    "https://www.wildberries.ru/catalog/160104666/detail.aspx",
    "https://www.wildberries.ru/catalog/160104694/detail.aspx",
    "https://www.wildberries.ru/catalog/160104611/detail.aspx",
    "https://www.wildberries.ru/catalog/160104662/detail.aspx",
    "https://www.wildberries.ru/catalog/160104585/detail.aspx",
    "https://www.wildberries.ru/catalog/160104563/detail.aspx",
    "https://www.wildberries.ru/catalog/198406647/detail.aspx",
    "https://www.wildberries.ru/catalog/160104685/detail.aspx",
    "https://www.wildberries.ru/catalog/160104660/detail.aspx",
    "https://www.wildberries.ru/catalog/160104663/detail.aspx",
    "https://www.wildberries.ru/catalog/175122377/detail.aspx",
    "https://www.wildberries.ru/catalog/160104627/detail.aspx",
    "https://www.wildberries.ru/catalog/187378836/detail.aspx",
    "https://www.wildberries.ru/catalog/187378837/detail.aspx",
    "https://www.wildberries.ru/catalog/187378838/detail.aspx",
    "https://www.wildberries.ru/catalog/160104520/detail.aspx",
    "https://www.wildberries.ru/catalog/160105469/detail.aspx",
    "https://www.wildberries.ru/catalog/182840414/detail.aspx",
    "https://www.wildberries.ru/catalog/160104638/detail.aspx",
    "https://www.wildberries.ru/catalog/160104679/detail.aspx",
    "https://www.wildberries.ru/catalog/166043632/detail.aspx",
    "https://www.wildberries.ru/catalog/217027614/detail.aspx",
    "https://www.wildberries.ru/catalog/197509681/detail.aspx",
    "https://www.wildberries.ru/catalog/159517505/detail.aspx",
    "https://www.wildberries.ru/catalog/159570165/detail.aspx",
    "https://www.wildberries.ru/catalog/159762019/detail.aspx",
    "https://www.wildberries.ru/catalog/159883044/detail.aspx",
    "https://www.wildberries.ru/catalog/159891842/detail.aspx",
    "https://www.wildberries.ru/catalog/159914465/detail.aspx",
    "https://www.wildberries.ru/catalog/183204796/detail.aspx",
    "https://www.wildberries.ru/catalog/218361267/detail.aspx",
    "https://www.wildberries.ru/catalog/160104618/detail.aspx",
    "https://www.wildberries.ru/catalog/160104619/detail.aspx",
    "https://www.wildberries.ru/catalog/160104637/detail.aspx",
    "https://www.wildberries.ru/catalog/160104537/detail.aspx",
    "https://www.wildberries.ru/catalog/160104529/detail.aspx",
    "https://www.wildberries.ru/catalog/160104669/detail.aspx",
    "https://www.wildberries.ru/catalog/160104639/detail.aspx",
    "https://www.wildberries.ru/catalog/160104609/detail.aspx",
    "https://www.wildberries.ru/catalog/160104599/detail.aspx",
    "https://www.wildberries.ru/catalog/175452116/detail.aspx",
    "https://www.wildberries.ru/catalog/198596885/detail.aspx",
    "https://www.wildberries.ru/catalog/222158378/detail.aspx",
    "https://www.wildberries.ru/catalog/198406647/detail.aspx",
    "https://www.wildberries.ru/catalog/198408681/detail.aspx",
]
# &nbsp позже убрать
element = r'<span class="price-block__wallet-price">(.*?)</span>'


def get_link(link, element):
    driver.get(link)
    time.sleep(7)
    html = driver.page_source
    time.sleep(3)
    return f"{link}::: {element in html}"


print("start")
with open("text.txt", "w") as text:
    for link in links_list:
        try:
            text.write(f"{get_link(link, element)}\n")
        except Exception as e:
            text.write(f"{type(e).__name__}\n")

driver.quit()
print("done")
