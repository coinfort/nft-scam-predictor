FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt requirements.txt
COPY resources/bert-scam-nft /opt/ml/model

RUN python3.9 -m pip install -r requirements.txt -t .

COPY . /app

CMD ["app.lambda_handler"]
