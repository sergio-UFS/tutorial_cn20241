from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Iniciar uma sessão Spark
    spark = SparkSession.builder.appName("ProcessCSV").getOrCreate()

    # Caminho do arquivo CSV no S3
    input_path = "s3://aws-logs-188255563909-us-east-1/athletes_new.csv"
    
    # Carregar o arquivo CSV
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    
    # Exemplo de processamento: Contar o número de linhas
    row_count = df.count()
    print(f"Number of rows: {row_count}")
    
    # Exemplo de transformação: Filtrar linhas com base em uma condição
    filtered_df = df.filter(df['country_code'] == 'BRA')

    # Salvar o resultado em outro caminho no S3
    output_path = "s3://aws-logs-188255563909-us-east-1/output/"
    filtered_df.write.csv(output_path, header=True)

    # Parar a sessão Spark
    spark.stop()
