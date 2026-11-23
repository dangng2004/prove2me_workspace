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
% Section conventions:
All sets in this section lie in fixed bounded regions. Directions are unit
vectors, with antipodal vectors identified when discussing lines. A finite
number of projective charts removes this distinction. For a bounded set
$A$, write $|A|_r$ for its covering number by balls of radius $r$. A tube has
bounded length and the stated perpendicular width; enlarging its length by
a fixed constant is always permitted. We use the ball-bound and subpower
conventions of Section~\ref{sec:conventions}. Bounds for radii in a fixed
larger bounded interval follow by changing constants. In particular,
incidence mass at least subpower means a lower bound $\delta^{o(1)}$.


\begin{theorem}[Linear projection gain]\label{ang:linear-gain}
Fix $k\ge2$ and
\[
 k-1\le q\le k-\tfrac12<t<k.
\]
Fix a tube-width constant $C$. In the case $q=k-1$, also fix
$\zeta>0$. There exist $\epsilon,c>0$ such that, for all sufficiently
small $\delta$, the following holds. Let $\mu$ be a bounded point
subprobability in $\R^{k+1}$ and $\nu$ a direction subprobability on $S^k$
with respective $t$- and $q$-ball bounds of loss $\delta^{-\epsilon}$
down to $\delta$. At $q=k-1$ assume in addition
\begin{equation}\label{ang:endpoint-plate}
 \nu\{w:\dist(w,H)\le r\}\le\delta^{-\epsilon}r^\zeta
       \qquad(\delta\le r\le1)
\end{equation}
for every linear hyperplane $H$. Let $E\subset\R^{k+1}\times S^k$ be a
measurable incidence relation, and write $E_w=\{x:(x,w)\in E\}$.
If each direction fiber $E_w$ is covered by at most
$\delta^{-q-\epsilon}$ tubes parallel to $w$ of width $C\delta$, then
\[
 (\mu\otimes\nu)(E)\le\delta^c.
\]
All constants are uniform over the measures and the incidence relations
with these fixed parameters.
\end{theorem}


# Context: results the proofs may cite

Earlier results of the same paper, which any proof may cite. Their proofs are omitted.

\begin{theorem}[Planar discretized Furstenberg estimate]
\label{ang:furstenberg}
Let $0<b<1$ and $b<f<2$. There is $\epsilon_0>0$ such that the
following holds for sufficiently small $\delta$. Suppose that $P$ is
a nonempty bounded $(\delta,f,\delta^{-\epsilon_0})$-set and that
each $x\in P$ has a nonempty family $\mathcal T_x$ of incident
$\delta$-tubes whose line parameters form a
$(\delta,b,\delta^{-\epsilon_0})$-set. Then
\[
 \left|\bigcup_{x\in P}\mathcal T_x\right|_\delta
       \ge\delta^{-2b-\epsilon_0}.
\]
The exponent may be decreased to absorb fixed bounded charts and fixed
width multiples.
\end{theorem}

\begin{lemma}[Planar measure incidence obstruction]
\label{ang:planar-measures}
Fix $0<b<1$ and $b<f<2$. There is no sequence $\delta\to0$ with the
following data. Let $\mu,\nu$ be subprobabilities on Borel label sets
$X,W$ in Euclidean spaces, and let
\[
 p:X\longrightarrow\R^2,\qquad v:W\longrightarrow S^1
\]
be measurable coordinate maps with fixed bounded images. Suppose that
$p_\#\mu$ and $v_\#\nu$ have respective $f$- and $b$-ball bounds
of loss $\delta^{-o(1)}$ down to $\delta$. Let $E\subset X\times W$ be a measurable
incidence relation with
\[
 (\mu\otimes\nu)(E)\ge\delta^{o(1)}.
\]
For each original direction label $\omega\in W$, put
$E_\omega=\{\xi\in X:(\xi,\omega)\in E\}$. Assume that the set of
point coordinates $p(E_\omega)$ is covered by at most
$\delta^{-b-o(1)}$ strips of width $C\delta$ parallel to $v(\omega)$.
\end{lemma}

\begin{lemma}[Haar band estimates]\label{ang:haar}
Let $0\le h\le n-1$, and let $V$ be a Haar-random codimension-$h$
linear subspace of $\R^n$.
For a unit vector $w$,
\[
 \Pr\{\dist(w,V)\le\delta\}\asymp\delta^h.
\]
If $j\le n-h$ unit vectors $w_1,\ldots,w_j$ have singular values
$d_1\ge\cdots\ge d_j\ge0$, then
\begin{equation}\label{ang:haar-multiple}
 \delta^{-jh}\Pr\{\dist(w_i,V)\le\delta\text{ for all }i\}
       \le C_{n,j}\prod_{i=1}^j(d_i+\delta)^{-h}.
\end{equation}
When $h=0$, the probability and the factors with exponent $h$ are one.
\end{lemma}

\begin{lemma}[Selection of slices]\label{ang:slice-selection}
Let $0\le h\le n-2$. Let point and direction subprobabilities $\mu,\nu$ in $\R^n$ have
$t$- and $q$-ball bounds with subpower losses, where $t,q>h$.
Assume the directions lie in a fixed small projective chart. Let an
incidence relation $E$ have mass at least subpower, and suppose each
direction fiber is covered by at most $\delta^{-q-o(1)}$ tubes of
width $C\delta$.

For Haar-random codimension-$h$ subspaces $V$ and
$z\in V^\perp$, set
\begin{align*}
 d\nu_V(w)&=\delta^{-h}\one_{\{|P_{V^\perp}w|\le\delta\}}\,d\nu(w),\\
 d\mu_{V,z}(x)&=\delta^{-h}
       \one_{\{|P_{V^\perp}x-z|\le\delta\}}\,d\mu(x).
\end{align*}
Integrate $z$ over a fixed sufficiently large ball. There are families of restrictions
$\widetilde\nu_V\le\nu_V$, $\widetilde\mu_{V,z}\le\mu_{V,z}$,
and relations $\widetilde E_{V,z}\subset E$, measurable in the displayed
parameters and restricted to the two bands defining $\mu_{V,z}$ and
$\nu_V$, such that
\[
 \mathbb E_V\int
 (\widetilde\mu_{V,z}\otimes\widetilde\nu_V)(\widetilde E_{V,z})\,dz
 \ge\delta^{o(1)},
\]
and the following hold:
\begin{enumerate}
\item The restricted measures have masses and ball losses at most
$\delta^{-o(1)}$, with exponents $q-h$ and $t-h$, respectively.
\item Each remaining direction fiber is covered by at most
$\delta^{-(q-h)-o(1)}$ width-$C'\delta$ tubes.
\item Put
\[
 p_{V,z}(x)=P_Vx,\qquad v_V(w)=P_Vw/|P_Vw|
 \quad\text{for }|P_{V^\perp}w|\le\delta.
\]
The first map is projection to $V+z$ followed by translation to $V$;
the second is well-defined on the direction band for small $\delta$.
The coordinate pushforwards of the restricted measures under these maps
satisfy the ball bounds in item~1, with fixed constant changes. For every
original direction label $w$ in that band, the coordinates
$p_{V,z}(\{x:(x,w)\in\widetilde E_{V,z}\})$ have the tube cover in
item~2 with direction $v_V(w)$. This cover remains attached to $w$ even
when two projected direction coordinates coincide.
\end{enumerate}
The direction restriction $\widetilde\nu_V$ depends on $V$ only, and its
mass has an a priori subpower upper bound valid for every $V$.
\end{lemma}

\begin{lemma}[Transverse tube counting]\label{ang:loomis-whitney}
Let $v_1,\ldots,v_m$ be unit vectors in $\R^m$, $m\ge2$, and suppose
$|\det(v_1,\ldots,v_m)|\ge\Delta>0$. If a bounded set $A$ is covered,
for each $i$, by $M_i$ tubes of width $C\delta$ parallel to $v_i$, then
\[
 |A|_{C_m\delta}\le C_{m,C}\Delta^{-m}
       \prod_{i=1}^m M_i^{1/(m-1)}.
\]
Changing the fixed constant in the covering radius changes only the
constant in this inequality.
\end{lemma}

\begin{lemma}[Weak radial estimate]\label{ang:weak-radial}
Fix $k\ge2$, $\zeta>0$, and
\[
 k-2<\ell<\frac{(k-1)^2}{k}.
\]
For every $e>0$ there exist $\epsilon,c>0$ with the following property
for sufficiently small $\delta$. Suppose that a probability $\lambda$
in a bounded subset of $\R^k$ satisfies
\begin{align*}
 \lambda(B(x,r))&\le\delta^{-\epsilon}r^{k-1},\\
 \lambda(H^{(r)})&\le\delta^{-\epsilon}r^\zeta
 \qquad(\delta\le r\le1)
\end{align*}
for every affine hyperplane $H$, where $H^{(r)}$ is its $r$-neighborhood.
There is a measurable pair set $G$ such that
\[
 (\lambda\otimes\lambda)(G^c)\lesssim\delta^c,
 \qquad
 \lambda\{z:(x,z)\in G,\ \pi_x(z)\in B(\theta,r)\}
       \le\delta^{-e}r^\ell
\]
for every $x$, every spherical cap center $\theta$, and
$\delta\le r\le1$. The diagonal is omitted from $G$. The conclusion
also holds for balls in projective direction space, with a fixed change
of constant, by taking the two antipodal caps.
\end{lemma}


# Proofs

## Proof A

