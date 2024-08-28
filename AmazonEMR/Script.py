from pyspark.sql import SparkSession

# Inicializa a Spark Session
spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

# Carrega dados do S3
df = spark.read.csv("s3://aws-logs-188255563909-us-east-1/crops.csv", header=True, inferSchema=True)

# Realize operações de análise de dados
df.createOrReplaceTempView("data")
result = spark.sql("SELECT crop, COUNT(*) as count FROM data GROUP BY crop")

# Salve o resultado no S3
result.write.mode("overwrite").csv("s3://your-bucket/path/to/output/")

# Finaliza a Spark Session
spark.stop()
