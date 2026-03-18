# UI Automation Level 2 — Selenium + Python

## Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

## Run locally (no Grid)

```bash
set EXECUTION_MODE=local
pytest -v
```

## Run on Selenium Grid (3 nodes)

```bash
docker-compose up -d
ping -n 30 127.0.0.1 > nul
pytest -n 3 --dist=loadscope --alluredir=reports/allure-results --junitxml=reports/junit.xml -v
docker-compose down
```

## Allure report

```bash
allure serve reports/allure-results
```

## Environment variables (optional overrides)

| Variable | Default |
|---|---|
| BASE_URL | https://react-frontend-api-testing.vercel.app |
| BROWSER | chrome |
| HEADLESS | false |
| EXECUTION_MODE | remote |
| GRID_URL | http://127.0.0.1:4444/wd/hub |
| ADMIN_EMAIL | admin@example.com |
| ADMIN_PASSWORD | Admin@123 |
