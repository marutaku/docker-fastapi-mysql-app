FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /

RUN pip3 install --upgrade setuptools && \
    pip3 install --upgrade pip
RUN pip3 install fastapi \
    uvicorn \
    mysqlclient \
    pymysql
