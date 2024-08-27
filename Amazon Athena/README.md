# Consulta SQL com Amazon Athena


## **Funcionamento**

![athena](https://github.com/user-attachments/assets/fa8370e3-dff1-4736-a50d-99f787b7772e)

O conjunto de dados salvos no Amazon S3 é catalogado pelo AWS Glue e a partir desses dados 
processados serão feitas as consultas com o AWS Athena.

## **Tutorial**

### 1. Selecionar conjunto de dados

Fonte utilizada no tutorial: Olimpiadas 2024
> https://www.kaggle.com/datasets/willianoliveiragibin/olympics-2024

[https://github.com/sergio-UFS/tutorial_cn20241/blob/main/Amazon%20Athena/athletes%20new.csv]

### 2. Configuração de Bucket S3

* Na página inicial da AWS, pesquisar o serviço **S3** e selecionar a opção **Criar bucket**

![image](https://github.com/user-attachments/assets/aab40850-5c10-4706-99c4-29f9bc316604)

* Escolher o nome do *bucket*, manter todas as outras configurações por padrão e selecionar a opção **Criar bucket**

* Acessar o bucket criado 
  
![image](https://github.com/user-attachments/assets/11ca703d-62bc-4213-bf73-b7fee58a23b6)

* Selecionar a opção **Criar Pasta**
  
![image](https://github.com/user-attachments/assets/a5f56616-0324-46b6-b669-cf6dc0a20b34)

* Escolher o nome da pasta e clicar em **Criar Pasta**

* **Dentro da pasta criada**, criar outras duas pastas refazendo o mesmo processo
  
Exemplo: Dentro da pasta **dados-teste** foram criadas as pastas **raw** e **processed** que serão usadas para armazenar os
dados brutos e processados, respectivamente.

![image](https://github.com/user-attachments/assets/15f4f486-a58a-4260-8579-c86a50576ab6)

* Na pasta **raw**, selecionar a opção **Carregar**
  
![image](https://github.com/user-attachments/assets/78840d09-e9f4-4dc3-95e2-2e777ce3f2b0)

* Em seguida clicar em **Adicionar arquivos** e selecionar o conjunto de dados escolhido anteriormente
  
![image](https://github.com/user-attachments/assets/19f30d31-8f0c-4697-8796-3e3609738200)


### 3. Criar Crawler com AWS Glue

* Na página inicial da AWS, pesquisar o serviço **AWS Glue** e selecionar a opção **Crawlers**

![image](https://github.com/user-attachments/assets/e28c59f9-58aa-4c6c-96e1-d6b8689d5c17)

* Após clicar na opção **Create Crawler**

![image](https://github.com/user-attachments/assets/34fc2716-2eb2-4cd4-b525-14702dafcd18)

* Escolher o nome nome do *crawler* e prosseguir em **Next**

![image](https://github.com/user-attachments/assets/9381cd1b-97bf-4e42-88b1-c8365cc88a13)

* Selecionar o conjunto de dados em **Add a data source**

![image](https://github.com/user-attachments/assets/1675c5ae-28ee-4279-aa09-920e764ce778)

* Escolher os dados armazenados no *bucket* criado anteriormente, selecionando a opção **Browse S3** e escolhendo a pasta **raw**

![image](https://github.com/user-attachments/assets/7b0fc1a7-1b93-4437-aa5f-cf295db6a20e)

> [!WARNING]
> Apagar a última barra do endereço selecionado

![image](https://github.com/user-attachments/assets/f4086b49-3442-4c04-9d0a-e12c1519fca7)


* Na terceira etapa de configuração, selecionar o perfil **"LabRole"**

![image](https://github.com/user-attachments/assets/55d2feef-e95f-4fde-b21a-0e6a34f22737)

* Em seguida, clicar em **Add Database**, escolher um nome para a base de dados e criar selecionando o botão **Create Database** 

![image](https://github.com/user-attachments/assets/96fce808-5517-40b9-b16b-d91c6ef3d34c)

* Voltando à configuração do *crawler* selecionar a base de dados criada

![image](https://github.com/user-attachments/assets/00c2c453-8c73-42cf-aa5a-7636a4184052)

* Por fim, revisar as configurações escolhidas e selecionar **Create crawler**

* Na página de *Crawlers* da AWS Glue será exibido o *crawler* criado. Para axecutá-lo, basta selecionar e clicar em **Run**

![image](https://github.com/user-attachments/assets/2055048c-8f67-4397-8871-d5404bf06ae2)

Ao executar o *crawler* é possível perceber que após a varredura na base de dados foi criada uma nova tabela com os metadados.

* Para visualizar essa tabela, basta ir na opção **Tables** da AWS Glue e selecionar a tabela criada

![image](https://github.com/user-attachments/assets/bb3a3a4b-d1c7-43be-a7ef-6611ae7fbac8)


### 4. Configurar o Amazon Athena

* Na página inicial da AWS, pesquisar o serviço **Athena**

* Selecionar a opção **Editor de consultas**

![image](https://github.com/user-attachments/assets/cfdedfa0-27a2-4359-83f4-db3ddd8b7a43)

* Configurar um local para os resultados das consultas

![image](https://github.com/user-attachments/assets/3014f5f6-d72a-4b85-9fb8-8f699af13a4f)

* Realizar as consultas

**Exemplo:**
![image](https://github.com/user-attachments/assets/30a24ba6-4996-4e1e-b2c4-2b840509b69a)

> Resultados obtidos
![image](https://github.com/user-attachments/assets/3010916e-7dc4-41bb-98fe-e9cafb1ec5be)




