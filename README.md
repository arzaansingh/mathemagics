# Mathemagics

*A Field Guide to Random Matrices and Spectral Clustering*

A textbook-style exposition of spectral theory of sample covariance matrices, building from probability foundations up to spiked covariance models and spectral clustering. Written by Arzaan Singh under the supervision of Prof. Gustavo Didier (Tulane University).

## Status

🚧 **Frame established, content fill-in in progress.**

The repository currently contains:

- A complete chapter/section skeleton (6 parts, 22 chapters, 5 appendices, 1 coda)
- Custom LaTeX class (`mathemagics.cls`) layered on top of `tufte-book`
- Five locked tcolorbox environments (`definition`, `theorem`, `intuition`, `example`, `aside`)
- Three structural recap macros (`\whereWeAre`, `\chapterRecap`, plus the cliff-notes track listing in the preface)
- Frontmatter (title, colophon, preface, notation, chapter dependency graph)
- Build infrastructure (`latexmkrc`, VS Code tasks, gitignore)

Content is filled in chapter by chapter as research progresses.

## Quick start

### Build

```bash
latexmk -pdf main.tex
```

This produces `main.pdf`. The `latexmkrc` enables `--shell-escape` for `minted` and runs `biber` for the bibliography.

### Edit

Open the folder in VS Code:

```bash
cd /path/to/Mathemagics
code .
```

VS Code will prompt you to install the recommended extensions (LaTeX Workshop, LaTeX Utilities, Code Spell Checker, Python, Jupyter). Accept; the build "just works" out of the box.

Keyboard shortcuts inside VS Code:

- **Build**: `Cmd+Alt+B`
- **View PDF (side-by-side)**: click the LaTeX-Workshop "View PDF" button in the toolbar
- **Forward search** (jump from `.tex` line to PDF location): `Cmd+Alt+J`
- **Inverse search** (jump from PDF back to source): `Cmd+Click` in the PDF

### Clean

```bash
latexmk -c    # remove intermediate files but keep main.pdf
latexmk -C    # remove everything including main.pdf
```

## Repository layout

```
Mathemagics/
├── main.tex              # master document
├── mathemagics.cls       # custom textbook class (built on tufte-book)
├── refs.bib              # bibliography
├── latexmkrc             # build configuration
├── .vscode/              # VS Code settings (LaTeX Workshop, tasks, spell-check)
├── style/                # colors, macros, environments
├── frontmatter/          # title, preface, notation, dependency graph
├── parts/                # six part dividers
├── chapters/             # 22 chapters (numbered 00–21)
├── coda/                 # closing chapter
├── appendices/           # solutions, notation, code listings, prereqs, reading list, index
├── figures/              # all figures (organized by chapter)
├── code/                 # standalone Python scripts that produce figures
└── colab-notebooks/      # Colab notebooks referenced from the simulation boxes
```

## Pedagogical conventions

The book targets a curious reader with high-school-level math, builds everything from first principles, and supports two reading speeds:

- **Cliff-notes track**: chapter openers, intuition boxes, figures, recaps. ~30% of the book by reading time.
- **Deep-diver track**: every theorem proved or sketched, every simulation reproducible.

Five tcolorbox environments do all the heavy lifting:

| Env | Visual | Purpose |
|---|---|---|
| `definition` | Blue tinted | Formal definition |
| `theorem` / `proposition` / `lemma` / `corollary` | White, dark rule | Formal claim |
| `intuition` | Cream | Plain-English version |
| `example` | Pale gray | Worked example |
| `aside` (margin) | Margin sans-serif | Tangent / history / fun |

All theorems, definitions, and examples share one counter (`mathemagicsCounter`) per chapter — easy to find by number.

## Source materials

The book draws on:

- Joseph Genzer's Tulane honors thesis, *Spectral Analysis of Multiscale Sample Covariance Matrices* (the structural seed)
- Ongoing meeting notes with Prof. Gustavo Didier (Spring 2026)
- Casella & Berger, *Statistical Inference*
- Strang, *Introduction to Linear Algebra*
- Vershynin, *High-Dimensional Probability*
- Bai & Silverstein, *Spectral Analysis of Large Dimensional Random Matrices*
- Anderson, Guionnet & Zeitouni, *An Introduction to Random Matrices*
- Tao, *Topics in Random Matrix Theory*
- Couillet & Debbah, *Random Matrix Methods for Wireless Communications*
- von Luxburg, *A Tutorial on Spectral Clustering*

## License

Source files licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The compiled book itself is intended for open distribution under the same license.

## Acknowledgments

- **Prof. Gustavo Didier** (advisor)
- **Joseph Genzer** (whose thesis is the structural foundation)
- **Tulane Department of Mathematics**
