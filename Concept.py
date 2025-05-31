import sys
from collections import defaultdict
from Data import agenten_kategorien, autonomie_quellen
from utils import (
    zeichne_radar,
    bewertungs_prozess,
    create_excel_table,
)


# Agentenname eingeben
agentenname = input("Bitte gib den Namen des erste Agenten ein: ").strip()
agentenname2 = input("Bitte gib den Namen des zweiten Agenten ein: ").strip()

# Name für die die Dateien später
agenten_slug = agentenname.strip().lower().replace(" ", "_")
agenten_slug2 = agentenname.strip().lower().replace(" ", "_")

# Speichert Kriterium mit Bewertungsantwort ab.
kriterien_textantworten = {}
kriterien_textantworten2 = {}

extra_prompts_gesamt = 0
extra_prompts_gesamt2 = 0

# --- Speichert die Bewertungen der sekundären Kriterien ---
sekundäre_kriterien_werte = defaultdict(list)
sekundäre_kriterien_werte2 = defaultdict(list)

# --- Speichert Mittelwerte sowie SonarQube Einträge.
code_kriterien_mittelwerte = {}  # Muss da bleiben
code_kriterien_mittelwerte2 = {}

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
    code_kriterien_mittelwerte,
    autonomie_detail_werte,
)

bewertungs_prozess(
    kriterien_textantworten2,
    extra_prompts_gesamt2,
    agentenname2,
    sekundäre_kriterien_werte2,
    agenten_werte2,
    code_kriterien_mittelwerte2,
    autonomie_detail_werte2,
)


# Radar-Grafiken speichern
# Datei-Namen dynamisch auf Basis des Agentennamens
datei_eigenschaften = f"{agenten_slug}_eigenschaften.png"
datei_autonomie = f"{agenten_slug}_autonomie.png"
datei_sek_kriterien = f"{agenten_slug}_sek_faktoren.png"

# Radar-Grafiken speichern
zeichne_radar(
    f"{agentenname} & {agentenname2} Eigenschaften",
    agenten_kategorien,
    agenten_werte.copy(),
    agenten_werte2.copy(),
    f"{agentenname}",
    f"{agentenname2}",
    datei_eigenschaften,
)
zeichne_radar(
    f"{agentenname} & {agentenname2} Autonomie",
    autonomie_quellen,
    autonomie_detail_werte.copy(),
    autonomie_detail_werte2.copy(),
    f"{agentenname}",
    f"{agentenname2}",
    datei_autonomie,
)
zeichne_radar(
    f"{agentenname} & {agentenname2} sekundäre Kriterien",
    sekundäre_kriterien_werte["kriterium_name"],
    sekundäre_kriterien_werte["werte"],
    sekundäre_kriterien_werte2["werte"],
    f"{agentenname}",
    f"{agentenname2}",
    datei_sek_kriterien,
)

print(
    f"\nRadar-Diagramme wurden gespeichert als '{datei_eigenschaften}' und '{datei_autonomie}' für Agent: {agentenname}"
)
# --- Excel-Datei mit Bewertungstexten erstellen ---
create_excel_table(
    kriterien_textantworten,
    agenten_slug,
    extra_prompts_gesamt,
    code_kriterien_mittelwerte,
    kriterien_textantworten2,
    agenten_slug2,
    extra_prompts_gesamt2,
    code_kriterien_mittelwerte2,
)


print(f"\nkriterien_textantworten: {kriterien_textantworten}")
print(f"\nagenten_slug: {agenten_slug}")
print(f"\nextra_prompts_gesamt: {extra_prompts_gesamt}")
print(f"\ncode_kriterien_mittelwerte: {code_kriterien_mittelwerte}")
print(f"\nagenten_name: {agentenname}")
print(f"\nsekundäre_kriterien_werte: {sekundäre_kriterien_werte}")
print(f"\ndatei_sek_kriterien: {datei_sek_kriterien}")
print(f"\ndatei_autonomie: {datei_autonomie}")
print(f"\nautonomie_detail_werte: {autonomie_detail_werte}")
print(f"\ndatei_eigenschaften: {datei_eigenschaften}")
print(f"\nagenten_werte: {agenten_werte}")

# DIESE MUSS ICH NOCH IN EIN TEST FILE ÜBERFÜHREN, DAMIT ICH DIE SOFTWARE TESTEN KANN
