import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
import pandas as pd
from collections import defaultdict
from Data import (
    always_asked_criteria,
    prompts,
    sekundäre_faktoren,
    code_kriterien_einmalig,
    autonomie_quellen,
    agenten_kategorien,
)


def bewertungs_prozess(
    kriterien_textantworten,
    extra_prompts_gesamt,
    agentenname,
    sekundäre_kriterien_werte,
    agenten_werte,
    code_kriterien_mittelwerte,
    autonomie_detail_werte,
):
    results = {}  # --- Speichert für jeden Prompt Kriterium, Kategorie sowie Bewertungs des Kriteriums ---

    print(f"\nBewertung des Agenten: {agentenname}\n")

    for prompt, criteria in prompts.items():
        print(f"\n{prompt} - Bitte bewerte die folgenden Kriterien:\n")
        results[prompt] = []

        # Frage nach Anzahl extra Prompts – außer bei Agenten Features
        if prompt != "Agenten Features":
            while True:
                try:
                    anzahl_extra_prompts = int(
                        input(
                            "Wie viele extra Prompts wurden benötigt bis der Code vollständig war und funktionierte? "
                        )
                    )
                    if anzahl_extra_prompts >= 0:
                        extra_prompts_gesamt += anzahl_extra_prompts
                        break
                    else:
                        print("Bitte eine nicht-negative Zahl eingeben.")
                except ValueError:
                    print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

        # Normale Kriterien
        for idx, criterion in enumerate(criteria):
            print("\n" + "#" * 30 + "\n")
            print(f"Kriterium {idx + 1}: {criterion['name']}")
            print(f"Beschreibung: {criterion['description']}")
            for i, option in enumerate(criterion["options"], 1):
                print(f"  [{i}] {option}")
            print()

            while True:
                try:
                    choice_input = input("Bitte Nummer der Bewertung eingeben: ")
                    choice = int(choice_input)
                    if 1 <= choice <= len(criterion["options"]):
                        bewertungstext = criterion["options"][choice - 1]

                        if len(criterion["options"]) == 2:
                            score = 1.0 if choice == 1 else 0.0
                        elif len(criterion["options"]) == 3:
                            score = [1.0, 0.5, 0.0][choice - 1]
                            print(score)
                        elif len(criterion["options"]) == 4:
                            score = [1.0, 0.66, 0.33, 0.0][choice - 1]
                        else:
                            score = 0.0
                        break
                    else:
                        print("Ungültige Eingabe.")
                except ValueError:
                    print("Bitte eine gültige Zahl eingeben.")

            results[prompt].append(
                {
                    "name": criterion["name"],
                    "category": criterion["category"],
                    "score": score,
                }
            )

            if criterion["name"] not in kriterien_textantworten:
                kriterien_textantworten[criterion["name"]] = bewertungstext

        # 👇 Hier: Nur wenn NICHT "Agenten Features" → Immer-gefragt-Kriterien abfragen
        if prompt != "Agenten Features":
            for idx, criterion in enumerate(always_asked_criteria):
                print("\n" + "#" * 30 + "\n")
                print(f"(Immer gefragt) Kriterium {idx + 1}: {criterion['name']}")
                print(f"Beschreibung: {criterion['description']}")
                for i, option in enumerate(criterion["options"], 1):
                    print(f"  [{i}] {option}")
                print()

                while True:
                    try:
                        choice_input = input(
                            "Bitte Nummer der Bewertung eingeben (oder Enter für keine Bewertung): "
                        )
                        if choice_input.strip() == "":
                            score = None
                            break
                        choice = int(choice_input)
                        if 1 <= choice <= len(criterion["options"]):
                            if len(criterion["options"]) == 2:
                                score = 1.0 if choice == 1 else 0.0
                            elif len(criterion["options"]) == 3:
                                score = [1.0, 0.5, 0.0][choice - 1]
                            elif len(criterion["options"]) == 4:
                                score = [1.0, 0.66, 0.33, 0.0][choice - 1]
                            else:
                                score = 0.0
                            break
                        else:
                            print("Ungültige Eingabe.")
                    except ValueError:
                        print("Bitte eine gültige Zahl eingeben.")

                if score is not None:
                    results[prompt].append(
                        {
                            "name": criterion["name"],
                            "category": criterion["category"],
                            "score": score,
                        }
                    )

        # Eingabe zur Fortsetzung
        while True:
            cont = (
                input("Möchtest du mit dem nächsten Prompt fortfahren? (j/n): ")
                .strip()
                .lower()
            )
            if cont == "j":
                break
            elif cont == "n":
                prompt_abbruch = True
                break
            else:
                print("Falsche Eingabe. Bitte j für Ja oder n für Nein.")
        if cont == "n":
            break

    process_bewertungen(
        results,
        sekundäre_kriterien_werte,
        code_kriterien_mittelwerte,
        agenten_werte,
        autonomie_detail_werte,
    )


