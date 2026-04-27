# Colab notebooks

This directory holds the Colab notebooks (and local copies) referenced from the simulation boxes in *Mathemagics*. Each chapter that has a simulation box references a notebook here.

## Index

| Notebook | Chapter | Topic | Colab link |
|---|---|---|---|
| `04-clt.ipynb` | 4 | CLT in pictures | _placeholder_ |
| `16-marchenko-pastur.ipynb` | 16 | MP as N grows | _placeholder_ |
| `17-tracy-widom.ipynb` | 17 | TW1 from GOE top eigenvalue | _placeholder_ |
| `18-qq-plots.ipynb` | 18 | QQ-plot diagnostic suite | _placeholder_ |
| `20-bbp-transition.ipynb` | 20 | BBP transition sweep | _placeholder_ |
| `21-spectral-clustering.ipynb` | 21 | Spectral clustering on synthetic data | _placeholder_ |

## Conventions

- Each notebook has a clear title cell pointing back to the chapter and section.
- All code is Python 3 with NumPy, SciPy, scikit-learn, and Matplotlib.
- Random seeds are set at the top of every notebook for reproducibility.
- Long-running cells are flagged.

## How to add a new notebook

1. Create the notebook in Colab.
2. Save a local copy in this directory.
3. Add a row to the index table above.
4. Reference the notebook in the appropriate chapter via `\colablink{name}{url}`.
5. Add the entry to `appendices/C-code-listings.tex`.
