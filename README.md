# Django-shop

Пример интернет-магазина с использованием Django

## О проекте

Интернет-магазин, выполненный на Django версии 3.1.7, Python 3.9.0, Bootstrap для фронта и PostgreSQL.

Магазин имеет следующий функционал:
- список категорий с возможностью отбора;
- список товаров с изображениями, описанием, ценой и остатками;
- поиск по названию или описанию товара;
- корзина с возможностью редактирования;
- оформление заказа через корзину c записью его в БД;
- отправка email'а с созданным заказом;
- уменьшение доступного остатка товаров при оформлении заказа;

## Установка

В виртуальном окружении (virtualenv) выполнить команду:
```
pip install -r requirements.txt
```
Далее запустить сервер командой:
```
python manage.py runserver
```

## Автор

* **Максим Сердюков**
