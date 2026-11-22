# EuroSAT Assistant

Projet du module ISEP IG.3513 : assistant IA multimodal sur le dataset
[EuroSAT](https://arxiv.org/abs/1709.00029) (images satellite Sentinel-2 RGB, 64×64, 10 classes).

L'assistant permet de :
- **classer** une image satellite (baseline classique et modèle deep learning) ;
- **générer** des images synthétiques d'une classe donnée (modèle génératif conditionnel) ;
- **répondre à des questions** sur l'occupation des sols à partir d'une base documentaire (RAG) ;
- **orchestrer** ces outils depuis une interface unique.

> Le dépôt contient pour l'instant l'infrastructure du projet : les composants sont à implémenter.

## Stack

| Composant | Outils |
|-----------|--------|
| Baseline | scikit-image (features), scikit-learn (classifieur) |
| Classifieur DL | PyTorch, torchvision |
| Modèle génératif | PyTorch (VAE, GAN ou diffusion) |
| LLM et embeddings | Ollama (en local) |
| RAG et orchestration | LangChain, Chroma ou FAISS |
| Interface | Gradio |

## Arborescence

```
.
├── configs/default.yaml     # configuration unique (graine, chemins, hyperparamètres)
├── splits/                  # splits train/val/test figés (versionnés)
├── data/                    # dataset EuroSAT (ignoré par Git)
├── models/                  # poids entraînés (ignorés par Git)
├── notebooks/               # exploration (EDA, analyses)
├── knowledge_base/
│   ├── raw/                 # documents sources du RAG
│   └── sources.md           # référence et licence de chaque document
├── reports/
│   ├── figures/             # figures du rapport
│   └── metrics/             # métriques produites par les scripts d'évaluation
├── docs/                    # documentation complémentaire
├── src/
│   ├── config.py            # chargement de la configuration
│   ├── interfaces.py        # contrats entre composants (Prediction, Classifier, ...)
│   ├── data/                # classes, téléchargement, splits, transformations, datasets
│   ├── baseline/            # features + classifieur classique
│   ├── dl/                  # classifieur deep learning
│   ├── generative/          # modèle génératif conditionnel
│   ├── rag/                 # ingestion, retriever, chaîne RAG
│   ├── tools/               # composants exposés comme outils
│   └── app/                 # orchestrateur et application Gradio
└── tests/                   # tests
```

Les classes EuroSAT sont définies **uniquement** dans `src/data/classes.py`, et tout prétraitement
d'image passe par `src/data/transforms.py`.

## Installation

Prérequis : Python 3.11 ou plus récent, Git.

```bash
git clone <url-du-dépôt>
cd <dossier-du-dépôt>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Vérifier l'installation :

```bash
ruff check .
pytest
```

### Ollama

1. Installer Ollama : https://ollama.com/download
2. Récupérer les modèles choisis dans `configs/default.yaml` (`rag.llm_model`, `rag.embedding_model`) :
   ```bash
   ollama pull <modèle-llm>
   ollama pull <modèle-embeddings>
   ```
3. Vérifier que le serveur répond : `ollama list`.

## Reproduire les expériences

Toutes les commandes se lancent depuis la racine du dépôt avec le venv activé.
La graine et les hyperparamètres sont lus dans `configs/default.yaml`.

| Étape | Commande |
|-------|----------|
| Télécharger les données et figer les splits | _à compléter_ |
| Entraîner et évaluer la baseline | _à compléter_ |
| Entraîner et évaluer le classifieur DL | _à compléter_ |
| Entraîner et évaluer le modèle génératif | _à compléter_ |
| Construire la base vectorielle et évaluer le RAG | _à compléter_ |

### Poids des modèles

Les poids ne sont pas versionnés dans Git. Lien de téléchargement : _à compléter_
(GitHub Releases ou Drive). Les placer dans `models/`.

## Lancer l'application

```bash
python -m src.app.app
```

## Licences et sources

- **EuroSAT** : « EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover
  Classification », IEEE JSTARS, 2019 (https://arxiv.org/abs/1709.00029).
  Licence : _à vérifier et compléter_.
- **Base de connaissances** : voir `knowledge_base/sources.md`.
- **Modèles pré-entraînés et LLM** : _à compléter_ (nom, source, licence).
