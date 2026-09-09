# User-Story 005: Kandidatentage berechnen

## Status

Umgesetzt und geprüft.

## Story

Als Nutzer möchte ich für ein Vergleichsjahr den Schulstart sowie den früheren
und späteren Kandidatentag berechnen lassen, damit die Kalenderregel eindeutig
und unabhängig von den Wetterdaten angewendet wird.

## Sichtbares Ergebnis

Im Dashboard kann ein Vergleichsjahr eingegeben werden. Die Anwendung zeigt
den ersten Montag nach dem 15. August, den Samstag direkt davor und den Samstag
eine Woche früher.

## Umfang

- Kalenderberechnung in einem eigenen, kleinen Python-Modul umsetzen
- Schulstart strikt als ersten Montag nach dem 15. August bestimmen
- späteren Kandidatentag als Samstag direkt vor dem Schulstart bestimmen
- früheren Kandidatentag als Samstag sieben Tage davor bestimmen
- Vergleichsjahr im Dashboard eingeben und die drei Daten anzeigen
- dokumentierte Beispieljahre und einen Sonderfall automatisch prüfen

## Nicht enthalten

- Kandidatentage bereits mit den Wetterwerten verbinden
- das Liniendiagramm auf echte Daten umstellen
- Ferienkalender aus einer externen Quelle laden
- allgemeine freie Kalenderauswahlen umsetzen

## Akzeptanzkriterien

- Für 2026, 2027 und 2028 entstehen die in `PROJECT.md` dokumentierten Daten.
- Fällt der 15. August auf einen Montag, wird dieser nicht als Schulstart
  verwendet.
- Schulstart ist immer ein Montag und beide Kandidatentage sind Samstage.
- Zwischen den Kandidatentagen liegen genau sieben Tage.
- Die Berechnung benötigt weder Internet noch Wetterdaten.
- Das Dashboard zeigt die drei berechneten Daten verständlich an.

## Umsetzungsergebnis

- Die Kalenderberechnung ist unabhängig von Datenabruf und Darstellung in
  einem eigenen Modul umgesetzt.
- Die dokumentierten Beispiele 2026, 2027 und 2028 stimmen überein.
- Der Sonderfall 2022 bestätigt, dass Montag, der 15. August, nicht selbst als
  Schulstart zählt.
- Eine Prüfung über alle Jahre von 1990 bis 2050 bestätigt Wochentage und den
  Abstand von sieben Tagen.
- Das Vergleichsjahr kann im Dashboard eingegeben werden; die drei berechneten
  Daten wurden im Browser für 2026 und 2022 kontrolliert.
- Insgesamt bestehen elf automatische Tests, davon fünf konkrete Fälle für die
  neue Kalenderlogik.
