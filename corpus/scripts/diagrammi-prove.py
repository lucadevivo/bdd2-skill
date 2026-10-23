#!/usr/bin/env python3
"""I diagrammi delle prove d'esame trascritte, in forma di descrizione per il generatore.

    python3 diagrammi-prove.py

Scrive i `.json` e i `.xml` in `soluzioni-studenti/diagrammi/<Sistema>/<tipo>/`, una
cartella per prova e una sottocartella per diagramma — così si apre un file per volta in
Visual Paradigm (`Project -> Import -> XML`) senza perdersi, e il progetto `.vpp` che VP
salva accanto resta nella sua cartella.

Le descrizioni sono ricavate **dalle trascrizioni** in `soluzioni-studenti/`, che a loro
volta vengono dagli svolgimenti manoscritti: non sono soluzioni ufficiali, e gli errori
degli autori sono riportati come sono. Dove la trascrizione segna un dubbio di lettura, il
diagramma lo eredita.

Per ogni prova, dove lo svolgimento le contiene: **concettuale**, **ristrutturato**,
**use-case**. DKLCloud ha solo il concettuale, perché dalla Domanda 6 in poi il foglio è
bianco.

Convenzione delle molteplicità: `molt_da` è quella scritta **accanto alla classe `da`**,
cioè quanti oggetti di `da` per ogni oggetto di `a`. Quando una classe associativa ha lo
stesso nome della sua associazione, l'associazione resta senza nome: è così che lo scrive
Visual Paradigm, e il nome lo porta la classe.
"""
import json, subprocess, sys
from copy import deepcopy
from pathlib import Path

QUI = Path(__file__).parent
DEST = QUI.parent / "soluzioni-studenti" / "diagrammi"

DISJ = "{disjoint, complete}"


# ─────────────────────────────────────────────────────────── EasyToll, 13 gennaio 2023

EASYTOLL = {
    "nome": "EasyToll 2023-01-13 — concettuale",
    "classi": {
        "ClienteTelepass": [["nome", "Stringa"], ["cognome", "Stringa"],
                            ["codFis", "CF {id}"], ["Iban", "IBAN"]],
        "Autostrada": [["codice", "COD {id}"], ["nome", "Stringa [0..1]"]],
        "Casello": [["nome", "Stringa {id}"], ["codCasello", "COD {id}"],
                    ["volumeMax", "Intero >= 0"], ["servizio", "bool"],
                    ["posKM", "Reale >= 0 {id2}"]],
        "CaselloTelepass": [],
        "Localita": [["nome", "Stringa {id}"]],
        "Pagamento": [["nome", "Stringa {id}"]],
        "Tagliando": {"attributi": [["senso", "bool"], ["codice", "COD {id}"]],
                      "operazioni": [["costo", "Reale >= 0"]]},
        "Veicolo": [["targa", "Targa {id}"]],
        "ClasseVeicolo": [["nome", "Stringa {id}"]],
        "Tutor": {"attributi": [["posInizioKM", "Reale >= 0"], ["posFineKM", "Reale >= 0"]],
                  "operazioni": [["senso", "booleano"]]},
        "Rilevazione": {"attributi": [["istInizio", "DataOra"], ["istFine", "DataOra"]],
                        "operazioni": [["velocita", "Reale > 0"]]},
        "entrata": [["ist", "DataOra"]],
        "uscita": [["ist", "DataOra"]],
        "tariffa": [["euroKM", "Reale >= 0"]],
        "velocitaMax": [["vel", "Intero > 0"]],
    },
    "associazioni": [
        {"nome": "cli_tel", "da": "ClienteTelepass", "molt_da": "0..1", "a": "Tagliando", "molt_a": "0..*"},
        {"nome": "tag_vei", "da": "Tagliando", "molt_da": "0..*", "a": "Veicolo", "molt_a": "1..1"},
        {"nome": "", "classe": "entrata", "da": "Tagliando", "molt_da": "0..*", "a": "Casello", "molt_a": "1..1"},
        {"nome": "", "classe": "uscita", "da": "Tagliando", "molt_da": "0..*", "a": "Casello", "molt_a": "0..1"},
        {"nome": "aut_cas", "da": "Autostrada", "molt_da": "1..1 {id}", "a": "Casello", "molt_a": "2..*"},
        {"nome": "cas_pay", "da": "Casello", "molt_da": "0..*", "a": "Pagamento", "molt_a": "1..*"},
        {"nome": "cas_loc", "da": "Casello", "molt_da": "0..*", "a": "Localita", "molt_a": "1..1"},
        {"nome": "aut_tut", "da": "Autostrada", "molt_da": "1..1", "a": "Tutor", "molt_a": "0..*"},
        {"nome": "tut_ril", "da": "Tutor", "molt_da": "1..1", "a": "Rilevazione", "molt_a": "0..*"},
        {"nome": "ril_vei", "da": "Rilevazione", "molt_da": "0..*", "a": "Veicolo", "molt_a": "1..1"},
        {"nome": "cla_vei", "da": "ClasseVeicolo", "molt_da": "1..1", "a": "Veicolo", "molt_a": "0..*"},
        {"nome": "", "classe": "tariffa", "da": "Autostrada", "molt_da": "0..*", "a": "ClasseVeicolo", "molt_a": "1..*"},
        {"nome": "", "classe": "velocitaMax", "da": "Tutor", "molt_da": "0..*", "a": "ClasseVeicolo", "molt_a": "1..*"},
    ],
    "generalizzazioni": [{"padre": "Casello", "figlie": ["CaselloTelepass"], "vincolo": ""}],
}

EASYTOLL_USECASE = {
    "nome": "EasyToll 2023-01-13 — use-case",
    "attori": ["SistemaFatturazione", "Casello", "CaselloTelepass", "Tutor"],
    "usecase": ["CalcoloConto", "RegistraTagliando", "RegTagliandoVirtuale", "Rilevazione"],
    "associazioni": [
        {"nome": "", "da": "SistemaFatturazione", "molt_da": "", "a": "CalcoloConto", "molt_a": ""},
        {"nome": "", "da": "Casello", "molt_da": "", "a": "RegistraTagliando", "molt_a": ""},
        {"nome": "", "da": "CaselloTelepass", "molt_da": "", "a": "RegTagliandoVirtuale", "molt_a": ""},
        {"nome": "", "da": "Tutor", "molt_da": "", "a": "Rilevazione", "molt_a": ""},
    ],
    "generalizzazioni": [{"padre": "Casello", "figlie": ["CaselloTelepass"], "vincolo": ""}],
}


