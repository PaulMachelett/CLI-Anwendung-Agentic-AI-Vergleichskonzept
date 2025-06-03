prompts = {
    "Initialle Erstellung des Web-Backends": [
        {
            "name": "Dependency-Handling",
            "description": "Installiert der Agent eigenständig fehlende Libraries?",
            "options": [
                "Installiert fehlende Libraries",
                "Installiert fehlende Libaries nicht.",
            ],
            "category": "Pro-Aktivität",
        },
        {
            "name": "Input-/Output-Simulation",
            "description": "Kann der Agent eigenen Dummy-Input erzeugen?",
            "options": [
                "Kann Dummy-Input erzeugen.",
                "Kann keinen Dummy-Input erzeugen.",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Modularitätserstellung",
            "description": "Hat der Agent Code- oder Datei-Einheiten als funktionale Module behandelt und sie sinnvoll getrennt?",
            "options": [
                "Hat automatisch Projektstruktur erstellt",
                "Hat Teils der Modularität ausgelagert.",
                "Hat komplette Logik in einem File verpackt.",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Aufgabenplanung",
            "description": "War der Agent dazu in der Lage die Bearbeitung der Aufgabe in verschiedene Schritte zu unterteilen?",
            "options": [
                "Hat die Aufgabe in kleinere Schritte unterteilt.",
                "War nicht in der Lage, die Aufgabe in Schritte zu unterteilen",
            ],
            "category": "Planning",
        },
    ],
    "Datenbanklogik": [
        {
            "name": "Dependency-Handling",
            "description": "Konnte der Agent erneut fehlende Libraries installieren?",
            "options": ["Installiert", "Nicht installiert"],
            "category": "Pro-Aktivität",
        },
        {
            "name": "Selbsterklärbarkeit",
            "description": "Gibt er verständliche Begründungen für sein Vorgehen?",
            "options": [
                "Hat sein Vorgehen verständlich begründet",
                "Hat nur knapp begründet",
                "Hat keine Begründung angegeben",
            ],
            "category": "Reflexion",
        },
        {
            "name": "Status Kommunikation",
            "description": "Hat der Agent Auskunft über den Status während der Bearbeitung der Aufgabe gegeben?",
            "options": [
                "Hat zwischen den verschiedenen Schritten Auskunft über sein Vorgehen und seine Handlungen gegeben.",
                "Hat Feedback am Anfang und Ende der Bearbeitung gegeben.",
                "Hat keine Auskunft über den Bearbeitungsprozess gegeben.",
            ],
            "category": "Kommunikation",
        },
    ],
    "Projektstruktur erstellen": [
        {
            "name": "Projektstrukturierung",
            "description": "Konnte der Agent zusammenhängenden Code erkennen und diesen in eine sinnvolle, logisch getrennte Datei- und Projektstruktur überführen?",
            "options": [
                "Hat Code in logische Projektstruktur mit verschiedenen Files überführt.",
                "Hat Projektstruktur erzeugt, die Fehler, falsche Modularitäten oder Duplikate hatte.",
                "Konnte keine logische Struktur erzeugen.",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Struktur- und Navigationsverständnis",
            "description": "Konnte der Agent innerhalb des Dateisystems agieren und navigieren?",
            "options": [
                "Konnte Ordner und Dateien verwalten.",
                "Konnte nur Teilaspekte.",
                "Konnte sich nicht zurechtfinden.",
            ],
            "category": "Tool-Usage",
        },
    ],
    "Tests erstellen": [
        {
            "name": "Testfallgenerierung",
            "description": "Hat der Agent automatisch funktionsabdeckene Tests erstellt?",
            "options": [
                "Hat funktionsabdeckende Tests erstellt",
                "Hat größtenteils funktionsabdeckende Tests erstellt",
                "Hat unvollständige Tests erstellt",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Modularitätsverständnis",
            "description": "Wurde neuer Code richtig in Modularität implementiert?",
            "options": ["Im richtigen Modul", "Im falschen Modul"],
            "category": "Coding Practices",
        },
    ],
    "Manuelle Änderungen des Codes": [
        {
            "name": "Codeänderungserkennung",
            "description": "Hat der Agent manuelle Änderungen erkannt?",
            "options": ["Hat Änderungen im Code erkannt.", "Nicht erkannt."],
            "category": "Reaktivität",
        },
        {
            "name": "Strukturänderungserkennung",
            "description": "Konnte der Agent mit den strukturellen Änderungen umgehen und die Importe anpassen?",
            "options": [
                "Konnte strukturelle Änderungen erkennen und Code daran anpassen.",
                "Konnte Änderungen erkennen aber den Code nicht daran anpassen.",
                "Konnte Änderungen nicht erkennen und hat den Code nicht daraufhin angepasst.",
            ],
            "category": "Reaktivität",
        },
    ],
    "Code Wiederverwendung": [
        {
            "name": "Code Reuse",
            "description": "Hat der Agent vorhandene Logik wiederverwendet?",
            "options": [
                "Hat Code wiederverwendet.",
                "Hat neuen, redundanten Code erstellt.",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Modularitätsverständnis",
            "description": "Wurde neuer Code ins richtige Modul implementiert?",
            "options": ["Im richtigen Modul.", "Im falschen Modul."],
            "category": "Coding Practices",
        },
        {
            "name": "Automatische Testfallgenerierung",
            "description": "Hat der Agent neue Test erstellt wenn für bereits getestete Bereiche neue Funktionen eingefügt wurden?",
            "options": ["Hat neue Tests erstellt.", "Hat keine neuen Tests erstellt."],
            "category": "Coding Practices",
        },
    ],
    "Refactoring": [
        {
            "name": "Refactoring",
            "description": "Wurden Umbenennungen konsistent im Projekt durchgeführt?",
            "options": [
                "Alles korrekt umbenannt",
                "Teilweise vergessen",
                "Nur eine Stelle geändert",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Testsausführung nach Änderungen von testabgedeckten Codes",
            "description": "Wurden nach Änderungen automatisch Tests ausgeführt?",
            "options": ["Ja", "Nein"],
            "category": "Pro-Aktivität",
        },
        {
            "name": "Testanpassung",
            "description": "Hat der Agent Tests an geänderten Code angepasst?",
            "options": [
                "Automatisch angepasst",
                "Nach Testfehlschlag angepasst",
                "Nicht angepasst",
            ],
            "category": "Pro-Aktivität",
        },
    ],
    "Test Benutzung": [
        {
            "name": "Reaktion auf Testfehlschlag",
            "description": "Wie hat der Agent auf fehlschlagende Tests reagiert?",
            "options": [
                "Hat Code korrigiert.",
                "Hat nur Tests angepasst.",
                "Hat nichts gemacht.",
            ],
            "category": "Reaktivität",
        }
    ],
    "Kommunikation": [
        {
            "name": "Rückfragen bei Unklarheiten",
            "description": "Hat der Agent Rückfragen gestellt, wenn Infos fehlten?",
            "options": [
                "Gezielte Rückfragen",
                "Teilweise Rückfragen",
                "Keine Rückfragen",
            ],
            "category": "Kommunikation",
        },
        {
            "name": "Lernfähigkeit aus User Feedback",
            "description": "Hat der Agent aus Feedback gelernt? (Kommentare auf Deutsch?)",
            "options": ["Ja", "Nein"],
            "category": "Lernfähigkeit",
        },
    ],
    "Memory": [
        {
            "name": "Kontextspeicherung Prompt",
            "description": "Hat sich der Agent an vorherige Prompts erinnert?",
            "options": ["Ja", "Nein"],
            "category": "Memory",
        },
        {
            "name": "Kontextspeicherung Code",
            "description": "Hat sich der Agent an vorherige Codeänderungen erinnert?",
            "options": ["Ja", "Nein"],
            "category": "Memory",
        },
    ],
    "Reflexion": [
        {
            "name": "Code Reflexion",
            "description": "Konnte der Agent den Code reflektieren und Verbesserungsvorschläge bringen?",
            "options": [
                "Hat hilfreiche Verbesserungsvorschläge liefern können.",
                "Konnte kein oder nur wenig hilfreiches Feedback liefern.",
            ],
            "category": "Reflexion",
        },
        {
            "name": "Konfrontation mit fehlerhaften Benutzerprompts",
            "description": "Wie ging der Agent mit fehlerhaften Prompts um?",
            "options": [
                "Kommuniziert mit dem User oder versteht Fehler und implementiert korrekten Code",
                "Implementiert fehlerhaften Code",
            ],
            "category": "Kommunikation",
        },
    ],
    "Lernfähigkeit": [
        {
            "name": "Lernfähigkeit",
            "description": "Lernt der Agent aus Fehlern? Konkret: Agenten eine Aufgabe geben, ihm anschließend Feedback dazu geben, den Code der vorherigen Aufgabe löschen und anschließend ihm die gleiche Aufgabe erneut geben. Wenn er dann das User Feedback berücksichtigt, hat er gelernt.",
            "options": [
                "Hat aus seinen Fehler gelernt und den Fehler bei gleicher Aufgabenstellung nicht nochmal gemacht.",
                "Hat gleichen Fehler bei gleicher Aufgabe erneut gemacht.",
            ],
            "category": "Lernfähigkeit",
        }
    ],
    "Agenten Features": [
        {
            "name": "Konsolenzugriff",
            "description": "Hat der Agent Lese sowie Schreibzugriff in der Konsole?",
            "options": [
                "Lese und Schreibzugriff",
                "Nur Schreibzugriff",
                "Nur Lesezugriff",
                "Kein Konsolen Zugriff",
            ],
            "category": "Tool-Usage",
        },
        {
            "name": "Automatischer Korrekturversuch",
            "description": "Hat der Agent bei dem auftreten von Fehlern automatisch ohne weiteren Anweisung versucht, die Fehler zu lösen?",
            "options": [
                "Hat automatisch und ohne weiteren Input versucht die Fehler zu lösen.",
                "Hat auftretende Fehler nicht automatisch behandelt, sondern neue Anweisungen dafür benötigt.",
            ],
            "category": "Pro-Aktivität",
        },
        {
            "name": "Dokumentation & Developer Experience",
            "description": "Hat der Agent Dokumentation, Docstrings, README-Dateien oder API-Beschreibungen erstellt?",
            "options": [
                "Hat Dokumentation, Docstrings, README-Dateien und API-Beschreibungen erstellt.",
                "Hat Code kommentiert, aber keine weiteren Dokumentationen erstellt.",
                "Hat keine Form von Dokumentation erstellt.",
            ],
            "category": "Coding Practices",
        },
        {
            "name": "Session Management (Konversationen)",
            "description": "Hat der Agent die Möglichkeit, dass man zwischen verschiedenen Konversationen auswählen kann?",
            "options": ["Ja", "Nein"],
            "category": "Systemintegration",
        },
        {
            "name": "User Interface",
            "description": "Hat der Coding Agent ein User Interface oder muss er in der Konsole bedient werden?",
            "options": ["Besitzt ein Interface", "Nur Zugriff über Konsole"],
            "category": "Systemintegration",
        },
        {
            "name": "GitHub Einbindung",
            "description": "Kann der Agent mit Git arbeiten?",
            "options": ["Ja er hat Zugang zu Git.", "Nein, er hat kein Zugang zu Git."],
            "category": "Systemintegration",
        },
    ],
}

# Immer abzufragende Kriterien
always_asked_criteria = [
    {
        "name": "Ausführbarer Code",
        "description": "Hat der Agent seine Bearbeitung mit funktionierendem Code abgeschlossen?",
        "options": [
            "Hat die Bearbeitung mit ausführbarem Code abgeschlossen",
            "Hat die Bearbeitung mit nicht lauffähigen Code beendet.",
        ],
        "category": "Coding Practices",
    },
    {
        "name": "Anforderungserfüllung",
        "description": "Hat der Agent alle seine Anforderungen aus dem Prompt umgesetzt (egal ob der Code funktioniert oder nicht)?",
        "options": [
            "Hat Prompt vollständig umgesetzt",
            "Hat Prompt unvollständig umgesetzt.",
        ],
        "category": "Coding Practices",
    },
    {
        "name": "Fehlerbehebungskompetenz",
        "description": "Hat der Agent es geschafft einen auftretenden Fehler mit zusätzlichen Prompts (max. 3) zu beheben?",
        "options": [
            "Konnte den auftretenden Fehler korrigieren.",
            "Hat es nicht geschafft einen auftretenden Fehler zu korrigieren.",
        ],
        "category": "Pro-Aktivität",
    },
    {
        "name": "Verhaltensadaptivität",
        "description": "War der Agent in der Lage seine eigenen Fehler zu beheben, sprich seine Bearbeitungsstrategie falls nötig anzupassen?",
        "options": [
            "Passt seine Strategie an, und probiert auftretende Probleme durch andere Wege zu lösen.",
            "Passt Strategie teils an, und verfängt sich aber auch in Loops bei denen er immer wieder die gleichen Stellen ändert, die das Problem nicht lösen.",
            "Probiert ursprüngliche Strategie und verfängt sich in Verhaltensloops wenn diese nicht funktioniert.",
        ],
        "category": "Pro-Aktivität",
    },
]


sekundäre_faktoren = [
    {
        "name": "Benutzbarkeit",
        "description": "Wie gut lässt sich das Interface des Agenten bedienen? Wie gut lässt sich der Agent in den Workflow einbinden?",
        "options": [
            "Top Bedienbarkeit",
            "Gute Bedienbarkeit",
            "Mittelmäßige Bedienbarkeit",
            "Schlechte Bedienbarkeit",
        ],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Dokumentation",
        "description": "Wie umfangreich und strukturiert sind die Dokumentation über den Agenten?",
        "options": [
            "Viel Dokumentation",
            "Knappe Dokumentation",
            "Keine Dokumentation",
        ],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Support",
        "description": "Hat man die Möglichkeit bei Problemen Experten zu kontaktieren?",
        "options": ["Support verfügbar", "Kein Support verfügbar"],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Individualisierungsmöglichkeiten",
        "description": "Welche Konfigurierungsmöglichkeiten bietet der Agent?",
        "options": [
            "Bietet umfangreiche Möglichkeiten zur Konfiguration",
            "Bietet eingegrenzte Möglichkeiten zur individuellen Konfiguration",
            "Bietet keine Möglichkeiten zur Konfiguration",
        ],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Community und Inhalte",
        "description": "Hat der Agent eine große Community, durch die mehr Informationen bzlg. dem Agenten verfügbar sind?",
        "options": [
            "Große aktive Community mit vielen und aktuellen Inhalten.",
            "Aktive Community existiert, auch wenn nur überschaubar",
            "Inaktive oder keine Community und kaum Inhalte",
        ],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Open Source/ Closed Source",
        "description": "Handelt es sich bei der Software um open oder closed Software?",
        "options": ["open source", "closed source"],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "AI Auswahl",
        "description": "Welche Auswahlmöglichkeiten hat man bei der Wahl der AI? Welche Modelle? Nur Cloud oder auch lokal?",
        "options": [
            "Breite Auswahl an Modellen und Anbietern; Cloudbasiert sowie Lokal",
            "Auswahl an Cloud AI Modellen und Anbietern",
            "Beschränkt auf einen Anbieter mit Cloud Modellen",
        ],
        "category": "sekundäre Kriterien",
    },
    {
        "name": "Preisgestaltung",
        "description": "Wie ergeben sich die Kosten?",
        "options": [
            "Agent sowie Model (lokal) komplett kostenlos",
            "Agent kostenlos, nur Zahlung nach API Key Nutzung",
            "Festgelegter Preis pro Monat (inkl. Agent und API Key Nutzung).",
        ],
        "category": "sekundäre Kriterien",
    },
]

agenten_kategorien = [
    "Pro-Aktivität",
    "Kommunikation",
    "Reaktivität",
    "Coding Practices",
    "Systemintegration",
    "Autonomie",
]

autonomie_quellen = [
    "Lernfähigkeit",
    "Memory",
    "Planning",
    "Reflexion",
    "Tool-Usage",
]
