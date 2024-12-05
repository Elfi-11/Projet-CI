# Projet-CI : 

# Collaborateur : 

Benjamin Mazars
François Talaban
Marina Estanco
Rémi Sauvere



# outil Git Hub ACtion, pourquoi?

*Avantages :

1 : Le projet est déjà sur le site Git Hub, du coup nous pouvons bénéficier de l'intégration native de Git Hub, ne nécessitant pas d'outil externe ;
2 : Support multiplateforme, prend en charge les environnments Linux, macOS et Windows ce qui permet de tester sous ces trois OS.
3 : Utilisation plus facile qu'un autre outil, car nous avons déjà les bases de Git Hub, permet de ne pas perdre de temps là dessus et les workflows sont configurés dans des fichiers YAML simples, ce qui correspond à notre projet.


*Inconvénient :
1 : Est payant pour les gros projets en cas que notre projet grossisse.
2 : Compléxicités des workflows dans le cas de gros projets, (encore une fois dans le cas ou il devrait grossir) car si complexes peuvent être difficiles à lire, en effet l'utilisation se fait par un seul fichier Yaml.
3 : Support limité, on s'enferme dans la logique git hub.




# Commande CI : 

git merge master --ff   (avance la branch dev avant main)
git ref log (voir les logs)

faire une branch dev, si le test est ok on push dans le main et on pull en local.

faire passer un commit et faire avancer le master sur le commit qu'on a fait!

si le test ne passe pas, il faut que l'outil créé une nouvelle branch failure et faire reculer la branch d'un commit en faisant un reset -hard. (Pour voir quand on doit corriger le commit) 

créer la branch dev + fichier Yaml.
et cleaner le git hub