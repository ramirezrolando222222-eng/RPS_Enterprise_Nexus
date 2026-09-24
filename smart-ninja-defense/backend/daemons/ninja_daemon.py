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
