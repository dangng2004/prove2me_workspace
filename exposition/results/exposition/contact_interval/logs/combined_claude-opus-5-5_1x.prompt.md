You are given several proofs of the same statement, in LaTeX. One is the original proof from the paper. The others were derived from independent formalizations of the result, so they may take different routes or make explicit steps the paper leaves implicit.

Write a new proof of the statement that is clearer and more legible than every one of the given proofs, judged by the rubric below.

Rules:

- Your proof must be correct and complete. It may cite only results stated in the provided context.
- Do not simply polish one version. Compare the versions, take the best ideas, structure and explanations from several of them, and in particular use what the formalization-derived versions contribute where it makes the proof simpler, clearer or more rigorous. If one route is simpler, you may build on it and borrow motivation or remarks from the others.
- You may restructure freely: add an overview, split the proof into claims, reorder steps, rename notation, or remove material that does not help the reader.
- Write in ordinary mathematical prose for a research mathematician.

Output exactly two blocks:

<proof>
The LaTeX proof, starting with `\begin{proof}` and ending with `\end{proof}`. You may put short lemma statements or a one-paragraph overview before it. Do not mention the source versions or formalization in this block.
</proof>
<notes>
A short list of what you took from which version and why.
</notes>


Length limit: your proof (everything inside the <proof> block) must be at most 147 words, counting words of prose and mathematics but not LaTeX commands. This is about the length of the original proof. Meet the limit by choosing what to include, not by skipping steps a careful reader needs.

# Rubric for proof exposition

Score each proof on each dimension from 1 (poor) to 5 (excellent). The dimensions follow research on how mathematicians read and judge proofs:

- Mejía-Ramos, Fuller, Weber, Rhoads and Samkoff (2012), "An assessment model for proof comprehension in undergraduate mathematics", Educational Studies in Mathematics 79: comprehension has local dimensions (meaning of terms, logical status of statements, justification of claims) and holistic ones (summarizing the main idea, seeing the modular structure, transferring the method).
- Lai, Weber and Mejía-Ramos (2012), "Mathematicians' perspectives on features of a good pedagogical proof", Cognition and Instruction 30: mathematicians revise proofs by adding overviews, introducing the main idea early, and removing details that do not help the reader.
- Lamport (1995), "How to write a proof", American Mathematical Monthly 102: hierarchical structure lets the reader see the outline first and drill down as needed.
- Hanna (1990) and the later literature on explanatory proof: a proof can show that a result holds, or also why it holds.

## Dimensions

1. **Correctness and completeness.** Every step is valid, and no step needed for the conclusion is missing or hand-waved. Gaps a careful reader must fill count against this score. A proof with an error scores at most 2.
2. **Overview and main idea.** The reader learns early what the strategy is and which idea makes the proof work.
3. **Structure.** The proof is divided into steps or claims whose roles are clear, and the reader can see how they fit together and which can be skipped on a first reading.
4. **Local justification.** Each claim says why it holds (which hypothesis, lemma or earlier step), so a reader can check it without reconstructing the reasoning.
5. **Economy.** The proof includes what the reader needs and nothing more. Irrelevant detail, repetition, and bookkeeping that hides the argument count against it. Brevity bought by skipping needed steps counts under dimension 1, not here.
6. **Notation and terminology.** Symbols and terms are defined before use, used consistently, and chosen to help the reader.
7. **Explanatory value.** The proof shows why the result is true, for example by making clear where each hypothesis is used and what would fail without it.

A proof may legitimately cite results that are stated in the provided context. Judge each proof as a document a research mathematician would read.


# Statement

