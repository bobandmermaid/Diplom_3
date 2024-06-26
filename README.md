# Diplom_3

## Дипломный проект. Задание 3: веб-приложение

### Тестирование [веб-приложения Stellar Burgers](https://stellarburgers.nomoreparties.site/)

Созданы тесты, покрывающие функциональность `Восстановление пароля`, 
`Личный кабинет`, `Проверка основного функционала`, `Раздел 'Лента заказов'`

### Структура

- `pages` - Содержит Page Object.
- `tests` - Содержит тесты, разделенные по классам.
- `conftest.py` - Содержит фикстуры, используемые в тестах.
- `data.py` - Содержит вспомогательные данные и методы, используемые в тестах.
- `locators.py` - Содержит локаторы, используемые в тестах.

### Запуск автотестов

1. **Установка браузеров**

- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/firefox/)

2. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

3. **Запуск автотестов и создание Allure-отчета**

    ```bash
    pytest -v tests --alluredir allure_results && allure serve allure_results
    ```