# Бэкенд для веб-сервиса сокращения ссылок

Сокращение ссылки - формирование короткой ссылки, по которой будет осуществлен переход на исходную ссылку. Сервис должен уметь сократить исходную ссылку (то есть сопоставить этой ссылке уникальную сокращенную) и по сокращенной ссылке восстановить исходную и перейти по ней.
Считаем, что домен у сайта может быть любой, и что он задается в виде аргумента при запуске сервера. Например:
## Установка

Клонирование репозитория:
```sh
git clone https://github.com/eagurin/shortener-flask
cd shortener-flask/
````
Зайдите в репо и создайте и активируйте виртуальную среду:
```sh
python -m venv env
source env/bin/activate
```
Установите используемые пакеты:
```sh
pip install -r requirements.txt
```
Инициализировать БД:
```sh
python init_db.py
```
Установить хост:
```sh
export HOST=localhost
```
Запустить тесты:
```sh
python -m unittest discover -p tests.py
```
Запуск локально:
```sh
python app.py
```
Для сокращения ссылки использоваться метод:
```sh
POST /_short
```
Данные о ссылке передаются в теле документа в формате JSON:
```sh
{"url": "https://www.site.com/with/long/url?and=param"}
```
Запрос на сокращение ссылки  выглядить следующим образом:
```sh
curl -H "Content-Type: application/json" \
-X POST \
-d '{"url": "https://www.site.com/with/long/url?and=param"}' \
http://localhost:8000/_short
```
Все ответы приходят в формате JSON. Так, на метод сокращения ссылки придет URL в формате:
```sh
{"shorten": "http://localhost:8000/xyz123"}
```
