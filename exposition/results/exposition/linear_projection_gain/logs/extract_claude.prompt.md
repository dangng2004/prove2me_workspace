You are given a Lean 4 formalization of a mathematical result and the result's statement in the paper it comes from. Write the proof that the Lean code carries out as an informal proof in LaTeX, the way it would appear in a mathematics paper.

Rules:

- Follow the Lean proof's own route: the same constructions, the same order of steps, the same case splits and the same intermediate claims. Do not substitute a different or better argument, and do not import ideas from the paper's proof that the Lean proof does not use.
- Results that the Lean file imports without proof (theorems it uses as black boxes) should be stated briefly and cited as lemmas, as a paper cites earlier results. Helper lemmas proved inside the file should be proved if they carry mathematical content, and summarized in a sentence if they are routine bookkeeping.
- Leave out Lean-specific matters (coercions, casts, `ENNReal` versus real arithmetic, measurability side conditions that are automatic in ordinary mathematics) unless they correspond to a genuine mathematical point.
- Write ordinary mathematical prose. Do not mention Lean, tactics, or names of Lean declarations.

Output only the LaTeX body of the proof, starting with `\begin{proof}` and ending with `\end{proof}`, preceded if needed by short `\begin{lemma}...\end{lemma}` statements of the cited black-box results. Use only standard LaTeX and amsmath macros.


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


# Lean formalization

```lean
-- ===== Statement.lean (Claude) =====
import Mathlib

open MeasureTheory

namespace OAI.Falconer

/-!
# Theorem 4.1 (Linear projection gain)

OpenAI, "The Falconer distance conjecture in all dimensions", Theorem 4.1
(`ang:linear-gain`), with the conventions of Section 1 (`sec:conventions`).

Readings chosen for this statement.

* Ambient space and directions. Points live in `EuclideanSpace ℝ (Fin (k+1))` and
  directions on its unit sphere `S^k = Metric.sphere 0 1`, with the subtype (chordal
  Euclidean) metric. Section 1: "A cap bound on a sphere has the analogous meaning for
  its Euclidean chordal metric." Directions are oriented (Section 1).
* Parameters. `k ≥ 2`, `k - 1 ≤ q ≤ k - 1/2 < t < k`, a width constant `C ≥ 0`,
  a support radius `R > 0` (the meaning of "bounded"), and `ζ > 0` are fixed first.
  `ζ` is only used when `q = k - 1`. Requiring `ζ > 0` in the other case costs
  nothing because it does not enter the hypotheses there.
* Quantifiers. After the fixed parameters: there exist `ε, c > 0` and `δ₀ > 0` such
  that for every `δ ∈ (0, δ₀)` and all measures and relations the bound holds. All
  constants are uniform over the measures and relations.
* "Subprobability": a (Borel) measure of total mass at most one.
* "Bounded point subprobability": `μ` gives zero mass to the complement of
  `closedBall 0 R`, where `R` is fixed in advance.
* "`s`-ball bound of loss `K` down to `δ`" (Section 1): `μ (ball z r) ≤ K r^s` for every
  center `z` and every `δ ≤ r ≤ 1`, here with `K = δ^{-ε}`. Open balls are used,
  which gives the weaker hypothesis. For `ν` the centers range over the sphere and
  the balls are chordal caps.
* Endpoint plate condition. For a linear hyperplane `H` with unit normal `n`,
  `dist(w, H) = |⟪n, w⟫|`. So the condition reads
  `ν {w | |⟪n, w⟫| ≤ r} ≤ δ^{-ε} r^ζ` for every unit vector `n` and `δ ≤ r ≤ 1`,
  assumed only when `q = k - 1`.
* Incidence relation. `E` is a measurable subset of `ℝ^{k+1} × S^k` for the product
  σ-algebra, and `E_w = {x | (x, w) ∈ E}`.
* Tubes. "A tube parallel to `w` of width `Cδ`" is read as the full cylinder
  `{x | ‖P_{w⊥}(x - a)‖ ≤ Cδ}`, where `P_{w⊥}` is the orthogonal projection onto the
  orthogonal complement of the line `ℝ w` and `a` is any anchor point. The cylinder
  contains every bounded-length tube with the same axis, and radius `Cδ` contains
  diameter `Cδ`. Both choices make the cover hypothesis weaker, so the statement is
  at least as strong as the paper's.
* "Covered by at most `δ^{-q-ε}` tubes": for each direction `w` there is a finite set
  of anchors `T` with `#T ≤ δ^{-q-ε}` and `E_w` is contained in the union of the
  tubes through the anchors. The covers may depend on `w` in any way. No
  measurability in `w` is assumed.