\begin{lemma}[Normalized dyadic gain]\label{lpg:unit}
Let $k,q,t,C,\zeta$ be as in the theorem. There are $\epsilon,c,d>0$ such that for every $N$ with $\delta=2^{-N}<d$, every pair $(\mu,\nu)$ satisfying the hypotheses at scale $\delta$ with loss $\epsilon$ and radius $\tfrac14$, and every measurable $E$ with $|x|\le\tfrac14$ for all $(x,w)\in E$ and the fiber cover at scale $\delta$ with loss $\epsilon$, we have $(\mu\otimes\nu)(E)\le\delta^c$.
\end{lemma}

This normalized estimate is taken from earlier work and is obtained in two regimes, writing $k=h+2$. In the endpoint case $q=k-1$ it follows from the endpoint angular gain estimate, after observing that the slab of directions within $r$ of a hyperplane is contained in the plate of \eqref{ang:endpoint-plate}. In the case $q>k-1$ it follows from the non-endpoint dyadic tube gain estimate, which is driven by the planar discretized Furstenberg estimate (Theorem~\ref{ang:furstenberg}). In both regimes the ball bounds are only needed at the dyadic radii $2^{-j}$, $j\le N$. The width condition $|P_{w^\perp}(x-a)|\le C\delta$ is the same as $|(x-a)-\langle w,x-a\rangle w|\le C\delta$.

We also use two elementary facts.

\emph{(a) Absorbing constants.} For $M\ge0$ and $c>0$ there is $d>0$ with $M\delta^c\le\delta^{c/2}$ for $0<\delta<d$. Indeed, $M\delta^{c/2}\to0$, so $M\delta^{c/2}<1$ for small $\delta$. Multiplying by $\delta^{c/2}$ gives the claim.

\emph{(b) Rounding the scale.} Let $\epsilon<\eta$ and $p+\eta\ge0$. Then there is $d>0$ such that $\delta^{-p-\epsilon}\le u^{-p-\eta}$ whenever $0<\delta<d$ and $0<u\le2\delta$. Indeed, choose $d$ so that $\delta^{\eta-\epsilon}\le2^{-p-\eta}$ for $\delta<d$. Then
\[
\delta^{-p-\epsilon}=\delta^{-p-\eta}\delta^{\eta-\epsilon}\le(2\delta)^{-p-\eta}\le u^{-p-\eta},
\]
where the last step uses $u\le2\delta$ and $-p-\eta\le0$.

\begin{proof}
Fix $k,q,t,C,\zeta$ as in the theorem. Fix also a radius $R\ge0$ such that all point measures are supported in $\{|x|\le R\}$. Note that $q\ge k-1\ge1>0$.

\emph{Step 1: bounded support at dyadic scales.} Let $\epsilon,c,d$ be given by Lemma~\ref{lpg:unit}. The closed ball $\overline B(0,R)$ is compact. Hence it is covered by finitely many open balls $B(b,\tfrac14)$ with $b\in\mathcal B$, where $\mathcal B$ is a finite set. By (a), choose $d'>0$ with $\#\mathcal B\cdot\delta^c\le\delta^{c/2}$ for $\delta<d'$.

