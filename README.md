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

---

## 🧬 Como treinar o modelo (já incluído)
