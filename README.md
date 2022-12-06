# SafeCiclism

## Esse e um projeto feito por alunos da faculdade Sapiens

### Como usar:

```Bash
# Crie uma virtual env usando o comando a seguir:
python3 -m venv venv
```
```Bash
# Execute a virtual env:
source venv/bin/activate
```
```Bash
# Em seguida instale os patch necessarios
pip install requirements.txt
```
```Bash
# E por ultimo dentro do diretorio do Safeciclism, execute o seguinte comando
FLASK_APP=server.py FLASK_DEBUG=true flask run --port 8080

