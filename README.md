# ConvertMoneyFrench

J'ai créé mon deuxième programme en Python. Un convertisseur de devises (uniquement celles de la Banque centrale européenne).

## Comment il marche ?

Le programme demande la liste des devises acceptées à l'API Frankfurter, puis il demande la devise de départ ainsi que le montant et la devise d'arrivée.

Il vérifie que les 2 devises sont bien compatibles avec l'API et que le montant est positif. Si ce n'est pas le cas, il renvoie des messages différents pour chaque problème.

Il demande ensuite le montant final converti à l'API et l'affiche pour l'utilisateur.

## Le site web

J'ai également laissé Bolt générer une interface avec mon code Python : https://currency-converter-u-hy2e.bolt.host

## Comment lancer

Il faut installer Python 3 et la bibliothèque requests.

Pour installer requests :

    pip install requests

Pour lancer le programme :

    python ConvertMoneyFrench.py

## Exemple

    Quelle est la devise de départ (3 lettres)? eur
    Quel est le montant de départ? 25
    Quelle est la devise d'arrivée (3 lettres)? gbp

    Avec 25.0 EUR, vous obtenez 21.409 GBP

## Ce que j'ai appris

- À faire attention à l'orthographe (requests avec un s, etc.)
- À appeler une API
- À convertir la réponse en dictionnaire
- Qu'un dictionnaire se lit par clé et pas par position comme une liste

## Améliorations

- Intégrer d'autres devises
- Créer une interface web
- Avoir une sortie de secours (si l'API ne répond plus ou change de lien)
- Le programme plante si on tape du texte au lieu d'un nombre