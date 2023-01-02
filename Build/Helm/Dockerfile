FROM apache/airflow:latest

RUN python3 -m pip install --no-cache-dir -U pip wheel \
    && pip install --no-cache-dir -U \
        apache-airflow-providers-sendgrid \
        scrapy \
    && pip check
