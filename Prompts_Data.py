prompts = {
    "Prompt 1": [
        {
            "name": "Dependency-Handling",
            "description": "Installiert der Agent eigenständig fehlende Libraries?",
            "options": [
                "Installiert fehlende Libraries",
                "Ist nicht in der Lage fehlende Libraries zu installieren."
            ],
            "category": "Pro-Aktivität"
        },
        {
            "name": "Input-/Output-Simulation",
            "description": "Kann der Agent eigenen Dummy-Input erzeugen?",
            "options": [
                "Kann Dummy-Input erzeugen.",
                "Kann keinen Dummy-Input erzeugen."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Modularitätserstellung",
            "description": "Hat der Agent Code- oder Datei-Einheiten als funktionale Module behandelt und sie sinnvoll getrennt?",
            "options": [
                "Hat automatische Projektstruktur erstellt",
                "Hat Teils der Modularität ausgelagert.",
                "Hat komplette Logik in einem File verpackt."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Aufgabenplanung",
            "description": "War der Agent dazu in der Lage die Bearbeitung der Aufgabe in verschiedene Schritte zu unterteilen?",
            "options": [
                "Hat die Aufgabe in kleinere Schritte unterteilt.",
                "War nicht in der Lage, die Aufgabe in Schritte zu unterteilen"
            ],
            "category": "Planning"
        }
    ],
    "Prompt 2": [
        {
            "name": "Dependency-Handling",
            "description": "Konnte der Agent erneut fehlende Libraries installieren?",
            "options": [
                "Installiert",
                "Nicht installiert"
            ],
            "category": "Pro-Aktivität"
        },
        {
            "name": "Selbsterklärbarkeit",
            "description": "Gibt er verständliche Begründungen für sein Vorgehen?",
            "options": [
                "Hat sein Vorgehen verständlich begründet",
                "Hat nur knapp begründet",
                "Hat keine Begründung angegeben"
            ],
            "category": "Reflexion"
        },
        {
            "name": "Status Kommunikation",
            "description": "Hat der Agent Auskunft über den Status während der Bearbeitung der Aufgabe gegeben?",
            "options": [
                "Hat zwischen den verschiedenen Schritten Auskunft über sein Vorgehen und seine Handlungen gegeben.",
                "Hat Feedback am Anfang und Ende der Bearbeitung gegeben.",
                "Hat keine Auskunft über den Bearbeitungsprozess gegeben."
            ],
            "category": "Kommunikation"
        }
    ],
    "Prompt 3": [
        {
            "name": "Projektstrukturierung",
            "description": "Konnte der Agent zusammenhängenden Code erkennen und diesen in eine sinnvolle, logisch getrennte Datei- und Projektstruktur überführen?",
            "options": [
                "Hat Code in logische Projektstruktur mit verschiedenen Files überführt.",
                "Hat Projektstruktur erzeugt, die Fehler, falsche Modularitäten oder Duplikate hatte.",
                "Konnte keine logische Struktur erzeugen."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Struktur- und Navigationsverständnis",
            "description": "Konnte der Agent innerhalb des Dateisystems agieren und navigieren?",
            "options": [
                "Konnte Ordner und Dateien verwalten.",
                "Konnte nur Teilaspekte.",
                "Konnte sich nicht zurechtfinden."
            ],
            "category": "Tool-Usage"
        }
    ],
    "Prompt 4": [
        {
            "name": "Testfallgenerierung",
            "description": "Hat der Agent automatisch funktionsabdeckene Tests erstellt?",
            "options": [
                "Hat funktionsabdeckende Tests erstellt",
                "Hat größtenteils funktionsabdeckende Tests erstellt",
                "Hat unvollständige Tests erstellt"
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Modularitätsverständnis",
            "description": "Wurde neuer Code richtig in Modularität implementiert?",
            "options": [
                "Im richtigen Modul",
                "Im falschen Modul"
            ],
            "category": "Coding Practices"
        }
    ],
    "Prompt 5": [
        {
            "name": "Codeänderungserkennung",
            "description": "Hat der Agent manuelle Änderungen erkannt?",
            "options": [
                "Erkannt nach Untersuchung",
                "Erkannt nach Hinweis (Durch weiteren Prompt)",
                "Nicht erkannt"
            ],
            "category": "Reaktivität"
        },
        {
            "name": "Strukturänderungserkennung",
            "description": "Konnte der Agent mit den strukturellen Änderungen umgehen und die Importe anpassen?",
            "options": [
                "Hat strukturelle Änderungen erkannt und Import angepasst?",
                "Hat strukturelle Änderungen erkennt, jedoch kein Importe angepasst.",
                "Hat strukturelle Änderung nicht erkannt."
            ],
            "category": "Reaktivität"
        }
    ],
    "Prompt 6": [
        {
            "name": "Code Reuse",
            "description": "Hat der Agent vorhandene Logik wiederverwendet?",
            "options": [
                "Hat Code wiederverwendet.",
                "Hat neuen, redundanten Code erstellt."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Modularitätsverständnis",
            "description": "Wurde neuer Code ins richtige Modul implementiert?",
            "options": [
                "Im richtigen Modul.",
                "Im falschen Modul."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Automatische Testfallgenerierung",
            "description": "Hat der Agent neue Test erstellt wenn für bereits getestete Bereiche neue Funktionen eingefügt wurden?",
            "options": [
                "Hat neue Tests erstellt.",
                "Hat keine neuen Tests erstellt."
            ],
            "category": "Coding Practices"
        }
    ],
    "Prompt 7": [
        {
            "name": "Refactoring",
            "description": "Wurden Umbenennungen konsistent im Projekt durchgeführt?",
            "options": [
                "Alles korrekt umbenannt",
                "Teilweise vergessen",
                "Nur eine Stelle geändert"
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Testsausführung nach Änderungen von testabgedeckten Codes",
            "description": "Wurden nach Änderungen automatisch Tests ausgeführt?",
            "options": [
                "Ja",
                "Nein"
            ],
            "category": "Pro-Aktivität"
        },
        {
            "name": "Testanpassung",
            "description": "Hat der Agent Tests an geänderten Code angepasst?",
            "options": [
                "Automatisch angepasst",
                "Nach Testfehlschlag angepasst",
                "Nicht angepasst"
            ],
            "category": "Pro-Aktivität"
        }
    ],
    "Prompt 8": [
        {
            "name": "Reaktion auf Testfehlschlag",
            "description": "Wie hat der Agent auf fehlschlagende Tests reagiert?",
            "options": [
                "Hat Code korrigiert.",
                "Hat nur Tests angepasst.",
                "Hat nichts gemacht."
            ],
            "category": "Reaktivität"
        }
    ],
    "Prompt 9": [
        {
            "name": "Rückfragen bei Unklarheiten",
            "description": "Hat der Agent Rückfragen gestellt, wenn Infos fehlten?",
            "options": [
                "Gezielte Rückfragen",
                "Teilweise Rückfragen",
                "Keine Rückfragen"
            ],
            "category": "Kommunikation"
        },
        {
            "name": "Lernfähigkeit aus User Feedback",
            "description": "Hat der Agent aus Feedback gelernt? (Kommentare auf Deutsch?)",
            "options": [
                "Ja",
                "Nein"
            ],
            "category": "Lernfähigkeit"
        }
    ],
    "Prompt 10": [
        {
            "name": "Kontextspeicherung Prompt",
            "description": "Hat sich der Agent an vorherige Prompts erinnert?",
            "options": [
                "Ja",
                "Nein"
            ],
            "category": "Memory"
        },
        {
            "name": "Kontextspeicherung Code",
            "description": "Hat sich der Agent an vorherige Codeänderungen erinnert?",
            "options": [
                "Ja",
                "Nein"
            ],
            "category": "Memory"
        }
    ],
    "Prompt 11": [
        {
            "name": "Code Reflexion",
            "description": "Konnte der Agent den Code reflektieren und Verbesserungsvorschläge bringen?",
            "options": [
                "Hat hilfreiche Verbesserungsvorschläge liefern können.",
                "Konnte kein oder nur wenig hilfreiches Feedback liefern."
            ],
            "category": "Reflexion"
        },
        {
            "name": "Konfrontation mit fehlerhaften Benutzerprompts",
            "description": "Wie ging der Agent mit fehlerhaften Prompts um?",
            "options": [
                "Kommuniziert mit dem User oder versteht Fehler und implementiert korrekten Code",
                "Implementiert fehlerhaften Code"
            ],
            "category": "Kommunikation"
        }
    ],
    "Prompt 12": [
        {
            "name": "Lernfähigkeit",
            "description": "Lernt der Agent aus Fehlern? Konkret: Agenten eine Aufgabe geben, ihm anschließend Feedback dazu geben, den Code der vorherigen Aufgabe löschen und anschließend ihm die gleiche Aufgabe erneut geben. Wenn er dann das User Feedback berücksichtigt, hat er gelernt.",
            "options": [
                "Hat aus seinen Fehler gelernt und den Fehler bei gleicher Aufgabenstellung nicht nochmal gemacht.",
                "Hat gleichen Fehler bei gleicher Aufgabe erneut gemacht."
            ],
            "category": "Lernfähigkeit"
        }
    ],
    "Prompt 13": [
        {
            "name": "Konsolenzugriff",
            "description": "Hat der Agent Lese sowie Schreibzugriff in der Konsole?",
            "options": [
                "Lese und Schreibzugriff",
                "Nur Schreibzugriff",
                "Nur Lesezugriff",
                "Kein Konsolen Zugriff"
            ],
            "category": "Tool-Usage"
        },
        {
            "name": "Automatischer Korrekturversuch",
            "description": "Hat der Agent bei dem auftreten von Fehlern automatisch ohne weiteren Anweisung versucht, die Fehler zu lösen?",
            "options": [
                "Hat automatisch und ohne weiteren Input versucht die Fehler zu lösen.",
                "Hat auftretende Fehler nicht automatisch behandelt, sondern neue Anweisungen dafür benötigt."
            ],
            "category": "Pro-Aktivität"
        },
        {
            "name": "Dokumentation & Developer Experience",
            "description": "Hat der Agent Dokumentation, Docstrings, README-Dateien oder API-Beschreibungen erstellt?",
            "options": [
                "Hat Dokumentation, Docstrings, README-Dateien und API-Beschreibungen erstellt.",
                "Hat Code kommentiert, aber keine weiteren Dokumentationen erstellt.",
                "Hat keine Form von Dokumentation erstellt."
            ],
            "category": "Coding Practices"
        },
        {
            "name": "Session Management (Konversationen)",
            "description": "Hat der Agent die Möglichkeit, dass man zwischen verschiedenen Konversationen auswählen kann?",
            "options": [
                "Ja",
                "Nein"
            ],
            "category": "Systemintegration"
        },
        {
            "name": "User Interface",
            "description": "Hat der Coding Agent ein User Interface oder muss er in der Konsole bedient werden?",
            "options": [
                "Besitzt ein Interface",
                "Nur Zugriff über Konsole"
            ],
            "category": "Systemintegration"
        },
        {
            "name": "GitHub Einbindung",
            "description": "Kann der Agent mit Git arbeiten?",
            "options": [
                "Ja er hat Zugang zu Git.",
                "Nein, er hat kein Zugang zu Git."
            ],
            "category": "Systemintegration"
        }
    ]
}

# Immer abzufragende Kriterien
always_asked_criteria = [
    {
        "name": "Fehlerbehebungskompetenz",
        "description": "Hat der Agent es geschafft einen auftretenden Fehler mit zusätzlichen Prompts (max. 3) zu beheben?",
        "options": [
            "Konnte den auftretenden Fehler korrigieren.",
            "Hat es nicht geschafft einen auftretenden Fehler zu korrigieren."
        ],
        "category": "Pro-Aktivität"
    },
    {
        "name": "Verhaltensadaptivität",
        "description": "War der Agent in der Lage seine eigenen Fehler zu beheben, sprich seine Bearbeitungsstrategie falls nötig anzupassen?",
        "options": [
            "Passt seine Strategie an, und probiert auftretende Probleme durch andere Wege zu lösen.",
            "Passt Strategie teils an, und verfängt sich aber auch in Loops bei denen er immer wieder die gleichen Stellen ändert, die das Problem nicht lösen.",
            "Probiert ursprüngliche Strategie und verfängt sich in Verhaltensloops wenn diese nicht funktioniert."
        ],
        "category": "Pro-Aktivität"
    },
    {
        "name": "Anforderungserfüllung",
        "description": "Hat der Agent alle seine Anforderungen aus dem Prompt umgesetzt (egal ob der Code funktioniert oder nicht)?",
        "options": [
            "Hat Prompt vollständig umgesetzt",
            "Hat Prompt unvollständig umgesetzt."
        ],
        "category": "Code Kriterium"
    },
    {
        "name": "Ausführbarer Code",
        "description": "Hat der Agent seine Bearbeitung mit funktionierendem Code abgeschlossen?",
        "options": [
            "Hat die Bearbeitung mit ausführbarem Code abgeschlossen",
            "Hat die Bearbeitung mit nicht lauffähigen Code beendet."
        ],
        "category": "Code Kriterium"
    }
]