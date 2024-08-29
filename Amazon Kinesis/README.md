# Representação de um modelo básico de produtor consumidor utilizando o Amazon Kinesis



## Como funciona o Amazon Kinesis?

![Representação da stream de dados do Kinesis](https://www.darede.com.br/wp-content/uploads/2023/09/kinesis.png)



## Tutorial
### Inicializando uma stream

1. Pesquise por Kinesis e selecione a primeira opção (tem o subtítulo: Work with Real-Time Streaming Data)
2. Na seção **Comece a usar** deixa selecionada a opção **Kinesis Data Streams** e clique em **Criar fluxo de dados**
3. Insira um nome para o fluxo
4. Na seção **Capacidade do fluxo de dados** deixe selecionada a opção **Sob demanda**
5. No final da página, clique em **Criar fluxo de dados**

### Criando o modelo produtor consumidor
1. Crie um ambiente do **Cloud9**
  - Clique em **Criar ambiente**
  - Selecione um nome para o ambiente e em **Tipo de ambiente** deixe selecionada a opção **Nova instância do EC2**
  - Na **Nova instância do EC2**, deixe selecionada a arquitetura **t2.micro (1 GiB RAM + 1 vCPU)** e a plataforma **Ubuntu Server 22.04 LTS**
  - Em configurações de rede, selecione a opção **Secure Shell (SSH)**
  - Clique em **Criar**
2. Abra seu ambiente no Cloud9
3. Dentro do ambiente, crie os arquivos **produtor.py** e **consumidor.py**, disponibilizados nesse repositório
4. No terminal, digite o comando **pip3 install boto3** (biblioteca para interagir com serviços aws)
5. No arquivo **produtor.py**, coloque na variável **stream_name** o nome da stream do Kinesis que você criou
6. Repita o mesmo processo no arquivo **consumidor.py**
7. No terminal, rode o comando **python produtor.py** para iniciar o produtor
8. Após alguns minutos, será possível visualizar na sua stream do Kinesis, na aba **Monitoramento**, o fluxo de dados sendo enviados
9. Quando os dados começarem a aparecer no Monitoramento da Stream, em um terminal separado, rode o comando **python consumidor.py** para consumir os dados da stream
