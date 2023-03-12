# Тестовое задание

### Задачи:
1) Дан массив связей пользователей. Необходимо реализовать функцию, которая принимает на вход три аргумента: информация о связях, как кортеж (tuple) кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если связь между любыми двумя заданными пользователями существует, например, если у двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе False.
2) Необходимо разработать небольшое WEB-приложение с использованием Django.
   Реализовать API принимающее файл формата xlsx с артикулами (артикулы должны вводиться построчно в первой колонке) или один артикул (не в файле, а исключительно одно значение). В API должно быть два инпута: файл или одно значение, передаваться должно что-то одно.
  API должно асинхронно взаимодействовать с найденным HTTP запросом в первом пункте и получать данные о карточке товара. Из полученных данных необходимо сделать PyDantic объект.
  ------------------------
### Ответ на 1 задачу находится в корне репозитория, Django приложение находится в task_2.
------------------------
### Реализован эндпоинт
*POST ai/v1/vendor-code
   * file: file.xlsx
   * code: str
------------------------
### Запуск:
1. Склонируйте данный репозиторий на свою локальную машину
2. Перейдите в папку task_2 и создайте файл .env
   Поместите в файл SECRET_KEY для Django
3. Создайте виртуальное окружение:
```sh
python -m venv venv
```
4. Активируйте виртуальное окружение:
Для Windows
```sh
.\venv\Scripts\activate
```
Для Linux
```linux
source venv/bin/activate
```

5. Примените миграции:
```sh
python manage.py migrate
```

6. Для запуска сервера используйте команду:
```sh
python manage.py runserver
```