% Macros: \R=\mathbb R, \eps=\varepsilon, \one=\mathbf 1 (indicator), \TV=total variation, \dist, \supp, \Lip as usual.
\begin{lemma}[A contact interval]\label{prep:contact}
Suppose $m:[0,1]\to\R$ is nondecreasing and Lipschitz,
$m(0)=0$, and $m(u)\ge su$. If $q<t<s$, there exist
$0<A<B<1$, with $B<2A$, such that
\begin{align}
 m(w)&\ge qw &&(0\le w\le A),\label{prep:contact-first}\\
 m(w)-m(A)&\ge t(w-A)&&(A\le w\le B),\label{prep:contact-middle}\\
 m(w)-m(B)&\ge q(w-B)&&(B\le w\le1).\label{prep:contact-last}
\end{align}
\end{lemma}


# Proofs

## Version 1 (the original proof from the paper)

\begin{proof}
Put $g(u)=m(u)-qu$ and $F(u)=\min_{u\le v\le1}g(v)$.
The function $F$ is nondecreasing and Lipschitz: if $u<v$, a minimizer
for $F(u)$ either lies in $[v,1]$, or comparison with $g(v)$ bounds
$F(v)-F(u)$ by $\Lip(g)(v-u)$. Moreover, $F(0)=0$ and
$F(1)\ge s-q>t-q$. Absolute continuity gives an interior
differentiability point $A$ at which $F'(A)>t-q$.
At this point $F(A)=g(A)$, since a strict gap would force the minimum
to be attained a fixed distance to the right and would make $F$ locally
constant. There are contact points $B>A$ arbitrarily close to $A$:
otherwise $F$ would be constant immediately to the right of $A$.
Choose such a $B<\min(2A,1)$ so close that
$F(w)-F(A)\ge(t-q)(w-A)$ on $[A,B]$.
Using $g(w)\ge F(w)$ proves Equation~\eqref{prep:contact-middle}.
The first inequality follows from $m(w)\ge sw$, and the last follows
from $g(w)\ge F(B)=g(B)$ for $w\ge B$.
\end{proof}


## Version 2 (derived from a formalization)

\begin{proof}
Let $K$ be a Lipschitz constant of $m$ on $[0,1]$; in particular $m$ is continuous. (The monotonicity of $m$ will not be used.) Put
\[
 g(w)=m(w)-qw\qquad(0\le w\le 1),
\]
which is continuous on $[0,1]$. For $u\in[0,1]$ choose, by compactness of $[u,1]$, a point $P(u)\in[u,1]$ minimizing $g$ on $[u,1]$, and write $F(u)=g(P(u))=\min_{[u,1]}g$. Note that $t-q>0$.

\medskip\noindent\textbf{Key step.} \emph{Suppose $0<v<u\le \tfrac12$, $3u\le 4v$, and
\begin{equation}\label{eq:gap}
 (t-q)(u-v)\le F(u)-F(v).
\end{equation}
Then there are $A,B$ with all the required properties.}

Let $x=P(v)\in[v,1]$, so $g(x)=F(v)$. Since the left side of \eqref{eq:gap} is positive, $F(v)<F(u)$.

First, $x<u$: otherwise $x\in[u,1]$, so $F(u)\le g(x)=F(v)$, a contradiction. Also $F(u)\le g(u)$ because $u\in[u,1]$.

\emph{Intermediate values.} If $0\le y\le u$ and $g(y)\le F(u)$, then since $g(y)\le F(u)\le g(u)$, the intermediate value theorem gives $z\in[y,u]$ with $g(z)=F(u)$.

\emph{Choice of $B$.} Let $T=\{z\in[x,u]: g(z)=F(u)\}$. It is closed (by continuity of $g$), bounded, and nonempty (apply the intermediate value remark with $y=x$, using $g(x)=F(v)<F(u)$). Let $B=\sup T$; then $B\in T$, so $x\le B\le u$ and $g(B)=F(u)$.

\emph{$B$ is a contact point:} $g(B)\le g(y)$ for all $y\in[B,1]$. If $y\ge u$ this is the minimality of $F(u)=g(B)$ on $[u,1]$. If $y<u$ and $g(y)<F(u)$, the intermediate value remark yields $z\in[y,u]$ with $g(z)=F(u)$; then $z\in T$, so $z\le B\le y\le z$, whence $z=y$ and $g(y)=F(u)$, a contradiction.

