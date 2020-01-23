FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /urls-checker
WORKDIR /urls-checker
COPY requirements.txt .
RUN ls -l
RUN pip install -r ./requirements.txt
COPY . /urls-checker