def easytoll_ristrutturato():
    """Fusione su Casello: la sottoclasse sparisce e diventa il booleano `telepass`.
    Ogni classe prende un identificatore primario, i domini passano ai nomi SQL, e
    l'operazione `senso()` del Tutor diventa un attributo."""
    r = deepcopy(EASYTOLL)
    r["nome"] = "EasyToll 2023-01-13 — ristrutturato"
    c = r["classi"]
    del c["CaselloTelepass"]
    r["generalizzazioni"] = []
    c["Casello"] = [["nome", "Stringa {id}"], ["codCasello", "COD {id1}"],
                    ["volumeMax", "Int_GEZ"], ["servizio", "bool"],
                    ["posKM", "Real_GEZ {id2}"], ["id", "serial {id3}"], ["telepass", "bool"]]
    c["Tutor"] = [["posInizioKM", "Real_GEZ"], ["posFineKM", "Real_GEZ"],
                  ["id", "serial {id}"], ["senso", "bool"]]
    c["Rilevazione"] = [["istInizio", "DateTime"], ["istFine", "DateTime"],
                        ["id", "serial {id}"]]
    c["entrata"] = [["ist", "DateTime"]]
    c["uscita"] = [["ist", "DateTime"]]
    c["tariffa"] = [["euroKM", "Real_GEZ"]]
    c["velocitaMax"] = [["vel", "Int_GEZ"]]
    return r


# ─────────────────────────────────────────────────────────────── Slimmy, 30 gennaio 2023

SLIMMY = {
    "nome": "Slimmy 2023-01-30 — concettuale",
    "classi": {
        "Nazione": [["nome", "Stringa {id}"]],
        "Utente": [["nome", "Stringa"], ["cognome", "Stringa"], ["email", "Mail {id}"],
                   ["password", "Stringa"]],
        "Abbonamento": [["inizio", "Data"], ["fine", "Data"]],
        "DurataDieta": [["inizio", "Data"], ["Fine", "Data [0..1]"]],
        "Dieta": [["kCalMin", "Intero >= 0"], ["kCalMax", "Intero >= 0 [0..1]"],
                  ["nome", "Stringa"]],
        "Nutriente": [["nome", "Stringa {id}"]],
        "NutOpz": [],
        "Alimento": {"attributi": [["nome", "Stringa"], ["codice", "COD [0..1]"],
                                   ["kCal", "Intero >= 0"], ["porzione", "Reale >= 0"],
                                   ["quantita", "Reale >= 0"], ["istante", "Data"]],
                     "operazioni": [["invalido", "bool"]]},
        "AlimentoU": {"attributi": [], "operazioni": [["valido", "bool"]]},
        "AlimentoS": {"attributi": [], "operazioni": [["valido", "bool"]]},
        "Marca": [["nome", "Stringa {id}"]],
        "Unita": [["nome", "Stringa {id}"]],
        "TipoPasto": [["nome", "Stringa {id}"]],
        "Pasto": [["giorno", "Date"]],
        "die_nut": [["min", "Reale >= 0"], ["max", "Reale >= 0 [0..1]"]],
        "nut_al": [["grammatura", "Reale >= 0"]],
        "pas_ali": [["quantita", "Reale >= 0"]],
        "valida": [["ist", "Data"]],
        "invalida": [["ist", "Data"]],
    },
    "associazioni": [
        {"nome": "ute_naz", "da": "Utente", "molt_da": "0..*", "a": "Nazione", "molt_a": "1..1"},
        {"nome": "ute_abb", "da": "Utente", "molt_da": "1..1", "a": "Abbonamento", "molt_a": "0..*"},
        {"nome": "ute_die", "da": "Utente", "molt_da": "1..1", "a": "DurataDieta", "molt_a": "0..*"},
        {"nome": "dur_die", "da": "DurataDieta", "molt_da": "0..*", "a": "Dieta", "molt_a": "1..1"},
        {"nome": "", "classe": "die_nut", "da": "Dieta", "molt_da": "0..*", "a": "Nutriente", "molt_a": "0..*"},
        {"nome": "", "classe": "nut_al", "da": "Nutriente", "molt_da": "0..*", "a": "Alimento", "molt_a": "0..*"},
        {"nome": "ute_ali", "da": "Utente", "molt_da": "1..1", "a": "AlimentoU", "molt_a": "0..*"},
        {"nome": "", "classe": "valida", "da": "Utente", "molt_da": "0..*", "a": "AlimentoU", "molt_a": "0..*"},
        {"nome": "", "classe": "invalida", "da": "Utente", "molt_da": "0..*", "a": "Alimento", "molt_a": "0..*"},
        {"nome": "ute_pas", "da": "Utente", "molt_da": "1..1", "a": "Pasto", "molt_a": "0..*"},
        {"nome": "tip_pas", "da": "TipoPasto", "molt_da": "1..1", "a": "Pasto", "molt_a": "0..*"},
        {"nome": "", "classe": "pas_ali", "da": "Pasto", "molt_da": "0..*", "a": "Alimento", "molt_a": "1..*"},
        {"nome": "ali_mar", "da": "Alimento", "molt_da": "0..*", "a": "Marca", "molt_a": "0..1"},
        {"nome": "ali_uni", "da": "Alimento", "molt_da": "0..*", "a": "Unita", "molt_a": "1..1"},
    ],
    "generalizzazioni": [
        {"padre": "Alimento", "figlie": ["AlimentoU", "AlimentoS"], "vincolo": DISJ},
        {"padre": "Nutriente", "figlie": ["NutOpz"], "vincolo": ""},
    ],
}

SLIMMY_USECASE = {
    "nome": "Slimmy 2023-01-30 — use-case",
    "attori": ["UtenteWeb", "Redazione", "Utente", "UtentePremium"],
    "usecase": ["Registrazione", "ArchivioAlimenti", "AcquistoAbbonamento",
                "ValidazioneAlimento", "Statistiche", "RicercaAlimenti",
                "ResocontoDieta", "CreazioneDieta"],
    "associazioni": [
        {"nome": "", "da": "UtenteWeb", "molt_da": "", "a": "Registrazione", "molt_a": ""},
        {"nome": "", "da": "Redazione", "molt_da": "", "a": "ArchivioAlimenti", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "ArchivioAlimenti", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "AcquistoAbbonamento", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "ValidazioneAlimento", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "Statistiche", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "RicercaAlimenti", "molt_a": ""},
        {"nome": "", "da": "UtentePremium", "molt_da": "", "a": "ResocontoDieta", "molt_a": ""},
        {"nome": "", "da": "UtentePremium", "molt_da": "", "a": "CreazioneDieta", "molt_a": ""},
    ],
    "generalizzazioni": [{"padre": "Utente", "figlie": ["UtentePremium"], "vincolo": ""}],
}


def slimmy_ristrutturato():
    """«Fusione su alimento. Fusione su nutriente.» — le due sottoclassi di Alimento
    spariscono (resta `utente [0..1]` a distinguerle) e NutOpz diventa il booleano `opz`."""
    r = deepcopy(SLIMMY)
    r["nome"] = "Slimmy 2023-01-30 — ristrutturato"
    c = r["classi"]
    for sparita in ("AlimentoU", "AlimentoS", "NutOpz"):
        del c[sparita]
    r["generalizzazioni"] = []
    r["associazioni"] = [a for a in r["associazioni"] if a["a"] != "AlimentoU"] + [
        {"nome": "ute_ali", "da": "Utente", "molt_da": "0..1", "a": "Alimento", "molt_a": "0..*"},
        {"nome": "", "classe": "valida", "da": "Utente", "molt_da": "0..*", "a": "Alimento", "molt_a": "0..*"},
    ]
    c["Nutriente"] = [["nome", "Stringa {id}"], ["opz", "bool"]]
    c["Alimento"] = {"attributi": [["nome", "Stringa"], ["codice", "COD [0..1]"],
                                   ["kCal", "Int_GEZ"], ["porzione", "Real_GEZ"],
                                   ["quantita", "Real_GEZ"], ["istante", "Date"],
                                   ["id", "serial {id}"]],
                     "operazioni": [["invalido", "bool"], ["valido", "bool"]]}
    for nome, extra in (("Utente", "serial {id}"), ("Abbonamento", "serial {id}"),
                        ("DurataDieta", "serial {id}"), ("Dieta", "serial {id}"),
                        ("Pasto", "serial {id}")):
        voci = c[nome] if isinstance(c[nome], list) else c[nome]["attributi"]
        voci.append(["id", extra])
    return r