\emph{Gap on $[x,B]$.} Since $B\le u$ and $x\ge v$, we have $B-x\le u-v$, so by \eqref{eq:gap}
\begin{equation}\label{eq:gapB}
 (t-q)(B-x)\le (t-q)(u-v)\le F(u)-F(v)=g(B)-g(x).
\end{equation}
In particular $x<B$: if $x=B$, then $g(B)=g(x)$, i.e.\ $F(u)=F(v)$, contradicting $F(v)<F(u)$.

\emph{Choice of $A$.} Let $h(w)=g(w)-(t-q)w=m(w)-tw$, continuous on $[x,B]$, and let $A_0$ minimize $h$ on $[x,B]$. If $A_0<B$ set $A=A_0$. If $A_0=B$, set $A=x$; by \eqref{eq:gapB}, $h(x)\le h(B)=\min_{[x,B]}h$, so $x$ is also a minimizer. In either case $A\in[x,B)$ and $h(A)\le h(w)$ for all $w\in[x,B]$.

\emph{Verification.} We have $A\ge x\ge v>0$, $A<B$, and $B\le u\le\tfrac12<1$. Moreover $B\le u\le \tfrac43 v<2v\le 2A$ since $v>0$.
For $0\le w\le A$ we have $w\in[0,1]$ and $w\ge0$, $s>q$, so $m(w)\ge sw\ge qw$, which is \eqref{prep:contact-first}.
For $A\le w\le B$, $h(A)\le h(w)$ reads $m(A)-tA\le m(w)-tw$, which is \eqref{prep:contact-middle}.
For $B\le w\le 1$, $g(B)\le g(w)$ reads $m(B)-qB\le m(w)-qw$, which is \eqref{prep:contact-last}.
This proves the key step.

\medskip\noindent\textbf{Finding a suitable pair.} Let $u_k=\tfrac12(3/4)^k$ for $k\ge0$, so $0<u_k\le\tfrac12$.

\emph{Lower bound at $u_0=\tfrac12$.} Let $p=P(\tfrac12)\in[\tfrac12,1]$. Then $F(\tfrac12)=m(p)-qp\ge (s-q)p\ge \tfrac{s-q}{2}$, since $s-q>0$.

\emph{Upper bound at $u_n$.} Since $u_n\in[u_n,1]$, the Lipschitz bound and $m(0)=0$ give $m(u_n)\le |m(u_n)-m(0)|\le Ku_n$, hence
\[
 F(u_n)\le g(u_n)=m(u_n)-qu_n\le (K-q)u_n .
\]

Suppose, for contradiction, that $F(u_k)-F(u_{k+1})<(t-q)(u_k-u_{k+1})$ for every $k$. Telescoping gives, for all $n$,
\[
 F(u_0)-F(u_n)\le (t-q)(u_0-u_n)=(t-q)\bigl(\tfrac12-u_n\bigr).
\]
Combining with the two bounds,
\[
 \tfrac{s-q}{2}-(K-q)u_n\le (t-q)\bigl(\tfrac12-u_n\bigr),
 \quad\text{i.e.}\quad
 \tfrac{s-t}{2}\le (K-t)u_n\le |K-t|\cdot\tfrac12(3/4)^n .
\]
Since $s-t>0$ and $3/4<1$, choose $n$ with $(3/4)^n<\dfrac{s-t}{|K-t|+1}$; then $|K-t|(3/4)^n<s-t$, contradicting the last display.

Hence there is $k$ with $(t-q)(u_k-u_{k+1})\le F(u_k)-F(u_{k+1})$. Apply the key step with $u=u_k$, $v=u_{k+1}$: indeed $0<v<u\le\tfrac12$ and $3u=4v$. This yields the desired $A$ and $B$.
\end{proof}


