# Cервис управления рассылками, администрирования и получения статистики 
## Проект «Сервис рассылки»

<img width="960" alt="Безымянный" src="https://github.com/GalinaTsoktoeva/mailing_list/assets/5502809/6614a3c4-f723-4929-89db-cf268669cf57">

Проектная работа курса [«Python‑разработчик»](https://sky.pro/courses/programming/python-web-course) платформы SkyPro.   

[Посмотреть проект](https://github.com/GalinaTsoktoeva/mailing_list/)
## Краткое описание
Адаптивный сервис рассылки, который создан с использованием BOOTSTRAP и Django.   
База данных - Postgresql
#### Стек технологий
  * BOOTSTRAP;
  * Python
  * Django
  * PostgreSQL
  * Redis
#### С применением
  * ООП (Классы)
## Рефакторинг на будущее
Доработать верификацию пользователей
## Исходники
[Свёрстан по макету](https://getbootstrap.com/docs/5.0/examples/album/)

## Описание
* Интерфейс системы содержит следующие экраны:список рассылок, отчет проведенных рассылок отдельно, создание рассылки,
  удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
* При создании рассылки создается задача с периодическими рассылками, которая реализуется с помощью celery и redis.
* Реализовано приложение для ведения блога.
* Права доступа разделены для различных пользователей.
* Модель пользователя расширена для регистрации по почте, а также верификации.
* Настроено кеширование
## Сущности
* Блог
* Клиент
* Сообщение для рассылки
* Рассылка
* Пользователь

_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv

source venv/bin/activate
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_

_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для заполнения БД запустить команду:_

```
python3 manage.py fill
```

_Для создания администратора запустить команду:_

```
python3 manage.py csu
```

_Для запуска redis_:

```
redis-cli
```

_Для запуска приложения:_

```
python3 manage.py runserver
```
