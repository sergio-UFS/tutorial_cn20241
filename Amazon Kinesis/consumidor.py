import boto3

stream_name = "teste1" # Nome da data stream criada
region = "us-east-1" # Servidor que a data stream se encontra, por padrão é o "us-east-1"
client_kinesis = boto3.client('kinesis', region_name = region) # Inicia um client kinesis com as informações de nome e região da data-stream

# Itera sobre um determinado shard
shard_iterator = client_kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId="shardId-000000000000",
    ShardIteratorType="AT_TIMESTAMP",
    Timestamp=1459799926.480,
)["ShardIterator"]

# Enquanto houver dados no shard continua as iterações
while shard_iterator is not None:
    resultado = client_kinesis.get_records(ShardIterator=shard_iterator) # Faz a requisição get para o shard
    records = resultado["Records"]
    shard_iterator = resultado["NextShardIterator"]

    for record in records:
        print(record["Data"])