## Version 3 (derived from a formalization)

\begin{proof}
We use only two standard facts: a continuous function on a nonempty compact interval attains its minimum, and the following elementary consequence of continuity.

\emph{Claim.} Let $a<b$ and let $f$ be continuous on $[a,b]$ with $f(a)<y$. Then there is $x\in(a,b)$ with $f(x)<y$.

To see this, use continuity at $a$ to choose $\delta>0$ such that $|f(x)-f(a)|<y-f(a)$ whenever $x\in[a,b]$ and $|x-a|<\delta$. Put $x=a+\tfrac12\min(\delta,b-a)$. Then $x\in(a,b)$ and $f(x)<f(a)+(y-f(a))=y$.

Since $m$ is Lipschitz on $[0,1]$, it is continuous there. Monotonicity of $m$ is not needed. Define the continuous functions
\[
 h(u)=m(u)-tu,\qquad g(u)=m(u)-qu\qquad(u\in[0,1]).
\]

\emph{Construction of $A$.} We have $h(0)=m(0)=0$. Also $m(1)\ge s$ and $t<s$, so $h(1)=m(1)-t\ge s-t>0$. Hence $h(0)<h(1)$. Applying the Claim to $h$ on $[0,1]$ with $y=h(1)$ gives $a\in(0,1)$ with $h(a)<h(1)$. Let $A$ be a point at which $h$ attains its minimum on $[a,1]$. Then $A\ge a>0$. Moreover $h(A)\le h(a)<h(1)$, so $A\neq 1$, i.e. $A<1$.

\emph{Construction of $B$.} Put $d=\tfrac12\min(A,1-A)$, so that $0<d<A$ and $d<1-A$. Since $t>q$ and $d>0$, we have $g(A)<g(A)+(t-q)d$. Applying the Claim to $g$ on $[A,1]$ gives $c\in(A,1)$ with
\[
 g(c)<g(A)+(t-q)d .
\]
Let $B$ be a point at which $g$ attains its minimum on $[c,1]$. Then $B\ge c>A$. Two consequences of the minimality properties will be used: $g(B)\le g(c)$, and $h(A)\le h(B)$, the latter because $B\in[A,1]\subset[a,1]$.

\emph{$B$ is close to $A$.} We show that $B<A+d$. Suppose instead that $B\ge A+d$. The inequality $h(A)\le h(B)$ reads $m(A)-tA\le m(B)-tB$. The inequalities $g(B)\le g(c)<g(A)+(t-q)d$ give $m(B)-qB<m(A)-qA+(t-q)d$. Adding these two inequalities and cancelling $m(A)+m(B)$ yields
\[
 (t-q)(B-A)<(t-q)d .
\]
On the other hand, $t-q>0$ and $B-A-d\ge 0$ give $(t-q)(B-A)\ge(t-q)d$, a contradiction. Hence $B<A+d$.

Consequently $B<A+d<A+(1-A)=1$ and $B<A+d<2A$. Together with $0<A<B$, this gives all the required inequalities among $A$ and $B$.

\emph{The three estimates.}

\eqref{prep:contact-first}: Let $0\le w\le A$. Then $w\in[0,1]$, and since $q<t<s$ and $w\ge 0$, we get $qw\le sw\le m(w)$.

\eqref{prep:contact-middle}: Let $A\le w\le B$. Then $w\in[a,1]$, so $h(A)\le h(w)$, that is, $m(A)-tA\le m(w)-tw$. This is $m(w)-m(A)\ge t(w-A)$. In fact the same argument gives this inequality for every $w\in[A,1]$.

\eqref{prep:contact-last}: Let $B\le w\le 1$. Then $w\in[c,1]$, so $g(B)\le g(w)$, that is, $m(B)-qB\le m(w)-qw$. This is $m(w)-m(B)\ge q(w-B)$.
\end{proof}
