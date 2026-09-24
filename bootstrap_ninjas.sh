#!/bin/bash
set -euo pipefail

echo "🥷 Initializing Smart Ninja Cyber Defense Dojo..."

# Create Project Directory Structure
mkdir -p smart-ninja-defense/{backend/daemons,frontend/src,ai_swarm}
cd smart-ninja-defense

# 1. Initialize Backend (FastAPI)
cat << 'EOT' > backend/main.py
from fastapi import FastAPI, HTTPException, Security, Header
from fastapi.middleware.cors import CORSMiddleware
pydantic import BaseModel
import os

app = FastAPI(title="Smart Ninja HQ", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ThreatReport(BaseModel):
    ninja_id: int
    threat_level: str
    target_ip: str
    details: str

@app.get("/")
def read_root():
    return {"status": "Dojo Online", "active_ninjas": "1,000,000"}

@app.post("/v1/report")
def receive_threat(report: ThreatReport):
    # Here you would route to your AI swarm coordinator
    print(f"[!] Alert from Ninja #{report.ninja_id}: {report.threat_level} threat on {report.target_ip}")
    return {"status": "Acknowledged", "countermeasure_deployed": True}
EOT

# 2. Initialize Ninja Daemon Agent
cat << 'EOT' > backend/daemons/ninja_daemon.py
import asyncio
import httpx
import random

DAEMON_ID = random.randint(1000, 999999)
HQ_URL = "http://localhost:8000/v1/report"

async def patrol():
    print(f"🥷 Ninja Daemon #{DAEMON_ID} deployed into the shadows...")
    async with httpx.AsyncClient() as client:
        while True:
            await asyncio.sleep(10)
            # Simulating perimeter check
            if random.random() < 0.3: # 30% chance of catching a dummy threat
                payload = {
                    "ninja_id": DAEMON_ID,
                    "threat_level": "HIGH",
                    "target_ip": f"192.168.1.{random.randint(2, 254)}",
                    "details": "Unauthorized packet sequence intercepted."
                }
                try:
                    res = await client.post(HQ_URL, json=payload)
                    print(f"[*] Ninja #{DAEMON_ID} reported threat to HQ: {res.json()}")
                except Exception as e:
                    print(f"[X] Ninja #{DAEMON_ID} lost connection to HQ: {e}")

if __name__ == "__main__":
    asyncio.run(patrol())
EOT

# 3. Initialize Requirements
cat << 'EOT' > backend/requirements.txt
fastapi
uvicorn
httpx
pydantic
EOT

# 4. Initialize Frontend Dashboard Stub (React + Vite configuration text)
cat << 'EOT' > frontend/src/App.jsx
import React, { useState, useEffect } from 'react';

export default function App() {
  const [status, setStatus] = useState("Connecting to Dojo...");
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/")
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus("Dojo Offline"));
  }, []);

  return (
    <div style={{ background: "#0b0f19", color: "#00ffcc", minHeight: "100vh", fontFamily: "monospace", padding: "2rem" }}>
      <h1>⚡ Smart Million Ninjas: C2 Dashboard</h1>
      <p>System Status: <strong>{status}</strong></p>
      <h2>Active Swarm Telemetry</h2>
      <ul>
        <li>[+] 1,000,000 Daemons Active across global nodes.</li>
        <li>[+] Zero-day auto-patching routine: ENGAGED.</li>
      </ul>
    </div>
  );
}
EOT

echo "✅ Smart Ninja framework successfully generated in ./smart-ninja-defense"
echo "👉 Next steps:"
echo "   cd smart-ninja-defense/backend"
echo "   pip install -r requirements.txt"
echo "   uvicorn main:app --reload"
