from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

if __name__ == "__main__":
    # Iniciar uma sessão Spark
    spark = SparkSession.builder.appName("ProcessCSV").getOrCreate()

    # Caminho do arquivo CSV no S3
    input_path = "s3://bucket-projeto-cn2024/dataset_link_phishing.csv"
    
    # Carregar o arquivo CSV
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    
    # Exemplo de processamento: Contar o número de linhas
    filtered_df = df.select('url','google_index','page_rank',"web_traffic","nb_hyperlinks","domain_age","phish_hints","ratio_extHyperlinks","ratio_intHyperlinks","longest_word_path","longest_words_raw",'status')

    filtered_df = filtered_df.withColumn("status_boolean", when(col("status") == "legitimate", 0).when(col("status") == "phishing", 1).otherwise(None))

    filtered_df = filtered_df.drop("status")

    # Salvar o resultado em outro caminho no S3
    output_path = "s3://aws-logs-188255563909-us-east-1/output/"
    filtered_df.write.csv(output_path, header=True, mode="overwrite")

    # Parar a sessão Spark
    spark.stop()