# ──────────────────────────────────────────────────────── CozyRooms, 11 settembre 2023

COZYROOMS = {
    "nome": "CozyRooms 2023-09-11 — concettuale",
    "classi": {
        "Utente": {"attributi": [["nome", "Stringa"], ["cognome", "Stringa"],
                                 ["email", "Mail"], ["num", "Cell"]],
                   "operazioni": [["Fedelta", "Intero >= 0"]]},
        "Gestore": [["cod", "CF {id}"]],
        "Struttura": [["nome", "Stringa"], ["stelle", "1..7"], ["via", "Indirizzo"]],
        "Citta": [["nome", "Stringa"]],
        "Tipologia": [["nome", "Stringa {id}"]],
        "Sistemazione": [["nome", "Stringa"], ["posti", "Intero > 0"]],
        "Tariffa": [["posti", "Intero > 0 {id}"], ["giorno", "Data {id}"],
                    ["prezzo", "Reale >= 0"]],
        "Livello": [["nome", "Stringa"], ["pren", "Intero >= 0 {id}"]],
        "MetodoPay": [["nome", "Stringa {id}"]],
        "Prenotazione": [["istPren", "DataOra"], ["inizio", "Data"], ["fine", "Data"]],
        "Accettata": [["istAcc", "DataOra"]],
        "Rifiutata": [["istRif", "DataOra"]],
        "Annullata": [["istAnn", "DataOra"]],
        "Sconto": [["val", "int_unit"]],
        "occupanti": [["occupanti", "Intero > 0"]],
    },
    "associazioni": [
        {"nome": "ges_str", "da": "Gestore", "molt_da": "1..*", "a": "Struttura", "molt_a": "0..*"},
        {"nome": "cit_str", "da": "Citta", "molt_da": "1..1", "a": "Struttura", "molt_a": "0..*"},
        {"nome": "str_tip", "da": "Tipologia", "molt_da": "1..1", "a": "Struttura", "molt_a": "0..*"},
        {"nome": "sis_str", "da": "Struttura", "molt_da": "1..1", "a": "Sistemazione", "molt_a": "1..*"},
        {"nome": "sis_tar", "da": "Sistemazione", "molt_da": "1..1 {id}", "a": "Tariffa", "molt_a": "0..*"},
        {"nome": "pre_ute", "da": "Utente", "molt_da": "1..1", "a": "Prenotazione", "molt_a": "0..*"},
        {"nome": "pag_pre", "da": "MetodoPay", "molt_da": "1..1", "a": "Prenotazione", "molt_a": "0..*"},
        {"nome": "pre_sis", "classe": "occupanti", "da": "Prenotazione", "molt_da": "1..*", "a": "Sistemazione", "molt_a": "1..*"},
        {"nome": "sconto", "classe": "Sconto", "da": "Struttura", "molt_da": "0..*", "a": "Livello", "molt_a": "0..*"},
    ],
    "generalizzazioni": [
        {"padre": "Utente", "figlie": ["Gestore"], "vincolo": ""},
        {"padre": "Prenotazione", "figlie": ["Accettata", "Rifiutata"], "vincolo": "{disjoint}"},
        {"padre": "Prenotazione", "figlie": ["Annullata"], "vincolo": ""},
    ],
}

COZYROOMS_USECASE = {
    "nome": "CozyRooms 2023-09-11 — use-case",
    "attori": ["Utente", "Gestore"],
    "usecase": ["RicercaStanze", "InformazioniAccount", "RichiestaPrenotazioni",
                "RegistraStrutture", "StrutturePiene", "GestionePrenotazioni"],
    "associazioni": [
        {"nome": "", "da": "Utente", "molt_da": "", "a": "RicercaStanze", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "InformazioniAccount", "molt_a": ""},
        {"nome": "", "da": "Utente", "molt_da": "", "a": "RichiestaPrenotazioni", "molt_a": ""},
        {"nome": "", "da": "Gestore", "molt_da": "", "a": "RegistraStrutture", "molt_a": ""},
        {"nome": "", "da": "Gestore", "molt_da": "", "a": "StrutturePiene", "molt_a": ""},
        {"nome": "", "da": "Gestore", "molt_da": "", "a": "GestionePrenotazioni", "molt_a": ""},
    ],
    "generalizzazioni": [{"padre": "Utente", "figlie": ["Gestore"], "vincolo": ""}],
}


def cozyrooms_ristrutturato():
    """Le tre sottoclassi di Prenotazione diventano tre timestamp opzionali, il Gestore si
    fonde nell'Utente con `cod [0..1]`, e ogni classe prende un `id`."""
    r = deepcopy(COZYROOMS)
    r["nome"] = "CozyRooms 2023-09-11 — ristrutturato"
    c = r["classi"]
    for sparita in ("Accettata", "Rifiutata", "Annullata", "Gestore"):
        del c[sparita]
    r["generalizzazioni"] = []
    r["associazioni"] = [a for a in r["associazioni"] if a["nome"] != "ges_str"] + [
        {"nome": "ges_str", "da": "Utente", "molt_da": "1..*", "a": "Struttura", "molt_a": "0..*"}]
    c["Utente"] = {"attributi": [["nome", "Stringa"], ["cognome", "Stringa"],
                                 ["email", "Mail"], ["num", "Cell"],
                                 ["id", "serial {id}"], ["cod", "CF [0..1] {id1}"]],
                   "operazioni": [["Fedelta", "Int_GE2"]]}
    c["Prenotazione"] = [["istPren", "Timestamp"], ["inizio", "Date"], ["fine", "Date"],
                         ["istAcc", "Timestamp [0..1]"], ["istAnn", "Timestamp [0..1]"],
                         ["istRif", "Timestamp [0..1]"], ["id", "serial {id}"]]
    c["Struttura"] = [["id", "serial {id}"], ["nome", "Stringa"], ["stelle", "Star"],
                      ["via", "Indirizzo"]]
    c["Sistemazione"] = [["id", "serial {id}"], ["nome", "Stringa"], ["posti", "Int_G2"]]
    c["Tariffa"] = [["posti", "Int_G2 {id}"], ["giorno", "Date {id}"],
                    ["prezzo", "Real_GE2"], ["id", "serial {id1}"]]
    c["Citta"] = [["nome", "Stringa"], ["id", "serial {id}"]]
    c["Livello"] = [["nome", "Stringa"], ["pren", "Int_GE2 {id}"]]
    c["occupanti"] = [["occupanti", "Int_G2"]]
    c["Sconto"] = [["val", "int_unit"]]
    return r


# ────────────────────────────────────────────────────────── DKLCloud, 16 gennaio 2024

