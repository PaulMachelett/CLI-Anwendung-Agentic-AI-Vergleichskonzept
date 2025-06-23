import sys
from collections import defaultdict
from Data import agenten_kategorien, autonomie_quellen, einleitung
from utils import (
    zeichne_balkendiagramm,
    bewertungs_prozess,
    create_excel_table,
)

print(einleitung)

# Agentenname eingeben
agentenname = input("Bitte gib den Namen des erste Agenten ein: ").strip()
agentenname2 = input("Bitte gib den Namen des zweiten Agenten ein: ").strip()

# Name für die die Dateien später
agenten_slug = agentenname.strip().lower().replace(" ", "_")
agenten_slug2 = agentenname2.strip().lower().replace(" ", "_")

# Speichert Kriterium mit Bewertungsantwort ab.
kriterien_textantworten = {}
kriterien_textantworten2 = {}

extra_prompts_gesamt = [0]
extra_prompts_gesamt2 = [0]

# --- Speichert die Bewertungen der sekundären Kriterien ---
sekundäre_kriterien_werte = defaultdict(list)
sekundäre_kriterien_werte2 = defaultdict(list)

agenten_werte = []  # Muss da bleiben
agenten_werte2 = []

autonomie_detail_werte = []  # Muss da bleiben
autonomie_detail_werte2 = []

# # --- Speichert alle Katgorien ohne Duplikate ab ---
# all_categories = set(
#     criterion["category"] for criteria in prompts.values() for criterion in criteria
# )

# # --- Fügt Kategorien aus den immer gefragten Kriterien hinzu ---
# all_categories.update(c["category"] for c in always_asked_criteria)


# Bewertungsprozess
bewertungs_prozess(
    kriterien_textantworten,
    extra_prompts_gesamt,
    agentenname,
    sekundäre_kriterien_werte,
    agenten_werte,
    autonomie_detail_werte,
)

print(
    f"\n\nAnzahl der gesamgten Prompts von Agent {agentenname}: {extra_prompts_gesamt[0]}"
)

bewertungs_prozess(
    kriterien_textantworten2,
    extra_prompts_gesamt2,
    agentenname2,
    sekundäre_kriterien_werte2,
    agenten_werte2,
    autonomie_detail_werte2,
)


# Radar-Grafiken speichern
# Datei-Namen dynamisch auf Basis des Agentennamens
datei_eigenschaften = f"{agenten_slug}_{agenten_slug2}_eigenschaften.png"
datei_autonomie = f"{agenten_slug}_{agenten_slug2}_autonomie.png"
datei_sek_kriterien = f"{agenten_slug}_{agenten_slug2}_sek_faktoren.png"

# Radar-Grafiken speichern
zeichne_balkendiagramm(
    f"{agentenname} & {agentenname2} Eigenschaften",
    agenten_kategorien,
    agenten_werte.copy(),
    agenten_werte2.copy(),
    f"{agentenname}",
    f"{agentenname2}",
    datei_eigenschaften,
)
zeichne_balkendiagramm(
    f"{agentenname} & {agentenname2} Autonomie",
    autonomie_quellen,
    autonomie_detail_werte.copy(),
    autonomie_detail_werte2.copy(),
    f"{agentenname}",
    f"{agentenname2}",
    datei_autonomie,
)
zeichne_balkendiagramm(
    f"{agentenname} & {agentenname2} sekundäre Kriterien",
    sekundäre_kriterien_werte["kriterium_name"][:-2],
    sekundäre_kriterien_werte["werte"][:-2],
    sekundäre_kriterien_werte2["werte"][:-2],
    f"{agentenname}",
    f"{agentenname2}",
    datei_sek_kriterien,
)

print(
    f"\nRadar-Diagramme wurden gespeichert als '{datei_eigenschaften}' und '{datei_autonomie}' für Agent: {agentenname} und {agentenname2}"
)
# --- Excel-Datei mit Bewertungstexten erstellen ---
create_excel_table(
    kriterien_textantworten,
    agenten_slug,
    extra_prompts_gesamt[0],
    sekundäre_kriterien_werte,
    kriterien_textantworten2,
    agenten_slug2,
    extra_prompts_gesamt2[0],
    sekundäre_kriterien_werte2,
)
