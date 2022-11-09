
class Tikz(object):

    def __init__(self, code, tikzlibraries, tikzpictureoptions):
        self.code = code
        self.tikzlibraries = tikzlibraries
        self.tikzpictureoptions = tikzpictureoptions

    def latex(self):
        return r"""
\documentclass[convert={convertexe={convert},size=400x240,outext=.png},border=0pt]{standalone}
\usepackage[]{tikz}
\usetikzlibrary{""" + self.tikzlibraries + r"""}

\begin{document}
\begin{tikzpicture}[""" + self.tikzpictureoptions + r"""]
""" + self.code + r"""
\end{tikzpicture}
\end{document}
"""

c=r"""\node[state,initial]   (q)                {$q$};
\node[state]  (i) [right=of q] {$i$};
\node[state,accepting]  (f) [right=of q,below=of i] {$f$};
\path[->] (q) edge [above]   node         {$0$} (i)
(q) edge [loop below]   node         {$1$} ()
(q) edge [below]   node         {$1$} (f)
(f) edge [right]   node         {$\varepsilon$} (i);
"""

print(Tikz(c,"positioning,automata","on top/.style={preaction={draw=white,-}},on top/.default=4pt").latex())

#-l matrix -po "on top/.style={preaction={draw=white,-}},on top/.default=4pt"
