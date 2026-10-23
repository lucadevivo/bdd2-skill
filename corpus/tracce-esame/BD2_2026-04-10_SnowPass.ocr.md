# BD2_2026-04-10_SnowPass — testo riconosciuto automaticamente

> **Non e' il documento: il documento e' `BD2_2026-04-10_SnowPass.pdf`.** Questo testo viene da un OCR
> (tesseract, italiano, 300 dpi) di una scansione, e contiene errori. Serve per
> *cercare* fra le tracce; una volta trovata quella giusta si apre il PDF e si legge
> quello. In questo corso una parola sbagliata cambia una molteplicita'.

---

## Pagina 1

Sapisnza Universtà di Roma
Facoltà di Ing. dell'Informazione, Informatica e Statstica, Laurea i informanica
insegnamento di Basi di Dati, IMAodulo 2
Proff. Toni Mancini, Marco Esposto
Dipartimento di Informatica
bttps:/ fraise unirotnalit ftsaching

Edsme Es. 20260410 — Prova scrittà del 10 aprile 2025

Sì vuole progettare SnowPass, un sistema informativò per la gestionà uniiacata degl SMGpasa ©
degli accessi agli impianti di risalita di un grande cornsorzia sciistico. H sistema dovrà gestire le
anagrafiche, la validità dei titoli di viaggio e tracciare in dettaglio l'utiiizzo degh immprareti de parte
degli sciatori,

l consorzio comprende diversi comprenzori sciistici, Di ogni comprensonti Bteres5a CONOSCETE i
nome (iunivoco, es. “Dolomiti Superski”), la regione geografica in cui 5è trova, l’attiudare miratia €
massima (in metri sul livello del mare).

All’interno di ogni comprensorio sono presenti diversi impianti di rsslita. DN ogei empesstà
interessa un codice alfanumerico (univoco a fivello di consorzio), Éi nome, la tipologia {5 “Funaid .
‘“Seggiovia”, “Skilift”, “Cabinovia”) e la portata oraria massima (espressa in rageero di persone aill'ara}

Gli impianti servono le piste da sci. Di ogni pista si vuole memorizzare À nome {univoco all atarso

del comprensorio), la lunghezza in metri è la difficoltà. La difficottà è ciasezfarata medizrde i colon
standard ("Verde”, “Blu", “Rossa”, "Nera”). Nel sistema deve esgere mantens l'informazione cna
quali impianti danno accesso a quali piste, Si noti che un imipianto può dare accesso 3 puù P==
(anche di difficoltà diverse), e una singola pista puù essere raggiungibile tramita impignti GAterenti.
| clienti del sistema sono gli sciatori. Di ogni sciatore interessa mamvrigzarè d eod= fecoie
(univoco), il nome, il cognome, la data di nascità e un indirizzo email di comtatto. Gi scistori
interagiscono con il sistema acquistando gli skipass, che rappresentano i ro titoli di viaggio.
Ogni skipass è caratterizzato da un numero di serie univoco, la data è l'ora di emissione, d prezzò
pagato è lo sciatére proprietario.
Gli skipass si divideno in due categonie disgiunte:

. “Skipass a Tempao”: consentono accessi illimitati entro una certa finestra temporale. DE ss
interessa la data di inizio e la data di fine validità (es. giornaliero, settimanale, stagionale].

-%maa?unﬁ":mdmaﬁdim;aìduwnﬁiﬁàak.da…;dm;d@:aﬁìuu Di
essi interassa il saldo residuo.

tornello, il sistema registra un transito. Di ogni transito si deveé memorizzare l'istanta esatto (data
e cra), lo skipass utilizzato e l'impianto a cuiì si è acceduto. inoltre, per gestire correttamente g
ddnaa5:punﬁ.id;tunadewemwinae'ﬂ'cmh…ﬁ'diduumknﬁrﬂnàiu:a&a

l sistema deve applicare severi controlli: deve garantire che un transito avvenga solo se lo skipass
rhaJtaval:îtiu[l’ist:antedd…imwprmmlad:hdìhiàuuﬁﬁu:wiﬁmi;ump-u.ui
saldo residuo è sufficiente per i titoli a punti). Inoltre, per evitare l'uso fraudolento da parte di prù
w…-'dﬂùm#wn.iﬁmunamdne…ammﬁpmﬁ…h

tflililll…lb……a meno di 5 minuti di distanza l’uno dall'altro.

«D;n;am…tmmm,uimlr:pun;nî…i'…de;h:imd:…
effettuato accessi a impianti di almeno due tipologie diverse (es. hanno usato aimeno una

1

## Pagina 2

volta una “Funivia” e almeno una volta una “Seggiovia”). Per ciascuno di questi sciatori, sì
vuole ottenere il nome, il cognome e il numero totale di transiti effettuati nel comprensorio in

quel mese.

e Gli amministratori del consorzio vogliono identificare le piste potenzialmente più affollate per
programmare la battitura della neve. Si vuole calcolare l’insieme delle piste per le quali la
somma della portata oraria massima di tutti gli impianti che danno accesso a esse è massima.
