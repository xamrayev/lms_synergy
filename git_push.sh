#!/bin/bash

# Проверка на наличие аргумента (сообщения коммита)
if [ -z "$1" ]; then
    echo "❗ Укажите сообщение коммита:"
    echo "Пример: ./gitpush.sh 'обновил README'"
    exit 1
fi

# Основные команды git
git add .
git commit -m "$1"
git push origin main

# Проверка результата push
if [ $? -eq 0 ]; then
    echo "✅ Changes pushed successfully."
else
    echo "❌ Failed to push changes."
fi
