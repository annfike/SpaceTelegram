# Космический Телеграм

Сервис для скачивания фотографий на тему космоса и публикации их в Телеграм-канале.

### Как установить

 - Для использования скрипта необходимо зарегистрироваться на сайте [NASA](https://www.nasa.gov)
   и получить токен.
 - Также потребуется токен от Телеграм-бота (администратора Телеграм-канала) название канала в Телеграме.
 - Полученные токены и название телеграм-канала присвоить переменным окружения в файле ".env":
```python
   NASA_TOKEN=ВашТокен
   
   TG_BOT_TOKEN=ВашТокен

   TG_CHANNEL=название телеграм-канала
```
 - Python3 должен быть уже установлен.
 - Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
   pip install -r requirements.txt
   ```
 - Для запуска скрипта используйте команду:
```python
   python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