DKLCLOUD = {
    "nome": "DKLCloud 2024-01-16 — concettuale",
    "classi": {
        "Continente": [["nome", "Stringa {id}"]],
        "Nazione": [["nome", "Stringa {id}"]],
        "Citta": [["nome", "Stringa {id}"]],
        "Utente": [["codice", "COD {id}"]],
        "Privato": [["nome", "Stringa"], ["cognome", "Stringa"]],
        "Commerciale": [["ragione", "Stringa"]],
        "Carta": [["scad", "Data"], ["titolare", "Stringa"], ["numero", "NumCarta"]],
        "Tariffa": [["peso", "Range {id}"], ["def", "Data {id}"], ["prezzo", "Valuta"]],
        "Spedizione": {"attributi": [["oraRitiro", "Ora"], ["istSped", "DataOra"],
                                     ["pesoKG", "Reale >= 0"],
                                     ["importoAssicurato", "Valuta"]],
                       "operazioni": [["prezzo", "Valuta"]]},
        "InCarico": [],
        "SpedConsegnata": [["istCons", "DataOra"]],
        "Corriere": [["nome", "Stringa"]],
        "Depot": [],
        "Mezzo": [],
        "TipoMezzo": [["nome", "Stringa {id}"]],
        "ritira": [["indirizzo", "Ind"]],
        "spedisce": [],
        "spe_dep": [["inizio", "DataOra"], ["fine", "DataOra"]],
    },
    "associazioni": [
        {"nome": "con_naz", "da": "Continente", "molt_da": "1..1 {id}", "a": "Nazione", "molt_a": "0..*"},
        {"nome": "cit_naz", "da": "Nazione", "molt_da": "1..1 {id}", "a": "Citta", "molt_a": "0..*"},
        {"nome": "rit_cit", "da": "Citta", "molt_da": "1..1", "a": "ritira", "molt_a": "0..*"},
        {"nome": "spe_cit", "da": "Citta", "molt_da": "1..1", "a": "spedisce", "molt_a": "0..*"},
        {"nome": "ute_car", "da": "Utente", "molt_da": "0..*", "a": "Carta", "molt_a": "0..*"},
        {"nome": "spe_car", "da": "spedisce", "molt_da": "0..*", "a": "Carta", "molt_a": "1..1"},
        {"nome": "", "classe": "spedisce", "da": "Utente", "molt_da": "1..1", "a": "Spedizione", "molt_a": "0..*"},
        {"nome": "", "classe": "ritira", "da": "Utente", "molt_da": "1..1", "a": "Spedizione", "molt_a": "0..*"},
        {"nome": "cor_spe", "da": "Corriere", "molt_da": "1..1", "a": "InCarico", "molt_a": "0..*"},
        {"nome": "", "classe": "spe_dep", "da": "Spedizione", "molt_da": "0..*", "a": "Depot", "molt_a": "0..*"},
        {"nome": "spe_mez", "da": "spe_dep", "molt_da": "0..*", "a": "Mezzo", "molt_a": "1..1"},
        {"nome": "mez_tip", "da": "Mezzo", "molt_da": "0..*", "a": "TipoMezzo", "molt_a": "1..1"},
        {"nome": "cit_dep", "da": "Depot", "molt_da": "0..*", "a": "Citta", "molt_a": "1..1"},
    ],
    "generalizzazioni": [
        {"padre": "Utente", "figlie": ["Privato", "Commerciale"], "vincolo": "{complete, disj}"},
        {"padre": "Spedizione", "figlie": ["InCarico"], "vincolo": ""},
        {"padre": "InCarico", "figlie": ["SpedConsegnata"], "vincolo": ""},
    ],
}


# ─────────────────────────────────────────────────────────── TimeBank, 3 aprile 2024
#
# Copia di studente-A, l'unica delle due sul modulo UML (quella di studente-B è sul
# modulo ER). `feedback` è un'associazione che **specializza** `chiedesca`: nel
# generatore la si nomina con la chiave posizionale `·assocN`, perché un'associazione con
# classe associativa non ha nome proprio.

TIMEBANK = {
    "nome": "TimeBank 2024-04-03 — concettuale",
    "classi": {
        "Abilita": [["nome", "Stringa {id}"]],
        "Utente": {"attributi": [["nome", "Stringa"], ["cognome", "Stringa"],
                                 ["mail", "Email"], ["tel", "Tel"],
                                 ["istIsc", "DataOra"]],
                   "operazioni": [["saldo", "Reale >= 0"]]},
        "Scambio": {"attributi": [["inizioSca", "DataOra"], ["durataOre", "Reale > 0"]],
                    "operazioni": [["valore", "Reale > 0"]]},
        "AbiUte": {"attributi": [], "operazioni": [["media", "Reale >= 0"]]},
        "Feedback": [["voto", "1..10"]],
    },
    "associazioni": [
        {"nome": "abisca", "da": "Abilita", "molt_da": "1..1", "a": "Scambio", "molt_a": "0..*"},
        {"nome": "", "classe": "AbiUte", "da": "Abilita", "molt_da": "0..*", "a": "Utente", "molt_a": "0..*"},
        {"nome": "dasca", "da": "Utente", "molt_da": "1..1", "a": "Scambio", "molt_a": "0..*"},
        {"nome": "chiedesca", "da": "Utente", "molt_da": "1..1", "a": "Scambio", "molt_a": "0..*"},
        {"nome": "", "classe": "Feedback", "da": "Utente", "molt_da": "1..1", "a": "Scambio", "molt_a": "0..*"},
    ],
    # `·assoc4` è l'associazione di `Feedback`: specializza `chiedesca`
    "generalizzazioni": [{"padre": "chiedesca", "figlie": ["·assoc4"], "vincolo": ""}],
}


def timebank_ristrutturato():
    """Un identificatore primario `id` per Utente e Scambio, i domini SQL al posto dei tipi
    concettuali, e la specializzazione di associazione su `feedback` eliminata: resta
    un'associazione autonoma, retta dal vincolo esterno `V.FEEDBACK.SECHIEDE`."""
    r = deepcopy(TIMEBANK)
    r["nome"] = "TimeBank 2024-04-03 — ristrutturato"
    c = r["classi"]
    c["Utente"] = {"attributi": [["id", "serial {id}"], ["nome", "Stringa"],
                                 ["cognome", "Stringa"], ["mail", "Email"], ["tel", "Tel"],
                                 ["istIsc", "Timestamp"]],
                   "operazioni": [["saldo", "RealGEZ"]]}
    c["Scambio"] = {"attributi": [["id", "serial {id}"], ["inizioSca", "Timestamp"],
                                  ["durataOre", "RealGZ"]],
                    "operazioni": [["valore", "RealGZ"]]}
    c["AbiUte"] = {"attributi": [], "operazioni": [["media", "RealGEZ"]]}
    c["Feedback"] = [["voto", "Voto"]]
    r["generalizzazioni"] = []
    return r


