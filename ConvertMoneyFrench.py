import requests

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

try:
    site_0 = requests.get("https://api.frankfurter.dev/v1/currencies")
    except requests.exceptions.RequestException:
        print("Impossible de contacter le serveur, vérifie stp ta connexion ou l'état de Frankfurter")
        exit()
    devises_acceptees = site_0.json()
    

def message_depart(devises_acceptees):
    print(f"Voici les devises acceptées {devises_acceptees}")
    print("Quelle est la devise de départ (3 lettres)?")
    devise_depart = input().upper()
    print("Quel est le montant de départ? (Utilisez . et pas ,)")
    montant_depart1 = input()
    if len(montant_depart1) == 0:
        print("Le montant de départ doit contenir quelque chose")
        exit()
    for lettre in alphabet:
        if lettre in montant_depart1:
            print("Le montant de départ doit avoir uniquement des nombres.")
            exit()
    try:
        montant_depart = float(montant_depart1)
    except ValueError:
        print("Vérifie le nombre stp ( pas de , mais .)")
        exit()
    print("Quelle est la devise d'arrivée (3lettres) ?")
    devise_arrivee = input().upper()
    return devise_depart, montant_depart, devise_arrivee


def verification_erreurs(devise_depart, montant_depart, devise_arrivee, devises_acceptees):
    if devise_depart not in devises_acceptees:
        print(f"{devise_depart} n'est pas dans la liste des devises acceptées, vérifie stp.")
        exit()
    if devise_arrivee not in devises_acceptees:
        print(f"{devise_arrivee} n'est pas dans la liste des devises acceptées, vérifie stp.")
        exit()
    if montant_depart <= 0:
        print("Le montant de départ doit être positif, vérifie stp.")
        exit()


def demande_site(devise_depart, montant_depart, devise_arrivee):
    try:
        donnes = requests.get(f"https://api.frankfurter.dev/v1/latest?amount={montant_depart}&from={devise_depart}&to={devise_arrivee}").json()
    except requests.exceptions.RequestException:
        print("Impossible de contacter le serveur, vérifie stp ta connexion ou l'état de Frankfurter")
        exit()
    montant_final = donnes["rates"][devise_arrivee]
    print(f"Avec {montant_depart} {devise_depart}, vous obtenez {montant_final} {devise_arrivee}")


devise_depart, montant_depart, devise_arrivee = message_depart(devises_acceptees)
verification_erreurs(devise_depart, montant_depart, devise_arrivee, devises_acceptees)
demande_site(devise_depart, montant_depart, devise_arrivee)