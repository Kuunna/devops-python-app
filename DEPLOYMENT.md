# Руководство по развертыванию Python DevOps приложения

## 1. Получение исходного кода
Исходный код доступен в репозитории GitHub: ```https://github.com/Kuunna/devops-python-app```
Для клонирования репозитория выполните:
```bash
git clone https://github.com/Kuunna/devops-python-app.git
cd devops-python-app
```

## 2. Получение Docker образов
Docker образы можно получить двумя способами:

### Способ A: Сборка из исходного кода
```bash
# Собрать образ локально
docker build -t python-devops-app .

# Проверить созданный образ
docker images
```

### Способ B: Использование готовых образов
Основные образы Docker будут загружены автоматически:
- `python:3.9-alpine` - базовый образ Python
- `jenkins/jenkins:lts` - для Jenkins CI/CD
- `nginx:alpine` - для обратного прокси (если используется)

## 3. Основные команды для развертывания

### Локальное тестирование:
```bash
# Запустить приложение напрямую
python app.py

# Или через Docker
docker build -t myapp .
docker run -p 5000:5000 myapp
```

### Развертывание с Docker Compose:
```bash
# Запуск всех сервисов
docker-compose up -d

# Проверка статуса
docker-compose ps

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down
```

### Управление контейнерами:
```bash
# Список контейнеров
docker ps

# Остановка контейнера
docker stop <container_name>

# Удаление контейнера
docker rm <container_name>

# Просмотр логов
docker logs <container_name>
```

## 4. Пошаговое руководство по развертыванию

### Шаг 1: Подготовка окружения
```bash
# Клонирование репозитория
git clone https://github.com/Kuunna/devops-python-app.git
cd devops-python-app

# Настройка переменных окружения
cp .env.example .env
# Отредактируйте .env при необходимости
```

### Шаг 2: Сборка и запуск
```bash
# Способ A: Через Docker Compose (рекомендуется)
docker-compose up -d --build

# Способ B: Вручную
docker build -t python-app .
docker run -d -p 5000:5000 --name python-app-container python-app
```

### Шаг 3: Проверка развертывания
```bash
# Проверка здоровья приложения
curl http://localhost:5000/health

# Проверка основного эндпоинта
curl http://localhost:5000

# Проверка контейнеров
docker ps
docker-compose ps
```

### Шаг 4: Интеграция с Jenkins
1. Установите Jenkins: `docker run -d -p 8080:8080 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts`
2. Создайте новый Freestyle проект в Jenkins
3. Настройте Git репозиторий: `https://github.com/Kuunna/devops-python-app.git`
4. Добавьте Build Step с командами развертывания

### Шаг 5: Автоматическое развертывание
Настройте Jenkins Pipeline или Webhook для автоматического развертывания при пуше в репозиторий.

## 5. Проверка работоспособности

После развертывания проверьте:
1. Приложение доступно: `http://localhost:5000`
2. Health check работает: `http://localhost:5000/health`
3. Контейнеры запущены: `docker ps`
4. Логи без ошибок: `docker logs <container_name>`

## 6. Устранение неполадок

### Проблема: Порт 5000 занят
```bash
# Найдите процесс, использующий порт
sudo lsof -i :5000

# Или используйте другой порт
docker run -p 5001:5000 myapp
```

### Проблема: Ошибки Docker
```bash
# Проверьте, запущен ли Docker
docker version

# Перезапустите Docker
sudo systemctl restart docker
```

### Проблема: Отсутствуют зависимости
```bash
# Пересоберите образ
docker-compose up -d --build

# Или обновите зависимости вручную
docker exec -it <container> pip install -r requirements.txt
```

## 7. Мониторинг и логи

```bash
# Реальные логи приложения
docker logs python-app-container --tail=50 -f

# Логи Docker Compose
docker-compose logs -f

# Использование ресурсов
docker stats
```

## Контакты и поддержка

При возникновении проблем:
1. Проверьте логи: `docker-compose logs`
2. Проверьте issues в репозитории GitHub
3. Убедитесь, что все шаги выполнены правильно
