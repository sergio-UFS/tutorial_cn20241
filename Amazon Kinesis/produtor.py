import json
import boto3
import random

stream_name = "teste1" #nome da data stream criada
region = "us-east-1" #servidor que a data stream se encontra, por padrão é o "us-east-1"
client_kinesis = boto3.client('kinesis', region_name = region) #inicia um client kinesis com as informações de nome e região da data-stream

i = 0
while True:
    i += 1
    # Gera um dado para inserir na stream
    dict = {"id_pessoa" : i}
    
    # Insere o dado na stream
    response = client_kinesis.put_record(StreamName = stream_name, Data = json.dumps(dict), PartitionKey = "1", ExplicitHashKey = "1")
    # Retorna as requisições PUT realizadas
    print("Total ingested:"+str(i) +",ReqID:"+ response['ResponseMetadata']['RequestId'] + ",HTTPStatusCode:"+ str(response['ResponseMetadata']['HTTPStatusCode']))