TIMEBANK_USECASE = {
    "nome": "TimeBank 2024-04-03 — use-case",
    "attori": ["Utente", "UtenteRegistrato"],
    "usecase": ["Registrazione", "CercaUtente", "GestioneAbilita", "Feedback"],
    "associazioni": [
        {"nome": "", "da": "Utente", "molt_da": "", "a": "Registrazione", "molt_a": ""},
        {"nome": "", "da": "UtenteRegistrato", "molt_da": "", "a": "CercaUtente", "molt_a": ""},
        {"nome": "", "da": "UtenteRegistrato", "molt_da": "", "a": "GestioneAbilita", "molt_a": ""},
        {"nome": "", "da": "UtenteRegistrato", "molt_da": "", "a": "Feedback", "molt_a": ""},
    ],
    # i due attori sul foglio non sono legati da nessuna generalizzazione
    "generalizzazioni": [],
}


# ────────────────────────────────────────────── SafeOnTheBeach, 4 settembre 2020
#
# Unico svolgimento con un voto e una correzione, ma **scritto in notazione ER**:
# queste tre descrizioni sono la sua conversione in UML, fatta nella trascrizione.

SAFEONTHEBEACH_CONCETTUALE = {
    "nome": "SafeOnTheBeach 2020-09-04 — concettuale",
    "classi": {
        "Mare": [
            [
                "nome",
                "Stringa"
            ]
        ],
        "Litorale": [
            [
                "nome",
                "Stringa"
            ],
            [
                "estensioneKm",
                "Reale > 0"
            ]
        ],
        "Comune": [
            [
                "nome",
                "Stringa"
            ],
            [
                "provincia",
                "Provincia"
            ]
        ],
        "Zona": [
            [
                "nome",
                "Stringa"
            ],
            [
                "pax",
                "Intero > 0"
            ],
            [
                "superficiem2",
                "Reale > 0"
            ],
            [
                "animali",
                "Booleano"
            ]
        ],
        "RiservaAmb": [
            [
                "descrizione",
                "Stringa"
            ],
            [
                "istituzione",
                "Data"
            ]
        ],
        "Spiaggia": [
            [
                "serviziIgienici",
                "Booleano"
            ]
        ],
        "Localita": [
            [
                "posCentro",
                "Posizione"
            ]
        ],
        "AttivitaComm": [
            [
                "numeroTelefono",
                "Telefono"
            ]
        ],
        "StabilimentoBaln": [
            [
                "prezzo",
                "Reale > 0"
            ]
        ],
        "Bar": [
            [
                "nome",
                "Stringa"
            ]
        ],
        "Ristorante": [
            [
                "nome",
                "Stringa"
            ]
        ],
        "Attrezzatura": [
            [
                "nome",
                "Stringa"
            ]
        ],
        "Utente": [
            [
                "CF",
                "CodiceFiscale {id}"
            ]
        ],
        "UtenPrivato": [
            [
                "nome",
                "Stringa"
            ],
            [
                "cognome",
                "Stringa"
            ],
            [
                "genere",
                "{'M','F'}"
            ],
            [
                "dataNascita",
                "Data"
            ],
            [
                "luogoNascita",
                "Stringa"
            ]
        ],
        "UtenCommerciante": [
            [
                "ragioneSociale",
                "Stringa"
            ]
        ],
        "Evento": [
            [
                "nome",
                "Stringa"
            ],
            [
                "descrizione",
                "Stringa"
            ],
            [
                "prezzo",
                "Reale > 0 (0,1)"
            ],
            [
                "pax",
                "Intero > 0"
            ],
            [
                "inizio",
                "DataOra"
            ],
            [
                "fine",
                "DataOra"
            ]
        ],
        "Prenotazione": [
            [
                "arrivo",
                "DataOra"
            ],
            [
                "abbandono",
                "DataOra"
            ],
            [
                "nAnimali",
                "Intero >= 0"
            ]
        ],
        "Accesso": [
            [
                "arrivo",
                "DataOra"
            ]
        ],
        "AccTerminato": [
            [
                "abbandono",
                "DataOra"
            ]
        ],
        "prezzoGiorn": [
            [
                "prezzoGiorn",
                "Reale > 0"
            ]
        ]
    },
    "associazioni": [
        {
            "nome": "litMar",
            "da": "Litorale",
            "molt_da": "0..*",
            "a": "Mare",
            "molt_a": "1..*"
        },
        {
            "nome": "litCom",
            "da": "Litorale",
            "molt_da": "0..*",
            "a": "Comune",
            "molt_a": "1..*"
        },
        {
            "nome": "litZon",
            "da": "Litorale",
            "molt_da": "1..1",
            "a": "Zona",
            "molt_a": "1..*"
        },
        {
            "nome": "zonLoc",
            "da": "Zona",
            "molt_da": "0..*",
            "a": "Localita",
            "molt_a": "1..1"
        },
        {
            "nome": "locCom",
            "da": "Localita",
            "molt_da": "0..*",
            "a": "Comune",
            "molt_a": "1..1"
        },
        {
            "nome": "locFrazCom",
            "da": "Localita",
            "molt_da": "0..*",
            "a": "Comune",
            "molt_a": "0..1"
        },
        {
            "nome": "spiAtt",
            "da": "Spiaggia",
            "molt_da": "1..1",
            "a": "StabilimentoBaln",
            "molt_a": "0..*"
        },
        {
            "nome": "stabAttr",
            "da": "StabilimentoBaln",
            "molt_da": "0..*",
            "a": "Attrezzatura",
            "molt_a": "0..*",
            "classe": "prezzoGiorn"
        },
        {
            "nome": "comAtt",
            "da": "AttivitaComm",
            "molt_da": "0..*",
            "a": "UtenCommerciante",
            "molt_a": "1..1"
        },
        {
            "nome": "accUten",
            "da": "Accesso",
            "molt_da": "0..*",
            "a": "UtenPrivato",
            "molt_a": "1..1"
        },
        {
            "nome": "accZon",
            "da": "Accesso",
            "molt_da": "0..*",
            "a": "Zona",
            "molt_a": "1..1"
        },
        {
            "nome": "prenZon",
            "da": "Prenotazione",
            "molt_da": "0..*",
            "a": "Zona",
            "molt_a": "1..1"
        },
        {
            "nome": "prenEven",
            "da": "Prenotazione",
            "molt_da": "0..*",
            "a": "Evento",
            "molt_a": "0..*"
        },
        {
            "nome": "prenUten",
            "da": "Prenotazione",
            "molt_da": "0..*",
            "a": "UtenPrivato",
            "molt_a": "1..*"
        },
        {
            "nome": "evenZon",
            "da": "Evento",
            "molt_da": "0..*",
            "a": "Zona",
            "molt_a": "1..1"
        },
        {
            "nome": "commEven",
            "da": "Evento",
            "molt_da": "0..*",
            "a": "UtenCommerciante",
            "molt_a": "1..1"
        }
    ],
    "generalizzazioni": [
        {
            "padre": "Zona",
            "figlie": [
                "RiservaAmb",
                "Spiaggia"
            ],
            "vincolo": "{disjoint, complete}"
        },
        {
            "padre": "AttivitaComm",
            "figlie": [
                "StabilimentoBaln",
                "Bar",
                "Ristorante"
            ],
            "vincolo": "{disjoint, complete}"
        },
        {
            "padre": "Utente",
            "figlie": [
                "UtenPrivato",
                "UtenCommerciante"
            ],
            "vincolo": "{disjoint, complete}"
        },
        {
            "padre": "Accesso",
            "figlie": [
                "AccTerminato"
            ],
            "vincolo": ""
        }
    ]
}

