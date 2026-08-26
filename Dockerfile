FROM python:3.14-slim

WORKDIR /home/myapp

COPY requirements.txt .

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --no-cache-dir --upgrade pip setuptools \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python", "sample_app.py"]