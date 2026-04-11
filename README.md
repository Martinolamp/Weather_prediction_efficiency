# 🌤️ Weather Forecast Accuracy Analyzer

A data engineering project that continuously collects, stores, and compares weather forecast accuracy across **4 major weather API providers** for **Polish cities**.

> **"Which weather service is actually the most accurate when it comes to temperature prediction?"** — this project answers that question with real data.

---

## 📊 What it does

Every day, the system automatically fetches weather forecasts from 4 providers and stores them in a cloud database. After the forecasted day passes, actual temperatures are compared against what each provider predicted — enabling objective, data-driven accuracy comparison.

### Providers compared

| Label | Provider | Type | Forecast horizon |
|-------|----------|------|-----------------|
| A | [Open-Meteo](https://open-meteo.com/) | Free / Open Source | up to 6 days |
| B | [WeatherAPI](https://www.weatherapi.com/) | Commercial REST API | up to 3 days |
| C | [Meteoblue](https://www.meteoblue.com/) | Commercial REST API | up to 3 days |
| D | [Visual Crossing](https://www.visualcrossing.com/) | Commercial REST API | up to 6 days |

### Locations tracked

All **Polish voivodeship capitals** + selected mountain/resort cities:

Białystok, Bydgoszcz, Gdańsk, Gorzów Wielkopolski, Katowice, Kielce, Kraków, Krynica-Zdrój, Łódź, Lublin, Olsztyn, Opole, Poznań, Rzeszów, Suwałki, Szczecin, Toruń, Ustroń, Warszawa, Wisła, Wrocław, Zakopane, Zieleniec Duszniki, Zielona Góra, Karpacz

### Metrics calculated

- **MAE** (Mean Absolute Error) — average temperature prediction error in °C
- **RMSE** (Root Mean Square Error) — penalises larger errors more heavily
- Tracked separately for **max** and **min** daily temperature
- Analysed across **forecast horizons** (1-day ahead vs 6-day ahead accuracy)

---

## 📸 Dashboard screenshots

### Live temperature readings
Current temperatures across all tracked cities with daily min/max extremes.

![Live readings](./assets/screenshots/live_readings.png)

### Daily extremes
Min/max temperature comparison across all Polish cities.

![Daily extremes](./assets/screenshots/daily_extremes.png)

### Forecast comparison per city
Provider forecasts plotted against each other for selected cities.

![Forecast per city](./assets/screenshots/forecast_karpacz.png)

### Accuracy metrics
MAE and RMSE error trends across forecast horizons for all providers.

![MAE max temp](./assets/screenshots/mae_max_temp.png)
![MAE min temp](./assets/screenshots/mae_min_temp.png)

### Error summary tables
Detailed numerical breakdown of prediction errors per provider and forecast day.

![Error tables](./assets/screenshots/error_tables.png)

---

## 🏗️ Architecture

```
Weather APIs (4 providers)
        │
        ▼
  Python scripts          ← Daily automated data collection
        │
        ▼
  Supabase (PostgreSQL)   ← Cloud database storing forecasts & actuals
        │
        ▼
  Streamlit Dashboard     ← Interactive visualisation & model comparison
```

**Key design decisions:**
- Forecasts stored at collection time → enables retrospective accuracy analysis
- Cloud PostgreSQL (Supabase) → data persists independently of local machine
- Multi-horizon analysis → shows how accuracy degrades with forecast distance
- Actual temperatures collected hourly → precise daily min/max calculation

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Data collection | Python, REST APIs |
| Database | Supabase (PostgreSQL) |
| Data processing | Pandas |
| Dashboard | Streamlit |
| Scheduling | GitHub Actions / cron |

---

## 📈 Early Findings

> Project started: **February 8, 2026** — data collection ongoing.

Based on data collected so far (winter/spring 2026):

### Min temperature accuracy (1-day ahead MAE)
| Provider | MAE (°C) |
|----------|----------|
| **B – WeatherAPI** | **0.7** ✅ best |
| D – Visual Crossing | 1.5 |
| A – Open-Meteo | 2.3 |
| C – Meteoblue | 3.9 |

### Max temperature accuracy (1-day ahead MAE)
| Provider | MAE (°C) |
|----------|----------|
| **D – Visual Crossing** | **1.9** ✅ best |
| B – WeatherAPI | 2.0 |
| A – Open-Meteo | 3.3 |
| C – Meteoblue | 5.1 |

**Key observations:**
- WeatherAPI performs best for **minimum temperature** prediction
- Visual Crossing performs best for **maximum temperature** prediction
- Meteoblue shows the highest error rates across both metrics
- Accuracy degrades predictably with forecast horizon for all providers
- Free provider (Open-Meteo) performs competitively against commercial alternatives

*These findings are based on data from Feb–Apr 2026. Results will be updated as more data is collected.*

---

## 🚀 Running locally

```bash
# Clone the repo
git clone https://github.com/Martinolamp/Weather_prediction_efficiency.git
cd Weather_prediction_efficiency

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (Supabase credentials)
cp .env.example .env
# Edit .env with your Supabase URL and API key

# Run the dashboard
streamlit run Viz/app.py
```

---

## 📁 Project structure

```
Weather_prediction_efficiency/
├── scripts/          # Data collection & processing scripts
├── Viz/              # Streamlit dashboard
├── logs/             # Collection logs
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 💡 Motivation

Weather forecasting accuracy is rarely discussed openly — providers publish marketing claims but independent comparisons are hard to find. This project collects ground-truth data to answer the question objectively, using standard error metrics from data science (MAE, RMSE).

The project also serves as a practical exercise in building an **end-to-end data pipeline**: API integration → cloud storage → automated processing → interactive dashboard.

---

*Built by [Marthino](https://github.com/Martinolamp)*
