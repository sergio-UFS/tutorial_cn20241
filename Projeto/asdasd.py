from pyspark import SparkConf, SparkContext


if __name__ == "__main__":
    # Configuração do Spark
    conf = SparkConf().setMaster("local").setAppName("ContagemDePalavras")
    sc = SparkContext(conf=conf)

    # Texto de exemplo
    texto = ["Olá, este é um exemplo de teste para o PySpark", 
            "PySpark é ótimo para processar grandes volumes de dados"]

    # Criação do RDD a partir da lista de strings
    rdd = sc.parallelize(texto)

    # Transformações: separando as palavras e contando
    palavras = rdd.flatMap(lambda linha: linha.split(" "))
    contagem = palavras.map(lambda palavra: (palavra, 1)).reduceByKey(lambda a, b: a + b)

    # Ação: coletar o resultado
    resultado = contagem.collect()

    # Exibir o resultado
    for palavra, contagem in resultado:
        print(f"{palavra}: {contagem}")

    # Parar o contexto do Spark
    sc.stop()
