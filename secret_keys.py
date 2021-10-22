import os

os.environ['EMAIL_HOST_USER'] = 'anonyme0000xx@gmail.com'
os.environ['EMAIL_HOST_PASSWORD'] = 'anonyme0000@xx2'

os.environ['SECRET_KEY'] = 'django-insecure-_1qv!(sw*ks*@y5jfbf8&9%t92u&a%cepzam3ut1$fzsc!pkiw'
os.environ['POSTGRES_PASSWORD'] = 'amin'

os.environ['DJANGO_USERNAME'] = 'henteti'
os.environ['DJANGO_PASSWORD'] = 'aminChu7caex'

# heroku addons:create heroku-postgresql:hobby-dev
# heroku config -s | grep DATABASE_URL

# You can also run heroku pg:info to get details of your database on heroku. Add-on: will give you nameOfHerokuDB .
# Now lets push local database to herokuDB

# push local database:PGUSER="postgres" PGPASSWORD="amin" heroku pg:push postgres://wxvziazamavobe:5ab195009b3857f8572e0ff13ce6a4027caf387a3ff240856169b34ff2ad5d04@ec2-3-219-103-45.compute-1.amazonaws.com:5432/d74fr6u638mimu postgresql-graceful-64689