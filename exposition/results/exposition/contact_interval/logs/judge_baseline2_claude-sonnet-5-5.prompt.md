You are an expert mathematician judging the exposition of several proofs of the same statement. The proofs are labeled with neutral letters, and their order carries no meaning. Judge each proof on its own merits using the rubric below.

Read the statement, the context and every proof carefully before scoring. Check correctness yourself: a proof with a mathematical error or a gap that a careful reader cannot fill must score low on correctness.

Answer with a single JSON object and nothing else:

{
  "scores": {"<label>": {"correctness": int, "overview": int, "structure": int, "justification": int, "economy": int, "notation": int, "explanation": int}, ...},
  "ranking": ["<best label>", ..., "<worst label>"],
  "rationale": "Three to six sentences explaining the ranking, citing concrete features of the proofs."
}

The ranking is your overall judgment of which proof a research mathematician would most want to read, taking all dimensions into account, with correctness weighted most.


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

## Proof A

\begin{proof}
We seek two contacts with the running minimum
\[
g(u)=m(u)-qu,\qquad F(u)=\min_{v\in[u,1]}g(v).
\]
Comparing minimizers gives
\[
0\le F(v)-F(u)\le \Lip(g)(v-u)\qquad(u<v).
\]
Moreover, $F$ is locally constant wherever $F<g$: a strict gap keeps minimizers a positive distance to the right.

Since $F(0)=0$ and $F(1)\ge s-q>t-q$, absolute continuity supplies $A\in(0,1)$ with $F'(A)>t-q$. Local constancy forces $F(A)=g(A)$ and contacts $B>A$ arbitrarily close to $A$; otherwise $F$ would be constant on a right neighborhood of $A$. By differentiability, choose such a contact with $B<\min(2A,1)$ and
\[
F(w)-F(A)\ge(t-q)(w-A)\qquad(A\le w\le B).
\]
Together with $g\ge F$ and $g(A)=F(A)$, this proves \eqref{prep:contact-middle}. For $w\ge B$, monotonicity gives $g(w)\ge F(w)\ge F(B)=g(B)$, proving \eqref{prep:contact-last}. Finally, $m(w)\ge sw\ge qw$ proves \eqref{prep:contact-first}.
\end{proof}


## Proof B

Idea: take the running minimum of $m(u)-qu$ from the right; $A$ is a point where it grows faster than $t-q$, $B$ a nearby touching point.

\begin{proof}
Let $g(u)=m(u)-qu$, $L=\Lip(g)$, $F(u)=\min_{[u,1]}g$. Since $g(v)\ge(s-q)v\ge0=g(0)$, we get $F(0)=0$ and $F(1)=g(1)\ge s-q$.

For $u<v$, $F(u)=\min(\min_{[u,v]}g,F(v))$ and $\min_{[u,v]}g\ge g(v)-L(v-u)$, so $0\le F(v)-F(u)\le L(v-u)$. Hence $\int_0^1F'\ge s-q>t-q$; some $A\in(0,1)$ has $F'(A)>t-q>0$.

Call $v$ a contact point if $g(v)=F(v)$; a minimizer $v$ of $g$ on $[u,1]$ is one, as $g(v)=F(u)\le F(v)\le g(v)$. If $(A,A+\delta)$ had none, then $F(u)=F(A+\delta)$ for $u\in(A,A+\delta)$, contradicting $F'(A)>0$. Contact points form a closed set, so $A$ is one, and by differentiability there is a contact point $B\in(A,\min(2A,1))$ with $F(w)-F(A)\ge(t-q)(w-A)$ on $[A,B]$.

Now $m(w)\ge sw\ge qw$; on $[A,B]$, $g(w)-g(A)\ge F(w)-F(A)\ge(t-q)(w-A)$; for $w\ge B$, $g(w)\ge F(B)=g(B)$.
\end{proof}


## Proof C

\begin{proof}
\emph{Idea:} $A$ and $B$ are forward minimizers of $m(w)-tw$ and $m(w)-qw$. Only continuity of $m$ is used.

Let $h(w)=m(w)-tw$ and $g(w)=m(w)-qw$. Then \eqref{prep:contact-first} holds for any $A$: $m(w)\ge sw\ge qw$.

\emph{Choice of $A$.} As $h(0)=0<s-t\le h(1)$, continuity gives $a\in(0,1)$ with $h(a)<h(1)$. Let $A$ minimize $h$ on $[a,1]$. Then $A>0$, $A<1$ (since $h(A)\le h(a)<h(1)$), and $h\ge h(A)$ on $[A,1]$ gives \eqref{prep:contact-middle}.

\emph{Choice of $B$.} Let $d=\tfrac12\min(A,1-A)$. Continuity at $A$ gives $c\in(A,1)$ with $g(c)<g(A)+(t-q)d$. Let $B$ minimize $g$ on $[c,1]$. Then $B>A$, and $g\ge g(B)$ on $[B,1]$ gives \eqref{prep:contact-last}.

\emph{$B$ is near $A$.} Subtracting $h(B)\ge h(A)$ from $g(B)\le g(c)<g(A)+(t-q)d$ yields $(t-q)(B-A)<(t-q)d$. Hence $B<A+d<\min(2A,1)$.
\end{proof}


## Proof D

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


## Proof E

\begin{proof}
We obtain the two slope bounds by successive minimizations.
Put \(h(u)=m(u)-tu\) and \(g(u)=m(u)-qu\).
Since \(h(0)=0<h(1)\), continuity gives \(a\in(0,1)\) with \(h(a)<h(1)\).
Let \(A\) minimize \(h\) on \([a,1]\).
Then \(0<A<1\), since \(h(A)\le h(a)<h(1)\).

Set \(d=\min(A,1-A)>0\).
By continuity, choose \(c\in(A,1)\) with
\(g(c)<g(A)+(t-q)d\), and let \(B\) minimize \(g\) on \([c,1]\).
Because \(B\ge c>A\) and \(h(B)\ge h(A)\),
\[
(t-q)(B-A)\le g(B)-g(A)
\le g(c)-g(A)<(t-q)d.
\]
Thus \(B<A+d\le\min(2A,1)\).

Minimality of \(h(A)\) gives
\(m(w)-m(A)\ge t(w-A)\) for \(A\le w\le B\);
minimality of \(g(B)\) gives
\(m(w)-m(B)\ge q(w-B)\) for \(B\le w\le1\).
Finally, \(m(w)\ge sw\ge qw\) on \([0,A]\).
\end{proof}
