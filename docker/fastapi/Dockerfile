FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /

RUN pip3 install --upgrade setuptools && \
    pip3 install --upgrade pip
COPY docker/fastapi/requirements.txt ./
RUN pip3 install -r requirements.txt
