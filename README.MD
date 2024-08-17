### Эксперименты с to do list на Django
#### Запуск
1. Установить зависимости из requirements.txt
2. Прописать настройки доступа к БД файле .env в корне (образец в .env.sample)
3. Терминал: python todolist_core/manage.py runserver
4. Celery: celery -A conf worker --pool=threads --loglevel=info
4. Celery-beat: celery -A conf  beat --loglevel=info
5. Flower: celery -A conf flower

#### Текущее состояние
- Тест
