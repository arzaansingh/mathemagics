%% mathemagics.cls
%% Custom document class for "Mathemagics: A Field Guide to Random Matrices and Spectral Clustering"
%% Inherits from tufte-book and layers on our pedagogical UX.
%%
%% Author: Arzaan Singh (under the supervision of Gustavo Didier)
%% Tulane University, 2026

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mathemagics}[2026/04/26 v0.1 Mathemagics textbook class]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Pass options to tufte-book and load it
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% A "draft" toggle: \documentclass[draft]{mathemagics} reveals \TODO marks more loudly.
\newif\if@mathemagicsdraft\@mathemagicsdraftfalse
\DeclareOption{draft}{\@mathemagicsdrafttrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{tufte-book}}
\ProcessOptions\relax

\LoadClass[justified,nobib]{tufte-book}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Page geometry — Tufte feel: narrow main column, wide right margin for asides
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\geometry{
  paperheight=9in,
  paperwidth=8in,
  top=3pc,
  bottom=6pc,
  inner=3pc,
  outer=3pc,
  marginparsep=1pc,
  marginparwidth=10pc,
  includehead,
  bindingoffset=2pc,
  includemp
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Core packages
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Math
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{mathtools}
\RequirePackage{bm}
\RequirePackage{bbm}

% Microtypography
\RequirePackage{microtype}

% Tables and lists
\RequirePackage{booktabs}
\RequirePackage{enumitem}

% TikZ for figures, dependency graph, decorative pictograms
\RequirePackage{tikz}
\usetikzlibrary{positioning,arrows.meta,calc,fit,shapes,shapes.geometric,decorations.pathreplacing,backgrounds}

% tcolorbox for our five locked-in environments
\RequirePackage[most]{tcolorbox}
\tcbuselibrary{theorems,breakable,skins}

% minted for Python code (requires --shell-escape)
% Wrapped in a check so the document compiles without minted in environments where Pygments isn't available.
\IfFileExists{minted.sty}{%
  \RequirePackage{minted}
  \setminted{%
    fontsize=\small,
    breaklines=true,
    breakanywhere=true,
    baselinestretch=1.0,
    frame=none
  }
  \newcommand{\mathemagics@hasminted}{}
}{%
  % Fallback: provide stub commands so missing minted doesn't break compile
  \providecommand{\mintinline}[2]{\texttt{#2}}
  \providecommand{\mint}[1]{\texttt{#1}}
}

% URLs and hyperlinks
\RequirePackage{xurl}
\RequirePackage{hyperref}
% Cross-reference cleverness
\RequirePackage[noabbrev,capitalise]{cleveref}

% Bibliography (biblatex with biber backend)
\RequirePackage[style=alphabetic,backend=biber,maxbibnames=10,maxcitenames=2,giveninits=true]{biblatex}

% Index
\RequirePackage{imakeidx}
\makeindex[intoc]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Style: colors, macros, environments
% These three files define the visual identity in one place.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\input{style/colors}
\input{style/macros}
\input{style/environments}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hyperref color scheme — uses our locked-in palette from style/colors
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\hypersetup{
  colorlinks=true,
  linkcolor=mathemagicsLink,
  citecolor=mathemagicsLink,
  urlcolor=mathemagicsLink,
  pdftitle={Mathemagics: A Field Guide to Random Matrices and Spectral Clustering},
  pdfauthor={Arzaan Singh}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Theorem environments are defined entirely in style/environments.tex via
% tcolorbox, sharing one master counter (mathemagicsCounter) that resets per
% chapter.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TODO and draft tooling
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\if@mathemagicsdraft
  \newcommand{\TODO}[1]{\textbf{\textcolor{magenta}{[TODO: #1]}}}
\else
  \newcommand{\TODO}[1]{\textbf{\textcolor{red!75!black}{[TODO: #1]}}}
\fi

\newcommand{\PLACEHOLDER}[1]{%
  \par\medskip\noindent\fbox{%
    \begin{minipage}{0.95\linewidth}%
      \itshape Placeholder content for this section. #1%
    \end{minipage}%
  }\par\medskip%
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Footer: revision date / draft notice
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{datetime2}
\newcommand{\bookfoot}{\footnotesize\smallcaps{Mathemagics, draft \DTMtoday}}

\makeatletter
\renewcommand\frontmatter{%
  \cleardoublepage%
  \@mainmatterfalse%
  \fancyhf{}%
  \fancyfoot[LE]{\bookfoot}%
  \fancyfoot[RO]{\bookfoot}%
  \pagenumbering{roman}%
}
\renewcommand\mainmatter{%
  \cleardoublepage%
  \@mainmattertrue%
  \fancyhf{}%
  \renewcommand{\chaptermark}[1]{\markboth{\@chapapp\ \thechapter.\ ##1}{}}%
  \renewcommand{\sectionmark}[1]{\markright{\thesection.\ ##1}}%
  \fancyhead[LE]{\thepage\quad\smallcaps{\leftmark}}%
  \fancyhead[RO]{\smallcaps{\rightmark}\quad\thepage}%
  \fancyfoot[LE]{\bookfoot}%
  \fancyfoot[RO]{\bookfoot}%
  \pagenumbering{arabic}%
}
\renewcommand\backmatter{%
  \cleardoublepage%
  \@mainmatterfalse%
  \fancyhf{}%
  \fancyfoot[LE]{\bookfoot}%
  \fancyfoot[RO]{\bookfoot}%
}
\makeatother

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Tufte-book TOC depth and section numbering depth
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{1}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Block-paragraph style: no first-line indent, slight space between paragraphs.
% Locked house rule for Mathemagics — see STYLE.md.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\AtBeginDocument{%
  \setlength{\parindent}{0pt}%
  \setlength{\parskip}{0.6\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip}%
}

\endinput