Let $\delta=2^{-N}<\min(d,d')$. Let $(\mu,\nu)$ satisfy the hypotheses at scale $\delta$ with loss $\epsilon$ and radius $R$. Let $E$ be measurable for the completed product measure and have the fiber cover at scale $\delta$ with loss $\epsilon$. Choose a measurable $E_0\subset E$ with $E_0=E$ up to a $\mu\otimes\nu$-null set. Put
\[
F=E_0\cap\{(x,w):|x|\le R\}.
\]
Since $\mu$ is carried by $\{|x|\le R\}$, we have $(\mu\otimes\nu)(F)=(\mu\otimes\nu)(E)$. Moreover $F\subset E$, so $F$ inherits the fiber cover.

For $b\in\mathcal B$, put $P_b=F\cap\{(x,w):|x-b|\le\tfrac14\}$. Let $\mu_b$ be the pushforward of $\mu|_{\overline B(b,1/4)}$ under $x\mapsto x-b$. Let
\[
E_b=\{(x,w):(x+b,w)\in P_b\}.
\]
We check the hypotheses of Lemma~\ref{lpg:unit} for $\mu_b$, $\nu$ and $E_b$.
\begin{itemize}
\item The measure $\mu_b$ has total mass at most $\mu(\R^{k+1})\le1$, and it is carried by $\overline B(0,\tfrac14)$.
\item We have $\mu_b(B(x,r))\le\mu(B(x+b,r))\le\delta^{-\epsilon}r^t$.
\item The direction measure $\nu$ and its bounds are unchanged.
\item The set $E_b$ is measurable, and $|x|\le\tfrac14$ for every $(x,w)\in E_b$.
\item If $A_w$ is a tube cover for $F_w$, then $A_w-b$ covers $(E_b)_w$ with the same width and at most as many anchors.
\end{itemize}
Translation preserves product mass, so $(\mu_b\otimes\nu)(E_b)=(\mu\otimes\nu)(P_b)$. Lemma~\ref{lpg:unit} therefore gives $(\mu\otimes\nu)(P_b)\le\delta^c$.

Every point of $F$ has $|x|\le R$, so it lies in some $B(b,\tfrac14)$. Hence $F\subset\bigcup_{b\in\mathcal B}P_b$, and
\[
(\mu\otimes\nu)(E)=(\mu\otimes\nu)(F)\le\sum_{b\in\mathcal B}(\mu\otimes\nu)(P_b)\le\#\mathcal B\,\delta^c\le\delta^{c/2}.
\]
Rename $c/2$ as $c$ and $\min(d,d')$ as $\delta_0$. This proves the theorem for dyadic $\delta=2^{-N}<\delta_0$ with loss $\epsilon$, without assuming bounded support of $E$ and without localizing directions. In particular, it holds when all directions of $E$ lie in a cap of radius $\rho=1$ about some $w_0$.

\emph{Step 2: arbitrary scales.} Let $\eta,c,\delta_0$ be as obtained in Step 1. Apply (b) twice with loss gap $\eta/2<\eta$: once with $p=0$, giving a threshold $d_1$, and once with $p=q$, giving a threshold $d_2$. By (a), choose $d_3$ with $2^c\delta^c\le\delta^{c/2}$ for $\delta<d_3$. Set
\[
d=\min(1,\delta_0/2,d_1,d_2,d_3),\qquad \epsilon=\eta/2.
\]
Let $0<\delta<d$, and let $(\mu,\nu,E)$ satisfy the hypotheses at scale $\delta$ with loss $\eta/2$. Choose $N$ with $2^{-N-1}<\delta\le2^{-N}=:u$. Then $\delta\le u\le2\delta$, and $u<\delta_0$.
\begin{itemize}
\item By (b) with $p=0$, we have $\delta^{-\eta/2}\le u^{-\eta}$. The radii $u\le r\le1$ lie in $[\delta,1]$. So the ball bounds and the plate bound at scale $\delta$ with loss $\eta/2$ give the same bounds at scale $u$ with loss $\eta$.
\item By (b) with $p=q$, each anchor set satisfies $\#A_w\le\delta^{-q-\eta/2}\le u^{-q-\eta}$.
\item The width satisfies $C\delta\le Cu$.
\end{itemize}
Thus $(\mu,\nu,E)$ satisfies the hypotheses at the dyadic scale $u$ with loss $\eta$, and Step 1 gives
\[
(\mu\otimes\nu)(E)\le u^c\le2^c\delta^c\le\delta^{c/2}.
\]
This bound holds for every relation $E$ whose directions lie in a cap of radius $\rho=1$.

\emph{Step 3: removing the cap localization.} Let $\rho$, $\epsilon$, $c$ and $\delta_0$ be the constants from Step 2, so that the estimate holds for relations whose directions lie within $\rho$ of a fixed $w_0$. The sphere $S^k$ is compact, so it is covered by finitely many open caps $B(a,\rho)$ with $a\in\mathcal A$, where $\mathcal A$ is a finite set. By (a), choose $d$ with $\#\mathcal A\cdot\delta^c\le\delta^{c/2}$ for $\delta<d$.

Let $\delta<\min(\delta_0,d)$, and let $(\mu,\nu,E)$ satisfy the hypotheses of the theorem. For $a\in\mathcal A$, put
\[
F_a=E\cap\{(x,w):w\in B(a,\rho)\}.
\]
Each $F_a$ is measurable for the completed product measure, has the fiber cover because it is a subset of $E$, and has all its directions within $\rho$ of $a$. Step 2 therefore gives $(\mu\otimes\nu)(F_a)\le\delta^c$. Since $E\subset\bigcup_{a\in\mathcal A}F_a$,
\[
(\mu\otimes\nu)(E)\le\sum_{a\in\mathcal A}(\mu\otimes\nu)(F_a)\le\#\mathcal A\,\delta^c\le\delta^{c/2}.
\]
This is the claim, with loss $\epsilon$, gain $c/2$ and scale threshold $\min(\delta_0,d)$. These constants depend only on $k,q,t,C,R,\zeta$.
\end{proof}


## Proof B

\begin{lemma}[Dyadic non-endpoint gain]\label{lg:nonendpoint}
Let $h\ge1$ be an integer, $h<q\le h+\frac12$, $q<t<h+1$, $C\ge0$. There are $\epsilon,c,\delta_0>0$ such that for every $N$ with $D=2^{-N}<\delta_0$ and all $(\mu,\nu,E)$ in $\mathbb R^{h+2}\times S^{h+1}$ satisfying the dyadic hypotheses at scale $D$ with loss exponent $\epsilon$, exponents $(t,q)$ and width $C$, one has $(\mu\otimes\nu)(E)\le D^{c}$.
\end{lemma}

\begin{lemma}[Dyadic endpoint angular gain]\label{lg:angular}
Let $h\ge0$ be an integer, $h+\frac32<t<h+2$, $\zeta>0$, $C'\ge0$. There are $\epsilon,c>0$ and $N_0$ such that the following holds for $N\ge N_0$ and $D=2^{-N}$. Let $(\mu,\nu)$ on $\mathbb R^{h+3}\times S^{h+2}$ satisfy the ball, support and plate hypotheses above at scale $D$ with loss exponent $\epsilon$ and exponents $(t,h+1)$, let $E$ be measurable with first coordinates in $\{|x|\le\frac14\}$, and let $\{a_i\}_{i\in I}$ be a family of bounded anchors. Suppose that to each $w$ there is assigned a finite set $J(w)\subset I$ with $\#J(w)\le D^{-(h+1)-\epsilon}$ such that every $(x,w)\in E$ satisfies $|P_{w^\perp}(x-a_i)|\le C'D$ for some $i\in J(w)$. Then $(\mu\otimes\nu)(E)\le D^c$.
\end{lemma}

\begin{lemma}[Preparation of the tube relation]\label{lg:prepare}
Let $\mu$ be a finite measure, $E$ a measurable relation with first coordinates in $\{|x|\le\frac14\}$, $\delta>0$ and $M\in\mathbb N$, and suppose every fiber $E_w$ is covered by at most $M$ tubes of width $C\delta$ parallel to $w$. Then there are a finite set $G$ of bounded anchors, a measurable relation $F\subset E$ and, for each $w$, a set $J(w)\subset G$ with $\#J(w)\le M$, such that each fiber $(E\setminus F)_w$ is $\mu$-null and every $(x,w)\in F$ satisfies $|P_{w^\perp}(x-a)|\le (2C+1)\delta$ for some $a\in J(w)$.
\end{lemma}

The non-endpoint lemma rests on the planar discretized Furstenberg estimate (Theorem~\ref{ang:furstenberg}), and the endpoint lemma on transverse tube counting (Lemma~\ref{ang:loomis-whitney}).

\begin{proof}
\emph{Step 1: the endpoint dyadic statement for arbitrary covers.} Let $h\ge0$, $h+\frac32<t<h+2$, $\zeta>0$, $C\ge0$. We claim that the conclusion of Lemma~\ref{lg:nonendpoint} holds in $\mathbb R^{h+3}\times S^{h+2}$ with $q=h+1$, for $N\ge N_0$, when the plate condition is added to the dyadic hypotheses. Apply Lemma~\ref{lg:angular} with width constant $C'=2C+1$ to obtain $\epsilon,c,N_0$. Given $(\mu,\nu,E)$ at scale $D=2^{-N}$, $N\ge N_0$, apply Lemma~\ref{lg:prepare} with $M=\lfloor D^{-(h+1)-\epsilon}\rfloor$. This gives a finite anchor set $G$, a relation $F\subset E$ and sets $J(w)\subset G$ with $\#J(w)\le M\le D^{-(h+1)-\epsilon}$ such that every $(x,w)\in F$ lies in a tube of width $(2C+1)D$ parallel to $w$ about some anchor of $J(w)$. Since every fiber $(E\setminus F)_w$ is $\mu$-null, Fubini gives $(\mu\otimes\nu)(E\setminus F)=0$, hence $(\mu\otimes\nu)(F)=(\mu\otimes\nu)(E)$. The relation $F$ inherits the support condition from $E$, and Lemma~\ref{lg:angular} applied to $F$ with the anchors $G$ gives $(\mu\otimes\nu)(E)=(\mu\otimes\nu)(F)\le D^c$.

Similarly, Lemma~\ref{lg:nonendpoint} gives the dyadic statement in the non-endpoint range. Choose $N_0$ with $2^{-N}<\delta_0$ for $N\ge N_0$. A plate hypothesis is simply not used there.

\emph{Step 2: case split.} If $q=k-1$, write $k=h+2$ with $h\ge0$. Then $q=h+1$ and $h+\frac32<t<h+2$. The plate hypothesis \eqref{ang:endpoint-plate} is in force, since for a hyperplane with unit normal $n$ one has $\dist(w,H)=|\langle n,w\rangle|$. Step 1 provides the dyadic statement in $\mathbb R^{h+3}=\mathbb R^{k+1}$ with plate condition. If $q>k-1$, write $k=h+1$ with $h\ge1$. Then $h<q\le h+\frac12$, and $q\le k-\frac12<t<h+1$. Lemma~\ref{lg:nonendpoint} provides the dyadic statement in $\mathbb R^{h+2}=\mathbb R^{k+1}$. In either case we have, in $\mathbb R^{d}$ with $d=k+1$, constants $\epsilon_0,c_0>0$ and $N_0$ such that for $N\ge N_0$ every triple satisfying the dyadic hypotheses at scale $2^{-N}$ with loss exponent $\epsilon_0$ (together with the plate condition in the endpoint case) has product mass at most $2^{-Nc_0}$. It remains to pass from this dyadic, normalized form to the theorem at arbitrary scales and for support in a ball of radius $R$. Here only $t,q\ge0$ and $C\ge0$ are used.

\emph{Step 3: choice of constants.} Put $\epsilon=\epsilon_0/2$, $c=c_0/2$ and $s=1/(4(R+1))$, so that $0<s\le1$ and $sR\le\frac14$. Put
\[
 K=2^{\epsilon}s^{-t}+2^{q+\epsilon}.
\]
Then $K$ dominates each of $2^\epsilon s^{-t}$, $2^{q+\epsilon}$, $2^\epsilon$ and $s^{-t}$, because all these quantities are at least $1$. Since $2^{N\epsilon}\to\infty$, choose $N_1$ with $2^{N\epsilon}\ge K$ for all $N\ge N_1$. Set $\delta_0=\min(\frac14,2^{-(N_0+N_1+1)})$.

\emph{Step 4: the dyadic scale.} Let $0<\delta<\delta_0$ and let $\mu,\nu,E$ satisfy the hypotheses of the theorem. Choose $N$ with $2^N\le1/\delta<2^{N+1}$ and put $D=2^{-N}$. Then $D\le1$ and $\delta\le D<2\delta$. Moreover $2^{N_0+N_1+1}<1/\delta<2^{N+1}$, so $N\ge N_0+N_1$. Let $A=D^{-\epsilon}=2^{N\epsilon}$. Then $A\ge K\ge1$ and $D^{-\epsilon_0}=A^2$. Since $D/2\le\delta$, for every $e\ge0$
\[
 \delta^{-e}\le (D/2)^{-e}=2^{e}D^{-e};\qquad\text{in particular}\quad \delta^{-\epsilon}\le 2^\epsilon A .
\]

\emph{Step 5: rescaling.} Let $f(x)=sx$, $\mu'=f_\#\mu$, and
\[
 E'=\{(y,w):|y|\le\tfrac14,\ (s^{-1}y,w)\in E\},
\]
which is measurable. Then $\mu'$ has the same total mass as $\mu$, so it is a subprobability. Since $\mu$ is concentrated on $\overline B(0,R)$ and $sR\le\frac14$, the measure $\mu'$ is concentrated on $\{|y|\le\frac14\}$. By construction every point of $E'$ has first coordinate in that ball. We verify the dyadic hypotheses for $(\mu',\nu,E')$ at scale $D$ with loss exponent $\epsilon_0$.

\emph{Point balls.} Let $0\le j\le N$ and $r=2^{-j}$, so $D\le r\le1$. Since $f^{-1}(B(x,r))=B(s^{-1}x,r/s)$, we have $\mu'(B(x,r))=\mu(B(s^{-1}x,r/s))$. If $r/s\le1$, then $\delta\le r\le r/s$ and the $t$-ball bound for $\mu$ gives
\[
 \mu'(B(x,r))\le\delta^{-\epsilon}s^{-t}r^t\le(2^\epsilon s^{-t})A\,r^t\le KA\,r^t\le A^2r^t=D^{-\epsilon_0}r^t .
\]
If $r/s>1$, then $s<r$, and
\[
 \mu'(B(x,r))\le1=s^{-t}s^t\le A\,r^t\le A^2r^t ,
\]
using $s^{-t}\le K\le A$, $s^t\le r^t$ and $A\ge1$.

\emph{Direction balls and plates.} For $0\le j\le N$ and $r=2^{-j}$ we have $\delta\le D\le r\le1$. The $q$-ball bound for $\nu$ gives $\nu(B(w,r))\le\delta^{-\epsilon}r^q\le 2^\epsilon A r^q\le KAr^q\le A^2r^q$. In the endpoint case the same computation applies, for $D\le r\le1$, to the plate bound $\nu\{u:|\langle n,u\rangle|\le r\}\le\delta^{-\epsilon}r^\zeta\le A^2r^\zeta$.

\emph{Tube covers.} Fix $w$, and let $T$ be the set of at most $\delta^{-q-\epsilon}$ anchors covering $E_w$ by tubes of width $C\delta$. Take the anchors $sT$. Their number is at most
\[
 \delta^{-q-\epsilon}\le 2^{q+\epsilon}D^{-q-\epsilon}\le K D^{-q-\epsilon}\le A\,D^{-q-\epsilon}=D^{-q-\epsilon_0}.
\]
If $(y,w)\in E'$, then $x=s^{-1}y\in E_w$, so $|P_{w^\perp}(x-a)|\le C\delta$ for some $a\in T$. By linearity of $P_{w^\perp}$,
\[
 |P_{w^\perp}(y-sa)|=s\,|P_{w^\perp}(x-a)|\le C\delta\le CD,
\]
using $s\le1$ and $\delta\le D$. Thus $E'_w$ is covered by at most $D^{-q-\epsilon_0}$ tubes of width $CD$ parallel to $w$.

Since $N\ge N_0$, Step 2 yields
\[
 (\mu'\otimes\nu)(E')\le D^{c_0}.
\]

\emph{Step 6: comparison with the original relation.} We have $\mu'\otimes\nu=(f\times\mathrm{id})_\#(\mu\otimes\nu)$, so $(\mu'\otimes\nu)(E')=(\mu\otimes\nu)((f\times\mathrm{id})^{-1}E')$. If $(x,w)\in E$ and $|x|\le R$, then $|sx|\le sR\le\frac14$ and $(s^{-1}sx,w)=(x,w)\in E$, so $(x,w)\in(f\times\mathrm{id})^{-1}E'$. Hence
\[
 E\subset (f\times\mathrm{id})^{-1}E'\ \cup\ \bigl(\overline B(0,R)^c\times S^k\bigr).
\]
The second set has $(\mu\otimes\nu)$-measure $\mu(\overline B(0,R)^c)\,\nu(S^k)=0$. Therefore $(\mu\otimes\nu)(E)\le(\mu'\otimes\nu)(E')\le D^{c_0}$.

\emph{Step 7: return to the scale $\delta$.} Since $\delta\le\frac14$ we have $\sqrt\delta\le\frac12$, so $D\le2\delta=2\sqrt\delta\cdot\sqrt\delta\le\sqrt\delta$. Hence
\[
 (\mu\otimes\nu)(E)\le D^{c_0}\le\delta^{c_0/2}=\delta^{c}.
\]
The constants $\epsilon,c,\delta_0$ depend only on $k,q,t,C,R$ and, at the endpoint, on $\zeta$. This proves the theorem.
\end{proof}


## Proof C

\begin{proof}[Proof of Theorem~\ref{ang:linear-gain}]
We rule out any sequence with subpower input losses, subpower incidence
mass from below, and cover size $\delta^{-q-o(1)}$. This implies the
stated fixed-power result: if no positive $\epsilon,c$ worked, choose
counterexamples with $\epsilon=c=1/j$ at scales
$\delta_j<1/j$ tending to zero. They would form precisely such a
sequence. This observation will also justify all uses of the gain with
sufficiently small fixed losses.

By choosing one of finitely many small projective charts, we can assume
all relevant directions lie in a single chart and that incidence still
has subpower mass. If $q>k-1$, apply
Lemma~\ref{ang:slice-selection} with $h=k-1$. Select a slice with
subpower incidence and normalize its marginal restrictions; their
masses are bounded above by subpower and below by the incidence divided
by the other marginal mass. The coordinate maps take values in a plane, with
\[
 b=q-h\in(0,\tfrac12],\qquad
 f=t-h\in(\tfrac12,1),\qquad b<f,
\]
and tube count at most $\delta^{-b-o(1)}$. Apply
Lemma~\ref{ang:planar-measures} with the original sliced points and
directions as labels, and with coordinate maps $p_{V,z}$ and $v_V$.
Item~3 of Lemma~\ref{ang:slice-selection} gives the ball bounds on their
coordinate pushforwards and the separate cover for each original direction
label. The labeled incidence relation still has subpower mass, so these
data contradict the planar obstruction.

At $q=k-1$, slicing to the plane would leave direction exponent zero,
outside the range of Lemma~\ref{ang:planar-measures}. We therefore put
$h=k-2$, so the selected slices have dimension three, and let
\[
 g=t-h-\tfrac32>0.
\]
Choose once and for all $0<a<g/4$. We will find in one slice three
directions of determinant at least $c\delta^a$ with a common incident
point set of mass at least subpower. The resulting loss in
Lemma~\ref{ang:loomis-whitney} is $O(\delta^{-3a})$, which the
strict gap $g$ will absorb.

Parameterize our chart by $p\in\R^k$, with unit direction
$w(p)=(1,p)/\sqrt{1+|p|^2}$. Restricting and normalizing the chart
costs only a subpower factor; denote the resulting law in $p$ by
$\lambda$. In the rest of the endpoint proof the direction law supplied
to slicing is $w_\#\lambda$, and the incidence relation is restricted to
this chart. The slice law of the chart labels is
\[
 d\lambda_V(p)=\delta^{-h}
 \one_{\{|P_{V^\perp}w(p)|\le\delta\}}\,d\lambda(p),
 \qquad \nu_V=w_\#\lambda_V.
\]
Equation~\eqref{ang:endpoint-plate}
becomes the affine-hyperplane bound in the $p$ coordinates, because
an affine hyperplane there is the intersection of a linear hyperplane
with the chart. The ball exponent remains $k-1$. Choose
\[
 h<\ell<\frac{(k-1)^2}{k}=h+\frac1k.
\]
Apply Lemma~\ref{ang:weak-radial} to this chart law, with a small
fixed output loss $\delta^{-e}$. Its hypotheses hold at sufficiently
small scales for every fixed input-loss threshold. This deletes a
pair set of original product mass $O(\delta^{c_e})$ and gives, for
every anchor $p$, an $\ell$-cap bound $\delta^{-e}r^\ell$ on
the undeleted displacement directions. Also delete pairs at distance
less than $\delta^{b_0}$, where $b_0>0$ will be small. Denote the union
of these two exceptional pair relations by $\mathcal E_{\mathrm{pair}}$,
and call an anchored pair retained when it lies outside this union.

We first record how these deletions transfer to normalized slice-pair
mass. Equation~\eqref{ang:direction-pair-kernel}
shows that for every measurable chart-pair relation $\mathcal E$ with
$(\lambda\otimes\lambda)(\mathcal E)\le\delta^c$, and every fixed
$\theta>0$,
\begin{equation}\label{ang:exceptional-pair-transfer}
 \mathbb E_V(\lambda_V\otimes\lambda_V)(\mathcal E)
 \le C\delta^{c-\theta h}
       +\delta^{\theta(q-h)-o(1)}.
\end{equation}
For $0<\theta\le1$, the first term treats distances greater than
$\delta^\theta$, and the second treats smaller distances by the ball
bound and annular summation. For $\theta\ge1$, the kernel is at most
$C\delta^{-h}$, so the whole expectation is at most
$C\delta^{c-h}\le C\delta^{c-\theta h}$. The same annulus calculation
bounds the expected mass of the close pairs by
$\delta^{b_0(q-h)-o(1)}$. We leave $\theta$ free until $e$, and hence
the weak-radial deletion exponent $c_e$, has been fixed.

We next bound triples that are close to linearly dependent. For two
retained anchored pairs $(p,p'),(p,p'')$, set
\[
 \alpha=\left|
 \frac{p'-p}{|p'-p|}\wedge\frac{p''-p}{|p''-p|}\right|.
\]
In a bounded chart,
\begin{equation}\label{ang:chart-wedge}
 |w(p)\wedge w(p')\wedge w(p'')|
       \asymp |p'-p|\,|p''-p|\,\alpha.
\end{equation}
To see this, put $u=p'-p$ and $v=p''-p$ and subtract the first
unnormalized column from the other two. The orthogonal decomposition
of exterior powers gives the identity
\[
 |(1,p)\wedge(0,u)\wedge(0,v)|^2
       =|u\wedge v|^2+|p\wedge u\wedge v|^2.
\]
It supplies the lower bound, while boundedness of $p$ supplies the
upper bound. Normalizing the three columns changes only fixed constants.
Consequently a wedge smaller than $2\delta^a$ implies
$\alpha\le C\delta^{a-2b_0}$.

For $(w_1,w_2,w_3)=(w(p),w(p'),w(p''))$, the largest singular
value is comparable to one. Their first two columns span area at least $c\delta^{b_0}$,
so the second singular value is at least $c\delta^{b_0}$; by
Equation~\eqref{ang:chart-wedge}, the third is at least
$c\delta^{2b_0}\alpha$. Lemma~\ref{ang:haar} therefore bounds
their normalized expected slicing weight by
\begin{equation}\label{ang:triple-weight}
 \delta^{-3h}\Pr_V\{\max_{1\le i\le3}|P_{V^\perp}w_i|\le\delta\}
 \le C\delta^{-3hb_0}(\alpha+\delta)^{-h}.
\end{equation}
This includes singular values below $\delta$, since the kernel is
truncated there. At fixed $p,p'$, the weak radial estimate and
the two antipodal caps give
\[
 \lambda\{p'':(p,p'')\text{ is retained},\ \alpha\le r\}
       \le C\delta^{-e}r^\ell
       \qquad(\delta\le r\le1).
\]
Let $\mathcal T_\delta$ be the chart triples whose two anchored pairs
are retained and whose original wedge has size less than $2\delta^a$.
Summing dyadic annuli in Equation~\eqref{ang:triple-weight}, up to
$C\delta^{a-2b_0}$, gives
\begin{equation}\label{ang:bad-triples}
 \mathbb E_V\lambda_V^{\otimes3}(\mathcal T_\delta)
 \le C\delta^{(a-2b_0)(\ell-h)-e-3hb_0}.
\end{equation}
Since $\ell>h$, first choose $b_0>0$ sufficiently small depending
on $a,\ell,h$, and then $e>0$ sufficiently small, so that this
exponent is positive. These choices also ensure $a-2b_0>0$.
With $e$ fixed, the weak radial estimate fixes $c_e>0$. Now choose
$\theta>0$ small enough that $c_e-\theta h>0$. Since $q-h=1$, the
second exponent in Equation~\eqref{ang:exceptional-pair-transfer} is
also positive. Together with the close-pair bound, this proves that
$\mathcal E_{\mathrm{pair}}$ has power-small expected slice-pair mass.

Perform the restrictions in Lemma~\ref{ang:slice-selection}, and
write $\widetilde\lambda_V=(w^{-1})_\#\widetilde\nu_V$ for the restricted
law of chart labels. It is dominated by $\lambda_V$ and has the same
uniform subpower mass bound as $\widetilde\nu_V$. Define
\[
 F(V,z,x)=\widetilde\lambda_V
 \{p:(x,w(p))\in\widetilde E_{V,z}\}.
\]
Its integrated first moment is the retained sliced incidence and is at
least subpower, while the total integrated point mass is bounded by a
fixed constant.
H\"older's inequality consequently yields
\begin{equation}\label{ang:triple-incidence}
 \mathbb E_V\int\int F(V,z,x)^3
                 \,d\widetilde\mu_{V,z}(x)\,dz
       \ge\delta^{o(1)}.
\end{equation}
Dropping the point-incidence indicators bounds the contributions of
bad triples and exceptional anchored pairs by the left-hand sides below.
Equation~\eqref{ang:point-slice-total} and
$\widetilde\lambda_V\le\lambda_V$ give
\begin{align*}
 \mathbb E_V\int \|\widetilde\mu_{V,z}\|
      \widetilde\lambda_V^{\otimes3}(\mathcal T_\delta)\,dz
 &\le C\mathbb E_V\lambda_V^{\otimes3}(\mathcal T_\delta),\\
 \mathbb E_V\int \|\widetilde\mu_{V,z}\|\,\|\widetilde\lambda_V\|
      (\widetilde\lambda_V\otimes\widetilde\lambda_V)
          (\mathcal E_{\mathrm{pair}})\,dz
 &\le C\sup_V\|\widetilde\lambda_V\|\,
      \mathbb E_V(\lambda_V\otimes\lambda_V)
          (\mathcal E_{\mathrm{pair}}).
\end{align*}
Both quantities are power-small by Equation~\eqref{ang:bad-triples}
and the preceding bound for $\mathcal E_{\mathrm{pair}}$; the latter
also covers the two possible anchored pairs after changing the constant. No independence
between the point and direction slices is used. Hence a
subpower amount of the triple incidence in
Equation~\eqref{ang:triple-incidence} has original wedge at least
$2\delta^a$. Projection to $V$ and unit normalization change each
vector by $O(\delta)$, so their determinant in $V$ is at least
$\delta^a$ for small $\delta$.

The total parameter mass for integrating $(V,z)$ and three restricted
chart labels is at most subpower, since $\|\widetilde\lambda_V\|$ has a
uniform subpower bound and the $z$-domain is bounded.
It follows that some slice and some such triple have a common
incident point set of sliced mass at least subpower. Let $A$ be its
projected point coordinates. The pushforward of its restricted point
measure has the same mass and inherits the point-coordinate ball bound,
which implies
\[
 |A|_\delta\ge\delta^{-(t-h)+o(1)}.
\]
For each of the three original direction labels, the projected common
point set has its own cover by
$\delta^{-(q-h)-o(1)}=\delta^{-1-o(1)}$ tubes in that label's projected
direction. By
Lemma~\ref{ang:loomis-whitney},
\[
 |A|_\delta\le\delta^{-3/2-3a-o(1)}.
\]
This contradicts $3a<g=t-h-3/2$. When $k=2$ we have $h=0$;
all slicing weights equal one and the same proof applies, with the
$z$-integral interpreted as integration over the singleton
zero-dimensional space. The endpoint and the theorem are proved.
\end{proof}


## Proof D

\begin{proof}
The proof has two regimes. When \(q>k-1\), slicing reduces the problem to the planar measure incidence obstruction. At \(q=k-1\), planar slicing would leave direction exponent zero. We instead slice to three dimensions, use the plate hypothesis to find three quantitatively transverse directions with many common incident points, and apply transverse tube counting.

\emph{Reduction to subpower losses.}
It suffices to exclude a sequence \(\delta\to0\) for which the ball bounds, and the plate bound when applicable, have losses \(\delta^{-o(1)}\), every fiber has a cover by \(\delta^{-q-o(1)}\) tubes, and
\[
(\mu\otimes\nu)(E)\ge \delta^{o(1)}.
\]
Indeed, if the theorem failed, counterexamples with \(\epsilon=c=1/j\) could be chosen at scales tending to zero.

We may restrict \(E\) to the fixed bounded region carrying \(\mu\), without changing its product mass or increasing any fiber cover. We may also round \(\delta\) upward to a dyadic scale \(D\in[\delta,2\delta)\): the bounds remain valid with subpower losses, and tubes of width \(C\delta\) have width at most \(CD\). Rename this scale \(\delta\). Finally, a finite cover by small projective charts allows us to restrict the directions to one chart while retaining subpower incidence mass. All subsequent \(o(1)\)'s refer to this sequence.

\emph{The non-endpoint case.}
Suppose \(q>k-1\), and apply Lemma~\ref{ang:slice-selection} with \(h=k-1\). Its averaged incidence lower bound gives a slice with incidence mass at least subpower. Both restricted marginal masses are at most \(\delta^{-o(1)}\); each is also at least subpower, since their product dominates the incidence mass. Thus normalizing the two marginals preserves all subpower bounds and the incidence lower bound.

The coordinate maps of this slice take values in a plane, and their pushforwards have ball exponents
\[
b=q-(k-1)\in(0,\tfrac12],
\qquad
f=t-(k-1)\in(\tfrac12,1).
\]
In particular, \(0<b<f<2\). For every original direction label, item~3 of Lemma~\ref{ang:slice-selection} supplies a cover of its point coordinates by at most \(\delta^{-b-o(1)}\) strips in the corresponding projected direction. Keeping the original points and directions as labels, these data contradict Lemma~\ref{ang:planar-measures}.

\emph{The endpoint: setup and slicing identities.}
Now let \(q=k-1\), and put
\[
h=k-2,\qquad s=t-h,\qquad g=s-\tfrac32>0.
\]
The slices will have dimension three, point exponent \(s>\tfrac32\), and direction exponent \(q-h=1\). Choose
\[
0<a<g/4,
\qquad
h<\ell<\frac{(k-1)^2}{k}=h+\frac1k.
\]
Our objective is to find three projected directions with determinant at least \(\delta^a\) and a common incident point set of subpower sliced mass. Transverse tube counting will then give covering exponent at most \(\tfrac32+3a<s\).

After a fixed rotation, write the chosen direction chart as
\[
w(p)=\frac{(1,p)}{\sqrt{1+|p|^2}},
\qquad p\in\mathbb R^k
\]
with \(p\) in a fixed bounded set. Normalize the restricted direction measure and denote its chart-coordinate law by \(\lambda\). This costs only a subpower factor: the mass of the chart is at least its incidence mass. The chart map is bi-Lipschitz, so \(\lambda\) has a \((k-1)\)-ball bound with subpower loss. It also satisfies
\[
\lambda(H^{(r)})\le \delta^{-o(1)}r^\zeta
\qquad(\delta\le r\le1)
\]
for every affine hyperplane \(H\subset\mathbb R^k\). Indeed, the equation of an affine hyperplane in \(p\)-coordinates becomes a homogeneous linear equation in \((1,p)\), and the bounded chart changes distances only by fixed factors in the required inclusion.

For a codimension-\(h\) subspace \(V\), define
\[
d\lambda_V(p)=
\delta^{-h}\mathbf 1_{\{|P_{V^\perp}w(p)|\le\delta\}}\,d\lambda(p).
\]
We shall use two elementary consequences of the slicing definitions and Lemma~\ref{ang:haar}. First, for every \(V\),
\begin{equation}\label{new:point-total}
\int \|\mu_{V,z}\|\,dz\le C.
\end{equation}
This follows by integrating the indicator
\(\mathbf 1_{\{|P_{V^\perp}x-z|\le\delta\}}\) in \(z\); its integral is at most \(C\delta^h\).

Second, the two-vector Haar estimate and the chart geometry give
\begin{equation}\label{new:pair-kernel}
\delta^{-2h}
\Pr_V\{w(p),w(p')\text{ both lie in the direction band}\}
\le C(|p-p'|+\delta)^{-h}.
\end{equation}
Here the largest singular value of the two unit columns is comparable to one, and the smaller is comparable to \(|p-p'|\). Since \(q=h+1>h\), the ball bound for \(\lambda\), summed over dyadic annuli, yields
\begin{equation}\label{new:close-pairs}
\mathbb E_V\lambda_V^{\otimes2}
 \{(p,p'):|p-p'|\le r\}
\le \delta^{-o(1)}r^{q-h}
\qquad(\delta\le r\le1).
\end{equation}
The innermost ball contributes at most
\(\delta^{-h}\delta^{q-o(1)}\); the remaining annuli form a geometric sum with exponent \(q-h>0\).

Consequently, if a pair relation \(B\) has
\(\lambda^{\otimes2}(B)\le C\delta^c\), then, for \(0<\theta<1\),
\begin{equation}\label{new:pair-transfer}
\mathbb E_V\lambda_V^{\otimes2}(B)
\le C\delta^{c-\theta h}
   +\delta^{\theta(q-h)-o(1)}.
\end{equation}
To obtain this, split at \(|p-p'|=\delta^\theta\), using
\eqref{new:pair-kernel} on the distant pairs and
\eqref{new:close-pairs} on the close pairs.

\emph{Few sliced triples are nearly dependent.}
Choose \(\beta>0\) sufficiently small and then \(e>0\) sufficiently small that
\[
\beta<a/2,
\qquad
\eta:=(a-2\beta)(\ell-h)-3h\beta-e>0.
\]
Apply Lemma~\ref{ang:weak-radial} to \(\lambda\), with output loss \(\delta^{-e}\). Its fixed input-loss requirements hold eventually along our subpower sequence. It gives a pair relation \(G\) such that
\[
\lambda^{\otimes2}(G^c)\le C\delta^{c_e}
\]
for some \(c_e>0\), and, for every anchor \(p\), the retained displacement directions satisfy the \(\ell\)-cap bound with loss \(\delta^{-e}\).

Call \((p,p')\) good if it belongs to \(G\) and
\(|p-p'|\ge\delta^\beta\), and let \(B\) be the relation of pairs that are not good. Choose \(0<\theta<1\) so small that \(c_e-\theta h>0\). Equations~\eqref{new:close-pairs} and \eqref{new:pair-transfer}, together with \(q-h=1\), imply that, for some \(\kappa>0\),
\begin{equation}\label{new:bad-pairs}
\mathbb E_V\lambda_V^{\otimes2}(B)\le C\delta^\kappa.
\end{equation}

Consider a triple \((p,p',p'')\) for which both anchored pairs
\((p,p')\) and \((p,p'')\) are good. Set
\[
u=p'-p,\qquad v=p''-p,\qquad
\alpha=\left|\frac{u}{|u|}\wedge\frac{v}{|v|}\right|.
\]
The chart geometry gives
\begin{equation}\label{new:wedge}
|w(p)\wedge w(p')\wedge w(p'')|
\asymp |u|\,|v|\,\alpha.
\end{equation}
For completeness, subtracting the first unnormalized column from the other two gives
\[
|(1,p)\wedge(0,u)\wedge(0,v)|^2
=|u\wedge v|^2+|p\wedge u\wedge v|^2.
\]
Boundedness of \(p\), followed by normalization of the columns, proves \eqref{new:wedge}.

Let \(d_1\ge d_2\ge d_3\) be the singular values of these three unit columns. We have
\[
d_1\asymp1,\qquad d_2\gtrsim\delta^\beta,
\qquad d_3\gtrsim\delta^{2\beta}\alpha.
\]
The second inequality follows from the area spanned by the first two columns; the third follows from \eqref{new:wedge} and the boundedness of \(d_1d_2\). Lemma~\ref{ang:haar} therefore gives
\begin{equation}\label{new:triple-kernel}
\delta^{-3h}
\Pr_V\{w(p),w(p'),w(p'')\text{ all lie in the direction band}\}
\le C\delta^{-3h\beta}(\alpha+\delta)^{-h}.
\end{equation}

Let \(T\) consist of these good-anchored triples whose wedge in
\eqref{new:wedge} is smaller than \(2\delta^a\). Since
\(|u|,|v|\ge\delta^\beta\), every triple in \(T\) satisfies
\[
\alpha\le R:=C\delta^{a-2\beta}.
\]
For fixed \(p,p'\), the weak radial estimate, applied to the two antipodal caps about the direction of \(p'-p\), gives
\[
\lambda\{p'':(p,p'')\text{ is good},\ \alpha\le r\}
\le C\delta^{-e}r^\ell
\qquad(\delta\le r\le1).
\]
Because \(\ell>h\), summing dyadic annuli, including the innermost region \(\alpha\le\delta\), yields
\[
\int_{\substack{(p,p'')\text{ good}\\ \alpha\le R}}
(\alpha+\delta)^{-h}\,d\lambda(p'')
\le C\delta^{-e}R^{\ell-h}.
\]
Combining this with \eqref{new:triple-kernel} proves
\begin{equation}\label{new:bad-triples}
\mathbb E_V\lambda_V^{\otimes3}(T)
\le C\delta^{(a-2\beta)(\ell-h)-3h\beta-e}
=C\delta^\eta.
\end{equation}
Thus both exceptional pairs and nearly dependent good-anchored triples have power-small expected sliced mass.

\emph{Extracting a transverse triple with common incidence.}
Apply Lemma~\ref{ang:slice-selection} with \(h=k-2\), using the direction law \(w_\#\lambda\). Write its restricted measures as
\[
\widetilde\mu_{V,z},\qquad
\widetilde\lambda_V=(w^{-1})_\#\widetilde\nu_V,
\]
and its restricted relation as \(\widetilde E_{V,z}\). In particular,
\[
\widetilde\lambda_V\le\lambda_V,
\qquad
L_\delta:=\sup_V\|\widetilde\lambda_V\|
\le\delta^{-o(1)}.
\]
Define
\[
F(V,z,x)=
\widetilde\lambda_V
\{p:(x,w(p))\in\widetilde E_{V,z}\}.
\]
The slice-selection lemma gives
\[
I:=\mathbb E_V\int\!\int F(V,z,x)\,
d\widetilde\mu_{V,z}(x)\,dz\ge\delta^{o(1)}.
\]
By \eqref{new:point-total}, the measure against which \(F\) is integrated has total mass at most \(C\). Hölder's inequality therefore gives
\begin{equation}\label{new:triple-incidence}
\mathbb E_V\int\!\int F(V,z,x)^3\,
d\widetilde\mu_{V,z}(x)\,dz
\ge C^{-2}I^3\ge\delta^{o(1)}.
\end{equation}
This is the integrated mass of triples of directions incident to a common point.

We now remove triples with an exceptional anchored pair or belonging to \(T\). Dropping the point-incidence conditions and using
\eqref{new:point-total}, their contributions are bounded respectively by
\[
2C L_\delta\,
\mathbb E_V\lambda_V^{\otimes2}(B)
\quad\text{and}\quad
C\,\mathbb E_V\lambda_V^{\otimes3}(T).
\]
Both are power-small by \eqref{new:bad-pairs} and
\eqref{new:bad-triples}. This argument uses the uniform mass bound on
\(\widetilde\lambda_V\) and its independence of \(z\); it requires no independence between the point and direction slices.

It follows from \eqref{new:triple-incidence} that a subpower amount of common-point triple incidence has
\[
|w(p_1)\wedge w(p_2)\wedge w(p_3)|\ge2\delta^a.
\]
For directions in the band, projection to \(V\) and unit normalization change each vector by \(O(\delta)\). Since \(a<1\), their projected unit directions
\[
v_i=\frac{P_Vw(p_i)}{|P_Vw(p_i)|}
\]
therefore satisfy
\[
|\det_V(v_1,v_2,v_3)|\ge\delta^a
\]
for sufficiently small \(\delta\).

The total measure of the parameters \((V,z,p_1,p_2,p_3)\), using the three restricted direction measures, is at most
\(C L_\delta^3\le\delta^{-o(1)}\). Hence some slice and some such transverse triple have a common incident point set \(X_*\) with
\[
\widetilde\mu_{V,z}(X_*)\ge\delta^{o(1)}.
\]
Let \(A=P_V(X_*)\). The pushforward of
\(\widetilde\mu_{V,z}|_{X_*}\) has this same mass and inherits the point-coordinate \(s\)-ball bound. Consequently, for any fixed covering-radius constant \(K\ge1\),
\[
|A|_{K\delta}\ge\delta^{-s+o(1)}.
\]
For each of the three original direction labels, item~3 of the slice-selection lemma supplies a cover of \(A\) by at most
\[
\delta^{-(q-h)-o(1)}=\delta^{-1-o(1)}
\]
tubes parallel to \(v_i\). Lemma~\ref{ang:loomis-whitney}, in dimension three, now gives
\[
|A|_{K\delta}\le
C(\delta^a)^{-3}
\left(\delta^{-1-o(1)}\right)^{3/2}
=\delta^{-3/2-3a-o(1)},
\]
with a fixed permissible \(K\). This contradicts
\(s=\tfrac32+g>\tfrac32+3a\).

When \(k=2\), we have \(h=0\); all slicing weights equal one, and the \(z\)-integral is over the singleton zero-dimensional space. Every estimate above remains valid. Thus the endpoint is also impossible, completing the subpower contradiction and proving the theorem.
\end{proof}


## Proof E

\paragraph{Overview.} Write $n=k+1$. The proof is by contradiction, and it slices $\R^{n}$ by Haar-random codimension-$h$ subspaces (Lemma~\ref{ang:slice-selection}). There are two regimes.

\emph{Non-endpoint, $q>k-1$.} Slice with $h=k-1$ down to planes. The sliced exponents $b=q-h\in(0,\tfrac12]$ and $f=t-h\in(\tfrac12,1)$ lie in the range of the planar obstruction (Lemma~\ref{ang:planar-measures}), so that lemma gives the contradiction directly.

\emph{Endpoint, $q=k-1$.} Slicing to planes would give $b=0$, so we slice with $h=k-2$ to $3$-dimensional spaces instead. In a slice the direction exponent is $1$, the point exponent is $t-h>\tfrac32$, and each direction fiber needs about $\delta^{-1}$ tubes. If three directions were uniformly transverse, transverse tube counting (Lemma~\ref{ang:loomis-whitney}) would bound a common incident point set by $\delta^{-3/2}$ balls. The ball bound needs about $\delta^{-(t-h)}$ balls, which is a contradiction. The real work is to find three directions that are \emph{quantitatively} transverse, with determinant $\ge\delta^a$ for a small $a$, and that share an incident point set of non-negligible mass. This is where the plate hypothesis~\eqref{ang:endpoint-plate} enters. Through the weak radial estimate (Lemma~\ref{ang:weak-radial}) it prevents the directions from concentrating near great subspheres, which is exactly how all triples could be nearly coplanar. The Haar band estimates (Lemma~\ref{ang:haar}) show that this non-concentration survives slicing.

Throughout, $C,c$ denote positive constants depending only on the fixed parameters $k,q,t,C,\zeta$ and on the auxiliary exponents fixed below. They may change from line to line.

\begin{proof}
\textbf{Step 0: Reductions.}

\emph{(a) Sequences.} Suppose the theorem fails. Then for each $j$ the choice $\epsilon=c=1/j$ fails at arbitrarily small scales, so there is a counterexample at some scale $\delta_j<1/j$. Along $j\to\infty$ these counterexamples satisfy every hypothesis with losses $\delta^{-o(1)}$, the plate bound included when $q=k-1$. Each fiber needs at most $\delta^{-q-o(1)}$ tubes, and $(\mu\otimes\nu)(E)\ge\delta^{o(1)}$. Here and below, $o(1)$ refers to $j\to\infty$ and we drop the index $j$. It therefore suffices to show that no such sequence exists. In particular, any auxiliary result whose hypotheses require losses below a fixed threshold $\delta^{-\epsilon'}$ applies once $j$ is large.

\emph{(b) A single chart.} Cover $S^k$ by finitely many caps $U_1,\dots,U_m$ of a small fixed radius. Since $E\subset\bigcup_i E\cap(\R^n\times U_i)$, some $i$ satisfies $(\mu\otimes\nu)(E\cap(\R^n\times U_i))\ge\delta^{o(1)}/m=\delta^{o(1)}$. Replace $\nu$ by $\nu|_{U_i}$ and $E$ by $E\cap(\R^n\times U_i)$. All hypotheses survive, because fibers only shrink. Then rotate, which preserves balls, plates and tubes, so that $U_i$ is centered at $e_0$. Directions are now parametrized by
\[
 w(p)=\frac{(1,p)}{\sqrt{1+|p|^2}},\qquad p\in\Lambda,
\]
where $\Lambda\subset\R^k$ is a small ball about $0$. On $\Lambda$ the map $w$ is bi-Lipschitz with constants close to $1$. Every direction now lies in one small projective chart, as Lemma~\ref{ang:slice-selection} requires.

\textbf{Step 1: The case $q>k-1$.} Apply Lemma~\ref{ang:slice-selection} with $h=k-1\le n-2$. This is allowed because $t>q>h$. The pairs $(V,z)$ range over a probability space times a ball of fixed $h$-volume. Since
$\mathbb E_V\!\int(\widetilde\mu_{V,z}\otimes\widetilde\nu_V)(\widetilde E_{V,z})\,dz\ge\delta^{o(1)}$, some slice $(V,z)$ satisfies $(\widetilde\mu_{V,z}\otimes\widetilde\nu_V)(\widetilde E_{V,z})\ge\delta^{o(1)}$. By item~1 the two restricted measures have mass at most $\delta^{-o(1)}$. Dividing each by $\max(1,\text{its mass})$ makes them subprobabilities. This keeps their ball bounds and costs only a factor $\delta^{o(1)}$ in incidence.

Now apply Lemma~\ref{ang:planar-measures} in the plane $V\cong\R^2$. The labels are the original points $x$ and the original directions $w$ in the band $\{|P_{V^\perp}w|\le\delta\}$. The coordinate maps are $p_{V,z}$ and $v_V$, whose images are bounded, and the exponents are
\[
 b=q-h\in(0,\tfrac12],\qquad f=t-h\in(\tfrac12,1),\qquad b<f\quad(\text{since }q\le k-\tfrac12<t).
\]
Item~3 of Lemma~\ref{ang:slice-selection} supplies the $f$- and $b$-ball bounds of the coordinate pushforwards. It also gives, for each direction label $w$, a cover of $p_{V,z}$ of its fiber by $\delta^{-b-o(1)}$ strips of width $C'\delta$ parallel to $v_V(w)$. The incidence is $\ge\delta^{o(1)}$. Doing this for every $j$ produces exactly the sequence that Lemma~\ref{ang:planar-measures} excludes. This contradiction settles the case $q>k-1$.

\textbf{Step 2: Endpoint set-up ($q=k-1$).} Put $h=k-2$. Lemma~\ref{ang:slice-selection} applies because $0\le h\le n-2$ and $t>q=h+1>h$. In a slice the direction exponent is $q-h=1$, and
\[
 g:=t-h-\tfrac32\in(0,\tfrac12).
\]
Fix $0<a<g/3$. Then fix $\ell$ with $h<\ell<(k-1)^2/k=h+\frac1k$. Next fix $b_0\in(0,a/4)$ so small that
\[
 \kappa_0:=(a-2b_0)(\ell-h)-3hb_0>0,
\]
and put $e=\kappa_0/2$. Lemma~\ref{ang:weak-radial}, with these $k,\zeta,\ell,e$, then supplies $\epsilon_e,c_e>0$. Finally fix $\theta\in(0,1]$ with $\theta h<c_e/2$.

\emph{The chart law.} Let $\lambda=(w^{-1})_\#\nu$ be the law of chart labels, so that $\nu=w_\#\lambda$ and $\|\lambda\|\le1$. Since $w$ is bi-Lipschitz, the $q$-ball bound for $\nu$ gives
\begin{equation}\label{eq:lam-ball}
 \lambda(B(p,r))\le\delta^{-o(1)}r^{k-1}\qquad(\delta\le r\le1).
\end{equation}
Let $H=\{p:\langle\alpha,p\rangle=\beta\}$ be an affine hyperplane in $\R^k$ with $|\alpha|=1$, and let $H'$ be the linear hyperplane with normal $(-\beta,\alpha)$. For $p\in\Lambda$,
\[
 \dist(w(p),H')=\frac{|\langle\alpha,p\rangle-\beta|}{|(\beta,\alpha)|\sqrt{1+|p|^2}}.
\]
The set $H^{(r)}$ meets $\Lambda$ only if $|\beta|\le2$, and in that case $\dist(w(p),H')\ge c\,\dist(p,H)$. So \eqref{ang:endpoint-plate} gives $\lambda(H^{(r)})\le\delta^{-o(1)}r^\zeta$. The incidence is at most $\|\nu\|=\|\lambda\|$, so $\|\lambda\|\ge\delta^{o(1)}$. Hence $\hat\lambda=\lambda/\|\lambda\|$ is a probability satisfying the hypotheses of Lemma~\ref{ang:weak-radial} with loss $\delta^{-o(1)}\le\delta^{-\epsilon_e}$ for large $j$.

That lemma gives a pair set $G$, off the diagonal, with $(\lambda\otimes\lambda)(G^c)\le(\hat\lambda\otimes\hat\lambda)(G^c)\le C\delta^{c_e}$. Since $\lambda\le\hat\lambda$, it also gives for every anchor $p$ the bound
\begin{equation}\label{eq:radial}
 \lambda\{p'':(p,p'')\in G,\ \pi_p(p'')\in B(\pm\vartheta,r)\}\le C\delta^{-e}r^\ell
 \qquad(\delta\le r\le1),
\end{equation}
where $\pi_p(p'')=(p''-p)/|p''-p|$ and the two antipodal caps are counted. Define the \emph{exceptional pairs}
\[
 \mathcal E_{\rm pair}=G^c\cup\{(p,p'):|p-p'|<\delta^{b_0}\}.
\]
A pair outside $\mathcal E_{\rm pair}$ is called \emph{retained}.

\emph{Slicing kernels.} Set $\lambda_V=\delta^{-h}\one_{\{\dist(w(p),V)\le\delta\}}\lambda$, so that $\nu_V=w_\#\lambda_V$. Note that $|P_{V^\perp}w|=\dist(w,V)$. By Tonelli,
\[
 \mathbb E_V\lambda_V^{\otimes j}(S)=\int_S K_j\,d\lambda^{\otimes j},\qquad
 K_j(p_1,\dots,p_j)=\delta^{-jh}\Pr_V\{\dist(w(p_i),V)\le\delta\ \forall i\}.
\]

\emph{Claim A (wedges in the chart).} Let $p,p',p''\in\Lambda$, and put $u=p'-p$ and $v=p''-p$. Then
\[
 |w(p)\wedge w(p')|\ge c|u|,\qquad |w(p)\wedge w(p')\wedge w(p'')|\ge c|u\wedge v|=c|u||v|\alpha,
\]
where $\alpha=|\frac{u}{|u|}\wedge\frac{v}{|v|}|$.
To see this, write $(1,p')=(1,p)+(0,u)$ and similarly for $(1,p'')$. Subtracting the first column does not change the wedge. Splitting $\R^n=\R e_0\oplus\R^k$ orthogonally,
\[
 |(1,p)\wedge(0,u)\wedge(0,v)|^2=|u\wedge v|^2+|p\wedge u\wedge v|^2\ge|u\wedge v|^2,
\]
and the same computation gives $|(1,p)\wedge(0,u)|\ge|u|$. Normalizing the columns costs factors in $[c,1]$.

\emph{Claim B (kernel bounds).} For $p,p',p''\in\Lambda$:
\begin{align*}
 K_2(p,p')&\le C(|p-p'|+\delta)^{-h},\\
 K_3(p,p',p'')&\le C\delta^{-3hb_0}(\alpha+\delta)^{-h}\qquad\text{if }|p'-p|,|p''-p|\ge\delta^{b_0}.
\end{align*}
For the proof, use Lemma~\ref{ang:haar} with $n=k+1$ and $j\le3=n-h$. Let $d_1\ge\dots\ge d_j$ be the singular values of the matrix $M=(w_1,\dots,w_j)$. Then $d_1\le\sqrt j$, and $(d_1+\delta)^{-h}\le1$ because $d_1\ge|w_1|=1$. Also $d_1d_2=\|\Lambda^2M\|\ge|w_1\wedge w_2|$. Hence $d_2\ge c|w_1\wedge w_2|\ge c|p'-p|$ by Claim~A, which gives the bound for $K_2$. For $j=3$ this also yields $d_2\ge c\delta^{b_0}$. Moreover $d_3=|w_1\wedge w_2\wedge w_3|/(d_1d_2)\ge c\,\delta^{2b_0}\alpha$, using Claim~A and $d_1d_2\le3$. Therefore
\[
 (d_2+\delta)^{-h}(d_3+\delta)^{-h}\le C\delta^{-hb_0}\bigl(\delta^{2b_0}(\alpha+\delta)\bigr)^{-h}.
\]

\emph{Claim C (pair transfer).} Let $\delta\le\rho\le1$. Then
\[
 \int_{|p-p'|\le\rho}K_2\,d\lambda^{\otimes2}\le\delta^{-o(1)}\rho,
\]
while $K_2\le C\rho^{-h}$ wherever $|p-p'|>\rho$.
The second assertion is immediate from Claim~B. For the first, fix $p$ and split $p'$ into the ball $|p'-p|\le\delta$ and the dyadic annuli $r<|p'-p|\le2r$ with $\delta\le r<\rho$. By Claim~B and \eqref{eq:lam-ball}, these contribute $\delta^{-h}\cdot\delta^{-o(1)}\delta^{k-1}$ and $r^{-h}\cdot\delta^{-o(1)}(2r)^{k-1}$ respectively. Since $k-1-h=1$, the sum is $\le\delta^{-o(1)}\rho$. This is the one place where the exponent $q-h=1$ is used to sum.

\emph{Claim D (point slices).} For every $V$ we have $\int\|\widetilde\mu_{V,z}\|\,dz\le\int\|\mu_{V,z}\|\,dz\le C$.
By Tonelli, $\int\|\mu_{V,z}\|dz=\delta^{-h}\int|\{z\in V^\perp:|P_{V^\perp}x-z|\le\delta\}|\,d\mu(x)\le|B^h(0,1)|$.

\textbf{Step 3: Exceptional pairs are rare after slicing.} Apply Claim~C with $\rho=\delta^\theta$ to $G^c$. This gives
\[
 \mathbb E_V(\lambda_V\otimes\lambda_V)(G^c)\le C\delta^{-\theta h}(\lambda\otimes\lambda)(G^c)+\delta^{\theta-o(1)}\le C\delta^{c_e/2}+\delta^{\theta-o(1)}.
\]
Apply Claim~C with $\rho=\delta^{b_0}$ to the close pairs. This gives the bound $\delta^{b_0-o(1)}$. Hence there is $\kappa_1>0$ such that
\begin{equation}\label{eq:pairs}
 \mathbb E_V(\lambda_V\otimes\lambda_V)(\mathcal E_{\rm pair})\le\delta^{\kappa_1}\qquad\text{for large }j.
\end{equation}

\textbf{Step 4: Nearly coplanar triples are rare after slicing.} Let $\mathcal T$ be the set of triples $(p,p',p'')$ such that $(p,p')$ and $(p,p'')$ are both retained and $|w(p)\wedge w(p')\wedge w(p'')|<2\delta^a$. Retained pairs satisfy $|u|,|v|\ge\delta^{b_0}$, so Claim~A forces $\alpha\le r_0:=C\delta^{a-2b_0}$ on $\mathcal T$. Here $r_0\le1$ because $a>2b_0$.

Fix $p$ and $p'$. The condition $\alpha\le r$ says that $\pi_p(p'')$ lies within $Cr$ of $\pm\pi_p(p')$, so \eqref{eq:radial} gives
$\lambda\{p'':(p,p'')\text{ retained},\ \alpha\le r\}\le C\delta^{-e}r^\ell$.
Summing $(\alpha+\delta)^{-h}$ over $\{\alpha\le\delta\}$ and over the dyadic shells $\{r<\alpha\le2r\}$ with $r<r_0$ gives a geometric series, because $\ell>h$:
\[
 \int_{\{(p,p'')\text{ retained},\ \alpha\le r_0\}}(\alpha+\delta)^{-h}\,d\lambda(p'')\le C\delta^{-e}r_0^{\ell-h}.
\]
Combining this with Claim~B and $\|\lambda\|\le1$,
\begin{equation}\label{eq:triples}
 \mathbb E_V\lambda_V^{\otimes3}(\mathcal T)\le C\delta^{-3hb_0-e+(a-2b_0)(\ell-h)}=C\delta^{\kappa_0/2}.
\end{equation}

\textbf{Step 5: A good triple with a heavy common point set.} Apply Lemma~\ref{ang:slice-selection} to $\mu$, $\nu=w_\#\lambda$ and $E$. Put $\widetilde\lambda_V=(w^{-1})_\#\widetilde\nu_V$. Then $\widetilde\lambda_V\le\lambda_V$ and $\sup_V\|\widetilde\lambda_V\|\le\delta^{-o(1)}$. Define
\[
 F(V,z,x)=\widetilde\lambda_V\{p:(x,w(p))\in\widetilde E_{V,z}\}.
\]
Let $dm=dV\,dz\,d\widetilde\mu_{V,z}(x)$. By Claim~D, $\|m\|\le C$. By the conclusion of Lemma~\ref{ang:slice-selection}, $\int F\,dm\ge\delta^{o(1)}$. Hölder's inequality gives $(\int F\,dm)^3\le\|m\|^2\int F^3\,dm$, so
\[
 \int F^3\,dm=\mathbb E_V\!\int\!\!\int\widetilde\lambda_V^{\otimes3}\{(p_1,p_2,p_3):(x,w(p_i))\in\widetilde E_{V,z}\ \forall i\}\,d\widetilde\mu_{V,z}(x)\,dz\ge\delta^{o(1)}.
\]

Call a triple \emph{good} if $(p_1,p_2)$ and $(p_1,p_3)$ are retained and $|w(p_1)\wedge w(p_2)\wedge w(p_3)|\ge2\delta^a$. A triple that is not good lies in $\mathcal T$, or has $(p_1,p_2)\in\mathcal E_{\rm pair}$, or has $(p_1,p_3)\in\mathcal E_{\rm pair}$. Drop the incidence condition and use Claim~D, then $\widetilde\lambda_V\le\lambda_V$, then \eqref{eq:triples} and \eqref{eq:pairs}. The contribution of non-good triples to $\int F^3dm$ is at most
\[
 C\,\mathbb E_V\Bigl[\lambda_V^{\otimes3}(\mathcal T)+2\|\widetilde\lambda_V\|(\lambda_V\otimes\lambda_V)(\mathcal E_{\rm pair})\Bigr]
 \le C\delta^{\kappa_0/2}+\delta^{\kappa_1-o(1)}.
\]
Here the uniform bound on $\|\widetilde\lambda_V\|$ is what allows the factor to be taken outside the expectation. No independence between point and direction slices is needed. Hence good triples carry $\int F^3dm$ mass $\ge\delta^{o(1)}$.

This mass is the integral of $\Phi=\widetilde\mu_{V,z}\{x:(x,w(p_i))\in\widetilde E_{V,z}\ \forall i\}$ against $dV\,dz\,d\widetilde\lambda_V^{\otimes3}$ restricted to good triples, all lying in the direction band of $V$. That measure has total mass at most $C\sup_V\|\widetilde\lambda_V\|^3\le\delta^{-o(1)}$. Therefore some slice $(V,z)$ and some good triple $p_1,p_2,p_3$ in the band satisfy $\widetilde\mu_{V,z}(S)\ge\delta^{o(1)}$, where
\[
 S=\{x:(x,w(p_i))\in\widetilde E_{V,z},\ i=1,2,3\}.
\]

\textbf{Step 6: Counting gives the contradiction.} Let $w_i=w(p_i)$ and $v_i=v_V(w_i)\in V$. Since $|P_{V^\perp}w_i|\le\delta$, we have $|v_i-w_i|\le2\delta$. The wedge is multilinear, so
\[
 |\det\nolimits_V(v_1,v_2,v_3)|=|v_1\wedge v_2\wedge v_3|\ge2\delta^a-C\delta\ge\delta^a,
\]
using $a<1$.

Let $A=p_{V,z}(S)\subset V\cong\R^3$. By item~3, the pushforward of $\widetilde\mu_{V,z}$ under $p_{V,z}$ has $(t-h)$-ball bounds with loss $\delta^{-o(1)}$. So
\[
 \delta^{o(1)}\le\widetilde\mu_{V,z}(S)\le|A|_{C_3\delta}\cdot\delta^{-o(1)}(C_3\delta)^{t-h},
 \qquad\text{that is,}\qquad |A|_{C_3\delta}\ge\delta^{-(t-h)+o(1)}.
\]
Also by item~3, for each $i$ the set $A$ is covered by $\delta^{-(q-h)-o(1)}=\delta^{-1-o(1)}$ tubes of width $C'\delta$ parallel to $v_i$. Lemma~\ref{ang:loomis-whitney} with $m=3$ and $\Delta=\delta^a$ gives
\[
 |A|_{C_3\delta}\le C\delta^{-3a}\bigl(\delta^{-1-o(1)}\bigr)^{3/2}=\delta^{-3/2-3a-o(1)}.
\]
Comparing the two bounds yields $t-h\le\tfrac32+3a+o(1)$, that is $g\le3a+o(1)$. This contradicts $3a<g$.

When $k=2$ we have $h=0$. Then $V=\R^3$, all slicing weights and kernels $K_j$ equal $1$, the $z$-integral runs over the single point $V^\perp=\{0\}$, and the argument goes through unchanged. This completes the endpoint case and the proof.
\end{proof}
