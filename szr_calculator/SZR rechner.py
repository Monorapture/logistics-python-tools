import tkinter as tk
from tkinter import messagebox
import requests # Neu: Für den Internet-Abruf

def hole_aktuellen_szr_kurs():
    """
    Versucht, den aktuellen XDR (SZR) zu EUR Kurs zu holen.
    Gibt den Kurs als String zurück oder None, wenn es nicht klappt.
    """
    url = "https://open.er-api.com/v6/latest/XDR" # Kostenlose API
    
    try:
        # Der "Anruf" bei der API
        antwort = requests.get(url, timeout=2) # Max 2 Sekunden warten
        
        # Prüfen ob Antwort "OK" (Status 200) ist
        if antwort.status_code == 200:
            daten = antwort.json() # Die Antwort in ein Dictionary verwandeln
            kurs = daten['rates']['EUR'] # Den Euro-Wert rausgreifen
            return str(kurs)
            
    except Exception as e:
        print(f"API-Fehler: {e}") # Nur für dich zum Debuggen
        return None # Wenn was schiefgeht, geben wir nichts zurück
# --- 1. DAS BACKEND (Die Logik) ---
def berechne_haftung():
    try:
        # Wir holen uns die Werte aus den Eingabefeldern (.get())
        gewicht_input = entry_gewicht.get()
        warenwert_input = entry_wert.get()
        SZR_KURS_input = entry_kurs.get()

        # Datenbereinigung (falls jemand "kg" oder "," eingibt)
        # Wir ersetzen Komma durch Punkt für Python
        gewicht_sauber = gewicht_input.lower().replace('kg', '').replace(',', '.')
        wert_sauber = warenwert_input.lower().replace('€', '').replace(',', '.')
        kurs_sauber = SZR_KURS_input.lower().replace("€", "").replace(",",".")

        # Umwandlung in Zahlen
        gewicht = float(gewicht_sauber)
        warenwert = float(wert_sauber)
        KURS = float(kurs_sauber)

        # Die Konstante
        SZR_FAKTOR = 8.33
        

        # Berechnung
        haftungsgrenze = gewicht * SZR_FAKTOR * KURS
        differenz = warenwert - haftungsgrenze

        # --- ERGEBNIS ANZEIGEN ---
        # Wir formatieren die Zahlen schön (.2f = 2 Nachkommastellen)
        ergebnis_text = f"Haftungsgrenze: {haftungsgrenze:.2f} €\n"
        
        if warenwert > haftungsgrenze:
            label_ergebnis.config(text=ergebnis_text + f"⚠️ UNTERDECKUNG: {differenz:.2f} € Risiko!", fg="red")
        else:
            label_ergebnis.config(text=ergebnis_text + "✅ Alles gedeckt. Kein Risiko.", fg="green")

    except ValueError:
        # Falls jemand "Hallo" statt einer Zahl eingibt
        messagebox.showerror("Fehler", "Bitte gib gültige Zahlen ein!")

# --- 2. DAS FRONTEND (Das Fenster) ---
# Hauptfenster erstellen
root = tk.Tk()
root.title("Logistik CMR Checker 🚛")
root.geometry("400x350") # Breite x Höhe

# Überschrift
label_titel = tk.Label(root, text="CMR Haftungs-Prüfer", font=("Arial", 16, "bold"))
label_titel.pack(pady=10) # pady ist der Abstand nach oben/unten

# Eingabe Gewicht
label_gewicht = tk.Label(root, text="Bruttogewicht (kg):")
label_gewicht.pack()
entry_gewicht = tk.Entry(root)
entry_gewicht.pack(pady=5)

# Eingabe Warenwert
label_wert = tk.Label(root, text="Warenwert (€):")
label_wert.pack()
entry_wert = tk.Entry(root)
entry_wert.pack(pady=5)

label_kurs = tk.Label(root, text="Aktueller SZR-Kurs:")
label_kurs.pack()
entry_kurs = tk.Entry(root)
entry_kurs.pack(pady=5)

# HIER IST DER MAGIER-TRICK:
# Wir rufen die API und füllen das Feld automatisch!
automatischer_kurs = hole_aktuellen_szr_kurs()

if automatischer_kurs:
    entry_kurs.insert(0, automatischer_kurs) # Schreib es ins Feld
    label_kurs.config(text=f"Aktueller SZR-Kurs (Auto-Geladen):")
else:
    entry_kurs.insert(0, "1.25") # Fallback-Wert, falls Internet weg ist

# Der Button
# command=berechne_haftung verknüpft den Klick mit unserer Funktion oben
btn_calc = tk.Button(root, text="Prüfen", command=berechne_haftung, bg="lightgrey", font=("Arial", 10))
btn_calc.pack(pady=20)

# Das Ergebnisfeld (leer am Anfang)
label_ergebnis = tk.Label(root, text="", font=("Arial", 12))
label_ergebnis.pack(pady=10)

# --- 3. STARTEN ---
root.mainloop()