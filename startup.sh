#!/bin/bash

# Удаление репы, если существует!!!
# sudo rm -rf /server/

# Функция для проверки успешности выполнения команд
check_status() {
    if [ $? -ne 0 ]; then
        echo "Ошибка: $1"
        exit 1
    fi
}

# Обновление системы
echo "Начинается обновление системы..."
if sudo apt-get update -y; then
    echo "Обновление завершено успешно."
else
    echo "Обновление завершилось с ошибкой.Ебитесь."
    exit 1
fi

# Создание директории server в корне
echo "Создание директории /server..."
sudo mkdir -p /server/
check_status "Не удалось создать директорию /server"

# Переход в директорию server
cd /server/ || { echo "Не удалось перейти в директорию /server"; exit 1; }

# Клонирование репозитория
echo "Клонирование репозитория..."
git clone https://github.com/DeveloperInal/FullStackMagaize.git
check_status "Не удалось клонировать репозиторий"

# Переход в директорию репозитория
cd FullStackMagaize/ || { echo "Не удалось перейти в директорию FullStackMagaize"; exit 1; }

# Запуск сервисов Docker
echo "Запуск Docker Compose сервисов..."
sudo docker compose up -d --build
check_status "Не удалось запустить Docker Compose сервисы"

echo "Все шаги выполнены успешно."

