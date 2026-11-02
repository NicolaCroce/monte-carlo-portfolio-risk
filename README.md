# Monte Carlo Portfolio Risk Engine

Motor cuantitativo modular en Python para la simulación estocástica de portafolios de inversión y estimación de métricas de riesgo regulatorio (**VaR** y **CVaR**).

## Arquitectura del Proyecto
El proyecto sigue principios de desarrollo de software limpio y separación de responsabilidades:
- `config.py`: Centraliza los parámetros globales (activos, ponderaciones, horizonte de riesgo).
- `data_loader.py`: Ingesta automatizada de datos históricos vía `yfinance` y cálculo de retornos logarítmicos.
- `monte_carlo.py`: Motor estocástico que implementa la **descomposición de Cholesky** para simular escenarios correlacionados.
- `risk_metrics.py`: Estimación cuantitativa de *Value at Risk* y *Conditional Value at Risk (Expected Shortfall)*.
- `visualizer.py`: Generación de gráficos ejecutivos de distribución de pérdidas y ganancias.
- `main.py`: Orquestador principal del pipeline.

## Tecnologías Utilizadas
- **Python 3.13**
- `NumPy` & `Pandas` para álgebra lineal y manipulación de series temporales.
- `yFinance` para extracción de datos de mercado.
- `Matplotlib` & `Seaborn` para visualización financiera.

## Cómo Ejecutar
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt