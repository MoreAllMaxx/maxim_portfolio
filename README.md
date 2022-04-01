Portfolio app (EN/RU) by Maxim Dontsov.

Do the following to run the application:

Add settings.py in portfolio folder. From settings.py.default ctrl+A, ctrl+V to settings.py:
1) Add SECRET KEY to settings.py
2) Provide information about POSTGRESQL or any other database in DATABASES
3) Add Telegram BOT_TOKEN and your Telegram USER_ID to the relevant variables (optional for running bot.py command)

After adding info above install everything from requirements.txt file:

`pip install -r requirements.txt`

Then migrate:

`python manage.py migrate`

And runserver:

`python manage.py runserver`

Also you can run bot to track down new messages in DB:

`python manage.py bot`

Or you can view the portfolio by clicking on the link https://portfoliomoreallmax.herokuapp.com/
