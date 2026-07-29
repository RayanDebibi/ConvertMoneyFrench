# ConvertMoneyFrench
J'ai crée mon deuxième programme en Python. Un convertisseur de devises(uniquement ceux de la banque centrale européenne).
## Comment il marche?
Le programme demande la liste des devises qu'il à l'API Frankfurter puis il demande la devise de départ ainsi que le montant et la devise d'arrivée
Il vérifie que les 2 devises sont bien des devises compatibles avec l'API et que le montant est postif si ce n'est pas le cas il renvoie des messages difflrents pour chaque problème.
Il demande le montant_finl convertis à l'API et l'affiche pour l'utilisateur.
### Comment lancer

Il faut installer Python 3 et requests :
Pour requests : pip install requests 
Pour lancer programme : python ConvertMoneyFrench.py.
Exemple:
Quelle est la devise de départ (3 lettres)? eur
Quel est le montant de départ? 25
Quelle est la devise d'arrivée (3 lettres)? gbp

Avec 25.0 EUR, vous obtenez 21.409 GBP

#### Ce que j'ai appris
À faire attention à l'orthographe (request avec un s etc..)
À appeler une API
Convertir la réponse en dico

##### Améliorations
Intégrer d'autres devises
Créer interface web
Avoir une sortie de secours (si API ne répond plus ou change de lien) 