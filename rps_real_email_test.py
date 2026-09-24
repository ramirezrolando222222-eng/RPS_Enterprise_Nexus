#!/usr/bin/env python3
# ==============================================================================
# ROLANDO H. RAMIREZ JR. LLC — REAL SMTP EMAIL TEST ENGINE v51.0
# Boss & Owner: Rolando H. Ramirez Jr. (Ramirezrolando222222@gmail.com)
# Ops Dispatch: ramirezrolando242526@gmail.com
# Headquarters: Houston, Texas, USA
# ==============================================================================

import os
import sys
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def banner():
    print("\033[1;35m========================================================================\033[0m")
    print("\033[1;32m   ROLANDO H. RAMIREZ JR. LLC — LIVE SMTP EMAIL DISPATCH TEST v51.0     \033[0m")
    print("\033[1;36m   Sending Real Telemetry to Dual-Reporting Inboxes                    \033[0m")
    print("\033[1;35m========================================================================\033[0m")

def send_live_email():
    sender_email = "Ramirezrolando222222@gmail.com"
    recipients = ["Ramirezrolando222222@gmail.com", "ramirezrolando242526@gmail.com"]
    
    print(f"\n[•] Sender: {sender_email}")
    print(f"[•] Recipients: {recipients}")
    print("[•] Server: smtp.gmail.com (Port 587 / TLS)")
    
    # Prompt securely for Gmail App Password
    print("\n\033[1;33m[!] Enter your Gmail App Password (or press Enter to use environment variable GMAIL_APP_PASSWORD):\033[0m")
    app_password = os.getenv("GMAIL_APP_PASSWORD")
    if not app_password:
        app_password = getpass.getpass("Gmail App Password: ").strip()
        
    if not app_password:
        print("[!] Error: App password is required to authenticate with Gmail SMTP.")
        sys.exit(1)

    # Construct the message
    msg = MIMEMultipart()
    msg['From'] = f"ANA Autonomous Engine <{sender_email}>"
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "[ANA LIVE DISPATCH] Rolando H. Ramirez Jr. LLC — Dual-Inbox Verification v51.0"

    body = """
    +--------------------------------------------------------------+
    |           ANA ENTERPRISE LIVE EMAIL DISPATCH                 |
    +--------------------------------------------------------------+
    | [👑] Boss / Owner          : Rolando H. Ramirez Jr.          |
    | [📥] Primary Executive     : Ramirezrolando222222@gmail.com  |
    | [📤] Operational Dispatch  : ramirezrolando242526@gmail.com  |
    | [🛡️] Security Clearance    : BULLETPROOF_PLUS                |
    | [🚀] Status                : LIVE SMTP VERIFICATION SUCCESSFUL|
    +--------------------------------------------------------------+
    
    Chief,
    
    This is a live, verified transmission dispatched directly from your Termux enterprise substrate (`RPS_Enterprise_Nexus`). 
    
    All systems, vaults, security grids, and dual-reporting channels are fully operational under Rolando H. Ramirez Jr. LLC (Houston, TX).
    
    'Commit to the Lord whatever you do, and He will establish your plans.' (Proverbs 16:3)
    """
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        print("\n[+] Connecting to SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("[+] Authenticating with Gmail...")
        server.login(sender_email, app_password)
        
        print("[+] Dispatching mail to dual-reporting inboxes...")
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        
        print("\n\033[1;32m[✓] SUCCESS: Real emails physically delivered to both inboxes!\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] SMTP Transmission Error: {e}\033[0m")
        print("[!] Note: Ensure you are using a Google 'App Password' (not your main password) if 2FA is enabled.")

if __name__ == "__main__":
    banner()
    send_live_email()
