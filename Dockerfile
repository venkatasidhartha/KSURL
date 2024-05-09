FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
COPY gunicorn.conf.py /app/
EXPOSE 8000
RUN chmod +x start_enpoint.sh
CMD ["sh","start_enpoint.sh"]
