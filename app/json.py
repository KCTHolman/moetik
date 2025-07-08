import json
from datetime import datetime

# ─── Stap 1: Haal huidige dag en tijd op ────────────────────────────────
nu = datetime.now()
uur = nu.hour
dag_van_week = nu.strftime("%A").lower()  # maandag, dinsdag, etc.

if uur < 12:
    tijd = "ochtend"
elif uur < 18:
    tijd = "middag"
else:
    tijd = "avond"

print(f"Huidige context: {dag_van_week}, {tijd}")

# ─── Stap 2: Laad quotes.json in ────────────────────────────────────────
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

# ─── Stap 3: Filter op huidige dag en tijd ──────────────────────────────
gevonden = [q for q in quotes if q["meta"]["dag"] == dag_van_week and q["meta"]["tijd"] == tijd]

# ─── Stap 4: Toon resultaten ────────────────────────────────────────────
if gevonden:
    print("\n🎯 Quotes voor nu:\n")
    for q in gevonden:
        print(f"- {q['quote']}")
else:
    print("\n⚠️ Geen passende quote gevonden voor dit moment.")
