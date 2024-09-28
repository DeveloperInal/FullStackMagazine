#!/bin/bash

if sudo apt-get update -y; then
    echo "Обновление завершено"
else
    echo "Обновление завершилось с ошибкой. Ебитесь с ошибкой"
    exit 1
fi

# Создание директории server в корне
cd / && mkdir -p server/

# Переход в server и клон репы
cd server/ && git clone https://github.com/DeveloperInal/FullStackMagaize/tree/main

cd FullStackMagaize/

# Запуск сервисов
sudo docker compose up -d
