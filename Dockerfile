From python:3.9

COPY ./ workouttracker

WORKDIR /workouttracker

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["python","manage.py","runserver", "0.0.0.0:8080"]