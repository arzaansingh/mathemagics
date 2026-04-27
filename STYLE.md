# Mathemagics Style Guide

The single source of truth for how every chapter is written, designed, and audited. Read before starting a section, refer to during writing, and verify against before committing.

This document is **prescriptive**, when there's tension between "this is fast" and "this matches the guide," the guide wins. The point is consistency across 200 pages.

---

## 1. The non-negotiables

These are the rules that, if broken, the section gets sent back regardless of how good the content is:

1. **No paragraph indentation.** Block paragraphs only. Enforced at the class level.
2. **Lists, however, *are* indented.** Numbered and bulleted lists carry a left-margin indent so they read as visually distinct blocks from prose. Implemented via `enumitem` `\setlist` in `mathemagics.cls`. The block-paragraph rule applies to paragraphs only, not lists.
3. **No em dashes.** Neither `---` (LaTeX) nor `—` (Unicode). Use commas, semicolons, periods, or parentheses instead. En dashes (`--`) are still fine for numerical ranges (e.g., "pages 5–10"). Enforced by sweep before commit.
4. **Every page has at least one item in the right margin.** Even if it's a tiny callout. Empty margins are a bug.
5. **No inline icon graphics in body text.** TikZ icons (`\coin{H}`, `\die{3}`) belong in figures and in margin entries with room to be legible. In running prose, use plain text ("H", "T", "the outcome HH"). Inline icons at body-text size become unreadable.
6. **Default to in-house visualizations; reach for the right tool for each job.** TikZ for diagrams, matplotlib for data plots. When the *best* visualization of a concept already exists in published literature or open educational resources, reproducing it (faithfully or as a redrawing in our palette) with full attribution in the caption is allowed and sometimes preferred. AI-image-generator output is allowed for *purely illustrative cartoons* (a stylized character, a scene), saved as PNG with caption "Illustration generated for this book." The image generator is for cartoons and scenes, never for math diagrams.
7. **Research-first principle for new figures.** Before drawing a figure for any concept that appears in textbook literature, look at how 2–3 well-regarded sources have drawn it. Pick a pattern that is *known to work*. Only then start in TikZ. The "iterate until it looks OK" workflow burns time.
8. **Every figure passes a visual audit before commit.** The dependency-graph mishap (arrows passing through node interiors, text being clipped) and the Figure 2.1 v0.1/v0.2 mishaps (fanning arrows bunching, labels colliding with arrows) do not happen again.
9. **Voice is third person, present tense, collective "we."** Established by existing notes; matches the tone of Strang and Vershynin.
10. **Every theorem gets a picture or numerical experiment before its formal statement.** Picture before proof. Always.
11. **Every standard result is either proved in-line, sketched with pointer to chapter appendix, or cited.** No bare claims.
12. **Margin items must be visually linked to their body-text anchor.** Every margin entry (`\marginnote`, `\asideHistorical`, `\asideMatters`, `\marginfigure`) is paired with a colored dot (`\anchorDot{N}`) placed both in the body text at the relevant phrase *and* at the top of the margin item. Same `N`, same color, dot to dot. Five anchor colors cycle: 1 = coral, 2 = mint, 3 = lilac, 4 = gold, 5 = powder blue. Pick distinct numbers for adjacent anchors so neighbours don't collide. Margin items must also have **explicit visual breathing room** between them (`\marginGap` macro inserts ~1.4em of empty margin) so two adjacent items don't blend together.

13. **Audit spacing whenever a visual is resized.** If you change the size of an icon, cartoon, or figure, immediately check that *every container it sits in* still has enough breathing room around it: tabular row spacing, vertical gaps between margin items, distance from caption text, distance from body. Visuals that grow MUST be paired with a corresponding spacing increase, or shrunk back down. A picture that touches the next row, the page bottom, or another margin item is a regression. Audit gate: every commit that changes a `\foo`-bigsize macro or a `scale=` value must visually verify the surrounding layout.

---

## 2. Visual identity

### 2.1 Color palette

The palette is **soft pastel-academic**: light enough to feel airy, saturated enough that white title text remains legible on the rule color, and disciplined enough that nothing competes with the math. Eight colors do all the work. The palette is locked in `style/colors.tex`; do not introduce new colors anywhere else.