* Conclusion: `(μ ⊗ ν)(E) ≤ δ^c`.
-/
theorem linear_projection_gain (k : ℕ) (hk : 2 ≤ k) (q t : ℝ)
    (hq : (k:ℝ) - 1 ≤ q) (hq' : q ≤ (k:ℝ) - 1/2) (hqt : (k:ℝ) - 1/2 < t) (ht : t < k)
    (C : ℝ) (hC : 0 ≤ C) (R : ℝ) (hR : 0 < R) (ζ : ℝ) (hζ : 0 < ζ) :
    ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
    ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ (μ : Measure (EuclideanSpace ℝ (Fin (k+1))))
      (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1))
      (E : Set (EuclideanSpace ℝ (Fin (k+1)) ×
        Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1)),
    μ Set.univ ≤ 1 → ν Set.univ ≤ 1 →
    μ (Metric.closedBall 0 R)ᶜ = 0 →
    (∀ (z : EuclideanSpace ℝ (Fin (k+1))) (r : ℝ), δ ≤ r → r ≤ 1 →
      μ (Metric.ball z r) ≤ ENNReal.ofReal (δ^(-ε) * r^t)) →
    (∀ (w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1) (r : ℝ), δ ≤ r → r ≤ 1 →
      ν (Metric.ball w r) ≤ ENNReal.ofReal (δ^(-ε) * r^q)) →
    (q = (k:ℝ) - 1 → ∀ n : EuclideanSpace ℝ (Fin (k+1)), ‖n‖ = 1 →
      ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | |inner ℝ n (w : EuclideanSpace ℝ (Fin (k+1)))| ≤ r} ≤
          ENNReal.ofReal (δ^(-ε) * r^ζ)) →
    MeasurableSet E →
    (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1,
      ∃ T : Finset (EuclideanSpace ℝ (Fin (k+1))), (T.card : ℝ) ≤ δ^(-q-ε) ∧
        {x | (x, w) ∈ E} ⊆ ⋃ a ∈ T,
          {x | ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin (k+1))))ᗮ.orthogonalProjectionOnto (x - a)‖ ≤
            C * δ}) →
    (μ.prod ν) E ≤ ENNReal.ofReal (δ^c) := by
  sorry

end OAI.Falconer

-- ===== Proof.lean (Claude), lines 6080-6600: bridge and solution =====
-- Recovered fragment. Lines 1-6079 of the original Proof.lean were not recovered; per the
-- clarity review they are helper lemmas copied from the port (black-box inputs).
    (Measure.restrict_le_self _).trans (hslab w r hr hr1)
  have hg := hgain N (by omega) ι μ ν' w₀ E J v hνsupport hμ hμmass hν'mass
    hμball hν'ball hslab' hE hJ hJN hEb hanchors hcover
  exact (not_lt_of_ge hg) hw₀

end Falconer

end OAI
end

section
-- module Solutions.OAIQ088_FD.Falconer_Radial_EndpointTubeGain
attribute [-instance] _root_.OAI.Falconer.cellDistance_finite _root_.OAI.Falconer.cellLabelMeasurableSpace _root_.OAI.Falconer.instIsMarkovKernelSpaceRadialKernel _root_.OAI.Falconer.originalRadialSphereLaw_finite _root_.OAI.Falconer.radialFrequencyMeasure_finite _root_.OAI.Falconer.radialIntervalMeasure_finite _root_.OAI.Falconer.scalarProjectionLaw_finite _root_.OAI.Falconer.surfaceMeasure_finite _root_.OAI.Falconer.testedCellDistance_finite _root_.OAI.Falconer.testedCellPair_finite
set_option linter.all false
set_option linter.unusedVariables false
set_option linter.unusedTactic false
set_option linter.unreachableTactic false

namespace OAI

/-! # Endpoint decay for arbitrary original finite fiber covers -/

namespace Falconer
open Set MeasureTheory
open scoped ENNReal

