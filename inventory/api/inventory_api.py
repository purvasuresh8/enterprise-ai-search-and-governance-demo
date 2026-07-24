from fastapi import FastAPI
from inventory.ai.predictors import DemandPredictor
from inventory.ai.anomaly_detector import AnomalyDetector
from inventory.ai.summarizer import InventorySummarizer

app = FastAPI(
    title="Inventory Intelligence API",
    version="1.0.0"
)

predictor = DemandPredictor()
detector = AnomalyDetector()
summarizer = InventorySummarizer()


@app.get("/")
def health():
    return {
        "status": "healthy",
        "service": "inventory-intelligence"
    }


@app.get("/forecast")
def forecast():
    return predictor.predict()


@app.get("/anomalies")
def anomalies():
    return detector.detect()


@app.get("/summary")
def summary():
    return summarizer.generate_summary()