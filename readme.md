# Automatica тестовое API

## Запуск решения

Для запуска необходим установленный docker-compose, порядок установки можно найти здесь: https://docs.docker.com/compose/install/

Для запуска контейнера в папке с файлом docker-compose.yml выполните команду
> docker-compose up -d

## Superuser and static files

Далее нужно подключиться к контейнеру, для этого нужно выполнить
> docker-compose exec app /bin/bash

После этого выполним две команды
> ./manage.py collectstatic
>
> ./manage.py createsuperuser

## Готово!

Теперь можно заходить в админку и проверять работу
> http://localhost:8000/admin