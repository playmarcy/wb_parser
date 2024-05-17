from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Selenium с использованием ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск без графического интерфейса
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

with open("links.txt", "r", encoding="utf-8") as links, open("text2.txt", "w", encoding="utf-8") as text2:
    k = 0
    for url in links:
        if k == 10:
            break
        driver.get(url)
        time.sleep(5)
        try:
            title_element = driver.find_element(By.CLASS_NAME, 'product-page__title')
            title = title_element.text
            # Попробуем различные способы нахождения цены
            try:
                price_element = driver.find_element(By.CLASS_NAME, 'price-block__final-price')
            except:
                price_element = None
            
            if not price_element:
                try:
                    price_element = driver.find_element(By.XPATH, '//span[contains(@class, "price-block__final-price")]')
                except:
                    price_element = None

            if price_element and price_element.text:
                price = price_element.text
            else:
                price = "нет в наличии"
                
            text2.write(f'{title}:: {price}\n')
        except Exception as e:
            text2.write(f"Ошибка на {url}: {str(e)}\n")
        k += 1

# Закрытие браузера
driver.quit()
print("готово")