def process_bewertungen(
    results,
    sekundäre_kriterien_werte,
    code_kriterien_mittelwerte,
    agenten_werte,
    autonomie_detail_werte,
):
    # Speichert als Key Kriterienname und als Value eine Liste mit allen Bewertungen dieses Kriteriums
    kriterium_bewertungen = defaultdict(list)

    # --- Speichert alle Mittelwerte der Kriterien einer Kategorie, WICHTIG nicht die Mittelwerte der Kategorie, das kommt erst später ---
    # --- Sprich dieses Dict enthält als Key die Kategorie und dann dann als Value eine Liste mit allen Mittelwerten der Kriterien dieser Kategorie ---
    kriterien_mittelwerte_per_katergorie = defaultdict(list)

    # Speichert für jedes Kriterium(key) die Kategorie(value)
    kriterium_name_kategorie_map = {}

    # Einträge aus Results in "kriterium_bewertungen" überführt
    for prompt_criteria in results.values():
        for criterion in prompt_criteria:
            key = criterion["name"].strip()
            kriterium_bewertungen[key].append(criterion["score"])
            kriterium_name_kategorie_map[key] = criterion["category"]

    print("\n\n\nBewertung der SonarQube Kriterien:")

    # Speichert alle "Code Kriterium" Kritieren in code_kriterien_mittelwerte
    input_and_process_code_kriterien(
        code_kriterien_mittelwerte, kriterium_bewertungen, kriterium_name_kategorie_map
    )

    # --- Fragt sekunäre Kriterien ab und speichert diese in "sekundäre_kriterien_werte"
    input_sek_kriterien(sekundäre_kriterien_werte, sekundäre_faktoren)

    # Kategorie-Mittelwerte berechnen (ohne "Code Kriterium")
    for criterion_name, scores in kriterium_bewertungen.items():
        category = kriterium_name_kategorie_map[criterion_name]
        if category == "Code Kriterium":
            continue
        mean_crit = sum(scores) / len(scores)
        kriterien_mittelwerte_per_katergorie[category].append(mean_crit)

    # Mittelwert der Autonomie Kategorien berechnen
    autonomie_werte = [
        sum(kriterien_mittelwerte_per_katergorie[cat])
        / len(kriterien_mittelwerte_per_katergorie[cat])
        for cat in autonomie_quellen
        if cat in kriterien_mittelwerte_per_katergorie
        and kriterien_mittelwerte_per_katergorie[cat]
    ]

    # Finalen Autonomie Mittelwert berechnen
    autonomie_mittelwert = (
        sum(autonomie_werte) / len(autonomie_werte) if autonomie_werte else 0.0
    )

    # Finale Kategorie Mittelwerte berechnen
    for cat in agenten_kategorien:
        if cat == "Autonomie":
            agenten_werte.append(autonomie_mittelwert)
        else:
            werte = kriterien_mittelwerte_per_katergorie.get(cat, [])
            wert = sum(werte) / len(werte) if werte else 0
            agenten_werte.append(wert)

    # Autonomie Radar

    for cat in autonomie_quellen:
        werte = kriterien_mittelwerte_per_katergorie.get(cat, [])
        wert = sum(werte) / len(werte) if werte else 0
        autonomie_detail_werte.append(wert)


def input_and_process_code_kriterien(
    code_kriterien_mittelwerte, kriterium_bewertungen, kriterium_name_kategorie_map
):
    code_kriterien_bewertungen = {}

    # Frägt SonarQube Kriterien ab und speichert diese unter "code_kriterien_bewertungen"
    input_code_kriterien(code_kriterien_bewertungen)

    # Hier werden die Mittelwerte der "Code Kriterium" Kriterien berechnet
    for criterion_name, scores in kriterium_bewertungen.items():
        if kriterium_name_kategorie_map[criterion_name] == "Code Kriterium":
            mean_score = sum(scores) / len(scores)
            code_kriterien_mittelwerte[criterion_name] = {
                "category": "Code Kriterium",
                "score": mean_score,
            }

    # --- Ergänze "Code_Kriterium" Mittelwerte mit SonarQube Eingaben ---
    code_kriterien_mittelwerte.update(code_kriterien_bewertungen)


def input_code_kriterien(code_kriterien_bewertungen):
    for criterion in code_kriterien_einmalig:
        while True:
            try:
                print(f"\n{criterion['name']}: {criterion['description']}")
                value = float(input("Bitte Zahl eingeben: "))
                if value >= 0:
                    code_kriterien_bewertungen[criterion["name"]] = {
                        "category": criterion["category"],
                        "score": value,
                    }
                    break
                else:
                    print("Bitte eine positive Zahl eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")


def print_code_kriterien_bewertungen(code_kriterien_mittelwerte):
    print("\n\n\n#### Bewertungen Kriterien der Kategorie 'Code Kriterium': ####")

    for name, info in code_kriterien_mittelwerte.items():
        if name in ["Code Security", "Code Reliability", "Code Maintainability"]:
            print(f"- {name}: {int(info['score'])} SonarQube Meldung")
        else:
            print(f"- {name}: {int(info['score'] * 100)} % der Fälle")


