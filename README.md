# My Simple Upload with AWS S3

Aplicação web que faz uploads e downloads de arquivos em um bucket S3. 

Telas: [Home](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/home.png) [Upload](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/upload_2.png) [Downloads](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/downloads.png) 

[Dependências](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/dependencias.md)

[Passos para criar um bucket S3 e configurações](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/passos_s3.md)

[Arquitetura base](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/arquitetura.png)

[Execução da aplicação em uma instância EC2](https://github.com/armandossrecife/mysimpleuploads3/blob/main/docs/passos_ec2.md)

## 1. No servidor da aplicação, crie um ambiente virtual para a sua aplicação

Dentro do diretório principal (mysimpleuploads3)

```bash
python3 -m venv venv
```

## 2. Ative o ambiente virtual

```bash
source venv/bin/activate
```

## 3. Instale as dependências da sua aplicação

```bash
pip3 install -r requirements.txt
```

Obs: para listar os pacotes e as respectivas versões dos pacotes instalos:
```bash
pip3 list
```

## 4. Carregue as credenciais do usuário de execução da aplicação

Por exemplo: salvando as credencias AWS via variáveis de ambiente de Sistema Operacional (Linux/MacOS)

```bash
export ACCESS_KEY_ID=xxxxxxxxxxxxxxxx
export SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 5. Execute a aplicação principal
```bash
flask --app principal run --host=0.0.0.0 --port=5000
```
