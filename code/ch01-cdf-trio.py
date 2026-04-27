"""Three CDFs side by side: Bernoulli (staircase), Uniform (ramp), Normal (S).

Used as Figure 2.3 in Chapter 1, §1.2.4 (The CDF: unifying object).
Output: figures/ch01/cdf-trio.pdf

The point of this figure: the CDF is the unifying object that handles
discrete, continuous, and even mixed RVs through a single formal device.

Run from the repo root:
    python code/ch01-cdf-trio.py
"""
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from mathemagics_style import setup_plot, COLORS  # noqa: E402

setup_plot()

fig, axes = plt.subplots(1, 3, figsize=(7.0, 1.8))

# --- Bernoulli(0.6) staircase --------------------------------------------
ax = axes[0]
p = 0.6
# CDF: 0 for x<0, 1-p for 0<=x<1, 1 for x>=1
xs = np.linspace(-0.6, 1.6, 600)
ys = np.where(xs < 0, 0, np.where(xs < 1, 1 - p, 1))
ax.plot(xs, ys, color=COLORS["def"], lw=1.5, drawstyle="steps-post")
# Open-circle markers at jumps (visual cue for right-continuity)
ax.plot([0], [0], "o", markerfacecolor="white",
        markeredgecolor=COLORS["def"], markersize=4, lw=1)
ax.plot([0], [1 - p], "o", markerfacecolor=COLORS["def"],
        markeredgecolor=COLORS["def"], markersize=4)
ax.plot([1], [1 - p], "o", markerfacecolor="white",
        markeredgecolor=COLORS["def"], markersize=4, lw=1)
ax.plot([1], [1], "o", markerfacecolor=COLORS["def"],
        markeredgecolor=COLORS["def"], markersize=4)
ax.set_title("Bernoulli$(p{=}0.6)$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_ylabel("$F_X(x)$", fontsize=8, labelpad=4)
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.05, 1.1)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1 - p, 1])
ax.set_yticklabels(["0", "$1{-}p$", "1"])

# --- Uniform on [0,1] linear ramp ---------------------------------------
ax = axes[1]
xs = np.linspace(-0.4, 1.4, 600)
ys = np.where(xs < 0, 0, np.where(xs < 1, xs, 1))
ax.plot(xs, ys, color=COLORS["intu"], lw=1.5)
ax.set_title("Uniform on $[0,1]$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_xlim(-0.4, 1.4)
ax.set_ylim(-0.05, 1.1)
ax.set_xticks([0, 0.5, 1])
ax.set_yticks([0, 1])

# --- Normal(0,1) S-curve ------------------------------------------------
ax = axes[2]
xs = np.linspace(-3.5, 3.5, 600)
ys = stats.norm.cdf(xs, loc=0, scale=1)
ax.plot(xs, ys, color=COLORS["recap"], lw=1.5)
ax.set_title("Normal $\\mathcal{N}(0, 1)$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-0.05, 1.1)
ax.set_xticks([-3, 0, 3])
ax.set_yticks([0, 0.5, 1])

plt.subplots_adjust(wspace=0.35)

# Save
out_dir = Path(__file__).resolve().parent.parent / "figures" / "ch01"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "cdf-trio.pdf"
fig.savefig(out_path, format="pdf")
plt.close(fig)
print(f"Saved {out_path}")
