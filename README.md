# curriculum_vitae
# CV as Code

Warum 10 Minuten Word-Formatierung fixen, wenn man das Problem auch mit 200+ Zeilen Python für immer lösen kann?

Dieses Repository ist ein klassisches Beispiel für **konstruktives Overengineering**. 
Als Solution Architect und Nerd glaube ich an "Everything as Code", warum also nicht auch beim Lebenslauf? Das Skript generiert mein aktuelles Profil vollautomatisch, versionierbar und pixelgenau.

### Das Skript
`cv_modern.py` ersetzt den Drag-and-Drop-Editor durch Logik:
* **Engine:** Python 3 mit `fpdf2`.
* **Clean Code:** Keine `DeprecationWarnings`, moderne Syntax (`new_x`/`new_y`), saubere Struktur.
* **Layout:** Dynamisches zweispaltiges Design, danke an pw_, das auch komplexe Stationen (Doppelrolle Adesso & Pharmastore) sauber darstellt.

### Nutzung
Wer sehen will, wie man ein PDF *richtig* baut (oder wer einfach das Layout klauen will):

1. **Repo klonen**

2. **Dependencies installieren**
   (Sauber via Requirements-File):
   ```bash
   pip install -r requirements.txt
   ```	

3. **Generieren**
   ```bash
   python cv_modern.py
   ```

### Hinweis
Die Daten sind hardcoded. Das hier ist kein SaaS-Tool, sondern eine Maßanfertigung. Wer das Skript nutzt, bewirbt sich im Zweifel als ich - Forken und Anpassen also ausdrücklich empfohlen, sonst ist Dein Traumjob bald meiner.

---
*Manually formatted margins are so 2005.*
