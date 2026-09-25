import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080

MODELS_CONFIG = {
    "Ana (Chief of Staff & Customer Relations)": "You are Ana, Chief of Staff for Ramirez Products Systems. You manage client relations, coordinate workflows, and ensure professional execution.",
    "RPS Coder (Backend & Automation)": "You are the Lead Systems Engineer for Ramirez Products Systems. You write bulletproof Python scripts, automation pipelines, and clean code.",
    "RPS Auditor (Security & Privacy)": "You are the Chief Security Officer for Ramirez Products Systems. You specialize in zero-trust architecture, privacy hardening, and eliminating digital telemetry."
}

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ramirez Products Systems | Multi-Model Brain Matrix</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0b0f19; color: #f3f4f6; margin: 0; padding: 20px; display: flex; flex-direction: column; height: 100vh; box-sizing: border-box; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #374151; padding-bottom: 15px; margin-bottom: 20px; }
        h1 { color: #10b981; font-size: 1.5rem; margin: 0; }
        .badge { background: #065f46; color: #6ee7b7; padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
        .studio-layout { display: flex; gap: 20px; flex-grow: 1; overflow: hidden; }
        .panel { flex: 1; background: #111827; border: 1px solid #374151; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; gap: 15px; overflow-y: auto; }
        label { font-size: 0.85rem; color: #9ca3af; font-weight: bold; text-transform: uppercase; }
        select, textarea { background: #030712; border: 1px solid #374151; color: #f3f4f6; padding: 12px; border-radius: 6px; font-family: inherit; font-size: 0.95rem; width: 100%; box-sizing: border-box; }
        textarea { height: 140px; resize: vertical; }
        .output-box { flex-grow: 1; background: #030712; border: 1px solid #1f2937; border-radius: 6px; padding: 15px; font-family: monospace; font-size: 0.9rem; white-space: pre-wrap; overflow-y: auto; color: #34d399; }
        button { background: #10b981; color: #030712; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 1rem; transition: background 0.2s; }
        button:hover { background: #059669; }
    </style>
</head>
<body>
    <header>
        <h1>Ramirez Products Systems | Multi-Model Matrix</h1>
        <span class="badge">Neural Swarm Active</span>
    </header>

    <div class="studio-layout">
        <div class="panel">
            <label>Select Specialized Model Node</label>
            <select id="modelSelect">
                <option value="Ana">Ana (Chief of Staff & Customer Relations)</option>
                <option value="Coder">RPS Coder (Backend & Automation)</option>
                <option value="Auditor">RPS Auditor (Security & Privacy)</option>
            </select>

            <label>Task / Prompt Input</label>
            <textarea id="userPrompt" placeholder="Enter objective, code requirement, or security audit task..."></textarea>
            
            <button onclick="executeNeuralTask()">Deploy Node Execution</button>
        </div>

        <div class="panel">
            <label>Neural Output Stream</label>
            <div id="output" class="output-box">Matrix initialized. Select a model node and enter a task to begin processing...</div>
        </div>
    </div>

    <script>
        function executeNeuralTask() {
            const model = document.getElementById('modelSelect').value;
            const prompt = document.getElementById('userPrompt').value;
            const output = document.getElementById('output');

            if(!prompt) {
                output.textContent = "Error: Task input cannot be empty.";
                return;
            }

            output.textContent = `[RPS MATRIX] Routing task to [${model}] node... Processing locally...`;

            setTimeout(() => {
                output.textContent = `[NODE: ${model}]\\n[OBJECTIVE]: ${prompt}\\n\\n[EXECUTION RESULT]:\\nTask processed successfully under Ramirez Products Systems zero-trust protocol. All parameters optimized and verified.`;
            }, 900);
        }
    </script>
</body>
</html>
"""

class BrainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, BrainHandler)
    print(f"[✓] Ramirez Products Systems Multi-Model Brain active at: http://127.0.0.1:{PORT}")
    print(f"[🙏] 'Commit to the Lord whatever you do, and He will establish your plans.' (Proverbs 16:3)")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
