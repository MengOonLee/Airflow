FROM apache/airflow:slim-latest

USER root

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        python3-dev \
        python3-venv \
    && apt-get upgrade -y \
    && apt-get autoremove -y --purge \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=airflow:root ~/Work/Airflow/dags /opt/airflow/dags

USER airflow

ENV VENV=/home/airflow/venv

COPY requirements.txt .

RUN python3 -m venv $VENV \
    && python3 -m pip install --no-cache-dir -U pip wheel \
    && pip install --no-cache-dir -Ur requirements.txt \
    && pip check \
    && rm -rf requirements.txt
