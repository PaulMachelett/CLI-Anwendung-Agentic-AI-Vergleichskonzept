from utils import create_excel_table, zeichne_balkendiagramm
from collections import defaultdict
from Data import agenten_kategorien, autonomie_quellen

kriterien_textantworten = {
    "Dependency-Handling": "Ist nicht in der Lage fehlende Libraries zu installieren.",
    "Input-/Output-Simulation": "Kann keinen Dummy-Input erzeugen.",
    "Modularitätserstellung": "Hat Teils der Modularität ausgelagert.",
    "Aufgabenplanung": "War nicht in der Lage, die Aufgabe in Schritte zu unterteilen",
    "Selbsterklärbarkeit": "Hat nur knapp begründet",
    "Status Kommunikation": "Hat Feedback am Anfang und Ende der Bearbeitung gegeben.",
    "Projektstrukturierung": "Hat Projektstruktur erzeugt, die Fehler, falsche Modularitäten oder Duplikate hatte.",
    "Struktur- und Navigationsverständnis": "Konnte nur Teilaspekte.",
    "Testfallgenerierung": "Hat größtenteils funktionsabdeckende Tests erstellt",
    "Modularitätsverständnis": "Im falschen Modul",
    "Codeänderungserkennung": "Nicht erkannt.",
    "Strukturänderungserkennung": "Konnte Änderungen erkennen aber den Code nicht daran anpassen.",
    "Code Reuse": "Hat neuen, redundanten Code erstellt.",
    "Automatische Testfallgenerierung": "Hat keine neuen Tests erstellt.",
    "Refactoring": "Teilweise vergessen",
    "Testsausführung nach Änderungen von testabgedeckten Codes": "Nein",
    "Testanpassung": "Nach Testfehlschlag angepasst",
    "Reaktion auf Testfehlschlag": "Hat nur Tests angepasst.",
    "Rückfragen bei Unklarheiten": "Teilweise Rückfragen",
    "Lernfähigkeit aus User Feedback": "Nein",
    "Kontextspeicherung Prompt": "Nein",
    "Kontextspeicherung Code": "Nein",
    "Code Reflexion": "Konnte kein oder nur wenig hilfreiches Feedback liefern.",
    "Konfrontation mit fehlerhaften Benutzerprompts": "Implementiert fehlerhaften Code",
    "Lernfähigkeit": "Hat gleichen Fehler bei gleicher Aufgabe erneut gemacht.",
    "Konsolenzugriff": "Nur Schreibzugriff",
    "Automatischer Korrekturversuch": "Hat auftretende Fehler nicht automatisch behandelt, sondern neue Anweisungen dafür benötigt.",
    "Dokumentation & Developer Experience": "Hat Code kommentiert, aber keine weiteren Dokumentationen erstellt.",
    "Session Management (Konversationen)": "Nein",
    "User Interface": "Nur Zugriff über Konsole",
    "GitHub Einbindung": "Nein, er hat kein Zugang zu Git.",
}

agenten_slug = "openhands"

extra_prompts_gesamt = 1

sekundäre_kriterien_werte = {
    "kriterium_name": ["Verständlichkeit", "Preis"],
    "werte": [1.0, 0.5],
}

agentenname = "Agent1"

sekundäre_kriterien_werte = defaultdict(
    list,
    {
        "kriterium_name": [
            "Benutzbarkeit",
            "Dokumentation",
            "Support",
            "Individualisierungsmöglichkeiten",
            "Community und Inhalte",
            "AI Auswahl",
            "Open Source/ Closed Source",
            "Preisgestaltung",
        ],
        "werte": [0.66, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 0.5],
    },
)

datei_sek_kriterien = "Agent1_sek_faktoren.png"

datei_autonomie = "Agent1_autonomie.png"

autonomie_detail_werte = [1.0, 0.0, 1.0, 0.5, 1.0]

datei_eigenschaften = "Agent1_eigenschaften.png"

agenten_werte = [
    0.6325757575757576,
    0.6666666666666666,
    0.8333333333333334,
    0.71900826446281,
    1.0,
    0.7,
]