def safeonthebeach_ristrutturato():
    """Le generalizzazioni diventano relationship uno-a-uno (`risIsZon`, `staIsAtt`,
    `privIsUt`…), `AccTerminato` sparisce in favore di `Terminato` e `abbandono [0..1]`, e
    gli attributi composti si spianano: `Posizione` in `longCentro`/`latCentro`, `Telefono`
    in `prefissoTelefono`/`numeroTelefono`."""
    r = deepcopy(SAFEONTHEBEACH_CONCETTUALE)
    r["nome"] = "SafeOnTheBeach 2020-09-04 — ristrutturato"
    c = r["classi"]
    c["Localita"] = [["longCentro", "Reale"], ["latCentro", "Reale"]]
    c["AttivitaComm"] = [["id", "serial {id}"], ["prefissoTelefono", "Prefisso"],
                         ["numeroTelefono", "Telefono"]]
    c["Zona"] = [["id", "serial {id}"]] + c["Zona"]
    c["Accesso"] = [["arrivo", "DataOra"], ["Terminato", "Booleano"],
                    ["abbandono", "DataOra [0..1]"]]
    del c["AccTerminato"]

    ISA = [("risIsZon", "Zona", "RiservaAmb"), ("spiIsZon", "Zona", "Spiaggia"),
           ("staIsAtt", "AttivitaComm", "StabilimentoBaln"),
           ("barIsAtt", "AttivitaComm", "Bar"), ("risIsAtt", "AttivitaComm", "Ristorante"),
           ("privIsUt", "Utente", "UtenPrivato"), ("comIsUt", "Utente", "UtenCommerciante")]
    r["generalizzazioni"] = []
    r["associazioni"] = r["associazioni"] + [
        {"nome": n, "da": padre, "molt_da": "1..1", "a": figlia, "molt_a": "0..1"}
        for n, padre, figlia in ISA]
    return r


SAFEONTHEBEACH_USECASE = {
    "nome": "SafeOnTheBeach 2020-09-04 — usecase",
    "attori": [
        "UtenteWeb",
        "Ministero",
        "UtenteNonRegistrato",
        "UtenteCommerciante",
        "UtentePrivato"
    ],
    "usecase": [
        "StrumentiRicerca",
        "GestioneComuni",
        "StrumentiIscrizione",
        "GestioneEventi",
        "StrumentiPrenotazioni"
    ],
    "associazioni": [
        {
            "nome": "",
            "da": "UtenteWeb",
            "molt_da": "",
            "a": "StrumentiRicerca",
            "molt_a": ""
        },
        {
            "nome": "",
            "da": "Ministero",
            "molt_da": "",
            "a": "GestioneComuni",
            "molt_a": ""
        },
        {
            "nome": "",
            "da": "UtenteNonRegistrato",
            "molt_da": "",
            "a": "StrumentiIscrizione",
            "molt_a": ""
        },
        {
            "nome": "",
            "da": "UtenteCommerciante",
            "molt_da": "",
            "a": "GestioneEventi",
            "molt_a": ""
        },
        {
            "nome": "",
            "da": "UtentePrivato",
            "molt_da": "",
            "a": "StrumentiPrenotazioni",
            "molt_a": ""
        }
    ],
    "generalizzazioni": [
        {
            "padre": "UtenteWeb",
            "figlie": [
                "Ministero",
                "UtenteNonRegistrato",
                "UtenteCommerciante",
                "UtentePrivato"
            ]
        }
    ]
}

# ────────────────────────────────────────────── Citta' Verde (progetto 14, studente-A)

CITTAVERDE = {
    "nome": "Citta Verde — concettuale",
    "classi": {
        "Specie": [["nomeCom", "Stringa {id1}"], ["nomeSc", "Stringa {id2}"]],
        "Malattia": [["nomeCom", "Stringa {id1}"], ["nomeSc", "Stringa {id2}"],
                     ["grav", "Grav"]],
        "SoggVerde": [["dataPia", "Data"], ["lat", "Reale"], ["long", "Reale"],
                      ["rischio", "Rischio"]],
        "SoggRim": [["dataRim", "Data"]],
        "CausaRim": [["nome", "Stringa {id}"]],
        "TipoMisura": [["nome", "Stringa"], ["unita", "Stringa"]],
        "PeriodoMal": [["inMal", "Data"], ["fineMal", "Data [0..1]"]],
        "AreaVerde": [["nome", "Stringa {id}"]],
        "Fruibile": [],
        "NonFruibile": [],
        "Sensibile": [],
        "TipoArea": [["nome", "Stringa {id}"]],
        "Intervento": [["inInt", "Data"], ["durataGg", "Intero > 0"],
                       ["fineInt", "Data [0..1]"], ["nPers", "Intero > 0"],
                       ["prio", "1..10"]],
        "TipoInt": [["nome", "Stringa {id}"]],
        "Attrezzo": [["nome", "Stringa {id}"], ["tipoAtt", "TipoAtt"]],
        "Squadra": [["cod", "CodSqua {id}"], ["dataFor", "Data"],
                    ["dataSc", "Data [0..1]"]],
        "Operatore": [["nome", "Stringa"], ["cognome", "Stringa"], ["dataIn", "Data"],
                      ["dataFine", "Data [0..1]"], ["CF", "CodiceFiscale {id}"]],
        "Partecipa": [["inPar", "Data"], ["finePar", "Data"]],
        "Capo": [],
        "misSog": [["valore", "Reale > 0"]],
        "intSqu": [["istAcq", "DataOra"]],
    },
    "associazioni": [
        {"nome": "sogSpe", "da": "Specie", "molt_da": "1..1", "a": "SoggVerde", "molt_a": "0..*"},
        {"nome": "", "classe": "misSog", "da": "TipoMisura", "molt_da": "0..*", "a": "SoggVerde", "molt_a": "0..*"},
        {"nome": "cauRim", "da": "CausaRim", "molt_da": "1..1", "a": "SoggRim", "molt_a": "0..*"},
        {"nome": "malPer", "da": "Malattia", "molt_da": "1..1", "a": "PeriodoMal", "molt_a": "0..*"},
        {"nome": "malSog", "da": "SoggVerde", "molt_da": "1..1", "a": "PeriodoMal", "molt_a": "0..*"},
        {"nome": "areaSog", "da": "AreaVerde", "molt_da": "1..1", "a": "SoggVerde", "molt_a": "0..*"},
        {"nome": "areaTipo", "da": "AreaVerde", "molt_da": "0..*", "a": "TipoArea", "molt_a": "1..1"},
        {"nome": "areaInt", "da": "AreaVerde", "molt_da": "1..1", "a": "Intervento", "molt_a": "0..*"},
        {"nome": "intSog", "da": "SoggVerde", "molt_da": "0..*", "a": "Intervento", "molt_a": "0..*"},
        {"nome": "intTipo", "da": "Intervento", "molt_da": "0..*", "a": "TipoInt", "molt_a": "0..*"},
        {"nome": "attInt", "da": "Intervento", "molt_da": "0..*", "a": "Attrezzo", "molt_a": "0..*"},
        {"nome": "attOpe", "da": "Attrezzo", "molt_da": "0..*", "a": "Operatore", "molt_a": "0..*"},
        {"nome": "", "classe": "intSqu", "da": "Intervento", "molt_da": "0..*", "a": "Squadra", "molt_a": "0..1"},
        {"nome": "parSqu", "da": "Squadra", "molt_da": "1..1", "a": "Partecipa", "molt_a": "0..*"},
        {"nome": "opePar", "da": "Partecipa", "molt_da": "0..*", "a": "Operatore", "molt_a": "1..1"},
        {"nome": "capSqu", "da": "Squadra", "molt_da": "1..1", "a": "Capo", "molt_a": "0..*"},
        {"nome": "capOpe", "da": "Capo", "molt_da": "0..*", "a": "Operatore", "molt_a": "1..1"},
    ],
    "generalizzazioni": [
        {"padre": "SoggVerde", "figlie": ["SoggRim"], "vincolo": ""},
        {"padre": "AreaVerde", "figlie": ["Fruibile", "NonFruibile"], "vincolo": DISJ},
        {"padre": "Fruibile", "figlie": ["Sensibile"], "vincolo": ""},
        {"padre": "Partecipa", "figlie": ["Capo"], "vincolo": ""},
    ],
}

