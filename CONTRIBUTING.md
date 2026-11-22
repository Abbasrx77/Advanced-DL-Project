# Contribuer

## Branches

- Une branche par composant : `feature/<composant>` (ex. `feature/baseline`, `feature/rag`).
- **Jamais de push direct sur `main`** : tout passe par une pull request.
- Toute PR est relue et approuvée par **un autre membre** de l'équipe avant d'être fusionnée.
- Remplir le modèle de PR (composant, résumé, comment tester, métriques, checklist).

## Commits

Format : `type(scope): message`

| Type | Usage |
|------|-------|
| `feat` | nouvelle fonctionnalité |
| `fix` | correction de bug |
| `docs` | documentation |
| `exp` | expérience (config, entraînement, résultats) |
| `chore` | maintenance, outillage, dépendances |

Exemples : `feat(data): add split loading`, `docs(readme): add install steps`.

## Données et poids

- **Aucune donnée ni aucun poids de modèle dans Git.** `data/` et `models/` sont ignorés.
- Les poids sont partagés via GitHub Releases ou Drive, et le lien est ajouté dans le README.
- Toute source de la base de connaissances est référencée dans `knowledge_base/sources.md`
  (URL, licence, date de consultation).

## Rigueur expérimentale

- Les splits sont figés une fois pour toutes dans `splits/`.
- Le **test set sert uniquement à l'évaluation finale**. Les choix de modèles et
  d'hyperparamètres se font sur la validation.
- La graine (`seed`) est notée dans chaque config, et chaque résultat est associé à sa config.
- Les classes viennent de `src/data/classes.py` et le prétraitement de `src/data/transforms.py`.
  Ils ne doivent pas être redéfinis ailleurs.

## Avant d'ouvrir une PR

```bash
ruff check .
pytest
```
