# Tinkoff Scraper

Этот проект собирает информацию о финансовых инструментах (лучшие заявки/предложения и последняя сделка) с использованием асинхронного клиента Tinkoff API. Данные тикеров импортируются из CSV, результаты сохраняются в CSV.

## 📦 Возможности

- Импорт тикеров из CSV
- Асинхронная работа с API
- Сохранение информации в CSV
- Логирование процесса

---

## 🛠 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Sneguradik/TinkoffScraper.git
cd TinkoffScraper
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

### 3. Активация виртуального окружения
- Windows:
```bash
venv\Scripts\activate
```
- Linux/macOS:
```bash
source venv/bin/activate
```

### 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

## ⚙️ Настройка .env
Создай файл .env рядом с main.py и добавь строку:
```dotenv
TOKEN=ваш_API_токен
```

## 📄 Формат входного CSV
CSV-файл должен содержать колонку ticker или просто список тикеров в первом столбце:
```csv
Tickers
SBER
GAZP
ELMT
```

## 🚀 Запуск скрипта
```bash
python main.py --i path/to/input.csv --o path/to/output.csv
```
### Аргументы:
| Аргумент | Описание                  | Обязательный | Значение по умолчанию |
| -------- | ------------------------- | ------------ | --------------------- |
| `--i`    | Путь к CSV с тикерами     | ✅ да         | —                     |
| `--o`    | Путь к файлу вывода (CSV) | ❌ нет        | `output.csv`          |

## 📂 Формат выходного CSV
```csv
figi,isin,ticker,class_code,
best_bid_price,best_bid_volume,best_bid_direction,best_bid_time,
best_offer_price,best_offer_volume,best_offer_direction,best_offer_time,
last_deal_price,last_deal_volume,last_deal_direction,last_deal_time
```
