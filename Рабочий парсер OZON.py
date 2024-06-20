from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import re

options = ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument('--headless')  # Запуск без графического интерфейса

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Чтение ссылок из файла
with open("links.txt", "r", encoding="utf-8") as file:
    links_list = file.readlines()
    links_list = [i.strip() for i in links_list]

def get_link(link):
    driver.get(link)
    try:
        # Ожидание появления элемента <span> с классом l8z_27 zl6_27
        price_element = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.l8z_27.zl6_27"))
        )
        price_text = price_element.text.replace('&nbsp;', '').replace('₽', '').strip()

        # Ожидание появления элемента <h1> с классом n3m_27 tsHeadline550Medium
        title_element = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.n3m_27.tsHeadline550Medium"))
        )
        title_text = title_element.text.strip()

        return f"{link}:: {price_text}:: {title_text}"
    except Exception as e:
        return f"Error: {type(e).__name__}"

print("start")
with open("text.txt", "w", encoding="utf-8") as text:
    for link in links_list:
        try:
            result = get_link(link)
            text.write(f"{result}\n")
            print(result)  # вывод для отладки
        except Exception as e:
            error_message = f"Error: {type(e).__name__}"
            text.write(f"{error_message}\n")
            print(error_message)  # вывод для отладки

driver.quit()
print("done")
