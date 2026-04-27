"""Distribution sandbox sample output: empirical histogram + theoretical PMF/PDF.

Used as Figure 2.4 in Chapter 1, §1.2.6 (Distribution sandbox), and as a
preview of what readers will see when they run the live Colab notebook.

Output: figures/ch01/sandbox-sample.pdf

Run from the repo root:
    python code/ch01-distribution-sandbox.py
"""
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from mathemagics_style import setup_plot, COLORS  # noqa: E402

setup_plot()

rng = np.random.default_rng(seed=2026)

fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.0))

# --- LEFT: Bin(20, 0.3) — 5,000 samples vs theoretical PMF --------------
ax = axes[0]
n_bin, p_bin, n_samples = 20, 0.3, 5_000
samples = rng.binomial(n_bin, p_bin, size=n_samples)
ks = np.arange(0, n_bin + 1)
emp_freq = np.bincount(samples, minlength=n_bin + 1) / n_samples
theoretical = stats.binom.pmf(ks, n_bin, p_bin)

ax.bar(ks - 0.18, emp_freq, width=0.35, color=COLORS["def"],
       edgecolor=COLORS["thm"], linewidth=0.4, label="empirical")
ax.bar(ks + 0.18, theoretical, width=0.35, color=COLORS["intu"],
       edgecolor=COLORS["thm"], linewidth=0.4, label="theoretical")
ax.set_title(f"Discrete: Bin$(n{{=}}{n_bin},\\,p{{=}}{p_bin})$, "
             f"$N{{=}}{n_samples:,}$", fontsize=9, pad=4)
ax.set_xlabel("$k$", fontsize=8, labelpad=2)
ax.set_ylabel("probability", fontsize=8, labelpad=4)
ax.set_xticks([0, 5, 10, 15, 20])
ax.legend(loc="upper right", fontsize=7, frameon=False)

# --- RIGHT: Normal(0, 1) — 5,000 samples vs theoretical PDF -----------
ax = axes[1]
samples = rng.normal(loc=0, scale=1, size=n_samples)
ax.hist(samples, bins=40, density=True, color=COLORS["recap"],
        edgecolor=COLORS["thm"], linewidth=0.3, alpha=0.55,
        label="empirical")
xs = np.linspace(-4, 4, 400)
ax.plot(xs, stats.norm.pdf(xs), color=COLORS["aside"], lw=1.5,
        label="theoretical")
ax.set_title(f"Continuous: $\\mathcal{{N}}(0, 1)$, $N{{=}}{n_samples:,}$",
             fontsize=9, pad=4)
ax.set_xlabel("$x$", fontsize=8, labelpad=2)
ax.set_ylabel("density", fontsize=8, labelpad=4)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.5)
ax.set_xticks([-3, 0, 3])
ax.legend(loc="upper right", fontsize=7, frameon=False)

plt.subplots_adjust(wspace=0.3)

# Save
out_dir = Path(__file__).resolve().parent.parent / "figures" / "ch01"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "sandbox-sample.pdf"
fig.savefig(out_path, format="pdf")
plt.close(fig)
print(f"Saved {out_path}")
