FROM python:3.6-stretch

RUN mkdir src
WORKDIR /src
COPY client.py /src
RUN pip install autobahn[twisted]

CMD ["python", "client.py"]