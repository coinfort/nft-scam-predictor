FROM public.ecr.aws/lambda/python:3.9

COPY . .
COPY resources/bert-scam-nft /opt/ml/model

RUN python3.9 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
