# Projeto: ETL + Aplicação de Machine Learning com Amazon EMR, SageMaker e Athena

Este tutorial irá guiá-lo através do processo de utilização do Amazon EMR para carregar dados, Amazon SageMaker para coletar dados e Amazon Athena para obter informações dos dados.

## Funcionamento

O Amazon EMR será responsável por realizar as etapas de Extração, Transformação e Carregamento dos dados, com o objetivo de realizar um preprocessamento e limpeza dos dados. Com os dados processados, esses estarão prontos para serem utilizados em outras tecnologias, como o SageMaker.

Neste, o Amazon SageMaker será utilizado para coletar e processar os dados, utilizando algoritmos de Machine Learning para realizar análises e previsões. Por fim, o Amazon Athena será utilizado para consultar os dados e obter informações relevantes, como estatísticas e insights, além de facilitar o processo de consulta de dados, principalmente em tabelas fixas, como um CSV, por exemplo.


Para fins de validação do projeto, será realizado o treinamento de um modelo e avaliação de sua performance, utilizando o Sagemaker, por fim, os objetos gerados serão armazenados no S3, como o retorno de um teste realizado. Com isso, será avialiado o desempenho do modelo com treinamentos de uma base com mais de 2 milhões de registros.


### Objeto de Estudo

O Conjunto de dados: [phishing-url-detection](https://www.kaggle.com/datasets/sergioagudelo/phishing-url-detection) será utilizado para a realização do projeto. Este conjunto de dados contém informações sobre URLs e se elas são ou não phishing, com isso vamos utilizar os conceitos de Machine Learning para realizar a classificação das URLs e tentar achar padrões que possam ser utilizados para a identificação de URLs maliciosas.

Para aproveitar mais a utilização do EMR, o conjunto de dados será dividido em 3 partes, sendo elas: Treino, Validação e Teste. O conjunto de dados de treino será utilizado para treinar o modelo, o conjunto de dados de validação será utilizado para validar o modelo e o conjunto de dados de teste será utilizado para testar o modelo. Além de separar os dados em algumas partes, para criar rotinas de coletas de dados.

### Estrutura do Projeto

O projeto está dividido em 3 partes, sendo elas:

1. Extração, Transformação e Carregamento dos Dados (ETL) com Amazon EMR
2. Treinamento e Avaliação do Modelo com Amazon SageMaker
3. Consulta de Dados com Amazon Athena

Os detalhes do projeto serão documentados para facilitar o entendimento e a replicação do projeto.


### Plano de Ação em tempo


|            | Avaliação de Possibilidade do Projeto | Desenvolvimento | Geração de Documentação | Apresentação |
|------------|----------------------------------------|-----------------|-------------------------|--------------|
| Semana 1   | X                                      |                 |                         |              |
| Semana 2   |                                        | X               |                         |              |
| Semana 3   |                                        | X               | X                       | X            |







