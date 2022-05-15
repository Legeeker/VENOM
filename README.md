# VENOM

# Projet d'informatique Othello , Adel Chafik et Mourad Aarab 

Ce projet consiste en la réalisation d'une intelligence artificielle (IA) pour le jeu Othello.
Notre IA qui sera le client devra interagir avec le serveur pour pouvoir se connecter.
Cela nous permettra d'échanger des informations avec le serveur afin de respecter certaines conditions pour démarrer le championnat . 
## Stratégie utilisée
Notre projet se base sur une fonction :  
    -bestcoup()

Cette fonction permet de jouer les meilleurs coups possibles face à une IA random. 
Le principe est simple : lorsque le serveur nous envoie une requette de certaines cases de possibilité à jouer , la fonction sélectionnera les cases censées être les mieux jouées (via la fonction possibleMove). 

Les meilleures cases sont principalement les coins (bestcoup). 
La fonction bestcoup renvoie du meilleur coup possible à jouer au pire coup c'est à dire que si aucun meilleur coup est à jouer , il devra être obliger de jouer un coup pas très utile . 


## Listes des requêtes / réponses : 

### Inscription : 

Afin de pouvoir jouer, le client doit s'inscrire sur celui-ci. Pour cela, il doit envoyer un message sous format Json au serveur contenant ses données, en communiquant au serveur qui se trouve sur le port 3000.

Contenu du message : 

```json
{
"request": "subscribe",
"port": port,
"name": name,
"matricules": ["20132", "20104"]
}
```



Si tout se passe correctement, le serveur répond : 

```json
{
   "response": "ok"
}
```


### Vérification de la présence : 


 Afin de vérifier si le client est toujours connecté, le serveur envoie régulièrement des requêtes "ping" sur le port mentionné lors de l'inscription, auxquelle nous devons répondre "pong".

Requête ping : 

```json
{
   "request": "ping"
}
```
Réponse : 

```json
{
   "response": "pong"
}
```
Réponse en cas d'erreur:
```json
{
   "response": "error",
   "error": "error message"
}
```json
### Requête de coup : 



Lorsque c'est au tour du joueur de donner son coup, le serveur envoit une requête play au client qui devra renvoyer son coup .


Requête play du serveur : 

```json
{
   "request": "play",
   "lives": 3,
   "errors": list_of_errors,
   "state": state_of_the_game
}
```

La variable lives donne le nombre de vies restantes du joueur, chaque joueur a 3 vies par match et en perd une à chaque mauvais mouvement effectué. Si le nombre de vies tombe à 0, le joueur perd.

La variable errors liste les raisons pour lesquelles les coups joués étaient mauvais.

La variable state donne l'état du jeu, elle contient différentes informations nécessaires au client afin qu'il puisse décider comment jouer. 

La réponse du client est: 

```json
{
   "response": "move",
   "move": the_move_played,
   "message": "Fun message"
}
```
La variable Players donne les noms des joueurs inscris au match, le premier joueur représente celui qui joueura en premier avec les pions noirs. 

La variable current donne l'indice dans la liste Players du joueur devant donner son coup.

La variable board donne le plateau de jeu. 

### Lancement du jeu 

Pour lancer le jeu , il faut tout d'abord se connecter au serveur (vérifier que l'addresse correspond bien (ligne 15 du code) ). 
Ensuite il faut lancer le terminal et lancer le fichier VENOM . Après ça le jeu peut commencer .

### Bibliothèques utilisées
-'json'
-'pytest'
-'game'
-'socket'
-'random'
-'copy'
