import dico
from pile import Pile


def distance(mot1,mot2,k):
    """
    :param mot1: Le premier mot
    :param mot2: Le second mot
    :param k: La longueur des mots
    :return: calcule la distance entre 2 mots de k lettres
    """
    i = 0
    dist = 0
    while i < k:
        if mot1[i] != mot2[i]:
            dist = dist + 1
        i =i + 1
    return dist


def creation():
    """
    :return: dictionnaire des mots adjacents au mot de la liste
    """
    g={}
    for element1 in dico.DICO:
        liste=[]
        for element2 in dico.DICO:
            if distance(element1,element2,4) == 1:
                liste.append(element2)
        g[element1] = liste
    return g
graphe=creation()
print(graphe['ours'])


###########################################################
# rajouter votre classe pile ici

############################################################
def Solution(end, parents):
    """
    :param end: Le mot d'arrivée
    :param parents: Dictionnaire associant chaque mot à celui qui l'a précédé
    :return: La liste ordonnée des mots du départ jusqu'à l'arrivée.
    """
    solution = []
    courant = end
    while courant != None:
        solution = [courant] + solution
        courant = parents[courant]
    return solution


def solve(graphe, depart, arrivee):
    """
    :param graphe: Le dictionnaire d'adjacence des mots
    :param depart: Le mot de départ
    :param arrivee: Le mot cible à atteindre
    :return: Le chemin trouvé sous forme de liste de mots
    """
    candidats = Pile()
    candidats.empiler(depart)
    visite = dict()
    visite[depart] = None
    trouve = False
    while candidats.vide() == False and not trouve:
        courant = candidats.depiler()
        if courant == arrivee:
            trouve = True
        else:
            for value in graphe[courant]:
                if not value in visite and not value in candidats.elements:
                    visite[value] = courant
                    candidats.empiler(value)
    if trouve:
        return Solution(arrivee, visite)
    else:
        return None


print(solve(graphe, 'ours', 'cage'))