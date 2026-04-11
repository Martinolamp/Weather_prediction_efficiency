# 🌤️ Weather Forecast Accuracy Analyzer

A data engineering project that continuously collects, stores, and compares weather forecast accuracy across **4 major weather API providers** for **Polish cities**.

> **"Which weather service is actually the most accurate?"** — this project answers that question with real data.

---

## 📊 What it does

Every day, the system automatically fetches weather forecasts from 4 providers and stores them in a cloud database. After the forecasted day passes, actual temperatures are compared against what each provider predicted — enabling objective, data-driven accuracy comparison.

### Providers compared

| Label | Provider | Type |
|-------|----------|------|
| A | [Open-Meteo](https://open-meteo.com/) | Free / Open Source |
| B | [WeatherAPI](https://www.weatherapi.com/) | Commercial REST API |
| C | [Meteoblue](https://www.meteoblue.com/) | Commercial REST API |
| D | [Visual Crossing](https://www.visualcrossing.com/) | Commercial REST API |

### Locations tracked

All **Polish voivodeship capitals** + selected cities of interest:
Warszawa, Kraków, Łódź, Wrocław, Poznań, Gdańsk, Szczecin, Bydgoszcz, Lublin, Białystok, Katowice, Rzeszów, Kielce, Olsztyn, Opole, Zielona Góra, Toruń, Karpacz and more.

### Metrics calculated

- **MAE** (Mean Absolute Error) — average temperature prediction error in °C
- **RMSE** (Root Mean Square Error) — penalises larger errors more heavily
- Tracked separately for **max** and **min** daily temperature
- Analysed across **forecast horizons** (1-day ahead vs 5-day ahead accuracy)

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

## 📈 Key Findings (so far)

> Project started: **February 8, 2026** — data collection ongoing.

Early results show notable differences in accuracy between providers, particularly for longer forecast horizons (4-5 days ahead). Short-range forecasts (1 day) show much tighter performance across all providers.

*Dashboard updates automatically as new data is collected.*

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

*Built by [Marcin Papaj](https://github.com/Martinolamp)*
