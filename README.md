# A Django and Postgres project setup in Docker


## To run

docker-compose -f docker-compose.yml --env-file=dev.env up -d


## Add a new python package 

   * update requirements.txt
   * docker-compose -f docker-compose.yml build


# DB updates

   * python manage.py makemigrations beans_intake
   * python manage.py sqlmigrate beans_intake 0001
   * python manage.py migrate
   * migrations.RunSQL(
   *    'ALTER SEQUENCE beans_intake_location_id_seq RESTART WITH 10000;'
   * )

# Static file

   * docker exec espresso-web /bin/sh -c "python manage.py collectstatic --noinput"
   * docker exec espresso-web /bin/sh -c "python manage.py createsuperuser"