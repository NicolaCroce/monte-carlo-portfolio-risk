# 📈 Quantitative Risk Engine: Multi-Asset Monte Carlo & CVaR Simulation

## Overview
Modular Python quantitative risk engine designed for market risk analysis, portfolio simulation, and regulatory metrics estimation (**VaR** and **CVaR**) following institutional engineering standards.

## Key Features & Regulatory Alignment
* **Regulatory Horizon**: Calibrated to a **10-day holding period**, matching international market risk standards (**Basel III / FRTB**).
* **Confidence Level**: Implements a strict **99% confidence level** (1% left-tail risk) for extreme stress testing and capital adequacy.
* **Advanced Analytics**: Computes both **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR / Expected Shortfall)** to capture tail-risk severity.
* **Stochastic Modeling**: Employs **Cholesky Decomposition** on historical covariance matrices to simulate realistic cross-asset correlations.

## Project Architecture
* `config.py`: Centralizes global parameters (tickers, portfolio weights, time horizon, confidence levels).
* `data_loader.py`: Automated historical data ingestion via `yfinance` and log-returns computation.
* `monte_carlo.py`: Stochastic engine for multivariate correlated asset simulation and portfolio aggregation.
* `risk_metrics.py`: Quantitative estimation of VaR and Expected Shortfall.
* `visualizer.py`: Executive risk distribution plots highlighting regulatory thresholds.
* `main.py`: Main pipeline orchestrator.

## Tech Stack
* **Python 3.13**
* `NumPy` & `Pandas`: Vectorized matrix operations and high-performance financial data manipulation.
* `yFinance`: Automated market data extraction.
* `Matplotlib` & `Seaborn`: Executive risk density visualization.

## Quickstart
1. Clone the repository:
   ```bash
   git clone https://github.com/NicolaCroce/monte-carlo-portfolio-risk.git
   cd monte-carlo-portfolio-risk
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the risk engine:
   ```bash
   python main.py
   ```
# 📈 Motor de Riesgo Cuantitativo: Simulación Monte Carlo Multiactivo y CVaR

## Descripción General

Motor cuantitativo modular en Python diseñado para el análisis de riesgo de mercado, simulación de portafolios y estimación de métricas de riesgo regulatorio (**VaR** y **CVaR**) bajo estándares de ingeniería financiera institucional.

## Características Clave y Alineación Regulatoria

* **Horizonte Regulatorio**: Calibrado a un período de **10 días hábiles**, cumpliendo con los estándares internacionales de riesgo de mercado (**Basilea III / FRTB**).

* **Nivel de Confianza**: Implementa un nivel de confianza estricto del **99%** (riesgo de cola del 1%) para pruebas de estrés severo y suficiencia de capital.

* **Analítica Avanzada**: Calcula tanto el **Value at Risk (VaR)** como el **Conditional Value at Risk (CVaR / Expected Shortfall)** para capturar la severidad del riesgo de cola.

* **Modelación Estocástica**: Emplea **Descomposición de Cholesky** sobre matrices de covarianza históricas para simular correlaciones realistas entre activos.

## Arquitectura del Proyecto

* `config.py`: Centraliza los parámetros globales (activos, ponderaciones, horizonte temporal, niveles de confianza).

* `data_loader.py`: Ingesta automatizada de datos históricos vía `yfinance` y cálculo de retornos logarítmicos.

* `monte_carlo.py`: Motor estocástico para simulación de activos correlacionados y agregación de portafolio.

* `risk_metrics.py`: Estimación cuantitativa de VaR y Expected Shortfall.

* `visualizer.py`: Gráficos ejecutivos de distribución de riesgos destacando umbrales regulatorios.

* `main.py`: Orquestador principal del pipeline.

## Tecnologías Utilizadas

* **Python 3.13**

* `NumPy` & `Pandas`: Operaciones matriciales vectorizadas y manipulación avanzada de series temporales financieras.

* `yFinance`: Extracción automatizada de datos de mercado.

* `Matplotlib` & `Seaborn`: Visualización ejecutiva de densidades de riesgo.

## Cómo Ejecutar

1. Clonar el repositorio:

   ```
   git clone https://github.com/NicolaCroce/monte-carlo-portfolio-risk.git
   cd monte-carlo-portfolio-risk
   ```

2. Instalar dependencias:

   ```
   pip install -r requirements.txt
   ```

3. Ejecutar el motor de riesgo:

   ```
   python main.py
   ```