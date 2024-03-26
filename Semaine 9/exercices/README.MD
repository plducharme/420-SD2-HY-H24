# Exercices

## Source des données
Source masses moléculaires: https://powderprocess.net/Tools_html/Data_Diagrams/Chemical_Compound_Molecular_Weight.html

## Comparateur de tris
1) Le module *comparateurtris.py* permet de comparer les divers temps d'exécution des tris
    - C'est le module que vous allez exécuter pour lancer la comparaison des tris
    - Vous pouvez modifier la liste des tris comparés (vers la ligne 66)
2) Le module *visualisateurresultats.py* contient une application Pyside6 pour visualiser les résultats
   - Vous devrez installer les packages "matplotlib" et "PySide6"
   - Vous pouvez regarder le code si ça vous dit, c'est un exemple du cadriciel utilisé dans le prochain cours (420-SD3)
3) Vous devez implémenter chaque Tri dans chacun leur module
   - Les Tris implémentent la classe abstraite Tri (voir Tri.py)
   - Chaque Tri est dans son propre fichier (voir les modules importés dans *comparateurtris.py*)
   - Le Tri Shell est une amélioration du tri par insertion. Pour plus d'informations et le pseudo-code:
     https://fr.wikipedia.org/wiki/Tri_de_Shell
4) Les objets à comparer sont définis par la classe molécules. Les molécules sont automatiquement importées par *comparateurtris.py*.
   - Vous pouvez ajouter la surcharge des opérateurs pour la comparaison
5) Analyser les résultats
   - L'augmentation de temps en fonction du nombre d'éléments
   - La différence de performance si vous avez des _print()_ ou si vous n'en avez pas
   - Changer le code de la classe DataUtils dans *comparateurtris.py* pour que les listes retournées soient aléatoires au
   lieu des X premiers éléments chargés.
     - Regarder si une autre distribution des données donne des résultats différents.