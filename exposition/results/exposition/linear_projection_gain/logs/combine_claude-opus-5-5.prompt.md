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

## Version 1 (the original proof from the paper)

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


## Version 2 (derived from a formalization)

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


## Version 3 (derived from a formalization)

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
