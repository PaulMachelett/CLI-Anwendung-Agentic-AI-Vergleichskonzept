from utils import create_excel_table

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

code_kriterien_mittelwerte = {
    "Anforderungserfüllung": {"category": "Code Kriterium", "score": 0.0},
    "Ausführbarer Code": {"category": "Code Kriterium", "score": 0.0},
    "Code Security": {"category": "Code Kriterium", "score": 2.0},
    "Code Reliability": {"category": "Code Kriterium", "score": 2.0},
    "Code Maintainability": {"category": "Code Kriterium", "score": 2.0},
}

sekundäre_kriterien_werte = {
    "kriterium_name": ["Verständlichkeit", "Preis"],
    "werte": [1.0, 0.5],
}


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

code_kriterien_mittelwerte2 = {
    "Anforderungserfüllung": {"category": "Code Kriterium", "score": 0.0},
    "Ausführbarer Code": {"category": "Code Kriterium", "score": 0.0},
    "Code Security": {"category": "Code Kriterium", "score": 2.0},
    "Code Reliability": {"category": "Code Kriterium", "score": 2.0},
    "Code Maintainability": {"category": "Code Kriterium", "score": 2.0},
}

sekundäre_kriterien_werte2 = {
    "kriterium_name": ["Verständlichkeit", "Preis"],
    "werte": [1.0, 0.5],
}


create_excel_table(
    kriterien_textantworten,
    agenten_slug,
    extra_prompts_gesamt,
    code_kriterien_mittelwerte,
    sekundäre_kriterien_werte,
    kriterien_textantworten2,
    agenten_slug2,
    extra_prompts_gesamt2,
    code_kriterien_mittelwerte2,
    sekundäre_kriterien_werte2,
)
