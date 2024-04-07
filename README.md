# My Simple Upload with AWS S3

## 1. Crie um ambiente virtual para a sua aplicação

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

## 4. Execute a aplicação principal
```bash
flask --app principal run --host=0.0.0.0 --port=5000
```