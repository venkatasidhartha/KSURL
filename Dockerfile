FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade -y
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
COPY gunicorn.conf.py /app/
EXPOSE 8000
RUN chmod +x start_enpoint.sh
CMD ["sh","start_enpoint.sh"]
