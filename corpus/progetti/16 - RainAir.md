# 16 - RainAir

> Fonte: `RainAir - Testo.pdf` (progetto P.20050704, non presente fra i 15 del corso: viene dalla raccolta di studente-A).
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina.

---

Progetto 20050704 (P.20050704)
                                       RainAir
                                                                             Progetto P.20050704

    RainAir
    2. Speciﬁca dei Requisiti
                 Speciﬁca dei Requisiti
              Per l’applicazione sono di interesse i clienti (con nome, cognome ed indirizzo di resi-
              denza), i voli aerei, tutti giornalieri, e le prenotazioni fatte dai clienti. In particolare,
              dei voli interessa codice (una stringa), numero di miglia percorse, orari ed aeroporti di
              partenza ed arrivo (ad es., il volo “RA 1234” parte ogni giorno alle 13:50 dall’aeroporto
              di Roma Ciampino e arriva a Londra Stansted alle 15:50, percorrendo 1000 miglia), ed
              il velivolo usato, mentre delle prenotazioni è importante conoscere il momento in cui
              vengono eﬀettuate.
              Degli aeroporti da cui partono e arrivano voli bisogna rappresentare il codice (una
              stringa di 3 caratteri, ad es. “CIA”) il nome, la città e lo stato dove è collocato, e
              l’ammontare delle tasse di decollo e atterraggio.
              Dei velivoli è di interesse conoscere codice (una stringa), tipo, numero di posti e
              costo al miglio (ovvero quanto il velivolo costa alla compagnia per ogni miglio di volo).
              Dei biglietti di un volo è di interesse conoscere il loro “prezzo base”, base di partenza
              per il calcolo del prezzo ﬁnale. Il prezzo base dipende dal costo che la compagnia deve
              sostenere per eﬀettuare il volo. Quest’ultimo è dato da due addendi: (i) il prodotto tra
              il numero di miglia eﬀettuate e il costo al miglio del velivolo in uso e (ii) la somma delle
              tasse di decollo e atterraggio negli aeroporti di partenza e arrivo, rispettivamente. Il
              prezzo base di un biglietto è dato dal costo su descritto diviso per il numero di posti del
              velivolo, e incrementato del 20% (che è il ricarico che la compagnia vuole applicare).
              Una prenotazione da parte di un cliente può essere relativa anche a più voli (almeno
              uno). Di ogni volo prenotato, interessa la data in cui il cliente vuole volare, ed il numero
              di posti richiesti.
              Una prenotazione può, ma non obbligatoriamente, essere relativa anche ad un hotel,
              nel qual caso interessa conoscere la data di check-in, quella di check-out, e il numero di
              stanze prenotate (si ignorino, per semplicità, le diverse tipologie di stanze). Di un hotel
              sono di interesse il nome, l’indirizzo, la categoria (ovvero il numero di stelle, da una a
              cinque), la tariﬀa per stanza per notte, la città dove è collocato, la distanza dal centro
                                                                             Progetto P.20050704

    RainAir
    2. Speciﬁca dei Requisiti
              cittadino, e la possibile informazione sull’aeroporto più vicino, con relativa distanza (le
              distanze siano tutte in Km).
              Alcuni clienti sono “frequent ﬂyers”. Di questi interessa conoscere il codice, la data
              di aﬃliazione, e il numero di miglia che hanno accumulato ﬁno ad un certo momen-
              to. Il numero di miglia accumulate ﬁno al momento richiesto è la somma delle miglia
              guadagnate con le prenotazioni eﬀettuate a suo nome per voli prenotati dopo la data
              di aﬃliazione, ed eﬀettuati ﬁno a quel momento. In particolare, il guadagno di miglia
              relative ad un singolo volo è pari al numero di miglia percorse dal volo per il numero di
              posti prenotati. Se una prenotazione è relativa a più voli, le miglia guadagnate sono la
              somma di quelle relative ad ogni singolo volo.
              Inoltre, sono previsti beneﬁci per le prenotazioni che includono anche hotel (indipen-
              dentemente dalle date di check-in e check-out). In particolare, le miglia relative ad una
              prenotazione raddoppiano se questa prevede anche un hotel ﬁno a 4 stelle, e triplicano
              se l’hotel prenotato è a 5 stelle.
              Il Sistema prenotazioni (un sistema esterno) necessita di calcolare il numero di posti
              disponibili all’istante corrente su un dato volo di una certa data. Il numero di posti
              disponibili è calcolato a partire dal numero di posti del velivolo che eﬀettua il volo in
              questione, diminuito del numero di posti già prenotati (all’istante corrente).
              Il Sistema prenotazioni deve anche poter calcolare il prezzo complessivo, all’istante
              corrente, di un certo numero di biglietti per un volo di un dato giorno. Tale prezzo è
              da considerarsi valido solo nel caso in cui il volo disponga, al momento corrente, di un
              numero suﬃciente di posti per la data richiesta, e si calcola moltiplicando il prezzo di
              un biglietto singolo per il numero di biglietti richiesti.
              Il prezzo di un singolo biglietto è altamente ﬂessibile, ed è composto da diverse
              componenti, dovute a diversi fattori:
                1. Il prezzo base, che dipende dal volo;
                2. Il numero di posti disponibili al momento corrente per la data di volo richiesta.
              Il calcolo del prezzo del biglietto parte dal suo prezzo base, e subisce poi delle modiﬁche
              a seconda della disponibilità attuale di posti sulla data di volo richiesta. In particolare,
              al prezzo base si applica la seguente regola: se il numero di posti disponibili al momento
              della prenotazione per il volo in questione è maggiore della metà dei posti totali (ovvero
              quelli del velivolo che eﬀettua il volo), si applica uno sconto del 2% per ogni posto libero
              oltre la metà. Al contrario, se il numero di posti disponibili è minore della metà, si
              applica un sovrapprezzo del 2% in modo del tutto analogo. Ad esempio, se il velivolo
              che eﬀettua il volo ha 100 posti in totale, e, al momento della prenotazione, ne sono
              ancora liberi 53 per la data di volo richiesta, si applicherà uno sconto del 2% al prezzo
              base per tre volte (cosa diversa dall’applicare il 6% di sconto), mentre, se i posti liberi
              fossero 47, si applicherebbe un sovrapprezzo del 2% per tre volte.
              Il Sistema prenotazioni vuole oﬀrire anche il seguente servizio: data una città e una
              tariﬀa massima, vuole suggerire un insieme di hotel in quella città che abbiano tutti una
                                                                             Progetto P.20050704

    RainAir
    2. Speciﬁca dei Requisiti
              tariﬀa al più pari a quella indicata. La scelta degli hotel avviene secondo le seguenti
              regole (a parte quella sulla tariﬀa, che deve essere sempre rispettata):
                 • Farà parte del risultato l’hotel più vicino al centro della città in questione con
                 tariﬀa entro la soglia; sia questo hotel A.
                 • Farà inoltre parte del risultato qualunque altro hotel con lo stesso numero di stelle
                 di A che abbia una distanza dal centro pari al più il 110% di quella di A.
                 • Inﬁne, faranno parte del risultato anche quegli hotel che hanno più stelle di A, ma
                 più lontani di A dal centro. In particolare, quelli per cui la distanza dal centro sia
                 al massimo il 120% di quella di A.
                                                                             Progetto P.20050704