theorem endpoint_dyadic_tube_gain (hLW : PublishedFiniteLoomisWhitney)
    {h : ℕ} {t ζ C : ℝ} (ht : (h:ℝ)+3/2 < t) (ht' : t < (h:ℝ)+2)
    (hζ : 0 < ζ) (hC : 0 ≤ C) :
    ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧ ∃ N₀ : ℕ,
      ∀ N ≥ N₀, ∀ (μ : Measure (Space (h+3))) (ν : Measure (Sphere (h+3)))
        [IsFiniteMeasure μ] [IsFiniteMeasure ν],
      ∀ E : Set (Space (h+3) × Sphere (h+3)),
      (∀ᵐ x ∂μ, ‖x‖ ≤ 1/4) → μ univ ≤ 1 → ν univ ≤ 1 →
      (∀ x : Space (h+3), ∀ j : ℕ, j ≤ N → μ (Metric.ball x (1/(2:ℝ)^j)) ≤
        ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*(1/(2:ℝ)^j)^t)) →
      (∀ w : Sphere (h+3), ∀ j : ℕ, j ≤ N → ν (Metric.ball w (1/(2:ℝ)^j)) ≤
        ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*(1/(2:ℝ)^j)^(h+1:ℝ))) →
      (∀ w : Sphere (h+3), ∀ r : ℝ, 1/(2:ℝ)^N ≤ r → r ≤ 1 →
        ν {u : Sphere (h+3) | |inner ℝ (w:Space (h+3)) (u:Space (h+3))| ≤ r} ≤
          ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*r^ζ)) →
      MeasurableSet E → (∀ u ∈ E, ‖u.1‖ ≤ 1/4) →
      (∀ w : Sphere (h+3), ∃ S : Finset (Space (h+3)),
        (S.card : ℝ) ≤ (1/(2:ℝ)^N)^(-(h+1:ℝ)-ε) ∧
        ∀ x, (x,w) ∈ E → ∃ a ∈ S,
          ‖perpendicularPart (w:Space (h+3)) (x-a)‖ ≤ C*(1/(2:ℝ)^N)) →
      (μ.prod ν) E ≤ ENNReal.ofReal ((1/(2:ℝ)^N)^c) := by
  classical
  obtain ⟨ε,c,hε,hc,N₀,hgain⟩ := endpoint_dyadic_angular_gain hLW ht ht' hζ
    (by linarith : 0 ≤ 2*C+1)
  refine ⟨ε,c,hε,hc,N₀,?_⟩
  intro N hN μ ν _ _ E hμ hμmass hνmass hμball hνball hslab hE hEb hcover
  let δ : ℝ := 1/(2:ℝ)^N
  have hδ : 0 < δ := by dsimp [δ]; positivity
  obtain ⟨G,hG,J,F,hF,hFE,hJ,hcard,hzero,hcoverF⟩ :=
    prepare_original_tube_relation μ E hE hδ (Nat.floor (δ^(-(h+1:ℝ)-ε))) hEb (by
      intro w
      obtain ⟨S,hS,hcoverS⟩ := hcover w
      exact ⟨S,Nat.le_floor hS,hcoverS⟩)
  have hmass : (μ.prod ν) F = (μ.prod ν) E := by
    have hh := product_inter_eq_of_null_original_fibers μ μ ν Measure.AbsolutelyContinuous.rfl
      E F hE hF hzero
    simpa only [inter_eq_right.mpr hFE] using hh
  rw [← hmass]
  refine hgain N hN {a // a ∈ G} μ ν F J (fun a => a.val)
    hμ hμmass hνmass hμball hνball hslab hF hJ ?_
    (fun u hu => hEb u (hFE hu)) (fun _ i _ => hG i.val i.property) ?_
  · intro w
    have hh : ((J w).card : ℝ) ≤ (Nat.floor (δ^(-(h+1:ℝ)-ε)) : ℝ) := by exact_mod_cast hcard w
    exact hh.trans (Nat.floor_le (Real.rpow_nonneg hδ.le _))
  · intro u hu
    obtain ⟨a,ha,hp⟩ := hcoverF u hu
    refine ⟨a,ha,?_⟩
    nlinarith

end Falconer

end OAI
end

section
-- Bridge to Theorem 4.1
set_option linter.all false

namespace OAI

namespace Falconer.LinearGain
open Set MeasureTheory Filter
open scoped ENNReal Topology

/-- The paper's tube: the orthogonal projection onto the complement of the line `ℝ w`
has the same norm as the port's `perpendicularPart`. -/
theorem norm_orthogonalProjection_eq_perpendicularPart {d : ℕ} (w : Sphere d) (v : Space d) :
    ‖(ℝ ∙ (w : Space d))ᗮ.orthogonalProjectionOnto v‖ = ‖perpendicularPart (w : Space d) v‖ := by
  have hw : ‖(w : Space d)‖ = 1 := by simp
  rw [Submodule.orthogonalProjectionOnto_orthogonal, Submodule.coe_norm]
  change ‖v - (ℝ ∙ (w : Space d)).starProjection v‖ = _
  rw [Submodule.starProjection_singleton, hw]
  simp [perpendicularPart]

theorem perpendicularPart_smul {d : ℕ} (w v : Space d) (s : ℝ) :
    perpendicularPart w (s • v) = s • perpendicularPart w v := by
  simp only [perpendicularPart, inner_smul_right, smul_sub, smul_smul]

theorem scale_preimage_ball {d : ℕ} {s : ℝ} (hs : 0 < s) (y : Space d) (r : ℝ) :
    (fun x : Space d => s • x) ⁻¹' Metric.ball y r = Metric.ball (s⁻¹ • y) (r / s) := by
  ext x
  simp only [mem_preimage, Metric.mem_ball, dist_eq_norm]
  have he : s • x - y = s • (x - s⁻¹ • y) := by
    rw [smul_sub, smul_smul, mul_inv_cancel₀ hs.ne', one_smul]
  rw [he, norm_smul, Real.norm_of_nonneg hs.le, lt_div_iff₀ hs, mul_comm]

/-- Inverse dyadic powers. -/
theorem one_div_rpow_neg {x e : ℝ} (hx : 0 < x) : (1 / x) ^ (-e) = x ^ e := by
  rw [one_div, Real.inv_rpow hx.le, Real.rpow_neg hx.le, inv_inv]

/-- Loss comparison between a scale `δ` and a dyadic scale `D < 2δ`. -/
theorem rpow_neg_le_of_half_le {δ D e : ℝ} (hD : 0 < D) (hδ : D / 2 ≤ δ) (he : 0 ≤ e) :
    δ ^ (-e) ≤ 2 ^ e * D ^ (-e) := by
  have h1 : δ ^ (-e) ≤ (D / 2) ^ (-e) :=
    Real.rpow_le_rpow_of_nonpos (by positivity) hδ (by linarith)
  have h2 : (D / 2) ^ (-e) = 2 ^ e * D ^ (-e) := by
    rw [Real.div_rpow hD.le (by norm_num), Real.rpow_neg (by norm_num : (0:ℝ) ≤ 2) e]
    field_simp
  linarith

/-- The finite-scale dyadic form supplied by the port, abstracted over the
dimension, the exponents, the width constant and the presence of the plate
condition. -/
def DyadicTubeGain (d : ℕ) (t q ζ C : ℝ) (plate : Prop) : Prop :=
  ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧ ∃ N₀ : ℕ, ∀ N ≥ N₀,
    ∀ (μ : Measure (Space d)) (ν : Measure (Sphere d))
      [IsFiniteMeasure μ] [IsFiniteMeasure ν] (E : Set (Space d × Sphere d)),
    (∀ᵐ x ∂μ, ‖x‖ ≤ 1/4) → μ univ ≤ 1 → ν univ ≤ 1 →
    (∀ x : Space d, ∀ j : ℕ, j ≤ N →
      μ (Metric.ball x (1/(2:ℝ)^j)) ≤ ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*(1/(2:ℝ)^j)^t)) →
    (∀ w : Sphere d, ∀ j : ℕ, j ≤ N →
      ν (Metric.ball w (1/(2:ℝ)^j)) ≤ ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*(1/(2:ℝ)^j)^q)) →
    (plate → ∀ w : Sphere d, ∀ r : ℝ, 1/(2:ℝ)^N ≤ r → r ≤ 1 →
      ν {u : Sphere d | |inner ℝ (w:Space d) (u:Space d)| ≤ r} ≤
        ENNReal.ofReal ((1/(2:ℝ)^N)^(-ε)*r^ζ)) →
    MeasurableSet E → (∀ u ∈ E, ‖u.1‖ ≤ 1/4) →
    (∀ w : Sphere d, ∃ S : Finset (Space d),
      (S.card : ℝ) ≤ (1/(2:ℝ)^N)^(-q-ε) ∧
      ∀ x, (x,w) ∈ E → ∃ a ∈ S,
        ‖perpendicularPart (w:Space d) (x-a)‖ ≤ C*(1/(2:ℝ)^N)) →
    (μ.prod ν) E ≤ ENNReal.ofReal ((1/(2:ℝ)^N)^c)

