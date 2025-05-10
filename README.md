
# 🚀 PicPay Case — Machine Learning Engineer

Este projeto é uma solução para o case técnico de MLE (Machine Learning Engineer) do PicPay. Ele envolve transformação de dados com Spark, treinamento de modelo de machine learning, disponibilização de uma API com FastAPI e containerização via Docker.

---

## 📌 Objetivo do Modelo

O modelo tem como objetivo prever se um voo terá **atraso superior a 15 minutos na chegada** com base nas seguintes variáveis:

- Atraso na partida (`dep_delay`)
- Distância entre origem e destino (`distance`)
- Tempo de voo (`air_time`)
- Aeroporto de origem (codificado como inteiro)
- Aeroporto de destino (codificado como inteiro)

---

## 🧠 Tecnologias Utilizadas

- Python 3.11
- FastAPI + Uvicorn
- Scikit-learn
- PySpark
- Joblib
- Docker
- pytest + httpx (testes)

---

## 🧪 Como executar os testes unitários

```bash
pip install -r requirements.txt
pytest tests/
```

---

## 🧬 Como treinar o modelo (já incluído)

O modelo foi treinado com regressão logística usando `LogisticRegression`. O target foi definido como:

```python
target = (df["arr_delay"] > 15).astype(int)
```

Para salvar:

```python
joblib.dump(model, "model.pkl")
```

---

## ⚙️ Como executar a API localmente

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Rode a API com Uvicorn

```bash
uvicorn src.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 Endpoints da API

| Método | Rota               | Descrição                                               |
|--------|--------------------|----------------------------------------------------------|
| GET    | `/health/`         | Verifica se a API está online                           |
| POST   | `/model/load/`     | Faz upload e carrega um modelo `.pkl`                   |
| POST   | `/model/predict/`  | Recebe dados de voo e retorna predição (0 ou 1)         |
| GET    | `/model/history/`  | Retorna histórico de predições feitas                   |

---

### 🔎 Exemplo de payload para predição

```json
{
  "dep_delay": 45.0,
  "distance": 2000.0,
  "air_time": 280.0,
  "origin": 1,
  "destination": 2
}
```

> Obs.: Os campos `origin` e `destination` devem ser **inteiros**, codificados conforme os valores usados no treino.

---

## 🐳 Como executar com Docker

### 1. Build da imagem

```bash
docker build -t picpay-mle-api .
```

### 2. Rodar o container

```bash
docker run -p 8000:8000 picpay-mle-api
```

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧾 Observações

- As APIs externas utilizadas no enriquecimento dos dados foram:
  - AirportDB (coordenadas)
  - Weatherbit (condições climáticas)
- Como o ambiente do Databricks não permite chamadas externas, as APIs foram consumidas localmente e os dados foram integrados manualmente via upload.

---

## ✅ Status da entrega

- ✅ Transformações e análises em PySpark
- ✅ Respostas das 17 perguntas
- ✅ Enriquecimento com APIs
- ✅ Modelo treinado e serializado
- ✅ API completa com 4 endpoints
- ✅ Testes automatizados
- ✅ Dockerfile funcional

---
