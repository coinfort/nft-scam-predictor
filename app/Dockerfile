FROM public.ecr.aws/lambda/python:3.9
USER root
COPY ./requirements.txt ./requirements.txt
COPY ./resources/bert-scam-nft /opt/ml/model
COPY . .
RUN chmod 777 .env

RUN python3.9 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
