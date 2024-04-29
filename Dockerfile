FROM python:3.12

WORKDIR /mlops_hw3

COPY . .

RUN pip install -r requirements.txt

CMD ["bash", "./pipeline.sh"]
