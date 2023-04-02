---
title: conclusion
layout: center
---

## Conclusion : une diversité d'approches

---
title: conclusion
layout: center
---

|  | **argparse** | **docopt** | **click** | **fire** |
|---|---|---|---|---|
| **approche** | API design de CLI | regexp sur docstring | décorateur sur code métier | inspection du code métier |
| **design** | orienté-CLI<br />(-> nestable parser) | orienté-CLI<br />(-> aide) | orienté-métier | orienté-métier (nested objects) |
| **typage des valeurs** | API du parser | str ou bool | API des décorateurs | heuristique interne (annotations ignorées 😕) |
| **verbosité** et **couplage** | parser verbeux +/- couplé aux fonctions métier | verbosité fonction de la docstring (syntaxe élaborée) | couplage des fonctions métier aux décorateurs empilés | 0 boilerplate, le code est métier-first (avec des hacks pour la CLI) |
| **documentation** | champs *description* ou *help* | la docstring source | champs *help* et docstring de fonction | docstring et signature de fonctions / méthodes |

<!--
Pour ou contre CLick ?
- http://xion.io/post/programming/python-dont-use-click.html
- https://click.palletsprojects.com/en/8.1.x/why/
-->

---
title: conclusion
layout: center
---

# Merci !
