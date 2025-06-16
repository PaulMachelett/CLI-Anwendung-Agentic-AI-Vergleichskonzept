prompts_text = {
    "Prompt1": """
    Prompt 1:
    
    "Erstelle ein funktionales Web-Backend mit Python (Flask), das folgende Anforderungen erfüllt:
    
    1. Benutzer können sich registrieren (Name, E-Mail, Passwort).
    2. Eine Login-Funktion gibt ein einfaches Session-Token oder Login-Erfolgsmeldung zurück.
    3. Nach erfolgreichem Login können Benutzer eigene Notizen erstellen, lesen, bearbeiten und löschen.
    4. Es gibt eine Administrator-Funktion, mit der Benutzer gelöscht werden können.
    
    Die Datenbank enthält zwei Tabellen: 
      1. Tabelle `users` mit den Spalten: - `id` (INTEGER, Primary Key, unique) - `name` (TEXT, unique) - `email` (TEXT, unique) - `admin` (BOOLEAN)
      2. Tabelle `notes` mit den Spalten: - `id` (INTEGER, Primary Key) - `title` (TEXT) - `content` (TEXT) - `owner_id` (INTEGER, Foreign Key, verweist auf `users.id`)

    Implementiere REST-Endpunkte, die JSON-Daten empfangen und zurückgeben. Die Endpunkte sollen alle CRUD-Operationen (Create, Read, Update, Delete) vollständig abbilden. 
    Da keine echte Datenbank angebunden ist, soll die Datenhaltung über einfache Python-Listen erfolgen, die die Inhalte zur Laufzeit speichern. 
    Fülle diese Listen ebenfalls mit Dummy Daten. Die CRUD-Operationen sollen ihre Funktionalität vollständig auf diesen Listen ausführen.

    Unterteile dein Vorgehen dafür in verschiedene Schritte.

    Führe den Code anschließend aus."
    """,
    "Prompt2": """
    Prompt 2:
    
    "Erweitere dein bestehendes Flask-Backend so, dass es jetzt eine echte SQLite-Datenbankanbindung mit SQLAlchemy strukturell korrekt umsetzt.
    Dabei sollst du die gesamte Logik so aufbauen, als würdest du mit einer realen SQLite-Datenbank arbeiten – inklusive realistischer SQL-Strukturen, Abfragen und Datenbankmodelle. 
    Die beiden Datenbankmodelle sollen "Note" und "User" genannt werden.
    
    Wichtig: Da aktuell keine echte SQLite-Datenbank angeschlossen ist, sollst du die Datenbanklogik durch eine eigene Mock-Schicht simulieren, die das Verhalten der 
    echten SQLite-Datenbank vollständig nachbildet. 
    Innerhalb der Mock Prozesse sollen die Datenbankmodelle mit einbezogen werden.

    Gib mir während der Bearbeitung nach jeder deiner Handlungen ein kleinen Statusbericht, was du als letztes gemacht hat, mache danach aber automatisch weiter ohne auf weiteren 
    Input des Nutzers zu warten.

    Ich möchte, dass du mir dein Vorgehen sowie die Art deiner Implementierung im Anschluss begründest.

    Führe den Code anschließend aus."
    """,
    "Prompt3": """
    Prompt 3:
    
    "Strukturiere den bestehenden Python-Code in eine saubere, modulare Projektstruktur um. 
    Lege einen `myapp/`-Ordner an und verschiebe die Modulbestandteile in folgende Dateien:
      - CRUD-Logik in `myapp/crud.py`
      - API-Routen in `myapp/routes.py`
      - Datenbankmodelle in `myapp/models.py`
      - DB-Verbindung und Initialisierung in `myapp/db.py`
      - Hilfsfunktionen in `myapp/utils.py` (optional)
      - Weitere Ordner je nach Bedarf.

        
    Die Datei `main.py`, die die Anwendung startet, soll nicht im `myapp/`-Ordner liegen, sondern auf der obersten Projektebene bleiben.
    Achte darauf, dass alle Importe korrekt funktionieren, das Projekt weiterhin ausführbar ist und keine Duplikate im Code vorhanden sind.

    Führe den Code anschließend aus."
    """,
    "Prompt4": """
    "Prompt 4:
    
    "Schreibe Integrationstests mit pytest, die die REST-Endpunkte des Flask Backends über einen Test-Client testen. 
    Teste Registrierung, Login, Notiz erstellen und Notizen abrufen – inklusive Erfolgs- und Fehlerfällen.
    Die Datenbank soll dabei vollständig gemockt sein es erfolgt also kein echter Datenbankzugriff. Die Tests sollen alle ausführbar sein und funktionieren. 
    Achte bei der Testerstellung auf die vorhandene Projektstuktur und lege die Tests in einem passenden Modul an.
    
    Führe anschließend die Tests aus."
    """,
    "Prompt 5": """
    Manuelle Änderungen:
    - API Route abändern. Bsp. aus "notes/<int:note_id>" => "notes/<int:note_i>" machen.
    - crud.py File verschieben

    Prompt 5: 
    
    "Ich habe Änderungen im Code vorgenommen. Bitte fixe alle Fehler, die durch meine manuellen Änderungen im Code vorgenommen wurden."
    """,
    "Prompt 6": """
    Prompt 6:
    "Ergänze das bestehende Flask-Backend um eine weitere Route, die überprüft, ob eine E-Mail-Adresse bereits existiert, und als Antwort lediglich true oder false zurückgibt.

    Führe den Code anschließend aus."
    """,
    "Prompt 7": """
    Prompt 7:
    
    "Ändere innerhalb des models.py das Model der "Notes" Datenbanktabelle dahingehend, dass du das Attribut "owner_id" zu "user_id" umwandelst. 
    Zusätzlich möchte ich das du die REST Route "/api/login" zu "/api/userlogin" änderst.

    Zusätzlich möchte ich das du von jetzt an bei Änderungen französische Kommentare zu dem Code verfasst.

    Führe den Code anschließend aus."
    """,
    "Prompt 8": """
    Manuelle Änderungen:
    Führe Änderungen durch, die die Software starten lassen würden, aber die Tests fehlschlagen lassen. 
    Beispiel: API Route abändern und aus "notes/<int:note_id>" => "notes/<int:note_i>" machen.

    Prompt 8: 
    
    "Führe die Tests aus und korrigiere alle auftretenden Fehler."
    """,
    "Prompt 9": """
    Prompt 9:
    
    "Schreibe nun eine Funktion, die bestimmte Daten aus der Datenbank abruft und als Text in einer Datei abspeichert. Schreibe in einem kurzen Kommentar über der Funktion was diese macht.

    Führe den Code anschließend aus."
    """,
    "Prompt 10": """
    Prompt 10:
    
    "Ich möchte, dass du die Änderungen aus dem letzten Prompt sowie die letzten Änderungen in der routes.py wieder rückgängig machst.

    Führe den Code anschließend aus."
    """,
    "Prompt 11": """
    Prompt 11:
    
    "Füge als erstes innerhalb des routes.py eine GET-Route hinzu, die alle Notizen mit einem bestimmten "titel" löscht.

    Anschließend möchte ich, dass du mir Verbesserungsvorschläge für die gesamte Codebase gibt und mir sagst, was noch verbessert werden könnte.

    Führe den Code anschließend aus."
    """,
}
