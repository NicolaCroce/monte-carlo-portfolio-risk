import numpy as np
import pandas as pd
import yfinance as yf

# Deshabilitar la caché interna de yfinance para evitar bloqueos de SQLite
try:
    yf.enable_download_cache(False)
except AttributeError:
    pass

def fetch_market_data(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """
    Descarga precios desde Yahoo Finance para una lista de tickers,
    manejando de forma segura la estructura de columnas de yfinance.
    """
    print(f"[INFO] Descargando datos para: {tickers} desde {start} hasta {end}...")
    data = yf.download(tickers, start=start, end=end, progress=False)
    
    # Manejo robusto de la estructura de columnas (MultiIndex o plano)
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]
        elif "Close" in data.columns.levels[0]:
            data = data["Close"]
        else:
            raise KeyError("[ERROR] No se encontró 'Adj Close' ni 'Close' en las columnas descargadas.")
    else:
        if "Adj Close" in data.columns:
            data = data["Adj Close"]
        elif "Close" in data.columns:
            data = data["Close"]
        elif len(tickers) == 1:
            pass
        else:
            raise KeyError(f"[ERROR] Columnas disponibles: {list(data.columns)}")

    # Asegurar que sea un DataFrame si hay varios activos
    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers[0])
        
    # Eliminar filas con valores nulos
    data = data.dropna()
    
    if data.empty:
        raise ValueError("[ERROR] El DataFrame descargado está vacío. Verifica tu conexión o los símbolos.")
        
    return data

def calculate_portfolio_statistics(prices: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame, pd.DataFrame]:
    """
    Calcula los retornos logarítmicos diarios, el vector de retornos medios 
    y la matriz de covarianza diaria de los activos.
    """
    log_returns = np.log(prices / prices.shift(1)).dropna()
    mean_daily_returns = log_returns.mean()
    cov_matrix_daily = log_returns.cov()
    
    print("[INFO] Datos y estadísticas financieras calculadas correctamente.")
    return mean_daily_returns, cov_matrix_daily, log_returns