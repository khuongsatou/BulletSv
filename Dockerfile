FROM rabbitmq

RUN apk add --no-cache --update python3 py3-pip bash

COPY . .

RUN pip install -r requirements.txt

# CMD ["python","./example03.py"]
RUN rabbitmq-plugins enable --offline rabbitmq_management
EXPOSE 15671 15671