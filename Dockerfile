FROM python:3.9

# 
WORKDIR /code

ENV PYTHONPATH ./app

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app