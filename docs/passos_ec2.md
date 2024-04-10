# Execução em uma instância do EC2

Caso você queira publicar a aplicação na sua infraestrutura ASW, via instância EC2, basta alterar o protótipo com os seguintes passos:

## 1. Criação da instância

Crie uma instância do Ubuntu 22 no EC2 com as portas 5000 e 8000 liberadas para qualquer IP (0.0.0.0/0).

Faça as devidas configurações inbound/outbound no grupo de segurança da instância para liberar essas portas.

## 2. Execute a instância via console AWS 

Acesse o terminal da instância e atualize os pacotes apt da instância

```bash
sudo apt update
```

## 3. Revise as versões do Git e do Python

Git >= 2.23.0

Python >= 3.10

Obs: garanta que o instalador de pacotes do Python esteja devidamente instalado. 
```bash
sudo apt install python3-pip
```

## 4. Clone o repositório da aplicação

Faça o clone do repositório mysimpleuploads3

## 5. Política de segurança IAM

Faça uma associação de uma política de segurança de acesso completo aos serviços AWS S3