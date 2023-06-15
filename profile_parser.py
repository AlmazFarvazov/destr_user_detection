import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_user_data(post_url):
    # Загружаем страницу поста
    response = requests.get(post_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим ссылку на профиль автора поста
    author_link = soup.find('a', class_='story__user-link user__nick')['href']  # Обновите class в соответствии с HTML
    post_rating = soup.find('div', class_='story__rating-count').text
    post_text = soup.find('h1', class_='story__title').span.text
    publish_date = datetime.fromisoformat(soup.find('time').get('datetime'))

    # Загружаем страницу автора
    response = requests.get(author_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем данные с профиля автора
    user_rating = soup.find('span', class_='profile__digital hint').b.text  # Обновите class в соответствии с HTML
    user_name = soup.find('h1', class_='profile__nick').span.text  # Обновите class в соответствии с HTML
    user_name = user_name[0] + "***" + user_name[-1]
    reg_date = datetime.fromisoformat(soup.find('time').get('datetime'))

    # Здесь также можно извлечь дополнительные данные
    posts = soup.find_all('div', class_='story__main')
    posts_ratings = soup.find_all('div', class_='story__rating-block')
    data = []
    for i in range(len(posts) - 1):
      try:
        data.append(
          {
              'post_text' : posts[i].find('a', class_='story__title-link').text,
              'post_rating' : posts_ratings[i].find('div', class_='story__rating-count').text
          }
        )
      except AttributeError:
        print(i)
        
    # Возвращаем данные автора
    return {
        'name': user_name,
        'profile_rating': user_rating,
        'reg_date' : reg_date,
        'post_rating' : post_rating,
        'post_text' : post_text,
        'publish_date' : publish_date,
        'posts' : data
    }

