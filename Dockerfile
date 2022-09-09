FROM python:3.9
 
WORKDIR /TestAPI
 
COPY ./requirements.txt /TestAPI/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /TestAPI/requirements.txt
COPY ./app /TestAPI/app

EXPOSE 8080

USER 1000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
