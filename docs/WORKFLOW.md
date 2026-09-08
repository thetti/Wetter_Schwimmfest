# Einfacher Entwicklungsablauf

## 1. Fachlichkeit klären

Prüfe die Aufgabe gegen `CONTEXT.md`, `PROJECT.md` und `DECISIONS.md`. Halte neue
bestätigte Begriffe oder Produktentscheidungen direkt im passenden Dokument
fest. Dieser Schritt ist abgeschlossen, wenn keine entscheidende Annahme
versteckt bleibt.

## 2. Kleine Änderung planen

Formuliere einen überschaubaren Umsetzungsschritt mit sichtbarem Ergebnis.
Nenne betroffene Daten, erwartetes Verhalten und notwendige Prüfung. Dieser
Schritt ist abgeschlossen, wenn dies in einer User-Story festgehalten ist und der Nutzer den Umfang nachvollziehen kann.

## 3. Einfach umsetzen

Verwende Python und Poetry mit möglichst wenigen direkten Abhängigkeiten. Halte
Kalenderlogik, Datenbeschaffung, Auswertung und Darstellung voneinander
verständlich getrennt. Dieser Schritt ist abgeschlossen, wenn der geplante
Umfang umgesetzt und erklärbar ist.

## 4. Prüfen

Führe passende automatische Tests aus und kontrolliere Wetterdaten zusätzlich
an wenigen konkreten Jahren und Orten gegen die dokumentierte Quelle. Dieser
Schritt ist abgeschlossen, wenn Tests bestehen und Stichproben nachvollziehbar
dokumentiert sind.

## 5. Übergeben

Beschreibe Ergebnis, offene Punkte und den einfachsten nächsten Schritt auf
Deutsch und halte dies fest. Erstelle einen Git-Commit, nach Abschluss. Lass danach den Nutzer den gemeinsamen Stand
als Ausgangspunkt bestätigen.
