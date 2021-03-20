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