/-- The global statement at all small scales, in the form of Theorem 4.1. -/
def ScaleGain (d : ℕ) (t q ζ C R : ℝ) (plate : Prop) : Prop :=
  ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
    ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ (μ : Measure (EuclideanSpace ℝ (Fin d)))
      (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin d)) 1))
      (E : Set (EuclideanSpace ℝ (Fin d) × Metric.sphere (0 : EuclideanSpace ℝ (Fin d)) 1)),
    μ Set.univ ≤ 1 → ν Set.univ ≤ 1 →
    μ (Metric.closedBall 0 R)ᶜ = 0 →
    (∀ (z : EuclideanSpace ℝ (Fin d)) (r : ℝ), δ ≤ r → r ≤ 1 →
      μ (Metric.ball z r) ≤ ENNReal.ofReal (δ^(-ε) * r^t)) →
    (∀ (w : Metric.sphere (0 : EuclideanSpace ℝ (Fin d)) 1) (r : ℝ), δ ≤ r → r ≤ 1 →
      ν (Metric.ball w r) ≤ ENNReal.ofReal (δ^(-ε) * r^q)) →
    (plate → ∀ n : EuclideanSpace ℝ (Fin d), ‖n‖ = 1 →
      ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | |inner ℝ n (w : EuclideanSpace ℝ (Fin d))| ≤ r} ≤
          ENNReal.ofReal (δ^(-ε) * r^ζ)) →
    MeasurableSet E →
    (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin d)) 1,
      ∃ T : Finset (EuclideanSpace ℝ (Fin d)), (T.card : ℝ) ≤ δ^(-q-ε) ∧
        {x | (x, w) ∈ E} ⊆ ⋃ a ∈ T,
          {x | ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin d)))ᗮ.orthogonalProjectionOnto (x - a)‖ ≤
            C * δ}) →
    (μ.prod ν) E ≤ ENNReal.ofReal (δ^c)

