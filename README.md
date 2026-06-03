# 📌 Transaction Service API

REST API сервис для обработки транзакций с возможностью добавления, удаления и получения статистики. Проект построен на Django REST Framework и поддерживает запуск через Docker Compose.

---

# ⚙️ Стек технологий

- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Swagger (drf-yasg)

---

# 🚀 Возможности API

- 📥 Добавление транзакции
- 📊 Получение статистики (кол-во, среднее, топ-3)
- 🗑 Удаление всех транзакций
- 📄 Swagger документация
- 🌐 API с префиксом `/api/`

---

# 📁 Запуск проекта локально
http://localhost:8000/api/statistics/ GET Запрос
http://localhost:8000/api/transactions/ POST/DELETE Запрос
http://127.0.0.1:8000/swagger/

## 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/REPO.git
cd transaction_service