def input_sek_kriterien(sekundäre_kriterien_werte, sekundäre_faktoren):
    print("\n\nBewertung der sekundären Kriterien\n\n")

    for idx, criterion in enumerate(sekundäre_faktoren):
        print(f"Sekundäres Kriterium {idx + 1}: {criterion['name']}")
        print(f"Beschreibung: {criterion['description']}")
        for i, option in enumerate(criterion["options"], 1):
            print(f"  [{i}] {option}")
        print()

        while True:
            try:
                choice_input = input(
                    "Bitte Nummer der Bewertung eingeben (oder Enter für keine Bewertung): "
                )
                if choice_input.strip() == "":
                    score = None
                    break
                choice = int(choice_input)
                if 1 <= choice <= len(criterion["options"]):
                    if len(criterion["options"]) == 2:
                        score = 1.0 if choice == 1 else 0.0
                    elif len(criterion["options"]) == 3:
                        score = [1.0, 0.5, 0.0][choice - 1]
                    elif len(criterion["options"]) == 4:
                        score = [1.0, 0.66, 0.33, 0.0][choice - 1]
                    else:
                        score = 0.0
                    break
                else:
                    print("Ungültige Eingabe.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
        print("\n" + "#" * 30 + "\n")

        if score is not None:
            sekundäre_kriterien_werte["kriterium_name"].append(criterion["name"])
            sekundäre_kriterien_werte["werte"].append(score)


def zeichne_radar(titel, kategorien, werte1, werte2, label1, label2, dateiname):
    winkel = np.linspace(0, 2 * np.pi, len(kategorien), endpoint=False).tolist()

    # Zyklisch schließen
    werte1 += werte1[:1]
    werte2 += werte2[:1]
    winkel += winkel[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Plot für erste Instanz
    ax.plot(winkel, werte1, marker="o", label=label1)
    ax.fill(winkel, werte1, alpha=0.25)

    # Plot für zweite Instanz
    ax.plot(winkel, werte2, marker="s", label=label2)
    ax.fill(winkel, werte2, alpha=0.25)

    # Achsentitel etc.
    ax.set_title(titel, size=14, y=1.1)
    ax.set_xticks(winkel[:-1])
    ax.set_xticklabels(kategorien)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8])
    ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8"])
    ax.set_ylim(0, 1)

    # Legende & Layout
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(dateiname)
    plt.close()


def create_excel_table(
    kriterien_textantworten1,
    agenten_slug1,
    extra_prompts_gesamt1,
    code_kriterien_mittelwerte1,
    kriterien_textantworten2,
    agenten_slug2,
    extra_prompts_gesamt2,
    code_kriterien_mittelwerte2,
):
    # --- Falls Slugs gleich sind, umbenennen zur Sicherheit ---
    if agenten_slug1 == agenten_slug2:
        agenten_slug1 += "_1"
        agenten_slug2 += "_2"

    # --- Textantworten in DataFrames ---
    df1 = pd.DataFrame(
        list(kriterien_textantworten1.items()), columns=["Kriterium", agenten_slug1]
    )
    df2 = pd.DataFrame(
        list(kriterien_textantworten2.items()), columns=["Kriterium", agenten_slug2]
    )
    df = pd.merge(df1, df2, on="Kriterium", how="outer")

    # --- Code-Kriterien vorbereiten ---
    alle_kriterien = set(code_kriterien_mittelwerte1.keys()) | set(
        code_kriterien_mittelwerte2.keys()
    )
    code_kriterien_rows = []

    for kriterium in sorted(alle_kriterien):
        score1 = code_kriterien_mittelwerte1.get(kriterium, {}).get("score", "")
        score2 = code_kriterien_mittelwerte2.get(kriterium, {}).get("score", "")
        code_kriterien_rows.append(
            {"Kriterium": kriterium, agenten_slug1: score1, agenten_slug2: score2}
        )

    df_code = pd.DataFrame(code_kriterien_rows)

    # --- Leerzeile vorbereiten ---
    df_empty = pd.DataFrame(
        columns=["Kriterium", agenten_slug1, agenten_slug2], data=[["", "", ""]]
    )

    # --- Alle Abschnitte zusammenführen ---
    df_final = pd.concat([df, df_empty, df_code], ignore_index=True)

    # --- Excel-Datei schreiben ---
    excel_filename = f"{agenten_slug1}_vs_{agenten_slug2}_kriterien_inkl_code.xlsx"
    df_final.to_excel(excel_filename, index=False)

    # --- Openpyxl für Feinschliff ---
    wb = load_workbook(excel_filename)
    ws = wb.active

    # Spaltenbreite automatisch setzen
    for col in ws.columns:
        max_len = max((len(str(cell.value)) if cell.value else 0) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    # Leerzeile + extra Prompts am Ende
    last_row = ws.max_row + 2
    ws.cell(row=last_row, column=1, value="Anzahl benötigter extra Prompts")
    ws.cell(row=last_row, column=2, value=extra_prompts_gesamt1)
    ws.cell(row=last_row, column=3, value=extra_prompts_gesamt2)

    wb.save(excel_filename)
    print(f"\n✅ Excel-Datei gespeichert als '{excel_filename}'")
