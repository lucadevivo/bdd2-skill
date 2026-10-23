# 03 - TuTubi

> Fonte: `(03) Progetto TuTubi - BD2.pdf`
> Estratto con PyMuPDF (conserva legature e formule); tolte le righe ripetute di intestazione e pie' di pagina e le etichette sparse dei diagrammi, che sono ritagliati in `figure/` e richiamati nel punto in cui compaiono.

---

Progetto 20080401 (P.20080401)
                                        TuTubi
                                                                             Progetto P.20080401

    TuTubi
                           Indice
              Indice
              Introduzione
              Specifica dei Requisiti
                                                                             Progetto P.20080401

    TuTubi
    1. Introduzione
                 Introduzione
              Si vuole progettare e realizzare TuTubi, un sistema informatico da usarsi su un portale
              Web per la pubblicazione e condivisione di file video da parte degli utenti registrati. Il
              sistema deve permettere la memorizzazione dei video e la loro visualizzazione da parte
              degli utenti. Questi devono poter anche esprimere valutazioni e commenti.
                                                                             Progetto P.20080401

    TuTubi
    2. Specifica dei Requisiti
                 Specifica dei Requisiti
              TuTubi deve consentire la registrazione degli utenti, di cui interessa il nome e la data
              di iscrizione. Gli utenti registrati possono pubblicare video, visualizzare quelli disponibili,
              oltre che esprimere su di essi valutazioni e commenti testuali.
           In particolare, di un video pubblicato da un utente interessa conoscere il titolo, la
           durata e la descrizione (oltre che il nome del file dove questo viene memorizzato da
           parte del sistema).
           Inoltre, di ogni video interessa conoscere la categoria (unica) a
           cui appartiene, oltre che un insieme di parole chiave dette tag (almeno una) che ne
           descrivano il contenuto in modo più strutturato. Delle categorie e dei tag interessa il
           nome.
           TuTubi deve anche permettere ad un utente di pubblicare un nuovo video segnalando
           che si tratta di una risposta ad un video già esistente (utile per temi come la politica dove
           vi possono essere posizioni diverse che stimolano un dibattito). TuTubi deve mantenere
           tale informazione in modo consistente, garantendo che nessun utente possa pubblicare
           un video in risposta ad un video pubblicato da sé stesso.
           TuTubi deve poi fornire un servizio di cronologia, ricordando la sequenza di tutti i
           video visionati da ogni singolo utente, con relativa data e ora. Inoltre, per ogni video
           interessa conoscere il numero complessivo di volte che è stato visionato.
           Gli utenti di TuTubi devono inoltre avere la facoltà di esprimere una valutazione
           (un valore da 0 –pessimo– a 5 –ottimo) per ogni video che visionano. Tali valutazioni
           serviranno poi al sistema per promuovere i video più belli (cfr. seguito) e scovare i più
           brutti. Tuttavia, per evitare degenerazioni nel meccanismo delle votazioni, l’utente che
           ha pubblicato un video non può votarlo, mentre ogni altro utente può votarlo al più una
           volta, indipendentemente dal numero di volte che l’ha visionato. In ogni caso però deve
           essere impossibile per un utente votare un video che non ha mai visionato.
           Inoltre, per favorire uno spirito di comunità tra gli utenti del servizio, si prevede che
           questi possano esprimere commenti testuali ai video che visionano (dei quali interessa
           anche data e ora). A differenza delle valutazioni, un utente può esprimere più commenti
                                                                             Progetto P.20080401

    TuTubi
    2. Specifica dei Requisiti
              per lo stesso video.
              Anche qui, non deve essere permesso ad un utente di scrivere
              commenti per video che non ha mai visionato.
              Ogni utente può creare delle playlist personali, ovvero delle collezioni ordinate di
              video che gradisce vedere, oppure vuole condividere con altri utenti. Le playlist infatti
              (di cui interessa il nome e la data di creazione) possono essere pubbliche o private: solo
              le playlist pubbliche possono essere visualizzate dagli altri utenti. A tal fine, il sistema
              deve permettere ad ogni utente di ottenere le playlist pubbliche di un altro utente a sua
              scelta.
              TuTubi deve permettere ad un utente di iscriversi, pubblicare nuovi video, creare e
              modificare le sue playlist, ed esprimere valutazioni e commenti sui video che visiona.
              Inoltre, TuTubi deve consentire la ricerca di video: in particolare, data una categoria,
              un insieme di tag, ed un intero v tra 0 e 5, si vogliono restituire tutti i video disponibili
              di quella categoria che posseggono almeno uno tra i tag indicati, e che abbiano una
              valutazione media di almeno v (se un video non ha ancora alcuna valutazione, deve
              essere restituito comunque). TuTubi deve poi permettere di cercare, data una categoria,
              i video di quella categoria che hanno il numero maggiore di video in risposta, al fine di
              isolare le discussioni più animate tra gli utenti.
              La redazione di TuTubi ha infine la facoltà di censurare dei video, ad esempio perché
              di contenuto coperto da copyright, osceno, ecc. Un video censurato non può essere né
              visionato, né votato, né commentato, né aggiunto ad alcuna playlist, né restituito come
              risultato di una ricerca. Un video, una volta censurato, non può tornare più visibile. Il
              motivo di una censura deve essere mantenuto nel sistema per usi interni.
                                                                             Progetto P.20080401