CITTAVERDE_USECASE = {
    "nome": "Citta Verde — use-case",
    "attori": ["Comune", "Management", "Operatore", "Sistema"],
    "usecase": ["GestisciVerde", "GestisciAttrezzi", "GestioneSquadra", "GestioneInterventi",
                "AreeSensibili", "InterventiEseguiti", "CercaSquadre", "TassoMalattia"],
    "associazioni": [
        {"nome": "", "da": "Comune", "molt_da": "", "a": "GestisciVerde", "molt_a": ""},
        {"nome": "", "da": "Comune", "molt_da": "", "a": "GestisciAttrezzi", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "GestioneSquadra", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "GestioneInterventi", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "AreeSensibili", "molt_a": ""},
        {"nome": "", "da": "Operatore", "molt_da": "", "a": "InterventiEseguiti", "molt_a": ""},
        {"nome": "", "da": "Sistema", "molt_da": "", "a": "CercaSquadre", "molt_a": ""},
        {"nome": "", "da": "Sistema", "molt_da": "", "a": "TassoMalattia", "molt_a": ""},
    ],
    "generalizzazioni": [],
}


def cittaverde_ristrutturato():
    """Fusione su SoggVerde (la sottoclasse SoggRim diventa dataRim opzionale piu' la
    causa opzionale), fusione su AreaVerde (la gerarchia diventa i booleani fruibile e
    sensibile), divisione su Capo (la sottoclasse di Partecipa diventa una classe a se',
    con inizio e fine propri). Identificatori tecnici dove servivano, domini SQL."""
    r = deepcopy(CITTAVERDE)
    r["nome"] = "Citta Verde — ristrutturato"
    c = r["classi"]
    for morta in ("SoggRim", "Fruibile", "NonFruibile", "Sensibile"):
        del c[morta]
    r["generalizzazioni"] = []
    c["SoggVerde"] = [["id", "Serial {id}"], ["dataPia", "Date"], ["dataRim", "Date [0..1]"],
                      ["lat", "Real"], ["long", "Real"], ["rischio", "Rischio"]]
    c["AreaVerde"] = [["nome", "Stringa {id}"], ["fruibile", "Bool"], ["sensibile", "Bool"]]
    c["TipoMisura"] = [["id", "Serial {id}"], ["nome", "Stringa"], ["unita", "Stringa"]]
    c["misSog"] = [["valore", "RealGZ"]]
    c["PeriodoMal"] = [["id", "Serial {id}"], ["inMal", "Date"], ["fineMal", "Date [0..1]"]]
    c["Intervento"] = [["id", "Serial {id}"], ["inInt", "Date"], ["durataGg", "IntGZ"],
                       ["fineInt", "Date [0..1]"], ["nPers", "IntGZ"], ["prio", "Prio"]]
    c["intSqu"] = [["istAcq", "Timestamp"]]
    c["Partecipa"] = [["id", "Serial {id}"], ["inPar", "Date"], ["finePar", "Date"]]
    c["Capo"] = [["id", "Serial {id}"], ["inizio", "Date"], ["fine", "Date"]]
    # `cauRim` non parte piu' dalla sottoclasse ma dalla classe fusa
    for a in r["associazioni"]:
        if a["nome"] == "cauRim":
            a["a"] = "SoggVerde"
    return r


# ───────────────────────────────────────────── My Precious (progetto 15, studente-A)

MYPRECIOUS = {
    "nome": "My Precious — concettuale",
    "classi": {
        "Nazione": [["nome", "Stringa {id}"]],
        "Citta": [["nome", "Stringa {id1}"]],
        "Autore": [["nomeAut", "Stringa {id}"], ["annoNas", "Intero"],
                   ["annoMor", "Intero [0..1]"]],
        "Categoria": [["nome", "Stringa {id}"]],
        "Tecnica": [["nome", "Stringa {id}"]],
        "Corrente": [["nome", "Stringa {id}"]],
        "Opera": [["nomeOpe", "Stringa"], ["annoOpe", "Intero"], ["prestabile", "Booleano"]],
        "Prestito": [["inizioPre", "DataOra"], ["finePre", "DataOra"]],
        "PrestitoDato": [],
        "PrestitoPreso": [],
        "Museo": [["nome", "Stringa"]],
        "Restauro": [["inizioRes", "DataOra"], ["finePres", "DataOra [0..1]"]],
        "Esposizione": [["inizioEsp", "DataOra"], ["sezione", "Stringa"]],
        "EspPerm": [],
        "EspTemp": [["fineEsp", "DataOra"], ["nomeEsp", "Stringa"]],
        "Tema": [["nome", "Stringa {id}"]],
        "Biglietto": [["dataBigl", "Data"]],
        "BiglFull": [],
        "BiglPerm": [],
        "BiglTemp": [],
    },
    "associazioni": [
        {"nome": "citNaz", "da": "Nazione", "molt_da": "1..1 {id1}", "a": "Citta", "molt_a": "0..*"},
        {"nome": "autCit", "da": "Citta", "molt_da": "1..1", "a": "Autore", "molt_a": "0..*"},
        {"nome": "autOpe", "da": "Autore", "molt_da": "1..1", "a": "Opera", "molt_a": "0..*"},
        {"nome": "catOpe", "da": "Categoria", "molt_da": "1..1", "a": "Opera", "molt_a": "0..*"},
        {"nome": "opeTec", "da": "Tecnica", "molt_da": "0..1", "a": "Opera", "molt_a": "0..*"},
        {"nome": "corOpe", "da": "Corrente", "molt_da": "0..*", "a": "Opera", "molt_a": "0..*"},
        {"nome": "opePre", "da": "Opera", "molt_da": "1..1", "a": "Prestito", "molt_a": "0..*"},
        {"nome": "opeRes", "da": "Opera", "molt_da": "1..1", "a": "Restauro", "molt_a": "0..*"},
        {"nome": "espOpe", "da": "Opera", "molt_da": "0..*", "a": "Esposizione", "molt_a": "0..*"},
        {"nome": "musPre", "da": "Museo", "molt_da": "1..1", "a": "Prestito", "molt_a": "0..*"},
        {"nome": "espTema", "da": "Tema", "molt_da": "1..1", "a": "EspTemp", "molt_a": "0..*"},
        {"nome": "bigEsp", "da": "EspTemp", "molt_da": "1..1", "a": "BiglTemp", "molt_a": "0..*"},
    ],
    "generalizzazioni": [
        {"padre": "Prestito", "figlie": ["PrestitoDato", "PrestitoPreso"], "vincolo": DISJ},
        {"padre": "Esposizione", "figlie": ["EspPerm", "EspTemp"], "vincolo": DISJ},
        {"padre": "Biglietto", "figlie": ["BiglFull", "BiglPerm", "BiglTemp"], "vincolo": DISJ},
    ],
}

