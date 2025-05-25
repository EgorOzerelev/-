from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/news/'  # URL с новостями ОмГТУ
    response = requests.get(url)
    print(f"Статус ответа: {response.status_code}")

    if response.status_code != 200:
        print("Не удалось получить доступ к сайту.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдём все элементы, содержащие заголовки новостей
    news_titles = soup.find_all('a', class_='news-card__link')

    titles = []
    for title in news_titles:
        titles.append(title.get_text(strip=True))

    # Запись заголовков в файл
    with open('omgtu_news_titles.txt', 'w', encoding='utf-8') as file:
        for t in titles:
            file.write(t + '\n')

    print(f"Найдено {len(titles)} заголовков и сохранено в файл 'omgtu_news_titles.txt'.")

if __name__ == '__main__':
    parse()