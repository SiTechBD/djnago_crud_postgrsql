# djnago_crud_postgrsql
django crud using postgresql

1) Install a library for use postgresql
   ```
   pip install psycopg2
   ```

2) Change the Database settings in settings.py
   ```
   DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'sample2',
		'USER': 'shafiq',
		'PASSWORD': '123456789',
		'HOST':'localhost',
		'PORT':'5432',
	}
}
   ```
