
import pandas as pd
from statistics import mean, median, stdev
import numpy as np

explorer_df = pd.read_csv("./parcours_explorateurs.csv")

# Filtrer le dataframe pour obtenir les listes de noeuds de départ et d'arrivée
array_starting_node = explorer_df[explorer_df["type_aretes"] == "depart"]["noeud_amont"].values
array_arrival_node = explorer_df[explorer_df["type_aretes"] == "arrivee"]["noeud_aval"].values

# Créer un dictionnaire associant des noeuds amonts à des noeuds avals
dict_upstream_downstream = {row["noeud_amont"]: row["noeud_aval"] for _, row in explorer_df.iterrows()}

# Créer une liste pour stocker les longueurs de tous les chemins
all_path_lengths = []

for starting_node in array_starting_node:
    current_path = [starting_node]
    while current_path[-1] not in array_arrival_node:
        current_node = current_path[-1]
        next_node = dict_upstream_downstream[current_node]
        current_path.append(next_node)

    # Ajouter la longueur du chemin courant à la liste de toutes les longueurs de chemin
    all_path_lengths.append(len(current_path))

    print(current_path)

# Trouver le chemin le plus long et sa longueur
longest_path = max(all_path_lengths)
print("Chemin le plus long:", [path for path in array_starting_node if len(path) == longest_path - 1][0])
print("Longueur du chemin le plus long:", longest_path)

# Trouver le chemin le plus court et sa longueur
shortest_path = min(all_path_lengths)
print("Chemin le plus court:", [path for path in array_starting_node if len(path) == shortest_path - 1][0])
print("Longueur du chemin le plus court:", shortest_path)

# Calculer les métriques
mean_length = mean(all_path_lengths)
median_length = median(all_path_lengths)
std_dev_length = stdev(all_path_lengths)
q75, q25 = np.percentile(all_path_lengths, [75, 25])
interquartile_range = q75 - q25

# Afficher les métriques
print("Moyenne des longueurs de chemin:", mean_length)
print("Médiane des longueurs de chemin:", median_length)
print("Écart-type des longueurs de chemin:", std_dev_length)
print("Écart interquartile des longueurs de chemin:", interquartile_range)
