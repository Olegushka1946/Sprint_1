# Проект REST API для туристических горных перевалов.
### Описание:
Этот проект разрабатывался в рамках обучения [SkillFactory](https://skillfactory.ru/python-developer) для Федерации Спортивного Туризма и Развития (ФСТР) с целью упростить
процесс учета горных перевалов и сократить время обработки данных. По заданию необходимо усовершенствовать  REST API 
для ведения базы горных перевалов, которая пополняется туристами.
Реализованы методы: API POST/submitData для добавления туристом информации о новом перевале; 
GET /submitData/<id> — получение одной записи о перевале по ее id, в том числе статус модерации;
PATCH /submitData/<id> — редактирование существующей записи, если она еще не поступила в работу модератору, 
а также GET /submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.

###  Параметры реализации:
1.При подготовке проекта использована база данных PostgreSQL, установка производится командой: 
```
pip install psycopg2
```
Порт, логин, пароль и путь к базе данных берется из переменных окружения с использованием библиотеки dotenv: 
```
pip install python-dotenv
```
2.В файле requirements.txt приведен список внешних зависимостей, который формируется командoй pip freeze > requirements.txt.
Установите зависимости командой:
```
pip install -r requirements.txt
```

### Как работать с API (endpoints):
1. По адресу /perevals/  можно создать информацию о новом перевале с помощью POST.
2. По адресу /perevals/id можно получить одну запись о перевале по ее id, в том числе статус модерации c помощью GET;
3. По адресу /perevals/id  можно редактировать существующую запись, если она еще не поступила в работу модератору с помощь PATCH;
4. Сменить статус модерации можно только через админ-панель по адресу: /admin. Возможность работы в ней обеспечивается созданием модератора по команде:
```
python manage.py createsuperuser
```
5. По адресу /api/submitData/user__email=<str:email>  можно с помощью GET получить список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
Пример запроса для получения данных обо всех объектах,которые пользователь с почтой <email.mail.ru> отправил на сервер, редактирования сведений о перевале:
[/api/submitData/user__email=<str:email>](http://127.0.0.1:8000/api/submitData/user__email=email@mail.ru)

```
[{"id": 2, "beauty_title": "beauty_title", "title": "title", "other_titles": "other_titles", "connect": "connect", "add_time": "2023-12-27 21:25:17", "level": {"summer": "1B", "autumn": "1B", "winter": "1B", "spring": "1B"},
"user": {"fam": "\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439", "name": "\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439", "otc": "\u0422\u0435\u0441\u0442", "email": "email@mail.ru", "phone": 79800024441},
"coord": {"latitude": 585.85, "longitude": 585.85, "height": 585}, "images": [{"title": "title", "date_added": "2023-12-27 21:25:17", "image": "https://image.com/image.jpg"}], "status": "new"},
{"id": 3, "beauty_title": "beauty_title222", "title": "title222", "other_titles": "other_titles222", "connect": "connect", "add_time": "2023-12-27 21:26:04", "level": {"summer": "1B", "autumn": "1B", "winter": "1B", "spring": "1B"},
"user": {"fam": "\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439", "name": "\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439", "otc": "\u0422\u0435\u0441\u0442", "email": "email@mail.ru", "phone": 79800024441},
"coord": {"latitude": 985.58, "longitude": 985.85, "height": 1234}, "images": [{"title": "title", "date_added": "2023-12-27 21:26:04", "image": "https://image.com/image1234.jpg"}], "status": "new"}]
```
Пример JSON-запроса для создания, редактирования сведений о перевале:
```
{
  
{
    "id": 2,
    "beauty_title": "beauty_title",
    "title": "title",
    "other_titles": "other_titles",
    "connect": "connect",
    "add_time": "2023-12-27 21:25:17",
    "level": {
        "summer": "1B",
        "autumn": "1B",
        "winter": "1B",
        "spring": "1B"
    },
    "user": {
        "fam": "Правильный",
        "name": "Тестовый",
        "otc": "Тест",
        "email": "email@mail.ru",
        "phone": 79800024441
    },
    "coord": {
        "latitude": 585.85,
        "longitude": 585.85,
        "height": 585
    },
    "images": [
        {
            "title": "title",
            "date_added": "2023-12-27 21:25:17",
            "image": "https://image.com/image.jpg"
        }
    ],
    "status": "new"
}
```