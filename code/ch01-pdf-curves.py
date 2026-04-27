"""Three PDF curves side by side: Uniform, Normal, Exponential.

Used as Figure 2.2 in Chapter 1, §1.2.3 (Continuous: the PDF).
Output: figures/ch01/pdf-curves.pdf

Run from the repo root:
    python code/ch01-pdf-curves.py
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

# --- Uniform on [0, 1] ---------------------------------------------------
ax = axes[0]
xs = np.linspace(-0.4, 1.4, 600)
ys = stats.uniform.pdf(xs, loc=0, scale=1)
ax.fill_between(xs, ys, color=COLORS["def"], alpha=0.35)
ax.plot(xs, ys, color=COLORS["def"], lw=1.4)
ax.set_title("Uniform on $[0,1]$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_ylabel("$f_X(x)$", fontsize=8, labelpad=4)
ax.set_xlim(-0.4, 1.4)
ax.set_ylim(0, 1.4)
ax.set_xticks([0, 0.5, 1])
ax.set_yticks([0, 1])

# --- Normal(0, 1) --------------------------------------------------------
ax = axes[1]
xs = np.linspace(-3.5, 3.5, 600)
ys = stats.norm.pdf(xs, loc=0, scale=1)
ax.fill_between(xs, ys, color=COLORS["intu"], alpha=0.35)
ax.plot(xs, ys, color=COLORS["intu"], lw=1.4)
ax.set_title("Normal $\\mathcal{N}(0, 1)$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(0, 0.5)
ax.set_xticks([-3, 0, 3])
ax.set_yticks([0, 0.4])

# --- Exponential(1) -----------------------------------------------------
ax = axes[2]
xs = np.linspace(-0.4, 4.5, 600)
ys = np.where(xs >= 0, stats.expon.pdf(xs, scale=1), 0)
ax.fill_between(xs, ys, color=COLORS["recap"], alpha=0.35)
ax.plot(xs, ys, color=COLORS["recap"], lw=1.4)
ax.set_title("Exponential$(\\lambda{=}1)$", fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_xlim(-0.4, 4.5)
ax.set_ylim(0, 1.2)
ax.set_xticks([0, 2, 4])
ax.set_yticks([0, 1])

plt.subplots_adjust(wspace=0.35)

# Save
out_dir = Path(__file__).resolve().parent.parent / "figures" / "ch01"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "pdf-curves.pdf"
fig.savefig(out_path, format="pdf")
plt.close(fig)
print(f"Saved {out_path}")
