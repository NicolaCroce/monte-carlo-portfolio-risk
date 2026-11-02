from datetime import datetime
from typing import List
import numpy as np

# --- CONFIGURACIÓN DEL PORTAFOLIO ---
TICKERS: List[str] = ["SPY", "QQQ", "TLT", "GLD"]
WEIGHTS: np.ndarray = np.array([0.40, 0.30, 0.20, 0.10])  # La suma debe ser 1.0
INITIAL_PORTFOLIO_VALUE: float = 1_000_000.0  # $1,000,000 USD
START_DATE: str = "2019-01-01"
END_DATE: str = datetime.today().strftime("%Y-%m-%d")

# --- PARÁMETROS DE SIMULACIÓN MONTE CARLO ---
NUM_SIMULATIONS: int = 10_000
TIME_HORIZON_DAYS: int = 10     # Horizonte de riesgo a 10 días
CONFIDENCE_LEVEL: float = 0.95  # Nivel de confianza para VaR / CVaR (95%)