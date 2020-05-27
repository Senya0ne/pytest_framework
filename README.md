# pytest_framework
Имеется приложение ToDo: http://todomvc.com/examples/react/
1) Сформировать сценарии ручной проверки (Формат и вид любой)
Какие задачи будут проверены в первую очередь и почему? Какие сценарии нужно отобрать для автоматизации.
Как оценить покрытие требований?
2) Используя Python.
Реализовать Smoke проверку данного приложения по ранее подготовленным тестам. Сопроводить инструкцией по запуску
Оценить покрытие

Архитектурно по PageObject
tests - папка с тестами <br>
pages - папка с методами базовыми и для взаимодействия с локаторами <br>
locators - папка с локаторами <br>

По заданию:
1. Главное что нужно прочекать - форму ввода.
2. Прочекать добавление записей(1 запись, 2 записи), комплит(зачеркивание записей), что меняется значение счетчика записей после комплита или удаления.
3. Не задавался этим вопросом, надо погуглить.
4. Реализовано с помощью ```@pytest.mark.smoke```
запускать такие тесты можно ```pytest -m smoke``` или незапускать smoke 
```pytest -m "not smoke"```

Инструкция по запуску:
1. Ставим python3
2. Ставим ```pip``` *pip install -U pip*
2. Ставим ```virtualenv``` *pip3 install virtualenv*
3. Поднимаем виртуальное окружение *python3 -m venv env*
4. Запускаем виртуальное окружение *source env/bin/activate*
5. Апгрейдим *pip install --upgrade pip*  
6. Ставим зависимости *pip install -r requrements.txt*
7. На всякий случай *pip install wheel*

Запуск тестов: команда ```pytest```

yml для Gitlab такой примерно можно накидать
```image: python:3.7

stages:
  - test

test:
  stage: test

  services:
    - name: selenium/standalone-chrome

  before_script:
    # Установка окружения
    - echo "Install environment"
    - apt-get update -q -y
    - pip3 install -r requirements.txt

    # скачиваем и подготавливаем к работе webdriver firefox
    - echo "Get geckodriver"
    - wget https://github.com/chrome/etc
    - tar -xvzf chromedriver.tar.gz
    - chmod +x chromdriver

  script:
    - echo "Run all tests"
    - pytest -v -m smoke