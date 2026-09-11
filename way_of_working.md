# Way of Working — Edge Computing-projektet (πCo)

## Kommunikation
- Discord för både skriftlig kommunikation och samtal
- Vid akuta/blockande problem: pinga direkt i kanalen istället för att vänta till nästa möte

## Arbetssätt & roller
- Vi mobbcodear tillsammans som huvudarbetssätt
- Ses fysiskt vid enstaka tillfällen för att testa/koppla hårdvaran
- Trots gemensamt mobbcodande ska alla ha egna committar/PR:ar i repot (krav för G)

## Git
- En feature-branch per person/uppgift
- PR krävs innan merge till `main`
- Minst en annan person i gruppen granskar och godkänner innan merge
- Commit-meddelanden ska vara korta och beskrivande (t.ex. `feat: lägg till ultraljudsavläsning`)

## Kanban
- GitHub Projects med kolumnerna: **To do / In progress / Review / Done**
- Uppdateras löpande av den som jobbar med uppgiften, inte bara vid möten

## Definition of Done
En uppgift räknas som klar när:
- Koden fungerar och är testad
- Det finns kort kommentar/dokumentation där det behövs
- PR är granskad och godkänd av minst en annan i gruppen
- Kanban-boarden är uppdaterad

## LLM-användning
- Tillåtet för mindre delar av koden och för idégenerering
- Inte tillåtet för att lösa hela uppgifter/delar
- LLM-genererad kod ska kommenteras som sådan i koden

## Möten & avstämning
- Korta avstämningar vid varje mobbcodande-session: vad är kvar, vad är blockerat
- Innan Demo 1: gemensam genomgång av vad som ska visas och vem som säger vad

## Beslutsfattande
- Tekniska vägval (t.ex. sensorval, pipeline-detaljer) diskuteras och beslutas gemensamt vid mobbcodande
- Vid oenighet: den som är mest insatt i den specifika delen har sista ordet, om inte annat bestäms

## Dokumentation
- README hålls uppdaterad löpande, inte bara i slutet
- Skärmdumpar och kort beskrivning av produkten samlas in efter hand, inte allt sista veckan