MYPRECIOUS_USECASE = {
    "nome": "My Precious — use-case",
    "attori": ["PatrimonioArtistico", "Management", "Biglietteria"],
    "usecase": ["GestioneOpere", "GestioneRestauri", "GestioneEsposizioni", "GestionePrestiti",
                "StatisticheOpere", "GestioneBiglietti", "StatisticheBiglietti"],
    "associazioni": [
        {"nome": "", "da": "PatrimonioArtistico", "molt_da": "", "a": "GestioneOpere", "molt_a": ""},
        {"nome": "", "da": "PatrimonioArtistico", "molt_da": "", "a": "GestioneRestauri", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "GestioneEsposizioni", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "GestionePrestiti", "molt_a": ""},
        {"nome": "", "da": "Management", "molt_da": "", "a": "StatisticheOpere", "molt_a": ""},
        {"nome": "", "da": "Biglietteria", "molt_da": "", "a": "GestioneBiglietti", "molt_a": ""},
        {"nome": "", "da": "Biglietteria", "molt_da": "", "a": "StatisticheBiglietti", "molt_a": ""},
    ],
    "generalizzazioni": [],
}


def myprecious_ristrutturato():
    """Tre gerarchie fuse verso l'alto, ognuna con il suo discriminante: `dato` sul
    prestito, `temp` sull'esposizione (con fineEsp e nomeEsp resi opzionali) e `temp`
    opzionale sul biglietto, dove NULL e' il terzo caso (full). Identificatori tecnici e
    domini SQL; espTema e bigEsp si allentano, perche' la gerarchia non li vincola piu'."""
    r = deepcopy(MYPRECIOUS)
    r["nome"] = "My Precious — ristrutturato"
    c = r["classi"]
    for morta in ("PrestitoDato", "PrestitoPreso", "EspPerm", "EspTemp",
                  "BiglFull", "BiglPerm", "BiglTemp"):
        del c[morta]
    r["generalizzazioni"] = []
    c["Opera"] = [["id", "Serial {id}"], ["nomeOpe", "Stringa"], ["annoOpe", "Integer"],
                  ["prestabile", "Bool"]]
    c["Autore"] = [["nomeAut", "Stringa {id}"], ["annoNas", "Integer"],
                   ["annoMor", "Integer [0..1]"]]
    c["Prestito"] = [["id", "Serial {id}"], ["inizioPre", "Timestamp"],
                     ["finePre", "Timestamp"], ["dato", "Bool"]]
    c["Museo"] = [["id", "Serial {id}"], ["nome", "Stringa"]]
    c["Restauro"] = [["id", "Serial {id}"], ["inizioRes", "Timestamp"],
                     ["finePres", "Timestamp [0..1]"]]
    c["Esposizione"] = [["id", "Serial {id}"], ["inizioEsp", "Timestamp"],
                        ["fineEsp", "Timestamp [0..1]"], ["sezione", "Stringa"],
                        ["nomeEsp", "Stringa [0..1]"], ["temp", "Bool"]]
    c["Biglietto"] = [["id", "Serial {id}"], ["dataBigl", "Date"], ["temp", "Bool [0..1]"]]
    for a in r["associazioni"]:
        if a["nome"] == "espTema":
            a["molt_da"], a["a"] = "0..1", "Esposizione"
        if a["nome"] == "bigEsp":
            a["da"], a["molt_da"], a["a"] = "Esposizione", "0..1", "Biglietto"
    return r


TUTTI = [
    ("2023-01-13-EasyToll-concettuale", EASYTOLL),
    ("2023-01-13-EasyToll-ristrutturato", easytoll_ristrutturato()),
    ("2023-01-13-EasyToll-usecase", EASYTOLL_USECASE),
    ("2023-01-30-Slimmy-concettuale", SLIMMY),
    ("2023-01-30-Slimmy-ristrutturato", slimmy_ristrutturato()),
    ("2023-01-30-Slimmy-usecase", SLIMMY_USECASE),
    ("2023-09-11-CozyRooms-concettuale", COZYROOMS),
    ("2023-09-11-CozyRooms-ristrutturato", cozyrooms_ristrutturato()),
    ("2023-09-11-CozyRooms-usecase", COZYROOMS_USECASE),
    ("2024-01-16-DKLCloud-concettuale", DKLCLOUD),
    ("2024-04-03-TimeBank-concettuale", TIMEBANK),
    ("2024-04-03-TimeBank-ristrutturato", timebank_ristrutturato()),
    ("2024-04-03-TimeBank-usecase", TIMEBANK_USECASE),
    ("2020-09-04-SafeOnTheBeach-concettuale", SAFEONTHEBEACH_CONCETTUALE),
    ("2020-09-04-SafeOnTheBeach-ristrutturato", safeonthebeach_ristrutturato()),
    ("2020-09-04-SafeOnTheBeach-usecase", SAFEONTHEBEACH_USECASE),
    ("progetto-CittaVerde-concettuale", CITTAVERDE),
    ("progetto-CittaVerde-ristrutturato", cittaverde_ristrutturato()),
    ("progetto-CittaVerde-usecase", CITTAVERDE_USECASE),
    ("progetto-MyPrecious-concettuale", MYPRECIOUS),
    ("progetto-MyPrecious-ristrutturato", myprecious_ristrutturato()),
    ("progetto-MyPrecious-usecase", MYPRECIOUS_USECASE),
]

# SafeOnTheBeach non e' uno svolgimento di studente: viene dal sito del docente, e i suoi
# diagrammi stanno di conseguenza sotto `docente-ufficiale/`.
DEST_DOCENTE = QUI.parent / "docente-ufficiale" / "diagrammi"
RADICE = {"SafeOnTheBeach": DEST_DOCENTE}


if __name__ == "__main__":
    for nome, spec in TUTTI:
        # "2023-01-13-EasyToll-concettuale" -> EasyToll/concettuale/
        data, sistema, tipo = nome.rsplit("-", 2)[0], nome.rsplit("-", 2)[1], nome.rsplit("-", 2)[2]
        cartella = RADICE.get(sistema, DEST) / sistema / tipo
        cartella.mkdir(parents=True, exist_ok=True)
        descrizione = cartella / f"{nome}.json"
        descrizione.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
        subprocess.run([sys.executable, str(QUI / "genera-vpp-xml.py"),
                        str(descrizione), str(cartella / f"{nome}.xml")], check=True)
