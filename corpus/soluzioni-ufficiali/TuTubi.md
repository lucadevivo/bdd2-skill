# TuTubi — soluzione ufficiale

## Passo A.1 — Associazione valutazione

> Fonte: `Associazione valutazione.txt`

```
Specifica Associazione valutazione

[V.valutazione.utente_ha_visualizzato_video]
	Se (u:Utente, v:Video): valutazione allora deve esistere
		vis:Visualizzazione tale che:
			(u,vis): ut_vis,   (v, vis): vid_vis

	ALL u,v,i_val   valutazione(u,v) and istante(u,v i_val) -->
				EXISTS vis, i_vis    
					ut_vis(u,vis) and vid_vis(v,vis) and istante(vis, i_vis) and i_vis <= i_val.


[V.valutazione.utente_non_autore]
	Se (u:Utente, v:Video):valutazione allora deve non esistere
			(u,v):utente_pubblica_video

	Formalmente:

	ALL u, v    valutazione(u, v) --> 
					not utente_pubblica_video(u,v).



[V.valutazione.non_censurato]
	not EXISTS u, vid, i_val, i_cens
		Utente(u) and VideoCensurato(vid) and istante(u, vid, i_val) and
			istante(vid, i_cens) and i_cens < i_val.
```

## Passo A.1 — Classe Commento

> Fonte: `Classe Commento.txt`

```
Specifica Classe Commento


[V.Commento.visualizzazione_pregressa]
	ALL c, ic, u, v    
		Commento(c) and istante(c, ic) and
		comm_vid(c, v) and comm_ut(c, u)
			-->
				EXISTS vis, ivis   
					Visualizzazione(vis) and
					istante(vis, ivis) and ivis < ic and
					ut_vis(u, vis) and
					vid_vis(v, vis).
```

## Passo A.1 — Classe Video

> Fonte: `Classe Video.txt`

```
Specifica classe Video

[V.Video.autore_non_risponde_a_se_stesso]
	Per ogni r:Video, per cui esiste v:Video tale che
		(r,v): risponde_a_video

	sia:
		- u:Utente tale che:
			(u, r): pubblica
	Deve che (u,v) non è un link di pubblica.

	Formalmente:

	ALL r,v,u   Video(r) and Video(v) and Utente(u) and 
				pubblica(u,r) and 
				risponde_a_video(r,v) -->
								not pubblica(u,v)



[V.Video_non_rispone_a_video_gia_censurato]
	Per esercizio


durataSec() : Intero >= 0
	pre: nessuna
	post: 
		result = durataSec(this.flusso)

		Formalmente, result è tale che:   
			EXISTS f  flusso(this,f) and durataSec(f, result).



n_visualizzazioni(): Intero >= 0
	pre: nessuna
	post:
		result è il numero di oggetti v:Visualizzazione tali che:
			(this, v): vid_vis.

		Formalmente:

		result = | {  vis  |   
							Visualizzazione(vis) and 
							vid_vis(this, vis) 
				  } |.
```

## Passo A.1 — Classe Visualizzazione

> Fonte: `Classe Visualizzazione.txt`

```
Classe Visualizzazione


[V.Visualizzazione.non_censurato]
	not EXISTS vis, i_vis, vid, i_cens
		Visualizzazione(vis) and istante(vis, i_vis) and vid_vis(vid, vis) and
			VideoCensurato(vid) and istante(vid, i_cens) and i_cens < i_vis.
```

## Passo A.1 — Tipi di dato

> Fonte: `Tipi di dato.txt`

```
Specifica dei tipi di dato


FileVideo: 
 - sequenza di byte che codifica un flusso video
 - operazioni del tipo di dato
 		durataSec(f:FileVideo): Intero >= 0
 			pre: nessuna
 			post: result è la durata di 'f'


Voto : 0..5 			

TipoPlaylist = {pubblica, privata}
```
