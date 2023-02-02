# TP2 Construire un index minimal
# Description du projet
Nous voulons extraire le nombre de fichiers, le nombre de jetons et le nombre moyen de jetons par fichier pour les urls dans le fichier crawled_urls.json. Les informations sur l'index sont écrites dans le fichier title.non_pos_index.json et les statistiques dans le fichier metadata.json.
Dans le fichier index_TP2, nous construisons l'index pour ce faire. L'index web a été construit et des statistiques ont été obtenues sur la base de la tokenisation du texte et de la construction d'un vocabulaire.
Comme le fichier source contient 500 urls, il est trop long de toutes les récupérer. L'utilisateur peut donc définir la plage de recherche en modifiant les positions de début et de fin et le délai d'attente.

## Etapes de la mise en place
* Connectez ce github `git clone https://github.com/ZZZIXUAN/TP1-Construire-un-crawler-minimal.git`
* Changez de répertoire `cd TP-1-Construire-un-crawler-minimal`
* Installez les exigences en exécutant `pip3 install -r requirements.txt`
* Exécutez le programme en utilisant `python3 main.py` (Exécutez avec les valeurs par défaut)
* Exécutez les tests en utilisant `python3 -m unittest discover`

### Contributeur

Zixuan WANG