# Image generation prompts — Chapter 1

This document holds detailed prompts for the cartoon illustrations referenced in Chapter 1. Generate each PNG using your preferred image-gen tool (Claude.ai's image generation, DALL-E, Midjourney, Stable Diffusion, etc.) and save them at the expected paths below.

The LaTeX is wired up via `\artOrTikz{<path>}{<TikZ fallback>}`. If the PNG exists, it's used; if not, the TikZ stand-in is rendered instead. So generation is purely additive.

## Common style guidelines

The book's aesthetic is **soft pastel-academic**. Cartoons should fit alongside this palette:

- Powder blue `#5A9CCB`
- Mustard `#B8901C`
- Coral `#C57A5C`
- Mint `#50A076`
- Lilac `#8273A8`
- Soft gold `#D4A028`
- Warm gray `#8B8378`
- Charcoal `#2D2D2D`

Style cues to include in every prompt:
- Hand-drawn / sketchy line work, not slick or 3D-rendered
- Soft pastel palette consistent with the colors above
- White or off-white background (`#F8F6F2` warm off-white is the page background)
- Calvin-and-Hobbes / Sandra Boynton / xkcd visual register, leaning playful and warm
- Black or charcoal line art, light pastel fills
- No photorealism, no anime style, no over-rendered shading

Aspect ratio: ~1:1 (square) for single-panel cartoons, ~3:2 (landscape) for multi-panel comic strips. The book renders these at margin width (~10pc ≈ 4.2cm wide).

## 1. `wizard-comic.png` — chapter-opener 4-panel comic

**Path:** `figures/ch01/wizard-comic.png`

**Aspect:** ~3:4 portrait, or 2:2 grid, whichever frames a 4-panel comic best at margin width.

**Prompt:**

> A 4-panel hand-drawn comic strip in the style of Calvin and Hobbes (Bill Watterson) or Sandra Boynton, with soft pastel colors and warm friendly characters.
>
> **Panel 1:** A young wizard character with a tall pointed hat (lilac purple `#8273A8`) holds up a coin, looking curious. Speech bubble: "Heads or tails?"
>
> **Panel 2:** The wizard tosses the coin high in the air. The coin spins mid-air with motion lines. The wizard looks up, expectant.
>
> **Panel 3:** The coin lands on a table, balanced perfectly on its edge. The wizard's eyes go wide in surprise.
>
> **Panel 4:** The wizard scribbles on a chalkboard the equation `P(edge) ≈ 0`, with a small sweat drop. Speech bubble: "Probability is rigorous magic."
>
> Style: hand-drawn lines, soft pastel fills, warm off-white background `#F8F6F2`, charcoal-gray ink lines `#2D2D2D`, slight texture. Lilac, mustard, coral, mint, and soft gold accents. No text outside the speech bubbles. Friendly, gently humorous, NOT slick or stylized like an anime; closer to a children's book illustration that adults would also find charming.

**Caption that will appear below the image (already in the LaTeX):**
*Probability is rigorous magic: we name the unknown, weigh it, and pull conclusions out of it.*

## 2. `coin-cartoon.png` — talking coin character

**Path:** `figures/ch01/coin-cartoon.png`

**Aspect:** Square (1:1).

**Prompt:**

> A hand-drawn cartoon coin character with personality, in the style of a Sandra Boynton illustration or a friendly children's book.
>
> The coin is a large round shape (cream / pale-yellow `#FBF3D9` fill, with a charcoal `#2D2D2D` outline), shown front-on. The coin has a face: two big round eyes (both blinking or wide open with curiosity), small expressive eyebrows raised in question, and a small smile. The letter "H" is prominently embossed on the coin's face below the eyes.
>
> The coin is mid-thought. To the right, a small thought bubble (white, charcoal outline) trails up from the coin's head with two small puffs leading up to a larger speech-bubble shape. Inside the bubble, in a friendly serif font, is the equation: `P(H) = 1/2`.
>
> Style: warm hand-drawn ink, soft pastel palette, off-white background `#F8F6F2`. Charcoal lines, mustard / cream coin body, no harsh shading. Inviting, gently humorous. Think "the coin is being asked a question and is genuinely thinking about it."

**Caption (already in the LaTeX):**
*One coin flip is the simplest non-trivial experiment in all of probability.*

---

## How to use

1. Generate the PNG using your tool of choice with the prompt above.
2. Save it at the exact path listed (e.g., `figures/ch01/wizard-comic.png`).
3. Recompile the document (`latexmk -pdf` from repo root). The `\artOrTikz` macro automatically detects the file and uses it instead of the TikZ fallback.
4. To revert to the TikZ version: rename or delete the PNG.

## Style consistency note

If you generate cartoons for later chapters, keep the same prompt skeleton:
- Soft pastel palette (the eight colors above)
- Hand-drawn / sketchy line work
- White or off-white background
- Calvin-and-Hobbes / Sandra Boynton register
- No photorealism, no anime, no slick 3D rendering

This keeps the book's visual identity coherent across all illustrations.