set_option maxHeartbeats 1000000 in
theorem scaleGain_of_dyadic {d : ℕ} {t q ζ C R : ℝ} {plate : Prop}
    (ht : 0 ≤ t) (hq : 0 ≤ q) (hC : 0 ≤ C) (hR : 0 < R)
    (hgain : DyadicTubeGain d t q ζ C plate) : ScaleGain d t q ζ C R plate := by
  classical
  obtain ⟨ε₀, c₀, hε₀, hc₀, N₀, hg⟩ := hgain
  set ε : ℝ := ε₀ / 2 with hεdef
  set c : ℝ := c₀ / 2 with hcdef
  have hε : 0 < ε := by positivity
  have hc : 0 < c := by positivity
  set s : ℝ := 1 / (4 * (R + 1)) with hsdef
  have hs : 0 < s := by positivity
  have hs1 : s ≤ 1 := by
    rw [hsdef, div_le_one (by positivity)]; linarith
  have hsR : s * R ≤ 1/4 := by
    rw [hsdef, div_mul_eq_mul_div, one_mul, div_le_iff₀ (by positivity)]; linarith
  set K : ℝ := 2 ^ ε * s ^ (-t) + 2 ^ (q + ε) with hKdef
  have hst : 1 ≤ s ^ (-t) := Real.one_le_rpow_of_pos_of_le_one_of_nonpos hs hs1 (by linarith)
  have h2ε : 1 ≤ (2:ℝ) ^ ε := Real.one_le_rpow (by norm_num) hε.le
  have h2qε : 1 ≤ (2:ℝ) ^ (q + ε) := Real.one_le_rpow (by norm_num) (by linarith)
  have hK1 : 2 ^ ε * s ^ (-t) ≤ K := by
    have : 0 ≤ (2:ℝ) ^ (q + ε) := by positivity
    linarith
  have hK2 : (2:ℝ) ^ (q + ε) ≤ K := by
    have : 0 ≤ (2:ℝ) ^ ε * s ^ (-t) := by positivity
    linarith
  have hK3 : (2:ℝ) ^ ε ≤ K := by
    have : (2:ℝ) ^ ε ≤ 2 ^ ε * s ^ (-t) := by nlinarith
    linarith
  have hK4 : s ^ (-t) ≤ K := by
    have : s ^ (-t) ≤ 2 ^ ε * s ^ (-t) := by nlinarith
    linarith
  -- a dyadic threshold beyond which the loss `K` is absorbed
  have hlim : Tendsto (fun N : ℕ => ((2:ℝ) ^ N) ^ ε) atTop atTop :=
    (tendsto_rpow_atTop hε).comp
      (tendsto_pow_atTop_atTop_of_one_lt (by norm_num : (1:ℝ) < 2))
  obtain ⟨N₁, hN₁⟩ := eventually_atTop.mp (hlim.eventually (eventually_ge_atTop K))
  refine ⟨ε, c, hε, hc, min (1/4) (1 / (2:ℝ) ^ (N₀ + N₁ + 1)), by positivity, ?_⟩
  intro δ hδ hδ₀ μ ν E hμm hνm hsupp hμb hνb hplate hE hcov
  have hδ4 : δ ≤ 1/4 := (hδ₀.trans_le (min_le_left _ _)).le
  have hδN : δ < 1 / (2:ℝ) ^ (N₀ + N₁ + 1) := hδ₀.trans_le (min_le_right _ _)
  haveI : IsFiniteMeasure μ := ⟨hμm.trans_lt ENNReal.one_lt_top⟩
  haveI : IsFiniteMeasure ν := ⟨hνm.trans_lt ENNReal.one_lt_top⟩
  -- the dyadic scale `D = 2^{-N}` with `δ ≤ D < 2δ`
  obtain ⟨N, hN1, hN2⟩ := exists_nat_pow_near
    (show (1:ℝ) ≤ 1 / δ by rw [le_div_iff₀ hδ]; linarith) (by norm_num : (1:ℝ) < 2)
  set D : ℝ := 1 / (2:ℝ) ^ N with hDdef
  have h2N : (0:ℝ) < 2 ^ N := by positivity
  have hD : 0 < D := by positivity
  have hD1 : D ≤ 1 := by
    rw [hDdef, div_le_one h2N]; exact one_le_pow₀ (by norm_num)
  have hδD : δ ≤ D := by
    rw [hDdef, le_div_iff₀ h2N]
    rw [le_div_iff₀ hδ] at hN1
    linarith
  have hDδ : D / 2 ≤ δ := by
    rw [div_lt_iff₀ hδ] at hN2
    rw [hDdef, div_div, div_le_iff₀ (by positivity)]
    rw [pow_succ] at hN2
    linarith
  have hNbig : N₀ + N₁ ≤ N := by
    have h1 : (2:ℝ) ^ (N₀ + N₁ + 1) < 1 / δ := by
      rw [lt_div_iff₀ hδ]
      rw [lt_div_iff₀ (by positivity)] at hδN
      linarith
    have h2 : (2:ℝ) ^ (N₀ + N₁ + 1) < 2 ^ (N + 1) := h1.trans hN2
    have h3 := (pow_lt_pow_iff_right₀ (by norm_num : (1:ℝ) < 2)).mp h2
    omega
  -- the loss factor at scale `D`
  set A : ℝ := D ^ (-ε) with hAdef
  have hA : A = ((2:ℝ) ^ N) ^ ε := one_div_rpow_neg h2N
  have hKA : K ≤ A := by rw [hA]; exact hN₁ N (by omega)
  have hA0 : 0 < A := by positivity
  have hAA : D ^ (-ε₀) = A * A := by
    rw [hAdef, ← Real.rpow_add hD]; congr 1; rw [hεdef]; ring
  have hcount : D ^ (-q - ε₀) = D ^ (-q - ε) * A := by
    rw [hAdef, ← Real.rpow_add hD]; congr 1; rw [hεdef]; ring
  have hloss : δ ^ (-ε) ≤ 2 ^ ε * A := rpow_neg_le_of_half_le hD hDδ hε.le
  -- rescaled point law and relation
  let f : Space d → Space d := fun x => s • x
  have hf : Measurable f := measurable_const_smul s
  let μ' : Measure (Space d) := μ.map f
  let E' : Set (Space d × Sphere d) := {u | ‖u.1‖ ≤ 1/4 ∧ (s⁻¹ • u.1, u.2) ∈ E}
  have hE' : MeasurableSet E' := by
    refine (measurableSet_le (measurable_norm.comp measurable_fst) measurable_const).inter ?_
    exact hE.preimage (((measurable_const_smul (s⁻¹)).comp measurable_fst).prodMk measurable_snd)
  have hμ'univ : μ' univ = μ univ := by
    simp only [μ', Measure.map_apply hf MeasurableSet.univ, preimage_univ]
  haveI : IsFiniteMeasure μ' := ⟨by rw [hμ'univ]; exact hμm.trans_lt ENNReal.one_lt_top⟩
  have hsuppae : ∀ᵐ x ∂μ, x ∈ Metric.closedBall (0 : Space d) R := by
    rw [ae_iff]; exact hsupp
  have hμ'ae : ∀ᵐ x ∂μ', ‖x‖ ≤ 1/4 := by
    rw [ae_map_iff hf.aemeasurable (measurableSet_le measurable_norm measurable_const)]
    filter_upwards [hsuppae] with x hx
    rw [Metric.mem_closedBall, dist_zero_right] at hx
    change ‖s • x‖ ≤ 1/4
    rw [norm_smul, Real.norm_of_nonneg hs.le]
    nlinarith
  -- ball bounds at dyadic radii
  have hμ'b : ∀ x : Space d, ∀ j : ℕ, j ≤ N →
      μ' (Metric.ball x (1/(2:ℝ)^j)) ≤ ENNReal.ofReal (D^(-ε₀)*(1/(2:ℝ)^j)^t) := by
    intro x j hj
    set r : ℝ := 1/(2:ℝ)^j with hrdef
    have hr0 : 0 < r := by positivity
    have hDr : D ≤ r := by
      rw [hDdef, hrdef]
      exact one_div_le_one_div_of_le (by positivity) (pow_le_pow_right₀ (by norm_num) hj)
    have hr1 : r ≤ 1 := by
      rw [hrdef, div_le_one (by positivity)]; exact one_le_pow₀ (by norm_num)
    have hmap : μ' (Metric.ball x r) = μ (Metric.ball (s⁻¹ • x) (r / s)) := by
      simp only [μ', Measure.map_apply hf measurableSet_ball]
      rw [scale_preimage_ball hs]
    rw [hmap, hAA]
    by_cases hrs : r / s ≤ 1
    · have hδr : δ ≤ r / s := by
        have : r ≤ r / s := by rw [le_div_iff₀ hs]; nlinarith
        linarith
      apply (hμb _ _ hδr hrs).trans
      apply ENNReal.ofReal_le_ofReal
      have hrt : (r / s) ^ t = s ^ (-t) * r ^ t := by
        rw [Real.div_rpow hr0.le hs.le, Real.rpow_neg hs.le]; ring
      rw [hrt]
      have hrt0 : 0 ≤ r ^ t := by positivity
      have hst0 : 0 ≤ s ^ (-t) := by positivity
      calc δ ^ (-ε) * (s ^ (-t) * r ^ t) ≤ (2 ^ ε * A) * (s ^ (-t) * r ^ t) :=
            mul_le_mul_of_nonneg_right hloss (by positivity)
        _ = (2 ^ ε * s ^ (-t)) * A * r ^ t := by ring
        _ ≤ K * A * r ^ t := by gcongr
        _ ≤ A * A * r ^ t := by gcongr
    · rw [not_le] at hrs
      have hsr : s < r := by rwa [one_lt_div hs] at hrs
      apply (measure_mono (subset_univ _)).trans
      apply hμm.trans
      rw [← ENNReal.ofReal_one]
      apply ENNReal.ofReal_le_ofReal
      have h1 : s ^ t ≤ r ^ t := Real.rpow_le_rpow hs.le hsr.le ht
      have h2 : s ^ (-t) * s ^ t = 1 := by
        rw [← Real.rpow_add hs]; simp
      have hA1 : 1 ≤ A := by linarith
      have hst' : 0 ≤ s ^ t := by positivity
      calc (1:ℝ) = s ^ (-t) * s ^ t := h2.symm
        _ ≤ A * r ^ t := by gcongr; linarith
        _ ≤ A * A * r ^ t := by
          have h0 : 0 ≤ A * r ^ t := by positivity
          have h := mul_le_mul_of_nonneg_right hA1 h0
          calc A * r ^ t = 1 * (A * r ^ t) := by ring
            _ ≤ A * (A * r ^ t) := h
            _ = A * A * r ^ t := by ring
  have hνb' : ∀ w : Sphere d, ∀ j : ℕ, j ≤ N →
      ν (Metric.ball w (1/(2:ℝ)^j)) ≤ ENNReal.ofReal (D^(-ε₀)*(1/(2:ℝ)^j)^q) := by
    intro w j hj
    set r : ℝ := 1/(2:ℝ)^j with hrdef
    have hDr : D ≤ r := by
      rw [hDdef, hrdef]
      exact one_div_le_one_div_of_le (by positivity) (pow_le_pow_right₀ (by norm_num) hj)
    have hr1 : r ≤ 1 := by
      rw [hrdef, div_le_one (by positivity)]; exact one_le_pow₀ (by norm_num)
    apply (hνb w r (hδD.trans hDr) hr1).trans
    apply ENNReal.ofReal_le_ofReal
    rw [hAA]
    have : 0 ≤ r ^ q := by positivity
    calc δ ^ (-ε) * r ^ q ≤ (2 ^ ε * A) * r ^ q := mul_le_mul_of_nonneg_right hloss this
      _ ≤ (K * A) * r ^ q := by gcongr
      _ ≤ (A * A) * r ^ q := by gcongr
  have hslab : plate → ∀ w : Sphere d, ∀ r : ℝ, 1/(2:ℝ)^N ≤ r → r ≤ 1 →
      ν {u : Sphere d | |inner ℝ (w:Space d) (u:Space d)| ≤ r} ≤
        ENNReal.ofReal (D^(-ε₀)*r^ζ) := by
    intro hp w r hr hr1
    have hw : ‖(w : Space d)‖ = 1 := by simp
    apply (hplate hp (w : Space d) hw r (hδD.trans hr) hr1).trans
    apply ENNReal.ofReal_le_ofReal
    rw [hAA]
    have : 0 ≤ r ^ ζ := Real.rpow_nonneg (hD.le.trans hr) _
    calc δ ^ (-ε) * r ^ ζ ≤ (2 ^ ε * A) * r ^ ζ := mul_le_mul_of_nonneg_right hloss this
      _ ≤ (K * A) * r ^ ζ := by gcongr
      _ ≤ (A * A) * r ^ ζ := by gcongr
  have hE'b : ∀ u ∈ E', ‖u.1‖ ≤ 1/4 := fun u hu => hu.1
  have hcov' : ∀ w : Sphere d, ∃ S : Finset (Space d),
      (S.card : ℝ) ≤ D^(-q-ε₀) ∧
      ∀ x, (x,w) ∈ E' → ∃ a ∈ S,
        ‖perpendicularPart (w:Space d) (x-a)‖ ≤ C*D := by
    intro w
    obtain ⟨T, hT, hTcov⟩ := hcov w
    refine ⟨T.image f, ?_, ?_⟩
    · have h1 : ((T.image f).card : ℝ) ≤ T.card := by exact_mod_cast Finset.card_image_le
      have h2 : δ ^ (-q - ε) ≤ 2 ^ (q + ε) * D ^ (-q - ε) := by
        have := rpow_neg_le_of_half_le hD hDδ (show 0 ≤ q + ε by linarith)
        simpa only [neg_add'] using this
      rw [hcount]
      have : 0 ≤ D ^ (-q - ε) := by positivity
      calc ((T.image f).card : ℝ) ≤ δ ^ (-q - ε) := h1.trans hT
        _ ≤ 2 ^ (q + ε) * D ^ (-q - ε) := h2
        _ ≤ K * D ^ (-q - ε) := by gcongr
        _ ≤ A * D ^ (-q - ε) := by gcongr
        _ = D ^ (-q - ε) * A := by ring
    · intro x hx
      have hmem := hTcov hx.2
      simp only [mem_iUnion, mem_setOf_eq] at hmem
      obtain ⟨a, ha, hp⟩ := hmem
      refine ⟨f a, Finset.mem_image_of_mem f ha, ?_⟩
      have hxa : x - f a = s • (s⁻¹ • x - a) := by
        change x - s • a = s • (s⁻¹ • x - a)
        rw [smul_sub, smul_smul, mul_inv_cancel₀ hs.ne', one_smul]
      rw [hxa, perpendicularPart_smul, norm_smul, Real.norm_of_nonneg hs.le,
        ← norm_orthogonalProjection_eq_perpendicularPart]
      have hp0 : 0 ≤ ‖(ℝ ∙ (w : Space d))ᗮ.orthogonalProjectionOnto (s⁻¹ • x - a)‖ := norm_nonneg _
      calc s * ‖(ℝ ∙ (w : Space d))ᗮ.orthogonalProjectionOnto (s⁻¹ • x - a)‖
          ≤ 1 * (C * δ) := mul_le_mul hs1 hp (norm_nonneg _) zero_le_one
        _ ≤ C * D := by rw [one_mul]; exact mul_le_mul_of_nonneg_left hδD hC
  have hμ'm : μ' univ ≤ 1 := hμ'univ ▸ hμm
  have hNN₀ : N ≥ N₀ := by omega
  have hmain : (μ'.prod ν) E' ≤ ENNReal.ofReal (D ^ c₀) :=
    hg N hNN₀ μ' ν E' hμ'ae hμ'm hνm hμ'b hνb' hslab hE' hE'b hcov'
  -- compare the original incidence with the rescaled one
  have hcompare : (μ.prod ν) E ≤ (μ'.prod ν) E' := by
    have hprod : μ'.prod ν = (μ.prod ν).map (Prod.map f id) := by
      have := Measure.map_prod_map μ ν hf measurable_id
      rw [Measure.map_id] at this
      exact this
    rw [hprod, Measure.map_apply (hf.prodMap measurable_id) hE']
    have hsub : E ⊆ (Prod.map f id ⁻¹' E') ∪ ((Metric.closedBall (0 : Space d) R)ᶜ ×ˢ univ) := by
      intro u hu
      by_cases hx : u.1 ∈ Metric.closedBall (0 : Space d) R
      · left
        rw [Metric.mem_closedBall, dist_zero_right] at hx
        refine ⟨?_, ?_⟩
        · change ‖s • u.1‖ ≤ 1/4
          rw [norm_smul, Real.norm_of_nonneg hs.le]
          nlinarith
        · change (s⁻¹ • s • u.1, u.2) ∈ E
          rw [smul_smul, inv_mul_cancel₀ hs.ne', one_smul]
          exact hu
      · right
        exact ⟨hx, mem_univ _⟩
    calc (μ.prod ν) E
        ≤ (μ.prod ν) ((Prod.map f id ⁻¹' E') ∪ ((Metric.closedBall (0 : Space d) R)ᶜ ×ˢ univ)) :=
          measure_mono hsub
      _ ≤ (μ.prod ν) (Prod.map f id ⁻¹' E') +
            (μ.prod ν) ((Metric.closedBall (0 : Space d) R)ᶜ ×ˢ univ) := measure_union_le _ _
      _ = (μ.prod ν) (Prod.map f id ⁻¹' E') := by
          rw [Measure.prod_prod, hsupp, zero_mul, add_zero]
  -- final scale conversion: `D^{c₀} ≤ δ^{c₀/2}`
  have hfinal : D ^ c₀ ≤ δ ^ c := by
    have hsq : D ≤ Real.sqrt δ := by
      have h1 : Real.sqrt δ * Real.sqrt δ = δ := Real.mul_self_sqrt hδ.le
      have h2 : Real.sqrt δ ≤ 1/2 := by
        rw [Real.sqrt_le_left (by norm_num)]; linarith
      have h3 : 0 ≤ Real.sqrt δ := Real.sqrt_nonneg δ
      have h4 : D ≤ 2 * δ := by linarith
      nlinarith
    calc D ^ c₀ ≤ (Real.sqrt δ) ^ c₀ := Real.rpow_le_rpow hD.le hsq hc₀.le
      _ = δ ^ c := by
        rw [Real.sqrt_eq_rpow, ← Real.rpow_mul hδ.le, hcdef]; ring_nf
  calc (μ.prod ν) E ≤ (μ'.prod ν) E' := hcompare
    _ ≤ ENNReal.ofReal (D ^ c₀) := hmain
    _ ≤ ENNReal.ofReal (δ ^ c) := ENNReal.ofReal_le_ofReal hfinal

end Falconer.LinearGain

end OAI
end

section
set_option linter.all false

namespace OAI

namespace Falconer.LinearGain
open Set MeasureTheory Filter
open scoped ENNReal Topology

/-- Case `q > k - 1`, with `k = h + 1`: the port's nonendpoint gain for arbitrary covers. -/
theorem dyadic_nonendpoint {h : ℕ} {t q ζ C : ℝ}
    (hq : (h:ℝ) < q) (hq' : q-(h:ℝ) ≤ 1/2) (hqt : q < t) (ht : t-(h:ℝ) < 1)
    (hC : 0 ≤ C) (plate : Prop) :
    DyadicTubeGain (h+2) t q ζ C plate := by
  obtain ⟨ε, c, δ₀, hε, hc, hδ₀, hg⟩ :=
    nonendpoint_dyadic_tube_gain publishedPlanarFurstenberg_proved hq hq' hqt ht hC
  obtain ⟨N₀, hN₀⟩ := eventually_atTop.mp
    (dyadic_inverse_tendsto.eventually (Ioo_mem_nhdsGT hδ₀))
  refine ⟨ε, c, hε, hc, N₀, ?_⟩
  intro N hN μ ν _ _ E hμ hμm hνm hμb hνb _ hE hEb hcov
  exact hg N μ ν E (hN₀ N hN).2 hμ hμm hνm hμb hνb hE hEb hcov

/-- Case `q = k - 1`, with `k = h + 2`: the port's endpoint gain for arbitrary covers. -/
theorem dyadic_endpoint {h : ℕ} {t ζ C : ℝ}
    (ht : (h:ℝ)+3/2 < t) (ht' : t < (h:ℝ)+2) (hζ : 0 < ζ) (hC : 0 ≤ C)
    {plate : Prop} (hp : plate) :
    DyadicTubeGain (h+3) t ((h:ℝ)+1) ζ C plate := by
  obtain ⟨ε, c, hε, hc, N₀, hg⟩ :=
    endpoint_dyadic_tube_gain published_finite_loomis_whitney ht ht' hζ hC
  refine ⟨ε, c, hε, hc, N₀, ?_⟩
  intro N hN μ ν _ _ E hμ hμm hνm hμb hνb hslab hE hEb hcov
  exact hg N hN μ ν E hμ hμm hνm hμb hνb (hslab hp) hE hEb hcov

end Falconer.LinearGain

end OAI
end

open MeasureTheory in
/-- Theorem 4.1 (linear projection gain). Same type as
`OAI.Falconer.linear_projection_gain`. -/
theorem solution (k : ℕ) (hk : 2 ≤ k) (q t : ℝ)
    (hq : (k:ℝ) - 1 ≤ q) (hq' : q ≤ (k:ℝ) - 1/2) (hqt : (k:ℝ) - 1/2 < t) (ht : t < k)
    (C : ℝ) (hC : 0 ≤ C) (R : ℝ) (hR : 0 < R) (ζ : ℝ) (hζ : 0 < ζ) :
    ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
    ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ (μ : Measure (EuclideanSpace ℝ (Fin (k+1))))
      (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1))
      (E : Set (EuclideanSpace ℝ (Fin (k+1)) ×
        Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1)),
    μ Set.univ ≤ 1 → ν Set.univ ≤ 1 →
    μ (Metric.closedBall 0 R)ᶜ = 0 →
    (∀ (z : EuclideanSpace ℝ (Fin (k+1))) (r : ℝ), δ ≤ r → r ≤ 1 →
      μ (Metric.ball z r) ≤ ENNReal.ofReal (δ^(-ε) * r^t)) →
    (∀ (w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1) (r : ℝ), δ ≤ r → r ≤ 1 →
      ν (Metric.ball w r) ≤ ENNReal.ofReal (δ^(-ε) * r^q)) →
    (q = (k:ℝ) - 1 → ∀ n : EuclideanSpace ℝ (Fin (k+1)), ‖n‖ = 1 →
      ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | |inner ℝ n (w : EuclideanSpace ℝ (Fin (k+1)))| ≤ r} ≤
          ENNReal.ofReal (δ^(-ε) * r^ζ)) →
    MeasurableSet E →
    (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k+1))) 1,
      ∃ T : Finset (EuclideanSpace ℝ (Fin (k+1))), (T.card : ℝ) ≤ δ^(-q-ε) ∧
        {x | (x, w) ∈ E} ⊆ ⋃ a ∈ T,
          {x | ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin (k+1))))ᗮ.orthogonalProjectionOnto (x - a)‖ ≤
            C * δ}) →
    (μ.prod ν) E ≤ ENNReal.ofReal (δ^c) := by
  rcases eq_or_lt_of_le hq with heq | hlt
  · -- endpoint case `q = k - 1`, sliced with `h = k - 2`
    obtain ⟨h, rfl⟩ : ∃ h, k = h + 2 := ⟨k - 2, by omega⟩
    have hqh : q = (h:ℝ) + 1 := by push_cast at heq; linarith
    subst hqh
    push_cast at hqt ht
    have hg := OAI.Falconer.LinearGain.dyadic_endpoint (h := h) (t := t) (ζ := ζ) (C := C)
      (by linarith) (by linarith) hζ hC
      (plate := ((h:ℝ) + 1 = ((h+2 : ℕ) : ℝ) - 1)) (by push_cast; ring)
    exact OAI.Falconer.LinearGain.scaleGain_of_dyadic (d := h+2+1)
      (by linarith) (by positivity) hC hR hg
  · -- nonendpoint case `q > k - 1`, sliced with `h = k - 1`
    obtain ⟨h, rfl⟩ : ∃ h, k = h + 1 := ⟨k - 1, by omega⟩
    push_cast at hlt hq' hqt ht
    have hg := OAI.Falconer.LinearGain.dyadic_nonendpoint (h := h) (t := t) (q := q) (ζ := ζ)
      (C := C) (by linarith) (by linarith) (by linarith) (by linarith) hC
      (q = ((h+1 : ℕ) : ℝ) - 1)
    exact OAI.Falconer.LinearGain.scaleGain_of_dyadic (d := h+1+1)
      (by linarith) (by linarith) hC hR hg
```