| Role                  | Primary (rule, accent) | Background tint   | Use                                    |
|-----------------------|------------------------|-------------------|----------------------------------------|
| Definition            | powder blue `#5A9CCB`  | `#E8F2FB`         | `definition` boxes                     |
| Theorem / Prop / Lem  | charcoal `#2D2D2D`     | white             | formal claims; minimal, restrained     |
| Intuition             | mustard `#B8901C`      | `#FBF3D9` (cream) | "plain English" boxes, lightbulb cue   |
| Example               | warm gray `#8B8378`    | `#F5F2EE`         | worked examples                        |
| Aside (margin)        | coral `#C57A5C`        | none (margin)     | margin asides, cartoon flag            |
| Recap (chapter end)   | mint `#50A076`         | `#ECF5EE`         | end-of-chapter recap box only          |
| Where-we-are (chap top) | lilac `#8273A8`      | `#F1ECF7`         | top-of-chapter mini-map only           |
| Colab badge           | soft gold `#D4A028`    | `#FBF1D8`         | Colab links and simulation boxes only  |

These eight colors are the entire visible spectrum of Mathemagics. Plots and TikZ figures **must** use only these (with optional alpha variants, `mathemagicsDef!50` etc.). If a chapter needs a "new" color for a plot, the answer is: choose two of the existing ones with different alpha levels.

> **Audit gate**: a figure that uses any color outside this list fails the visual audit.

### 2.2 Typography

- Body text: tufte-book default (Palatino-ish serif at 10pt, handled by class)
- Section headings: italic small-caps (tufte default)
- Margin notes: sans-serif, 8pt, with small caps title
- Code: monospace, 9pt, in `mathemagicsCodeBg`-tinted boxes
- Math: Computer Modern via `amsmath`, never override

### 2.3 Page anatomy

Every page in the book follows the Tufte rhythm:

```
+------------------------+----------+
| Main text (narrow)     | margin:  |
|   block paragraphs     |  figure  |
|   no indent            |  aside   |
|   ~70 chars/line       |  code    |
| Theorem 4.2            |  Colab   |
|  (boxed, narrow)       |  badge   |
+------------------------+----------+
```

- Main text column ≈ 60% of page width
- Margin column ≈ 35% of page width
- 5% gap

### 2.4 Margin rules

The margin is sacred. Discipline:

- **Required**: at least one margin item per page. Empty margins fail audit.
- **Capped**: at most 2 items per page (3 only on dense pages).
- **Never load-bearing**: if every margin entry on the page were deleted, every proof and definition still reads cleanly.
- **Hierarchy of margin item types**, in priority order:
  1. **Small figure / schematic**, most-preferred. Visual reinforcement of the math next to it.
  2. **Definition restatement / cross-reference**, "(Def. 3.1, p.42)" or a 2-line restated definition for the reader who's forgotten.
  3. **Citation pointer**, "see Casella & Berger §5.5".
  4. **Code snippet**, `\margincode{}`, ≤10 lines, illustrates the equation immediately to its left.
  5. **Aside**, historical, "why this matters," or cartoon. Three flavors only.
- **Cartoon asides get a star pictogram** so the reader knows it's optional.

---

## 3. Voice and tone

### 3.1 Point of view

Third person, present tense, collective "we" for the journey.

| Yes                                                           | No                                                  |
|---------------------------------------------------------------|-----------------------------------------------------|
| "We define the moment generating function as…"                | "You define the…" (too directive)                   |
| "The reader who has seen the CLT before will recognize…"      | "I will now show…" (no first-person singular)       |
| "Note that…"                                                  | "Notice you can…"                                   |
| "It is enough to verify…"                                     | "You'll need to verify…"                            |

The exception: chapter openers and exercise prompts may use second person ("In this chapter you'll see…").

### 3.2 Register

The register slides between two extremes deliberately:

- **Conversational** in chapter openers, intuition boxes, asides, and recaps.
- **Technical** in definitions, theorems, proofs.

The transition is signaled by the environment, not by tone shifting mid-paragraph. Good:

> **Intuition.** The MGF is just a clever way to package an entire distribution into a single function, like a smoothie of all the moments.
>
> **Theorem 2.4.** *If $M_X(t) = M_Y(t)$ on an open neighborhood of zero, then $X \stackrel{d}{=} Y$.*

Bad: a theorem statement that says "now you'll see…" Don't mix.

### 3.3 Sentence-level discipline

- Active voice in prose; passive only in formal statements when required.
- Jargon defined or `\vocab{...}`-marked on first use.
- Acronyms spelled out on first use per chapter, then abbreviated.
- One idea per sentence. Two for a long one. No three-clause monsters.