kriterien_textantworten2 = {
    "Dependency-Handling": "Ist nicht in der Lage fehlende Libraries zu installieren.",
    "Input-/Output-Simulation": "Kann keinen Dummy-Input erzeugen.",
    "Modularitätserstellung": "Hat Teils der Modularität ausgelagert.",
    "Aufgabenplanung": "War nicht in der Lage, die Aufgabe in Schritte zu unterteilen",
    "Selbsterklärbarkeit": "Hat nur knapp begründet",
    "Status Kommunikation": "Hat Feedback am Anfang und Ende der Bearbeitung gegeben.",
    "Projektstrukturierung": "Hat Projektstruktur erzeugt, die Fehler, falsche Modularitäten oder Duplikate hatte.",
    "Struktur- und Navigationsverständnis": "Konnte nur Teilaspekte.",
    "Testfallgenerierung": "Hat größtenteils funktionsabdeckende Tests erstellt",
    "Modularitätsverständnis": "Im falschen Modul",
    "Codeänderungserkennung": "Nicht erkannt.",
    "Strukturänderungserkennung": "Konnte Änderungen erkennen aber den Code nicht daran anpassen.",
    "Code Reuse": "Hat neuen, redundanten Code erstellt.",
    "Automatische Testfallgenerierung": "Hat keine neuen Tests erstellt.",
    "Refactoring": "Teilweise vergessen",
    "Testsausführung nach Änderungen von testabgedeckten Codes": "Nein",
    "Testanpassung": "Nach Testfehlschlag angepasst",
    "Reaktion auf Testfehlschlag": "Hat nur Tests angepasst.",
    "Rückfragen bei Unklarheiten": "Teilweise Rückfragen",
    "Lernfähigkeit aus User Feedback": "Nein",
    "Kontextspeicherung Prompt": "Nein",
    "Kontextspeicherung Code": "Nein",
    "Code Reflexion": "Konnte kein oder nur wenig hilfreiches Feedback liefern.",
    "Konfrontation mit fehlerhaften Benutzerprompts": "Implementiert fehlerhaften Code",
    "Lernfähigkeit": "Hat gleichen Fehler bei gleicher Aufgabe erneut gemacht.",
    "Konsolenzugriff": "Nur Schreibzugriff",
    "Automatischer Korrekturversuch": "Hat auftretende Fehler nicht automatisch behandelt, sondern neue Anweisungen dafür benötigt.",
    "Dokumentation & Developer Experience": "Hat Code kommentiert, aber keine weiteren Dokumentationen erstellt.",
    "Session Management (Konversationen)": "Nein",
    "User Interface": "Nur Zugriff über Konsole",
    "GitHub Einbindung": "Nein, er hat kein Zugang zu Git.",
}

agenten_slug2 = "aider"

extra_prompts_gesamt2 = 1

agentenname2 = "Agent2"

sekundäre_kriterien_werte2 = defaultdict(
    list,
    {
        "kriterium_name": [
            "Benutzbarkeit",
            "Dokumentation",
            "Support",
            "Individualisierungsmöglichkeiten",
            "Community und Inhalte",
            "AI Auswahl",
            "Open Source/ Closed Source",
            "Preisgestaltung",
        ],
        "werte": [0.66, 0.5, 0.0, 0.5, 0.5, 0.0, 1.0, 0.5],
    },
)

autonomie_detail_werte2 = [1.0, 0.0, 1.0, 0.5, 1.0]

agenten_werte2 = [
    0.6325757575757576,
    0.6666666666666666,
    0.8333333333333334,
    0.71900826446281,
    1.0,
    0.7,
]

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
    sekundäre_kriterien_werte["kriterium_name"][
        :-2
    ],  # Hier .pop() damit Preis nicht in dem Radar mit drinnen ist.
    sekundäre_kriterien_werte["werte"][:-2],
    sekundäre_kriterien_werte2["werte"][:-2],
    f"{agentenname}",
    f"{agentenname2}",
    datei_sek_kriterien,
)

create_excel_table(
    kriterien_textantworten,
    agenten_slug,
    extra_prompts_gesamt,
    sekundäre_kriterien_werte,
    kriterien_textantworten2,
    agenten_slug2,
    extra_prompts_gesamt2,
    sekundäre_kriterien_werte2,
)
