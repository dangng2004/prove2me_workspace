<proof>
\begin{proof}
\emph{Idea:} $A$ and $B$ are forward minimizers of $m(w)-tw$ and $m(w)-qw$. Only continuity of $m$ is used.

Let $h(w)=m(w)-tw$ and $g(w)=m(w)-qw$. Then \eqref{prep:contact-first} holds for any $A$: $m(w)\ge sw\ge qw$.

\emph{Choice of $A$.} As $h(0)=0<s-t\le h(1)$, continuity gives $a\in(0,1)$ with $h(a)<h(1)$. Let $A$ minimize $h$ on $[a,1]$. Then $A>0$, $A<1$ (since $h(A)\le h(a)<h(1)$), and $h\ge h(A)$ on $[A,1]$ gives \eqref{prep:contact-middle}.

\emph{Choice of $B$.} Let $d=\tfrac12\min(A,1-A)$. Continuity at $A$ gives $c\in(A,1)$ with $g(c)<g(A)+(t-q)d$. Let $B$ minimize $g$ on $[c,1]$. Then $B>A$, and $g\ge g(B)$ on $[B,1]$ gives \eqref{prep:contact-last}.

\emph{$B$ is near $A$.} Subtracting $h(B)\ge h(A)$ from $g(B)\le g(c)<g(A)+(t-q)d$ yields $(t-q)(B-A)<(t-q)d$. Hence $B<A+d<\min(2A,1)$.
\end{proof}
</proof>
<notes>
- Route from Version 3. Both points are chosen as minimizers of continuous functions on compact intervals, so the proof needs no absolute continuity, no differentiability point and no running-minimum function $F$, unlike Version 1. Version 2's telescoping search over $u_k$ is also unnecessary on this route. I kept Version 3's choice of $d=\frac12\min(A,1-A)$ and its comparison of the two minima, but wrote that comparison as a direct subtraction rather than a proof by contradiction.
- From Versions 2 and 3: the remark that monotonicity is not needed and that the Lipschitz hypothesis is used only for continuity. This shows exactly where each hypothesis enters.
- From Version 1: the short overview that names $A$ and $B$ as contact points of $m-tw$ and $m-qw$, which explains why the result holds. I also kept its one-line proof of the first inequality from $m(w)\ge sw$.
- I left out Version 3's general continuity "Claim" and used continuity at a point directly. This keeps the proof within the word limit without skipping a step.
</notes>
