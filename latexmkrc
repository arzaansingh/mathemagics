## latexmkrc
## Build configuration for Mathemagics.
##
## Usage:
##   latexmk -pdf            # builds main.pdf
##   latexmk -c              # cleans intermediate files
##   latexmk -C              # cleans all (including main.pdf)

# Use pdflatex with shell-escape (required for minted)
$pdf_mode = 1;
$pdflatex = 'pdflatex --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Use biber for bibliography (biblatex backend)
$biber = 'biber --validate-datamodel %O %S';

# Run pdflatex up to 5 times to resolve cross-references
$max_repeat = 5;

# Recognize the additional output files we generate
push @generated_exts, 'glo', 'idx', 'ind', 'ist', 'gls', 'glg', 'bbl', 'bcf', 'run.xml';
$clean_ext .= ' synctex.gz tdo nav snm vrb';

# minted leaves a _minted-* directory; clean it on -C
$clean_full_ext .= ' _minted-* %R.bbl %R.blg %R.run.xml';
