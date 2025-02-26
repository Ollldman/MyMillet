# Online Store on Django

Welcome to the repository of my online store! This is a modern web application built using the latest versions of Python, Django, CSS, HTML, and JavaScript. The project combines high performance, user-friendly design, and a stylish interface.

## Project Description

This online store is a fully functional web application that allows users to browse products, add them to a cart, place orders, and manage their profiles. The project is implemented using modern technologies and frameworks, ensuring high speed and security.

### Key Features:
- **Product Catalog**: An intuitive and user-friendly interface for browsing products.
- **Shopping Cart**: Ability to add products to the cart and place orders.
- **User Profile**: Manage your profile, view order history, and update personal information. (in progress)
- **Admin Panel**: Convenient management of products, orders, and users for administrators. (in progress)

## Technologies Used

The following technologies and tools were used in this project:

<div align="center">

  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/" target="_blank">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  </a>
  <a href="https://www.postgresql.org/" target="_blank">
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  </a>

</div>

## Installation and Setup

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ollldman/MyMillet.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up the PostgreSQL database:
   - Create a database in PostgreSQL.
   - Update the settings in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```
7. Apply the migrations:
   ```bash
   python manage.py migrate
   ```
8. Run the server:
   ```bash
   python manage.py runserver
   ```
9. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Required Libraries

The following Python libraries are used in this project. You can install them using `pip` by running:

```bash
pip install -r requirements.txt
```

Contents of the `requirements.txt` file:

```plaintext
Django==5.0
psycopg2-binary==2.9.9
django-crispy-forms==2.1
Pillow==10.1.0
django-environ==0.11.2
```

- **Django**: The main framework for web application development.
- **psycopg2-binary**: Adapter for working with PostgreSQL.
- **django-crispy-forms**: Simplifies form creation in Django.
- **Pillow**: Library for image processing.
- **django-environ**: Simplifies managing settings using environment variables.

## License


---

<div align="center">
  <h3>Thank you for your interest! If you like the project, don't forget to give it a ⭐!</h3>
</div>

# Интернет-магазин на Django

Добро пожаловать в репозиторий моего интернет-магазина! Это современное веб-приложение, разработанное с использованием последних версий Python, Django, CSS, HTML и JavaScript. Проект сочетает в себе высокую производительность, удобство использования и стильный дизайн.

## Описание проекта

Этот интернет-магазин представляет собой полнофункциональное веб-приложение, которое позволяет пользователям просматривать товары, добавлять их в корзину, оформлять заказы и управлять своим профилем. Проект реализован с использованием современных технологий и фреймворков, что обеспечивает высокую скорость работы и безопасность.

### Основные функции:
- **Каталог товаров**: Удобный и интуитивно понятный интерфейс для просмотра товаров.
- **Корзина покупок**: Возможность добавлять товары в корзину и оформлять заказы.
- **Личный кабинет**: Управление профилем, просмотр истории заказов и изменение личных данных. (в разработке)
- **Админ-панель**: Удобное управление товарами, заказами и пользователями для администратора. (в разработке)

## Использованные технологии

В проекте использованы следующие технологии и инструменты:

<div align="center">

  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.djangoproject.com/" target="_blank">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  </a>
  <a href="https://www.postgresql.org/" target="_blank">
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  </a>

</div>

## Установка и запуск

Для запуска проекта на локальной машине выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Ollldman/MyMillet.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ваш-репозиторий
   ```
3. Создайте виртуальное окружение (рекомендуется):
   ```bash
   python -m venv venv
   ```
4. Активируйте виртуальное окружение:
   - Для Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Для macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
6. Настройте базу данных PostgreSQL:
   - Создайте базу данных в PostgreSQL.
   - Обновите настройки в `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'ваша_база_данных',
             'USER': 'ваш_пользователь',
             'PASSWORD': 'ваш_пароль',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```
7. Примените миграции:
   ```bash
   python manage.py migrate
   ```
8. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
9. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:8000/
   ```

## Необходимые библиотеки

Для работы проекта используются следующие библиотеки Python. Вы можете установить их с помощью `pip`, выполнив команду:

```bash
pip install -r requirements.txt
```

Содержимое файла `requirements.txt`:

```plaintext
Django==5.0
psycopg2-binary==2.9.9
django-crispy-forms==2.1
Pillow==10.1.0
django-environ==0.11.2
```

- **Django**: Основной фреймворк для разработки веб-приложения.
- **psycopg2-binary**: Адаптер для работы с PostgreSQL.
- **django-crispy-forms**: Упрощает создание форм в Django.
- **Pillow**: Библиотека для работы с изображениями.
- **django-environ**: Упрощает управление настройками через переменные окружения.

## Лицензия



---

<div align="center">
  <h3>Спасибо за внимание! Если вам понравился проект, не забудьте поставить ⭐!</h3>
</div>
```


