# Projet-Bomberman

## TOINE
```markdown
- Fonction `get_explosions` à définir :
  ```python
  def get_explosions(self: Grille) -> List[Case where explode == True]:
  ```

- Ajout d'un attribut `all_bombs` dans la grille qui recense toutes les bombes de la grille :
  ```python
  all_bombs: List[Bomb]
  ```

- Fonction `get` à définir, avec inversion abscisse et ordonnée dans la recherche par indice dans `self.cases` (self.cases[y][x]) :
  ```python
  def get(self: Grille, x, y) -> Case:
  ```

## JULES

- Lignes 41 à 75 dans Backend à optimiser/réduire.

- Mouvement du Bomber à modifier :
  - Déplacement par pixel plutôt que par case.
  - Appartenance aux cases donc à revoir également (comment le changement de case est détecté, mise à jour de `case.bomber`).

- Test du travail effectué jusqu'ici (si possible).

## SUITE

- Travail de l'interface avec pyxel :
  - Recherches animations.
  - Développement des méthodes.
  - Test/débogage (IMPORTANT) FIN.
  - Documentation, commentaires (présentation).

## ANNEXES
```

N'oubliez pas de remplacer les sections telles que `Grille`, `Case`, `Bomb`, etc., par les détails spécifiques à votre projet. Assurez-vous également d'ajouter des explications supplémentaires ou des exemples de code si nécessaire.
