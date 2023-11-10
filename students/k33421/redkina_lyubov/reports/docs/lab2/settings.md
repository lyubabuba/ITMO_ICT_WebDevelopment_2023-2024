Очевидно, что файл `settings.py` содержит важные настройки проекта. 
Большая часть из них автоматически сгенерировалась при создании проекта, но некоторые изменения были внесены вручную.

Так, например, я указываю собственную модель пользователя, которую ранее определила в приложении `conferences_app`.
```
AUTH_USER_MODEL = 'conferences_app.Author'
```

Также я добавляю определение установленного приложения `conferences_app` в проекте.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conferences_app'
]
```
Остальные настройки - язык, формат времени и прочее - оставила неизменными.