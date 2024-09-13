FROM jupyter/base-notebook
USER root
RUN apt-get update && apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
USER ${NB_UID}
WORKDIR /home/jovyan
EXPOSE 8888
