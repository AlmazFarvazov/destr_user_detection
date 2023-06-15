from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Предположим, что у вас есть DataFrame pandas df с двумя столбцами: 'text' и 'destructive'
df = pd.read_csv('data.csv')

# Предварительная обработка текста и векторизация
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['destructive']

# Разделение набора данных на обучающий и тестовый
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем модель SVM
svc = SVC(kernel='rbf')

# задаем сетку параметров, которую хотим проверить
param_grid = {
    'svm__C': [0.1, 1, 10],
    'svm__gamma': [0.1, 0.01, 0.001]
}

# Инициализируем GridSearchCV
grid_search = GridSearchCV(estimator=svc, param_grid=param_grid, cv=5)

# Проводим поиск по сетке
grid_search.fit(X_train, y_train)

# Выводим наилучшие параметры
print(grid_search.best_params_)

# Обучаем модель с наилучшими параметрами
svc_best = svm.SVC(**grid_search.best_params_)
svc_best.fit(X_train, y_train)

# Предсказываем метки для тестовых данных
y_pred = svc_best.predict(X_test)

# Оценка производительности модели
print(classification_report(y_test, y_pred))
