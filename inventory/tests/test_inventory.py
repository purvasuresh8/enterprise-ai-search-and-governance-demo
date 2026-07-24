from inventory.ai.predictors import DemandPredictor
from inventory.ai.anomaly_detector import AnomalyDetector
from inventory.ai.summarizer import InventorySummarizer


def test_predictor():

    predictor = DemandPredictor()

    assert predictor is not None


def test_anomaly_detector():

    detector = AnomalyDetector()

    assert detector is not None


def test_summarizer():

    summarizer = InventorySummarizer()

    assert summarizer is not None