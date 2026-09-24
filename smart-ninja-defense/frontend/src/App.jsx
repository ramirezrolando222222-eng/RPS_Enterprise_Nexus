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
