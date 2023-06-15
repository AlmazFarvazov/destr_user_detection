import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Загрузка стоп-слов
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words(['russian', 'english']))

# Функция для очистки и нормализации текста
def clean_and_normalize(text):
    # Очистка текста от пунктуации, ссылок и хештегов
    # Удаление ссылок
    text = re.sub(r'(https?:\/\/\S+)', '', text) 
    # Удаление хештегов
    text = re.sub(r'(#\w+)', '', text) 
    # Удаление пунктуации
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    
    # Нормализация текста
    word_tokens = word_tokenize(text)
    filtered_text = [word.lower() for word in word_tokens if word not in stop_words]

    return " ".join(filtered_text)
