[![Flake8](https://github.com/py-cyber/csv_processor/actions/workflows/flake8.yml/badge.svg)](https://github.com/py-cyber/csv_processor/actions)
[![Black](https://github.com/py-cyber/csv_processor/actions/workflows/black.yml/badge.svg)](https://github.com/py-cyber/csv_processor/actions/workflows/black.yml)

## Установка проекта:
Для установки проекта вы можете прописать следующую команду в терминал:
```bash
git clone https://gitlab.crja72.ru/django/2025/spring/course/projects/team-1.git
```

## Создание виртуального окружения для проекта:
* Создание виртуального окружения: 
```bash
python3 -m venv .venv
```
* Активация виртуального окружения:
```bash
source .venv/bin/activate
```
## Установка зависимостей
* Зависимости для продакшена: 
```bash
pip install -r requirements/prod.txt
```
* Зависимости для разработки:
```bash
pip install -r requirements/dev.txt
```
* Зависимости для тестирования: 
```bash
pip install -r requirements/test.txt
```
## Подготовка к запуску
* Скопируйте все параметры из файла template.env в .env с помощью команды:
```bash
cp -r template.csv .csv
```
## Тестироварние
```bash
pytest tests.py -v
```
## Запуск скрипта
```bash
python main.py {file_path} --where "condition" --aggregate "condition" --order-by "condition" 
```
## Пример
```bash
python main.py template.csv --where "brand=xiaomi" --aggregate "price=avg" --order-by "name=desc" 
```
