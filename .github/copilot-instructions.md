# Copilot Instructions for weather_prod_proj

## Project Overview
- **Purpose:** Compares the accuracy of weather services. Main logic is in `src/`, with supporting scripts in `scripts/` and data in `data/`.
- **Key Components:**
  - `src/`: Main application logic (details not shown, explore for core code).
  - `scripts/`: Utility scripts, e.g., `Supabase_operatoins.py` for database connection.
  - `data/raw/`: Raw data storage.
  - `sql/`: SQL scripts (if any, for DB setup or queries).
  - `assets/`: Static assets (e.g., images, configs).

## Database & External Services
- **Supabase:** Used for data storage. Connection logic in `scripts/Supabase_operatoins.py`.
  - Loads credentials from `.env` (ensure `SUPABASE_URL` and `SUPABASE_KEY` are set).
  - Uses the `supabase` Python client.

## Patterns & Conventions
- **Environment Variables:** Managed via `.env` and `dotenv`.
- **Class-based DB Connection:** See `SupabaseConnection` in `Supabase_operatoins.py` for pattern.
- **Script Execution:**
  - Scripts in `scripts/` are typically run directly (e.g., `python scripts/Supabase_operatoins.py`).
  - Main logic is guarded by `if __name__ == "__main__":`.
- **Error Handling:** Print-based, with clear success/failure messages for DB connection.

## Developer Workflows
- **Setup:**
  - Install dependencies: `pip install -r requirements.txt`
  - Set up `.env` with Supabase credentials.
- **Running Scripts:**
  - Example: `python scripts/Supabase_operatoins.py`
- **Virtual Environment:**
  - Recommended: `.venv/` (activate before running scripts).

## Notable Files
- `scripts/Supabase_operatoins.py`: Example of DB connection and environment loading.
- `README.md`: Project summary (Polish).

## Tips for AI Agents
- Prefer using the class-based pattern for new DB integrations.
- Reference `src/` for main logic and extend there for new features.
- Keep credentials and config in `.env` (never hardcode).
- Use print-based status for script feedback.

---
For more details, explore the `src/` directory and existing scripts. Update this file as new conventions emerge.
