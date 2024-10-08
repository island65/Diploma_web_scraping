# Веб скрапинг информации о товарах

## Описание проекта

Этот проект предназначен для сбора и обработки данных о продуктах из раздела "Парфюмерия" интернет-магазина Gold Apple. Используя веб-скрапинг, программа собирает информацию о товарах, включая ссылку на продукт, наименование, цену, рейтинг пользователей, описание, инструкцию по применению и страну-производителя. Полученные данные сохраняются в формате CSV.


### Описание основных файлов и каталогов

- **main.py**: Главный скрипт для запуска проекта. Он запускает процесс сбора данных, обрабатывает их и объединяет результаты в единый CSV файл.

- **data/**: Каталог для хранения сгенерированных CSV файлов.
  - **products.csv**: Файл, содержащий основную информацию о продуктах.
  - **details.csv**: Файл с детализированной информацией о продуктах.
  - **merged_data.csv**: Итоговый файл с объединёнными данными.
- **src/**: Каталог с исходными файлами, содержащими логику веб-скрапинга и обработки данных.
  - **fetch_product_data.py**: Скрипт для сбора основной информации о продуктах.
  - **get_detailed_info.py**: Скрипт для сбора детализированной информации о продуктах.
  - **merge_files.py**: Скрипт для объединения CSV файлов с данными.

- **tests/**: Каталог с тестами для проверки работоспособности кода.
  - **test_fetch_product_data.py**: Тесты для модуля fetch_product_data.
  - **test_get_detailed_info.py**: Тесты для модуля get_detailed_info.
  - **test_merge_files.py**: Тесты для модуля merge_files.

- **requirements.txt**: Файл с зависимостями, необходимыми для работы проекта.

## Установка и запуск

### Шаг 1: Клонирование репозитория

Сначала клонируйте репозиторий на локальный компьютер:

```bash
git clone https://github.com/island65/Diploma_web_scraping
```

### Шаг 2: Создание и активация виртуального окружения

Рекомендуется использовать виртуальное окружение для установки зависимостей:

```bash
python3 -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
```

### Шаг 3: Установка зависимостей

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### Шаг 4: Задать путь в папку для csv файлов

Создать файл .env. Прописать путь к папке и дать названия csv-файлам.
(Рекомендовано: `data/products.csv`, `data/details.csv`, `data/merged_data.csv`)

### Шаг 5: Запуск проекта

Для запуска процесса сбора данных используйте команду:

```bash
python main.py
```

Скрипт выполнит следующие действия:
1. Соберет основную информацию о продуктах и сохранит её в `data/products.csv`.
2. Соберет детализированную информацию и сохранит её в `data/details.csv`.
3. Объединит оба файла в `data/merged_data.csv`.

## Тестирование

Для запуска тестов используйте следующую команду:

```bash
pytest coverage run -m unittest
```

Для сбора информации в html файле запустите команду:
```bash
python -m coverage html 
```

Тесты проверяют основные функциональности кода, включая сбор и обработку данных.

## Результаты

Итоговый файл с объединенными данными можно найти по следующему пути:

[Скачать merged_data.csv](./data/merged_data.csv) 