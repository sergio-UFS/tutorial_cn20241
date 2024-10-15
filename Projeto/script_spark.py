from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct
from pyspark.ml.feature import StringIndexer
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":
    # Iniciar uma sessão Spark
    spark = SparkSession.builder.appName("ProcessCSV").getOrCreate()


    input_path = "s3://aws-logs-188255563909-us-east-1/dataset_link_phishing.csv"

    # Ler o CSV com o schema definido
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Selecionar colunas
    selected_columns = ["url", "url_length", "hostname_length", "ip", "total_of.", "total_of-", "total_of@", "total_of?", "total_of&", "https_token", "status"]
    df_selected = df.select(selected_columns)


    # Obter labels únicos
    labels = df_selected.select("status").distinct().collect()
    print("Labels únicos:", [row["status"] for row in labels])

    # Dividir os dados em conjuntos de treino e teste
    train_df, test_df = df_selected.randomSplit([0.7, 0.3], seed=42)

    # Definir caminhos de saída
    train_output_path = "s3://aws-logs-188255563909-us-east-1/output/"
    test_output_path = "s3://aws-logs-188255563909-us-east-1/output/"

    # Salvar os dataframes como CSV
    train_df.write.csv(train_output_path, header=True, mode="overwrite")
    test_df.write.csv(test_output_path, header=True, mode="overwrite")

    spark.stop()