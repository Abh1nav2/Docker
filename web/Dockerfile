
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ARG GAMER="Abhinav"

ENV GAMER="${GAMER}"

VOLUME ["/app/data"]

CMD ["python", "app.py"]

