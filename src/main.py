from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import joblib
import tempfile


app = FastAPI()

model = None
history = []


class FlightPayload(BaseModel):
    dep_delay: float
    distance: float
    air_time: float
    origin: int
    destination: int


@app.post("/model/predict/")
def predict(payload: FlightPayload):
    if model is None:
        raise HTTPException(status_code=400, detail="Modelo não carregado.")

    features = [[
        payload.dep_delay,
        payload.distance,
        payload.air_time,
        payload.origin,
        payload.destination
    ]]

    prediction = model.predict(features)[0]
    entry = {"input": payload.dict(), "prediction": int(prediction)}
    history.append(entry)
    return {"prediction": int(prediction)}


@app.post("/model/load/")
def load_model(file: UploadFile = File(...)):
    global model
    if not file.filename.endswith('.pkl'):
        raise HTTPException(status_code=400, detail="O arquivo deve ser .pkl")

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    model = joblib.load(tmp_path)

    return {"message": "Modelo carregado com sucesso."}


@app.get("/model/history/")
def get_history():
    return {"history": history}


@app.get("/health/")
def health():
    return {"status": "ok"}
