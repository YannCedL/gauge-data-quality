# API FastAPI pour le moteur Gauge Data Quality
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .validator import evaluate_quality

app = FastAPI(
    title="Gauge Data Quality API",
    description="Moteur d'Évaluation de Qualité & Fraîcheur des Données",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec scorecard de qualite
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Gauge API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Gauge", "version": "1.0.0"}

@app.get("/api/v1/quality", response_model=ResultContract)
def get_quality(dataset_name: str = Query("flux_annonces_bodacc")):
    return evaluate_quality(dataset_name)
