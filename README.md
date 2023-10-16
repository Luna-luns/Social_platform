![Logo](Yatube_logo.png)

# Yatube

Современная социальная платформа для блоггинга

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

## Описание проекта:

Проект предоставляет возможноть:
- публиковать и редактировать посты;
- писать к постам комментарии;
- добавлять посты в группы;
- подписываться на любимых авторов.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Luna-luns/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Пример запроса к API
Запрос:
`POST http://localhost:port/api/v1/posts/`

```
{
"text": "string",
"image": "string",
"group": 0
}
```
Ответ:
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

## 🚀 Обо мне

Начинающий backend-разработчик на Python
- [@Елизавета Струнникова](https://github.com/Luna-luns)
  
## Обратная связь

Email: liza.strunnikova@yandex.ru<br>
Telegram: @l_lans