---

## 4. Chapter anatomy

### 4.1 Standard structure

Every content chapter (Chapters 1–21) follows this skeleton. Deviations require a one-sentence justification.

```latex
\chapter{Title}
\label{ch:slug}

\whereWeAre{
  Two-three sentences. What we're about to do, what we're using from earlier
  chapters, what this feeds.
}

% Chapter opener: 1 paragraph, includes a hook and a chapter-defining figure
% (the figure can live in the margin if the page is tight).
[Hook paragraph]

\section{Motivation}
[Why does this concept exist? A picture, a story, a question.]

\section{The simplest case}
\begin{definition}{Object}{def:slug-object}
  ...
\end{definition}
\begin{intuition}
  ...
\end{intuition}
\begin{example}{Trivial}{ex:slug-trivial}
  ...
\end{example}

\section{The main result}
\begin{theorem}{Name}{thm:slug-name}
  ...
\end{theorem}
\begin{intuition}
  ...
\end{intuition}
\begin{proof}[Sketch] ... \end{proof}

\section{Three perspectives}  % only for central results
\subsection*{Picture}
\subsection*{Sketch derivation}
\subsection*{Pointer to full rigor}

\section{Simulation}
\begin{colabbox}
  ...
\end{colabbox}

\section*{Brief warm-ups}
\begin{warmup}[\coffee{1}] ... \end{warmup}
\begin{warmupSolution} ... \end{warmupSolution}
[3-5 of these]

\chapterRecap{
  \begin{itemize}
    \item Punchline 1
    \item Punchline 2
    \item Punchline 3 (the most important one)
  \end{itemize}
}

\section*{Exercises}
\begin{exercise}[\coffee{1}] ... \end{exercise}
[8-15 of these, mix of difficulty]
% Solutions go in appendices/A-solutions.tex
```

### 4.2 Pedagogical patterns

These patterns are non-negotiable:

#### Picture before proof
Every theorem has either a figure, a numerical experiment, or a low-dimensional worked-out case **before** its formal statement. The reader sees what is true before being convinced of it.

#### Three perspectives (for central results only)
Marchenko–Pastur, Tracy–Widom, BBP transition, the spectral-clustering equivalences, these "load-bearing theorems of the book" each get presented three ways:
1. Heuristic / picture / numerical experiment.
2. Sketch derivation, or low-dimensional exact case.
3. Pointer to full rigorous proof (chapter appendix or "Optional rigor" subsection).

This is borrowed from von Luxburg's spectral-clustering tutorial. It's the difference between a book the reader bounces off and a book the reader internalizes.

#### Build then prove
Establish that something is true (with examples and simulations) before proving it. The formal proof comes when the reader already believes the statement.

#### Forward references are explicit
"We will see in Chapter 17 that…" is fine. A bare claim "the MP density vanishes like a square root at the edge" without saying when we'll prove it is not fine.

#### Cliff-notes track must be self-contained
A reader who reads only:
- Chapter openers
- `whereWeAre` boxes
- `intuition` boxes
- Figures and captions
- `chapterRecap` boxes

…must come away with the conceptual picture. Test by reading those alone after writing the chapter.

---

## 5. Math and notation

### 5.1 Notation discipline

All notation lives in `style/macros.tex`. **Never redefine inline.** If a new macro is needed, add it to `macros.tex` and document it in `appendices/B-notation.tex`.

Conventions already locked:

| Object              | Notation                |
|---------------------|--------------------------|
| Real numbers        | `\R`                    |
| Expectation         | `\E[X]`                 |
| Variance            | `\Var(X)`               |
| Population covariance | `\Sigma`              |
| Sample covariance (n obs) | `\Shat`           |
| Convergence (a.s./P/d) | `\convas`, `\convp`, `\convd` |
| Vectors             | `\vect{v}` (boldface)   |
| Matrices            | `\mat{M}` (boldface upper) |
| Identity matrix     | `I_p`                   |

### 5.2 Math typography

- Inline math: `$ ... $`
- Display math: `\[ ... \]` for unnumbered; `\begin{equation} ... \end{equation}` for numbered
- Multi-line aligned: `\begin{aligned} ... \end{aligned}` inside display
- Don't ever use `$$ ... $$` (deprecated)
- No bare `\mathbb{R}` in prose, always `\R`
- Punctuate display math: equations end with periods or commas as if they were sentences

