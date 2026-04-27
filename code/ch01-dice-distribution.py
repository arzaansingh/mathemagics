"""Generate the bar chart of P(X = k) for X = sum of two fair dice.

Used as a margin figure in Chapter 1, §1.1, Example 1.2.
Output: figures/ch01/dice-distribution.pdf

Run from the repo root:
    python code/ch01-dice-distribution.py
"""
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt

# Project-local imports (resolve from the script's directory).
sys.path.insert(0, str(Path(__file__).parent))
from mathemagics_style import setup_plot, COLORS  # noqa: E402

setup_plot()

# X = sum of two fair dice. P(X = k) = #{(i,j): i+j = k} / 36 for k = 2..12.
ks = np.arange(2, 13)
counts = np.array([min(k - 1, 13 - k) for k in ks])
probs = counts / 36.0

fig, ax = plt.subplots(figsize=(2.6, 1.65))
bars = ax.bar(
    ks, probs,
    width=0.72,
    color=COLORS["def"],
    edgecolor=COLORS["thm"],
    linewidth=0.5,
    alpha=0.85,
)

ax.set_xlabel(r"$k$", fontsize=8, labelpad=2)
ax.set_ylabel(r"$\mathbb{P}(X = k)$", fontsize=8, labelpad=4)
ax.set_xticks(ks)
ax.set_xticklabels([str(k) for k in ks], fontsize=6.5)
ax.set_yticks([0, 1 / 12, 1 / 6])
ax.set_yticklabels(["0", r"$\frac{1}{12}$", r"$\frac{1}{6}$"], fontsize=7)
ax.set_xlim(1.5, 12.5)
ax.set_ylim(0, 0.185)

# Annotate the peak (k = 7) so the eye lands on it
ax.annotate(
    "peak\n(6 outcomes)",
    xy=(7, 6 / 36),
    xytext=(9.5, 0.15),
    fontsize=6.5,
    color=COLORS["aside"],
    arrowprops=dict(
        arrowstyle="->",
        color=COLORS["aside"],
        lw=0.5,
        shrinkA=2,
        shrinkB=2,
    ),
)

# Save under figures/ch01/
out_dir = Path(__file__).resolve().parent.parent / "figures" / "ch01"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "dice-distribution.pdf"
fig.savefig(out_path, format="pdf")
plt.close(fig)
print(f"Saved {out_path}")
