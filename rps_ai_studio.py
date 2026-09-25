import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 8080

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RPS AI Studio | Sovereign Model & Prompt Playground</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0b0f19; color: #f3f4f6; margin: 0; padding: 20px; display: flex; flex-direction: column; height: 100vh; box-sizing: border-box; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #374151; padding-bottom: 15px; margin-bottom: 20px; }
        h1 { color: #10b981; font-size: 1.5rem; margin: 0; }
        .badge { background: #065f46; color: #6ee7b7; padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
        .studio-layout { display: flex; gap: 20px; flex-grow: 1; overflow: hidden; }
        .panel { flex: 1; background: #111827; border: 1px solid #374151; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; gap: 15px; overflow-y: auto; }
        label { font-size: 0.85rem; color: #9ca3af; font-weight: bold; text-transform: uppercase; }
        textarea, select { background: #030712; border: 1px solid #374151; color: #f3f4f6; padding: 12px; border-radius: 6px; font-family: inherit; font-size: 0.95rem; width: 100%; box-sizing: border-box; resize: vertical; }
        textarea { height: 120px; }
        .output-box { flex-grow: 1; background: #030712; border: 1px solid #1f2937; border-radius: 6px; padding: 15px; font-family: monospace; font-size: 0.9rem; white-space: pre-wrap; overflow-y: auto; color: #34d399; }
        button { background: #10b981; color: #030712; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 1rem; transition: background 0.2s; }
        button:hover { background: #059669; }
    </style>
</head>
<body>
    <header>
        <h1>Ramirez Products Systems | AI Studio</h1>
        <span class="badge">Sovereign Playground v1.0</span>
    </header>

    <div class="studio-layout">
        <div class="panel">
            <label>System Instructions</label>
            <textarea id="sysPrompt">You are Ana, Chief of Staff for Ramirez Products Systems. You assist Rolando H. Ramirez Jr. with secure coding, automation, and enterprise execution.</textarea>
            
            <label>User Prompt / Task</label>
            <textarea id="userPrompt" style="height: 150px;" placeholder="Enter your prompt, code request, or automation task here..."></textarea>
            
            <button onclick="runStudioTask()">Execute Generation</button>
        </div>

        <div class="panel">
            <label>Neural Output Stream</label>
            <div id="output" class="output-box">Ready for execution, Chief. Configure instructions and prompt on the left to begin...</div>
        </div>
    </div>

    <script>
        function runStudioTask() {
            const sys = document.getElementById('sysPrompt').value;
            const prompt = document.getElementById('userPrompt').value;
            const output = document.getElementById('output');

            if(!prompt) {
                output.textContent = "Error: Please enter a prompt.";
                return;
            }

            output.textContent = "Processing neural transmission locally...";

            // Simulated studio response execution (can be wired directly to OpenRouter API bridge)
            setTimeout(() => {
                output.textContent = `[RPS AI STUDIO EXECUTION LOG]\\nSystem: ${sys}\\nPrompt: ${prompt}\\n\\n[RESULT]:\\nTask processed successfully under Ramirez Products Systems sovereign parameters. All systems operational.`;
            }, 1000);
        }
    </script>
</body>
</html>
"""

class StudioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, StudioHandler)
    print(f"[✓] RPS AI Studio running locally at: http://127.0.0.1:{PORT}")
    print(f"[🙏] 'Commit to the Lord whatever you do, and He will establish your plans.' (Proverbs 16:3)")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
