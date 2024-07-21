### Эксперименты с todo list на Django
#### Запуск
1. Установить зависимости из requirements.txt
2. Прописать настройки доступа к БД файле .env в корне (образец в .env.sample)
3. Терминал: python todolist_core/manage.py runserver

#### Текущее состояние
- Добавлен DRF, сериализатор для моделей Task, Tag, Comment
- Добавлены соответствующие им вьюсеты и эндпоинты
- Добавлен drf-yasg, доступен по /swagger/