### 5.3 Theorem culture

- Use `definition`, `theorem`, `proposition`, `lemma`, `corollary`, `example` from `style/environments.tex`. Five total tcolorbox environments; do not invent new ones.
- All these share one counter (`mathemagicsCounter`) per chapter, easy to find by number.
- `intuition` is unnumbered (it accompanies a definition or theorem; it's a viewpoint, not a claim).
- Every theorem's proof is either:
  - Inline immediately after.
  - Sketched inline with a pointer to a fuller proof in the chapter appendix.
  - Quoted from the literature with full citation.

---

## 6. Figures and visualizations

### 6.1 Two acceptable tools

- **TikZ**, for: dependency graphs, geometric diagrams, schematics, illustrations, cartoon asides.
- **matplotlib**, for: simulations, histograms, density plots, Q-Q plots, scatter clouds.

Other tools (mermaid, draw.io, hand drawing, photos) are rejected. The point is consistency and the ability to re-render at any zoom.

### 6.2 TikZ standards

- Always specify `>={Stealth[length=...]}` for arrowheads, never the default `latex` arrows.
- Always set `line width` explicitly, never default.
- Node sizes use explicit `minimum width` and `minimum height`.
- Spacing controlled by `node distance` or absolute positioning. Avoid relying on default spacing.
- **Forbidden**: any arrow that visibly passes through a node's interior. Use `to[bend left=N]`, `to[out=A,in=B]`, or reroute via an intermediate point.
- Every TikZ figure compiles in isolation, copy it into a minimal document, it should still build.

### 6.3 matplotlib standards

A helper module `code/mathemagics_style.py` (created when the first plot lands) sets:

- Color cycler from the palette (8 colors)
- Default figure size matching text-column width or margin width
- Sans-serif fonts, light grid
- Tight layout

Every plot script imports from this module. No bare `plt.plot(...)` without first calling the style setup.

### 6.4 Caption discipline

- Captions are **complete sentences ending in periods**.
- Captions describe **what the reader should see**, not the mechanics of the plot.
  - Bad: "Histogram of 5000 simulated GOE top eigenvalues."
  - Good: "Top eigenvalues of GOE matrices concentrate near $\sqrt{2N}$; the asymmetric tail on the left is the visual signature of Tracy–Widom."
- Every figure is referenced from text **before** the figure appears: "see Figure 4.2."

### 6.5 Reproducibility

- Every plot has a corresponding script in `code/`.
- Every plot file is committed as a `.pdf` (vector, infinite zoom) in `figures/chN-slug/`.
- Random seeds explicit in every script.

---

## 7. Code and simulations

### 7.1 Three placements (recap)

| Placement              | Macro                    | Purpose                           |
|------------------------|--------------------------|-----------------------------------|
| Inline                 | `\mintinline{python}|…|` | One-liners in prose               |
| Margin                 | `\margincode{...}`       | ≤10 lines next to its equation    |
| Full-width simulation  | `\begin{colabbox}…\end{colabbox}` | Proper experiments       |

### 7.2 Colab discipline

Every `colabbox`:
- Has a corresponding `.ipynb` notebook in `colab-notebooks/`.
- Margin contains a `\colablink{name}{url}` badge.
- Listed in `appendices/C-code-listings.tex`.
- Reproducible from a fresh Colab runtime in under 30 seconds.

### 7.3 Python conventions

- Python 3 only.
- Standard imports at top of every script:
  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  from mathemagics_style import setup_plot
  setup_plot()
  rng = np.random.default_rng(seed=2026)
  ```
- Comments explain "why," not "what."
- No `for i in range(len(...))`, `enumerate` or `zip`.
- Vectorize when possible.

---

## 8. Audit process

Every section passes a **three-stage audit** before being committed.

The audit checklist lives in [AUDIT.md](AUDIT.md) (created when first applied). Below is the spec.

### 8.1 Visual audit

Open the compiled PDF and look at every page touched by the section.

- [ ] No box overlap, no clipped text, no arrows through node interiors
- [ ] Every page has at least one margin item; no page has more than 2 (3 max in dense areas)
- [ ] No widow lines (single line at top of next page) or orphan lines (single line at bottom of section)
- [ ] Color palette compliance (only the 8 colors)
- [ ] Cross-references resolve (no `??` or boxed labels)
- [ ] Captions complete; figures numbered
- [ ] Margin notes don't extend past page margin
- [ ] Page breaks happen at clean paragraph boundaries

### 8.2 Logical audit

Read the section as a critical reviewer.

- [ ] Every concept defined before first use
- [ ] Forward references explicitly tagged ("we will see in §X")
- [ ] Section flow respects: motivation → definition → intuition → example → theorem → proof
- [ ] Picture-before-proof rule applied to every theorem
- [ ] Cliff-notes path through the section is self-contained
- [ ] Dependency-graph still consistent (if section changes, does the graph need updating?)

### 8.3 Content audit

- [ ] Voice is third-person, present-tense
- [ ] No bare claims, everything proved, sketched, or cited
- [ ] Notation matches `macros.tex`; no inline redefinitions
- [ ] Spell check passes (Code Spell Checker; expand workspace dict for new technical terms)
- [ ] All citations resolve (run `latexmk` and check `.log` for missing-key warnings)
- [ ] All `\vocab{}`-tagged terms also in notation index

### 8.4 When audit fails

The section is not committed. The failing items are flagged as `% AUDIT-FAIL: ...` comments in the source and fixed before re-attempting.

---

## 9. Workflow

### 9.1 One section at a time

Sections are the unit of work. A section is:
- 1 to 4 pages of finished content
- 1 day's work (roughly)
- The granularity at which the audit applies

Don't open the next section's file until the current one passes audit and is committed.

### 9.2 Branching

- One feature branch per chapter: `ch-XX-slug`
- PR to `main` after audit passes
- `main` always compiles cleanly
- Tag releases when a part is done: `v0.1-part1`, `v0.2-part2`, …

### 9.3 Review with Gustavo

- After every two completed chapters, send a PDF to Gustavo
- Capture his feedback as GitHub issues, labeled `gustavo-feedback`
- Address before tagging the part as done

### 9.4 What "done" means

A section is done when:
1. It passes all three audit stages.
2. It compiles cleanly with no warnings other than overfull-box (which is sometimes unavoidable in Tufte layout).
3. The Colab notebooks (if any) run end-to-end without error.
4. The cliff-notes track for that section is self-contained (test by reading only the openers, intuition boxes, and recap).
5. It's committed with a descriptive message and pushed.

---

## 10. Specific anti-patterns to avoid

These have already shown up; do not let them come back.

### 10.1 The dependency-graph problem (live example)

**Symptom**: arrows passing through node interiors, text "Ch. 7" being clipped by an arrow, cramped vertical spacing, awkward page breaks.

**Why it happened**: figure was committed without visual audit.

**Fix**: redo with TikZ `bend left/right`, explicit out/in angles for crossing arrows, larger node spacing, and no cross-row arrows except via the margin path. Then visually inspect every arrow.

**Audit gate**: every diagram passes a visual check before commit. No exceptions.

### 10.2 Other anti-patterns

- Definitions without motivation paragraphs
- Theorems before pictures
- Margin items that are load-bearing
- Code without `np.random.default_rng(...)` seed
- Figures without captions
- Captions that just say "Plot of X"
- Citations to broken keys (always run `biber` to check)
- New colors introduced ad-hoc in TikZ, must be from the palette
- Plots that violate the matplotlib style helper
- Any inline `\textcolor{...}` outside the locked palette
- Inventing new tcolorbox environments instead of reusing the five

---

## 11. Cartoon asides

Cartoon asides are explicitly allowed and explicitly limited.

- **Frequency**: ≤1 per chapter. They lose impact if they're frequent.
- **Style**: stick-figure-simple, hand-sketched feel via TikZ. Drawn entirely from primitive shapes (circle, line, arc), never imported.
- **Topic**: a small joke that lands in 1 sentence in the margin. Not a meme, not a reference, not anything that requires outside context.
- **Pictogram**: every cartoon aside has a small star (★) glyph in the margin to flag "non-load-bearing." (Defined in `\cartoonglyph`.)

The bar is high: a cartoon either makes the reader smile and turn the page, or it doesn't appear.

---

## 12. Summary

If you remember nothing else from this document:

1. **No indents. Block paragraphs.**
2. **Every page has a margin item. Margins are never load-bearing.**
3. **All figures in-house. TikZ + matplotlib only. Pastel palette, 8 colors total.**
4. **Picture before proof.**
5. **Three-stage audit before commit. Visual, logical, content.**
6. **One section at a time.**

When in doubt, refer to this guide. When the guide is silent, ask before assuming.
