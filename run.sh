#!/usr/bin/env bash
set -e

echo "=========================================================="
echo " SYNAPSE HELIOS ID - KLASTER KOGNISI INDONESIA"
echo " Menjalankan Server FastAPI & Antarmuka Cyber-Architectural"
echo "=========================================================="

# Create venv if not exists
if [ ! -d ".venv" ]; then
    echo "[*] Membuat Python Virtual Environment..."
    python3 -m venv .venv
    ./.venv/bin/pip install --upgrade pip
    ./.venv/bin/pip install -r requirements.txt
fi

echo "[*] Menjalankan test suite..."
./.venv/bin/pytest -v

echo "[*] Memulai Uvicorn Server di http://localhost:8000 ..."
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
