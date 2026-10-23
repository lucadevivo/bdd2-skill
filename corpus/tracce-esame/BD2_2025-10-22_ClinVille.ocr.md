# BD2_2025-10-22_ClinVille — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2025-10-22_ClinVille.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapienza Università di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statistica, Laurea in Informatica
Insegnamento di Basi di Dati, Modulo 2
Proff. Toni Mancini, Marco Esposito
Dipartimento di Informatica
https://raise.uniroma1.it /teaching

Esame Es.20251022 — Prova scritta del 22 ottobre 2025

Si vuole progettare ClinVille, un sistema informativo per la gestione di studi clinici presso un
centro clinico sperimentale. Uno studio clinico ha lo scopo di testare un nuovo farmaco o un
nuovo trattamento sperimentale su esseri umani. Il sistema verrà utilizzato dal personale del centro
(ricercatori) e dal personale dell'azienda che promuove e finanzia lo studio (Promotore).

ClinVille dovrà permettere di rappresentare tutte le informazioni riguardanti gli studi clinici.

Di ogni studio clinico interessa conoscere il nome, il codice identificativo (una stringa), la data
di inizio, la data di fine prevista e quella effettiva.

| pazienti arruolati in uno studio clinico vengono suddivisi in coorti, cioè gruppi di pazienti che
seguono trattamenti sperimentali diversi.

| Ogni coorte di uno studio segue un piano definito da una sequenza di cosiddetti day, cioè visite
pianificate nelle quali devono essere svolte determinate attività. Un day è descritto dal giorno in cui
si tengono le sue attività (un intero non negativo), relativamente alla data di inizio dello studio. Ad
esempio, il day 7 descrive le attività da svolgere il settimo giorno dall’inizio dello studio.

Le attività sono delle seguenti tipologie:

1. misurazione di parametri vitali (p. es. pressione, temperatura corporea);
\ 2. somministrazione di farmaci;

{_ 3. esecuzione diyftest diagnostici (p. es. test di gravidanza).

interessa conoscere il nome (unico) e il valore di riferimento (un numero reale).

Di ogni attività di somministrazione interessa conoscere il farmaco e la dose da somministrare (in
milligre_xmrcho è descritto dal proprio nome (unico) e dal nome della casa farmaceutica
produttrice.

Infine, delle attività di esecuzione di test diagnostici, si vuole rappresentare il nome del test.

| pazienti sono memorizzati nel sistema in modo pseudonimizzato, allo scopo di proteggere la loro
privacy. Dunque, ClinVille non deve rappresentare alcuna informazione anagrafica, fatta esclusione
per la data di nascita, poiché l'età rientra tra i criteri di inclusione previsti dagli studi. Di ogni
pa_z_iÌeqtg interessa qu_ingiiygqngg(fr_(i un codice identificativo (una stringa alfanumerica). i

Ogni paziente arruolato in una coorte di uno studio seguirà il piano previsto per tale coorte
attraverso una sequenza di visite presso il centro clinico. Ogni visita è relativa a uno specifico day

Di ogni attività di misurazione interessa conoscere il parametro da misurare. Di ogni parametro

e deve rappresentare l'esito di tutte quante le attività previste da tale day sul paziente.

In particolare, per ogni attività di misurazione di un parametro vitale, si vuole conoscere il valore
misurato. Di ogni attività di somministrazione interessa l’istante esatto in cui si è effettuata ed
eventualmente delle note (una stringa). Di ogni attività di esecuzione di test diagnostici, interessa
rappresentare l’esito (per semplicità, si assuma che quest'ultimo sia una stringa di testo).

E estremamente importante che per ciascun paziente la sequenza dellﬁeìv.i&e segua esattamente
l'ordine dei day previsti dalla coorte in cui è arruolato.

E possibile che un paziente si ritiri da uno studio, cioè che non completi tutti i day previsti dalla

sua coorte. Per ogni ritiro interessa conoscere la motivazione e la data.

1

## Pagina 2

R

Infine, ClinVille deve poter rappresentare studi clinici sospesi o termmatt prematuramente. În
tali casi, è di interesse conoscere la motivazione e la data di sospensione o interruzione.
ClinVille deve permettere al personale del centro clinico di inserire i dati degli studi, dei pazienti

An

\_ e delle visite. QA CERLATO LA

Il sistema deve inoltre permettere al Promotore dello studio di accedere alle seguenti funzionalità
avanzate:

2 e dato uno studio, calcolare un resoconto che riporti, per ognuna delle sue coorti, il numero di

pazuentv che hanno effettuato tutte le v151te previste dal piano;

è e data una coorte, trovare i pazienti per i quali il valore dei parametri vitali misurati non ha mai
superato il valore di riferimento.
