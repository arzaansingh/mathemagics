"""Mathemagics matplotlib style helper.

Locks every plot to the Mathemagics palette and typography per STYLE.md §6.3.
Every plot script in code/ should call setup_plot() at the top, before any
plt.* calls.
"""
from matplotlib import cycler
import matplotlib.pyplot as plt

# The 8-color locked palette, mirroring style/colors.tex.
COLORS = {
    "def":    "#5A9CCB",  # powder blue
    "thm":    "#2D2D2D",  # charcoal
    "intu":   "#B8901C",  # mustard
    "ex":     "#8B8378",  # warm gray
    "aside":  "#C57A5C",  # coral
    "recap":  "#50A076",  # mint
    "where":  "#8273A8",  # lilac
    "colab":  "#D4A028",  # soft gold
}

# Background tints (used for fill / shading)
COLORS_BG = {
    "def":    "#E8F2FB",
    "intu":   "#FBF3D9",
    "ex":     "#F5F2EE",
    "recap":  "#ECF5EE",
    "where":  "#F1ECF7",
    "colab":  "#FBF1D8",
}

# Default plot color cycle: leads with the calmer hues, saves coral / lilac
# for accents. Eight entries so longer cycles still wrap to a known color.
CYCLE = cycler(color=[
    COLORS["def"],    # powder blue
    COLORS["intu"],   # mustard
    COLORS["recap"],  # mint
    COLORS["aside"],  # coral
    COLORS["where"],  # lilac
    COLORS["colab"],  # soft gold
    COLORS["ex"],     # warm gray
    COLORS["thm"],    # charcoal
])


def setup_plot():
    """Apply the Mathemagics matplotlib defaults to plt.rcParams."""
    plt.rcParams.update({
        "axes.prop_cycle":     CYCLE,
        "axes.spines.top":     False,
        "axes.spines.right":   False,
        "axes.linewidth":      0.6,
        "axes.edgecolor":      "#666666",
        "axes.labelsize":      9,
        "axes.titlesize":      10,
        "axes.titleweight":    "normal",
        "xtick.labelsize":     8,
        "ytick.labelsize":     8,
        "xtick.color":         "#444444",
        "ytick.color":         "#444444",
        "xtick.major.width":   0.5,
        "ytick.major.width":   0.5,
        "xtick.major.size":    3,
        "ytick.major.size":    3,
        "font.family":         "serif",
        "font.size":           9,
        "lines.linewidth":     1.4,
        "patch.linewidth":     0.5,
        "patch.edgecolor":     "#444444",
        "grid.color":          "#cccccc",
        "grid.linewidth":      0.4,
        "figure.dpi":          150,
        "savefig.dpi":         200,
        "savefig.bbox":        "tight",
        "savefig.pad_inches":  0.04,
        "savefig.transparent": True,
    })
