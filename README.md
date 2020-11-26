# Commit-RollBack-Operation-in-Python
## BENSAMMAR Mohamed Aimene 
## MERAD Fouad Fouzi
### Master 2 STDS

#### 1- Avant la transaction :
![Capture1](https://user-images.githubusercontent.com/74276606/100378533-99561700-3013-11eb-8acf-f18fb964226d.PNG)

#### 2- faire une modification sur la table fournisseur en changeant 'fouadmerad@yahoo.com' à 'fouadmerad@gmail.com'
![Capture4](https://user-images.githubusercontent.com/74276606/100378757-023d8f00-3014-11eb-89c0-a3266c5d17f6.PNG)

####    ça change dans l'affichage python mais pas dans la base de données
![Capture5](https://user-images.githubusercontent.com/74276606/100379092-9f98c300-3014-11eb-9c9a-e581afb3d84c.PNG)
![Capture1](https://user-images.githubusercontent.com/74276606/100378533-99561700-3013-11eb-8acf-f18fb964226d.PNG)

#### 3- on utilise commit dans le code (décommenter conn.commit()).  dans ce cas on voit que la valeur est changée dans la base de données
![Capture3](https://user-images.githubusercontent.com/74276606/100379376-11710c80-3015-11eb-8796-2d036625fa88.PNG)

#### 4- Rollback si il y a des erreurs elle annule les modifications et elle rend l'ancien résultat
