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
-- ===== Statement.lean (Codex) =====
import Mathlib

open Set MeasureTheory
open scoped ENNReal InnerProductSpace

namespace OAI.Falconer

/-
Readings of Theorem 4.1 (ang:linear-gain) and Section 1 conventions:
* k, q, t, the nonnegative width constant C, and a nonnegative support radius R
  are fixed before the losses, gain, or scale threshold are chosen.
* ζ is fixed at the same stage; it is required positive only when q = k - 1.
* A subprobability is a positive Borel measure of total mass at most one;
  it is not normalized. Bounded point support means ‖x‖ ≤ R μ-almost everywhere.
  The fixed origin is harmless, since any fixed bounded region lies in such a ball.
* S^k is the subtype Metric.sphere 0 1 in EuclideanSpace ℝ (Fin (k+1)).
  Its balls use the induced Euclidean chordal distance. Directions are oriented;
  no symmetry or identification of antipodal points is imposed on ν.
* Both ball bounds hold at every center and every real radius δ ≤ r ≤ 1,
  with multiplicative loss δ^(-ε), outside the power r^t or r^q.
* The endpoint condition holds for every linear hyperplane H (finrank H = k),
  on its closed r-neighborhood measured by ambient Euclidean distance.
* Incidence relations may be measurable in the completed product measure:
  NullMeasurableSet expresses this without requiring a Borel representative.
* For every direction, the entire fiber has a finite cover with real cardinality
  at most δ^(-q-ε). A closed width-Cδ tube about a+ℝw is expressed by the norm
  of orthogonal projection of x-a onto (ℝw)ᗮ. There is no common anchor list or
  measurable choice of covers among the hypotheses. Bounded length has no extra
  effect on incidence mass: inside the fixed source ball one can truncate all
  tubes to a fixed length (and discard points outside that ball at zero μ cost).
* ε, c and δ₀ are uniform over all μ, ν, E and all real 0 < δ < δ₀;
  there is no dyadic-scale restriction and no implicit output constant.
-/
theorem linear_projection_gain
    (k : ℕ) (hk : 2 ≤ k) (q t : ℝ)
    (hq : (k : ℝ) - 1 ≤ q) (hq' : q ≤ (k : ℝ) - 1 / 2)
    (ht : (k : ℝ) - 1 / 2 < t) (ht' : t < (k : ℝ))
    (C : ℝ) (hC : 0 ≤ C) (R : ℝ) (hR : 0 ≤ R)
    (ζ : ℝ) (hζ : q = (k : ℝ) - 1 → 0 < ζ) :
    ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
      ∀ δ : ℝ, 0 < δ → δ < δ₀ →
      ∀ (μ : Measure (EuclideanSpace ℝ (Fin (k + 1))))
        (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1)),
      μ univ ≤ 1 → ν univ ≤ 1 →
      (∀ᵐ x ∂μ, ‖x‖ ≤ R) →
      (∀ x : EuclideanSpace ℝ (Fin (k + 1)), ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        μ (Metric.ball x r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ t)) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν (Metric.ball w r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ q)) →
      (q = (k : ℝ) - 1 →
        ∀ H : Submodule ℝ (EuclideanSpace ℝ (Fin (k + 1))),
        Module.finrank ℝ H = k → ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | Metric.infDist (w : EuclideanSpace ℝ (Fin (k + 1))) (H : Set _) ≤ r}
          ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ ζ)) →
      ∀ E : Set (EuclideanSpace ℝ (Fin (k + 1)) ×
        Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1),
      NullMeasurableSet E (μ.prod ν) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∃ A : Finset (EuclideanSpace ℝ (Fin (k + 1))),
          (A.card : ℝ) ≤ δ ^ (-q - ε) ∧
          ∀ x : EuclideanSpace ℝ (Fin (k + 1)), (x, w) ∈ E →
            ∃ a ∈ A,
              ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin (k + 1))))ᗮ.orthogonalProjectionOnto
                (x - a)‖ ≤ C * δ) →
      (μ.prod ν) E ≤ ENNReal.ofReal (δ ^ c) := by
  sorry

end OAI.Falconer

-- ===== Proof.lean (Codex), lines 1-310: header and top bridge section =====
import Theorems.Thm_OAI_Falconer_controlled_dyadic_angular_gain
import Theorems.Thm_OAI_Falconer_controlled_endpoint_angular_gain
import Theorems.Thm_OAI_Falconer_endpoint_spherical_preparation
import Theorems.Thm_OAI_Falconer_publishedPlanarFurstenberg_proved




open Set MeasureTheory Filter
open scoped ENNReal InnerProductSpace Topology

/-- A raw-measure estimate on one small cap. The cap radius and all budgets must
be chosen before the laws, incidence relation, and cap center. This is the
remaining bridge, rather than a theorem assumed or added to the environment. -/
def SmallCapGain (k : ℕ) (q t C R ζ : ℝ) : Prop :=
  ∃ ρ : ℝ, 0 < ρ ∧ ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧
    ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ (μ : Measure (Point k)) (ν : Measure (Direction k)),
    Laws k q t R ζ ε δ μ ν → ∀ (w₀ : Direction k) (E : Set (Point k × Direction k)),
    NullMeasurableSet E (μ.prod ν) → FiberCover k q C ε δ E →
    (∀ u ∈ E, dist u.2 w₀ ≤ ρ) → (μ.prod ν) E ≤ ENNReal.ofReal (δ ^ c)

/-- Precise missing bridge lemma type, including both slicing regimes. -/
def SmallCapBridge : Prop :=
  ∀ (k : ℕ), 2 ≤ k → ∀ q t : ℝ,
    (k : ℝ) - 1 ≤ q → q ≤ (k : ℝ) - 1 / 2 →
    (k : ℝ) - 1 / 2 < t → t < (k : ℝ) →
    ∀ C : ℝ, 0 ≤ C → ∀ R : ℝ, 0 ≤ R →
    ∀ ζ : ℝ, (q = (k : ℝ) - 1 → 0 < ζ) → SmallCapGain k q t C R ζ

theorem fiberCover_mono {k : ℕ} {q C ε δ : ℝ} {E F : Set (Point k × Direction k)}
    (h : FiberCover k q C ε δ E) (hFE : F ⊆ E) : FiberCover k q C ε δ F := by
  intro w
  obtain ⟨A, hA, hcover⟩ := h w
  exact ⟨A, hA, fun x hx => hcover x (hFE hx)⟩

/-- The standalone tube definition has exactly the port's unit-vector formula. -/
theorem perpendicular_projection_formula {k : ℕ} (w : Direction k) (v : Point k) :
    ((ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto v : Point k) =
      v - inner ℝ (w : Point k) v • (w : Point k) := by
  have hw : ‖(w : Point k)‖ = 1 := by simpa using w.property
  rw [Submodule.coe_orthogonalProjectionOnto_apply,
    Submodule.starProjection_orthogonal_val,
    Submodule.starProjection_unit_singleton ℝ hw]

/-- Reanchor a tube at an incident point; its width increases by at most two. -/
theorem reanchor_tube {k : ℕ} (w : Direction k) (x y a : Point k) {s : ℝ}
    (hx : ‖(ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto (x - a)‖ ≤ s)
    (hy : ‖(ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto (y - a)‖ ≤ s) :
    ‖(ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto (x - y)‖ ≤ 2 * s := by
  let P := (ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto
  have hxy : P (x - y) = P (x - a) - P (y - a) := by rw [← map_sub]; congr 1; abel
  change ‖P (x - y)‖ ≤ 2 * s
  rw [hxy]
  exact (norm_sub_le _ _).trans (by change ‖P (x - a)‖ + ‖P (y - a)‖ ≤ 2 * s; linarith)

/-- Fixed finite sums of power-small masses have a power-small bound with no
output constant, after reducing the gain and shrinking the scale threshold. -/
theorem absorb_finite_constant (M c : ℝ) (hc : 0 < c) :
    ∃ d : ℝ, 0 < d ∧ ∀ δ : ℝ, 0 < δ → δ < d → M * δ ^ c ≤ δ ^ (c / 2) := by
  have hlim : Tendsto (fun δ : ℝ => M * δ ^ (c / 2)) (𝓝 0) (𝓝 0) := by
    simpa using (tendsto_id.rpow_const_nhds_zero (by linarith : 0 < c / 2)).const_mul M
  have hev : ∀ᶠ δ : ℝ in 𝓝 0, M * δ ^ (c / 2) < 1 :=
    hlim.eventually (gt_mem_nhds (by norm_num : (0 : ℝ) < 1))
  obtain ⟨d, hd, hbound⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨d, hd, fun δ hδ hδd => ?_⟩
  have hb := hbound (y := δ) (by simpa [Real.dist_eq, abs_of_pos hδ] using hδd)
  have hp : 0 ≤ δ ^ (c / 2) := Real.rpow_nonneg hδ.le _
  have heq : δ ^ c = δ ^ (c / 2) * δ ^ (c / 2) := by
    rw [← Real.rpow_add hδ]; congr 1; ring
  rw [heq, ← mul_assoc]
  simpa using mul_le_mul_of_nonneg_right hb.le hp

/-- A finite cover by small caps suffices; disjoint caps are unnecessary. -/
theorem finite_caps {k : ℕ} {ρ : ℝ} (hρ : 0 < ρ) :
    ∃ A : Finset (Direction k), ∀ w : Direction k, ∃ a ∈ A, dist w a < ρ := by
  classical
  have hcompact : IsCompact (univ : Set (Direction k)) := isCompact_univ
  obtain ⟨A, hA⟩ := hcompact.elim_finite_subcover
    (fun a : Direction k => Metric.ball a ρ) (fun _ => Metric.isOpen_ball)
    (by intro w _; exact mem_iUnion.mpr ⟨w, Metric.mem_ball_self hρ⟩)
  refine ⟨A, fun w => ?_⟩
  simpa only [mem_iUnion, Metric.mem_ball, exists_prop] using hA (mem_univ w)

/-- Fully proved global conclusion conditional on the explicitly named bridge.
There is no axiom or sorry supplying that bridge. -/
theorem global_of_smallCapGain
    {k : ℕ} {q t C R ζ : ℝ} (hlocal : SmallCapGain k q t C R ζ) :
    ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
    ∀ δ : ℝ, 0 < δ → δ < δ₀ →
    ∀ (μ : Measure (Point k)) (ν : Measure (Direction k)),
    Laws k q t R ζ ε δ μ ν → ∀ E : Set (Point k × Direction k),
    NullMeasurableSet E (μ.prod ν) → FiberCover k q C ε δ E →
    (μ.prod ν) E ≤ ENNReal.ofReal (δ ^ c) := by
  classical
  obtain ⟨ρ, hρ, ε, hε, c, hc, δ₀, hδ₀, hgain⟩ := hlocal
  obtain ⟨A, hA⟩ := finite_caps (k := k) hρ
  obtain ⟨d, hd, hsum⟩ := absorb_finite_constant (A.card : ℝ) c hc
  refine ⟨ε, hε, c / 2, by linarith, min δ₀ d, lt_min hδ₀ hd, ?_⟩
  intro δ hδ hδsmall μ ν hlaws E hE hcover
  let F : Direction k → Set (Point k × Direction k) :=
    fun a => E ∩ Prod.snd ⁻¹' Metric.ball a ρ
  have hF (a : Direction k) : NullMeasurableSet (F a) (μ.prod ν) :=
    hE.inter ((Metric.isOpen_ball.measurableSet.preimage measurable_snd).nullMeasurableSet)
  have hb (a : Direction k) : (μ.prod ν) (F a) ≤ ENNReal.ofReal (δ ^ c) := by
    apply hgain δ hδ (lt_min_iff.mp hδsmall).1 μ ν hlaws a (F a) (hF a)
      (fiberCover_mono hcover inter_subset_left)
    intro u hu
    exact (Metric.mem_ball.mp hu.2).le
  have hsub : E ⊆ ⋃ a ∈ A, F a := by
    intro u hu
    obtain ⟨a, ha, hua⟩ := hA u.2
    exact mem_iUnion.mpr ⟨a, mem_iUnion.mpr ⟨ha, hu, hua⟩⟩
  calc
    (μ.prod ν) E ≤ (μ.prod ν) (⋃ a ∈ A, F a) := measure_mono hsub
    _ ≤ ∑ a ∈ A, (μ.prod ν) (F a) := measure_biUnion_finset_le A F
    _ ≤ ∑ _a ∈ A, ENNReal.ofReal (δ ^ c) := Finset.sum_le_sum fun a _ => hb a
    _ = ENNReal.ofReal ((A.card : ℝ) * δ ^ c) := by
      rw [← ENNReal.ofReal_sum_of_nonneg (fun _ _ => Real.rpow_nonneg hδ.le _)]
      congr 1
      simp
    _ ≤ ENNReal.ofReal (δ ^ (c / 2)) :=
      ENNReal.ofReal_le_ofReal (hsum δ hδ (lt_min_iff.mp hδsmall).2)

end OAI.Falconer.LinearProjectionGainPartial


open Set MeasureTheory Filter
open scoped ENNReal InnerProductSpace Topology

namespace OAI.Falconer.LinearProjectionGainPartial

/-- The port's normalized estimate, stated using the target's raw hypotheses. -/
def UnitDyadicGain (k : ℕ) (q t C ζ : ℝ) : Prop :=
  ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ d : ℝ, 0 < d ∧
  ∀ N : ℕ, (1 / 2 : ℝ) ^ N < d →
  ∀ (μ : Measure (Point k)) (ν : Measure (Direction k)),
  Laws k q t (1 / 4) ζ ε ((1 / 2 : ℝ) ^ N) μ ν →
  ∀ E : Set (Point k × Direction k), MeasurableSet E →
  (∀ u ∈ E, ‖u.1‖ ≤ 1 / 4) →
  FiberCover k q C ε ((1 / 2 : ℝ) ^ N) E →
  (μ.prod ν) E ≤ ENNReal.ofReal (((1 / 2 : ℝ) ^ N) ^ c)


/-- Translate a restricted point law into the fixed source ball. -/
theorem translated_laws {k : ℕ} {q t R ζ ε δ : ℝ}
    {μ : Measure (Point k)} {ν : Measure (Direction k)}
    (h : Laws k q t R ζ ε δ μ ν) (b : Point k) :
    Laws k q t (1 / 4) ζ ε δ
      (Measure.map (fun x => x - b) (μ.restrict (Metric.closedBall b (1 / 4)))) ν := by
  obtain ⟨hm, hn, hs, hb, hq, hp⟩ := h
  refine ⟨?_, hn, ?_, ?_, hq, hp⟩
  · rw [Measure.map_apply (by fun_prop) MeasurableSet.univ, preimage_univ]
    exact (Measure.restrict_le_self _).trans hm
  · rw [ae_map_iff (by fun_prop : Measurable (fun x : Point k => x - b)).aemeasurable
      (measurableSet_le measurable_norm measurable_const)]
    filter_upwards [ae_restrict_mem measurableSet_closedBall] with x hx
    simpa only [Metric.mem_closedBall, dist_eq_norm] using hx
  · intro x r hδr hr
    rw [Measure.map_apply (by fun_prop) measurableSet_ball]
    have he : (fun y : Point k => y - b) ⁻¹' Metric.ball x r = Metric.ball (x + b) r := by
      ext y
      simp only [mem_preimage, Metric.mem_ball, dist_eq_norm]
      congr 2
      abel
    rw [he]
    exact (Measure.restrict_le_self _).trans (hb (x + b) r hδr hr)


/-- Translated relations retain their finite covers without changing width. -/
theorem translated_cover {k : ℕ} {q C ε δ : ℝ}
    {E : Set (Point k × Direction k)} (h : FiberCover k q C ε δ E) (b : Point k) :
    FiberCover k q C ε δ
      ((fun u : Point k × Direction k => (u.1 + b, u.2)) ⁻¹'
        (E ∩ Prod.fst ⁻¹' Metric.closedBall b (1 / 4))) := by
  classical
  intro w
  obtain ⟨A, hA, hc⟩ := h w
  refine ⟨A.image (fun a => a - b), ?_, ?_⟩
  · exact (show ((A.image (fun a => a - b)).card : ℝ) ≤ A.card by
      exact_mod_cast Finset.card_image_le).trans hA
  · intro x hx
    obtain ⟨a, ha, hxa⟩ := hc (x + b) hx.1
    refine ⟨a - b, Finset.mem_image.mpr ⟨a, ha, rfl⟩, ?_⟩
    convert hxa using 1 <;> congr 2 <;> abel


/-- Translation of a localized relation preserves its product mass. -/
theorem translated_mass {k : ℕ} (μ : Measure (Point k)) (ν : Measure (Direction k))
    [SFinite μ] [SFinite ν] (E : Set (Point k × Direction k)) (hE : MeasurableSet E)
    (b : Point k) :
    ((Measure.map (fun x => x - b) (μ.restrict (Metric.closedBall b (1 / 4)))).prod ν)
      ((fun u : Point k × Direction k => (u.1 + b, u.2)) ⁻¹'
        (E ∩ Prod.fst ⁻¹' Metric.closedBall b (1 / 4))) =
    (μ.prod ν) (E ∩ Prod.fst ⁻¹' Metric.closedBall b (1 / 4)) := by
  let F := E ∩ Prod.fst ⁻¹' Metric.closedBall b (1 / 4)
  have hF : MeasurableSet F := hE.inter ((measurableSet_closedBall).preimage measurable_fst)
  have he : ν = Measure.map id ν := Measure.map_id.symm
  conv_lhs => rw [he]
  rw [Measure.map_prod_map _ _ (by fun_prop) measurable_id,
    Measure.map_apply (by fun_prop) (hF.preimage (by fun_prop))]
  have hp : Prod.map (fun x : Point k => x - b) id ⁻¹'
      ((fun u : Point k × Direction k => (u.1 + b, u.2)) ⁻¹' F) = F := by
    ext u
    simp [Prod.map]
  rw [hp, Measure.restrict_prod_eq_prod_univ, Measure.restrict_apply hF]
  congr 1
  apply inter_eq_left.mpr
  intro u hu
  exact ⟨hu.2, mem_univ _⟩


/-- A normalized dyadic estimate extends to bounded support and completed relations.
A finite spatial cover avoids any change of scale. -/
theorem bounded_dyadic_gain {k : ℕ} {q t C R ζ : ℝ}
    (hunit : UnitDyadicGain k q t C ζ) :
    ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ d : ℝ, 0 < d ∧
    ∀ N : ℕ, (1 / 2 : ℝ) ^ N < d →
    ∀ (μ : Measure (Point k)) (ν : Measure (Direction k)),
    Laws k q t R ζ ε ((1 / 2 : ℝ) ^ N) μ ν →
    ∀ E : Set (Point k × Direction k), NullMeasurableSet E (μ.prod ν) →
    FiberCover k q C ε ((1 / 2 : ℝ) ^ N) E →
    (μ.prod ν) E ≤ ENNReal.ofReal (((1 / 2 : ℝ) ^ N) ^ c) := by
  classical
  obtain ⟨ε, hε, c, hc, d, hd, hg⟩ := hunit
  obtain ⟨A, hA⟩ := (isCompact_closedBall (0 : Point k) R).elim_finite_subcover
    (fun b : Point k => Metric.ball b (1 / 4)) (fun _ => Metric.isOpen_ball)
    (by intro x _; exact mem_iUnion.mpr ⟨x, Metric.mem_ball_self (by norm_num)⟩)
  obtain ⟨d', hd', habs⟩ := absorb_finite_constant (A.card : ℝ) c hc
  refine ⟨ε, hε, c / 2, by positivity, min d d', lt_min hd hd', ?_⟩
  intro N hN μ ν hl E hE hcov
  let δ : ℝ := (1 / 2 : ℝ) ^ N
  have hδ : 0 < δ := by dsimp [δ]; positivity
  letI : IsFiniteMeasure μ := ⟨hl.1.trans_lt (by simp)⟩
  letI : IsFiniteMeasure ν := ⟨hl.2.1.trans_lt (by simp)⟩
  obtain ⟨E₀, hsub, hE₀, heq⟩ := hE.exists_measurable_subset_ae_eq
  let F := E₀ ∩ {u : Point k × Direction k | ‖u.1‖ ≤ R}
  have hF : MeasurableSet F := hE₀.inter (measurableSet_le (by fun_prop) measurable_const)
  have hFE : F ⊆ E := inter_subset_left.trans hsub
  have hmass : (μ.prod ν) F = (μ.prod ν) E := by
    apply measure_congr
    filter_upwards [heq, Measure.quasiMeasurePreserving_fst.ae hl.2.2.1] with u hu hs
    apply propext
    change (u ∈ E₀ ∧ ‖u.1‖ ≤ R) ↔ u ∈ E
    simp only [hs, and_true]
    exact Iff.of_eq hu
  let P : Point k → Set (Point k × Direction k) :=
    fun b => F ∩ Prod.fst ⁻¹' Metric.closedBall b (1 / 4)
  have hb (b : Point k) : (μ.prod ν) (P b) ≤ ENNReal.ofReal (δ ^ c) := by
    let μb := Measure.map (fun x : Point k => x - b) (μ.restrict (Metric.closedBall b (1 / 4)))
    let Eb := (fun u : Point k × Direction k => (u.1 + b, u.2)) ⁻¹' P b
    have hEb : MeasurableSet Eb :=
      (hF.inter ((measurableSet_closedBall).preimage measurable_fst)).preimage (by fun_prop)
    have hbound : ∀ u ∈ Eb, ‖u.1‖ ≤ 1 / 4 := by
      intro u hu
      have hh : dist (u.1 + b) b ≤ 1 / 4 := hu.2
      simpa only [dist_eq_norm, add_sub_cancel_right] using hh
    have hh := hg N (lt_min_iff.mp hN).1 μb ν (translated_laws hl b) Eb hEb hbound
      (translated_cover (fiberCover_mono hcov hFE) b)
    rw [translated_mass μ ν F hF b] at hh
    exact hh
  have hcover : F ⊆ ⋃ b ∈ A, P b := by
    intro u hu
    have hx : u.1 ∈ Metric.closedBall (0 : Point k) R := by
      have hnorm : ‖u.1‖ ≤ R := hu.2
      simpa only [Metric.mem_closedBall, dist_zero_right] using hnorm
    obtain ⟨b, hb, hxb⟩ := mem_iUnion₂.mp (hA hx)
    exact mem_iUnion₂.mpr ⟨b, hb, hu, (Metric.mem_ball.mp hxb).le⟩
  rw [← hmass]
  calc
    (μ.prod ν) F ≤ (μ.prod ν) (⋃ b ∈ A, P b) := measure_mono hcover
    _ ≤ ∑ b ∈ A, (μ.prod ν) (P b) := measure_biUnion_finset_le A P
    _ ≤ ∑ _b ∈ A, ENNReal.ofReal (δ ^ c) := Finset.sum_le_sum (fun b _ => hb b)
    _ = ENNReal.ofReal ((A.card : ℝ) * δ ^ c) := by
      simp only [Finset.sum_const, nsmul_eq_mul]
      rw [← ENNReal.ofReal_natCast, ← ENNReal.ofReal_mul (Nat.cast_nonneg _)]
    _ ≤ ENNReal.ofReal (δ ^ (c / 2)) := ENNReal.ofReal_le_ofReal
      (habs δ hδ (lt_min_iff.mp hN).2)


end OAI.Falconer.LinearProjectionGainPartial

/- Helper proofs copied from port_sources.txt. Original module names below
identify their provenance. Only the listed platform nodes are imported. -/
section
-- module Solutions.OAIQ088_FD.Falconer_Slicing_SmallGaussianChart

-- ===== Proof.lean (Codex), lines 3700-4009: ending bridge and solution =====
-- Recovered fragment. Lines 311-3699 of the original Proof.lean were not recovered; per the
-- clarity review they are helper lemmas copied from the port (black-box inputs).
      exact norm_ne_zero_iff.mp (by rw [hw]; norm_num)
    have hg' := hg N hN₀ μ ν E hs hm hn
      (fun x j hj => by
        simpa only [one_div, inv_pow] using hmb x ((1 / 2 : ℝ) ^ j)
          (pow_le_pow_of_le_one (by norm_num) (by norm_num) hj)
          (pow_le_one₀ (by norm_num) (by norm_num)))
    rw [show (1 / 2 : ℝ) ^ N = 1 / (2 : ℝ) ^ N by simp [div_pow]]
    apply hg'
    · intro w j hj
      simpa only [he, one_div, inv_pow] using hnb w ((1 / 2 : ℝ) ^ j)
        (pow_le_pow_of_le_one (by norm_num) (by norm_num) hj)
        (pow_le_one₀ (by norm_num) (by norm_num))
    · intro w r hr hr1
      apply (measure_mono (slab_subset_plate w r)).trans
      simpa only [one_div, inv_pow] using
        (hp (by rw [he, hcast]; ring) _ (hdim w) r
          (by simpa only [one_div, inv_pow] using hr) hr1)
    · exact hE
    · exact hEb
    · intro w
      obtain ⟨A, hA, hAc⟩ := hcov w
      refine ⟨A, by simpa only [he, one_div, inv_pow] using hA, ?_⟩
      intro x hx
      obtain ⟨a, ha, hxa⟩ := hAc x hx
      refine ⟨a, ha, ?_⟩
      change ‖((ℝ ∙ (w : Point (h + 2)))ᗮ.orthogonalProjectionOnto (x - a) :
        Point (h + 2))‖ ≤ C * ((1 / 2 : ℝ) ^ N) at hxa
      rw [perpendicular_projection_formula] at hxa
      simpa only [perpendicularPart, one_div, inv_pow] using hxa
  · have hqgt : (h : ℝ) + 1 < q := by
      apply lt_of_not_ge
      intro hle
      apply he
      linarith
    obtain ⟨ε, c, d, hε, hc, hd, hg⟩ := nonendpoint_dyadic_tube_gain
      publishedPlanarFurstenberg_proved (h := h + 1) (t := t) (q := q) (C := C)
      (by push_cast; linarith) (by push_cast; linarith)
      (by linarith) (by push_cast; linarith) hC
    refine ⟨ε, hε, c, hc, d, hd, ?_⟩
    intro N hN μ ν hl E hE hEb hcov
    obtain ⟨hm, hn, hs, hmb, hnb, _⟩ := hl
    letI : IsFiniteMeasure μ := ⟨hm.trans_lt (by simp)⟩
    letI : IsFiniteMeasure ν := ⟨hn.trans_lt (by simp)⟩
    rw [show (1 / 2 : ℝ) ^ N = 1 / (2 : ℝ) ^ N by simp [div_pow]]
    apply hg N μ ν E (by simpa only [one_div, inv_pow] using hN) hs hm hn
    · intro x j hj
      simpa only [one_div, inv_pow] using hmb x ((1 / 2 : ℝ) ^ j)
        (pow_le_pow_of_le_one (by norm_num) (by norm_num) hj)
        (pow_le_one₀ (by norm_num) (by norm_num))
    · intro w j hj
      simpa only [one_div, inv_pow] using hnb w ((1 / 2 : ℝ) ^ j)
        (pow_le_pow_of_le_one (by norm_num) (by norm_num) hj)
        (pow_le_one₀ (by norm_num) (by norm_num))
    · exact hE
    · exact hEb
    · intro w
      obtain ⟨A, hA, hAc⟩ := hcov w
      refine ⟨A, by simpa only [one_div, inv_pow] using hA, ?_⟩
      intro x hx
      obtain ⟨a, ha, hxa⟩ := hAc x hx
      refine ⟨a, ha, ?_⟩
      change ‖((ℝ ∙ (w : Point (h + 2)))ᗮ.orthogonalProjectionOnto (x - a) :
        Point (h + 2))‖ ≤ C * ((1 / 2 : ℝ) ^ N) at hxa
      rw [perpendicular_projection_formula] at hxa
      simpa only [perpendicularPart, one_div, inv_pow] using hxa

end OAI.Falconer.LinearProjectionGainPartial


open Set MeasureTheory Filter
open scoped ENNReal Topology

namespace OAI.Falconer.LinearProjectionGainPartial

/-- A positive loss margin absorbs the fixed factor in replacing a real scale
by a comparable larger scale. -/
theorem input_scale_slack (p η ε : ℝ) (hεη : ε < η) (hpη : 0 ≤ p + η) :
    ∃ d : ℝ, 0 < d ∧ ∀ δ u : ℝ, 0 < δ → δ < d →
      0 < u → u ≤ 2 * δ → δ ^ (-p - ε) ≤ u ^ (-p - η) := by
  have hlim : Tendsto (fun δ : ℝ => δ ^ (η - ε)) (𝓝 0) (𝓝 0) :=
    tendsto_id.rpow_const_nhds_zero (sub_pos.mpr hεη)
  have hev : ∀ᶠ δ : ℝ in 𝓝 0, δ ^ (η - ε) < (2 : ℝ) ^ (-p - η) :=
    hlim.eventually (gt_mem_nhds (Real.rpow_pos_of_pos (by norm_num) _))
  obtain ⟨d, hd, hbound⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨d, hd, fun δ u hδ hδd hu huδ => ?_⟩
  have hb := hbound (y := δ) (by simpa [Real.dist_eq, abs_of_pos hδ] using hδd)
  calc
    δ ^ (-p - ε) = δ ^ (-p - η) * δ ^ (η - ε) := by
      rw [← Real.rpow_add hδ]; congr 1; ring
    _ ≤ δ ^ (-p - η) * (2 : ℝ) ^ (-p - η) :=
      mul_le_mul_of_nonneg_left hb.le (Real.rpow_nonneg hδ.le _)
    _ = (2 * δ) ^ (-p - η) := by rw [Real.mul_rpow (by norm_num) hδ.le, mul_comm]
    _ ≤ u ^ (-p - η) := Real.rpow_le_rpow_of_nonpos hu huδ (by linarith)

/-- The still-missing local bridge can be restricted to dyadic scales. -/
def DyadicSmallCapGain (k : ℕ) (q t C R ζ : ℝ) : Prop :=
  ∃ ρ : ℝ, 0 < ρ ∧ ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧
    ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ N : ℕ, (1 / 2 : ℝ) ^ N < δ₀ →
    ∀ (μ : Measure (Point k)) (ν : Measure (Direction k)),
    Laws k q t R ζ ε ((1 / 2 : ℝ) ^ N) μ ν →
    ∀ (w₀ : Direction k) (E : Set (Point k × Direction k)),
    NullMeasurableSet E (μ.prod ν) → FiberCover k q C ε ((1 / 2 : ℝ) ^ N) E →
    (∀ u ∈ E, dist u.2 w₀ ≤ ρ) →
    (μ.prod ν) E ≤ ENNReal.ofReal (((1 / 2 : ℝ) ^ N) ^ c)

/-- Exact missing bridge type. In particular there is no assertion that the
endpoint's pair and triple budgets are automatic from the controlled node. -/
def DyadicSmallCapBridge : Prop :=
  ∀ (k : ℕ), 2 ≤ k → ∀ q t : ℝ,
    (k : ℝ) - 1 ≤ q → q ≤ (k : ℝ) - 1 / 2 →
    (k : ℝ) - 1 / 2 < t → t < (k : ℝ) →
    ∀ C : ℝ, 0 ≤ C → ∀ R : ℝ, 0 ≤ R →
    ∀ ζ : ℝ, (q = (k : ℝ) - 1 → 0 < ζ) → DyadicSmallCapGain k q t C R ζ

/-- Transfer all three ball/plate bounds to a larger comparable scale, using
only a comparison of the multiplicative loss. -/
theorem laws_change_scale {k : ℕ} {q t R ζ ε η δ u : ℝ}
    {μ : Measure (Point k)} {ν : Measure (Direction k)}
    (h : Laws k q t R ζ ε δ μ ν) (hu0 : 0 ≤ u) (hδu : δ ≤ u)
    (hK : δ ^ (-ε) ≤ u ^ (-η)) : Laws k q t R ζ η u μ ν := by
  obtain ⟨hm, hn, hs, ht, hq, hz⟩ := h
  refine ⟨hm, hn, hs, ?_, ?_, ?_⟩
  · intro x r hur hr
    exact (ht x r (hδu.trans hur) hr).trans
      (ENNReal.ofReal_le_ofReal (mul_le_mul_of_nonneg_right hK (Real.rpow_nonneg (hu0.trans hur) _)))
  · intro w r hur hr
    exact (hq w r (hδu.trans hur) hr).trans
      (ENNReal.ofReal_le_ofReal (mul_le_mul_of_nonneg_right hK (Real.rpow_nonneg (hu0.trans hur) _)))
  · intro he H hH r hur hr
    exact (hz he H hH r (hδu.trans hur) hr).trans
      (ENNReal.ofReal_le_ofReal (mul_le_mul_of_nonneg_right hK (Real.rpow_nonneg (hu0.trans hur) _)))

/-- Non-dyadic scales follow by rounding upward, reducing the allowed input loss,
and reducing the output gain. There is no change to the measures or relation. -/
theorem smallCapGain_of_dyadic {k : ℕ} {q t C R ζ : ℝ}
    (hq : 0 ≤ q) (hC : 0 ≤ C) (hlocal : DyadicSmallCapGain k q t C R ζ) :
    SmallCapGain k q t C R ζ := by
  obtain ⟨ρ, hρ, η, hη, c, hc, d₀, hd₀, hgain⟩ := hlocal
  obtain ⟨d₁, hd₁, hballs⟩ := input_scale_slack 0 η (η / 2) (by linarith) (by linarith)
  obtain ⟨d₂, hd₂, hcounts⟩ := input_scale_slack q η (η / 2) (by linarith) (by linarith)
  obtain ⟨d₃, hd₃, hout⟩ := absorb_finite_constant ((2 : ℝ) ^ c) c hc
  let d := min 1 (min (d₀ / 2) (min d₁ (min d₂ d₃)))
  have hd : 0 < d := lt_min (by norm_num)
    (lt_min (by positivity) (lt_min hd₁ (lt_min hd₂ hd₃)))
  refine ⟨ρ, hρ, η / 2, by linarith, c / 2, by linarith, d, hd, ?_⟩
  intro δ hδ hδd μ ν hlaws w₀ E hE hcover hcap
  have hδ₁ : δ < 1 := lt_of_lt_of_le hδd (min_le_left _ _)
  have hδrest : δ < min (d₀ / 2) (min d₁ (min d₂ d₃)) :=
    lt_of_lt_of_le hδd (min_le_right _ _)
  have hδ₀ : δ < d₀ / 2 := (lt_min_iff.mp hδrest).1
  have hδd₁ : δ < d₁ := (lt_min_iff.mp (lt_min_iff.mp hδrest).2).1
  have hδd₂ : δ < d₂ := (lt_min_iff.mp (lt_min_iff.mp (lt_min_iff.mp hδrest).2).2).1
  have hδd₃ : δ < d₃ := (lt_min_iff.mp (lt_min_iff.mp (lt_min_iff.mp hδrest).2).2).2
  obtain ⟨N, hNlow, hNhigh⟩ := exists_nat_pow_near_of_lt_one hδ hδ₁.le
    (by norm_num : (0 : ℝ) < 1 / 2) (by norm_num : (1 / 2 : ℝ) < 1)
  let u : ℝ := (1 / 2 : ℝ) ^ N
  have hu : 0 < u := pow_pos (by norm_num) _
  have hδu : δ ≤ u := hNhigh
  have huδ : u ≤ 2 * δ := by
    have : u * (1 / 2) < δ := by simpa [u, pow_succ] using hNlow
    linarith
  have hu₀ : u < d₀ := by linarith
  have hK : δ ^ (-(η / 2)) ≤ u ^ (-η) := by
    simpa using hballs δ u hδ hδd₁ hu huδ
  have hlaws' := laws_change_scale hlaws hu.le hδu hK
  have hcover' : FiberCover k q C η u E := by
    intro w
    obtain ⟨A, hA, hcov⟩ := hcover w
    refine ⟨A, hA.trans (hcounts δ u hδ hδd₂ hu huδ), ?_⟩
    intro x hx
    obtain ⟨a, ha, hxa⟩ := hcov x hx
    exact ⟨a, ha, hxa.trans (mul_le_mul_of_nonneg_left hδu hC)⟩
  calc
    (μ.prod ν) E ≤ ENNReal.ofReal (u ^ c) := hgain N hu₀ μ ν hlaws' w₀ E hE hcover' hcap
    _ ≤ ENNReal.ofReal ((2 : ℝ) ^ c * δ ^ c) := by
      apply ENNReal.ofReal_le_ofReal
      rw [← Real.mul_rpow (by norm_num) hδ.le]
      exact Real.rpow_le_rpow hu.le huδ hc.le
    _ ≤ ENNReal.ofReal (δ ^ (c / 2)) := ENNReal.ofReal_le_ofReal (hout δ hδ hδd₃)

/-- An arbitrary finite cover of a bounded fiber can be replaced, with no
cardinality increase, by anchors in the fiber itself. This does not assert a
measurable choice of these covers as the direction varies. -/
theorem bounded_fiber_anchors {k : ℕ} {q C R ε δ : ℝ}
    {E : Set (Point k × Direction k)}
    (hE : ∀ u ∈ E, ‖u.1‖ ≤ R) (hcover : FiberCover k q C ε δ E) :
    ∀ w : Direction k, ∃ A : Finset (Point k),
      (A.card : ℝ) ≤ δ ^ (-q - ε) ∧ (∀ a ∈ A, ‖a‖ ≤ R) ∧
      ∀ x : Point k, (x, w) ∈ E → ∃ a ∈ A,
        ‖(ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto (x - a)‖ ≤ (2 * C) * δ := by
  classical
  intro w
  obtain ⟨A, hA, hcov⟩ := hcover w
  let P := (ℝ ∙ (w : Point k))ᗮ.orthogonalProjectionOnto
  let I := A.filter (fun a => ∃ y : Point k, (y, w) ∈ E ∧ ‖P (y - a)‖ ≤ C * δ)
  have hex (a : {a // a ∈ I}) :
      ∃ y : Point k, (y, w) ∈ E ∧ ‖P (y - a.val)‖ ≤ C * δ :=
    (Finset.mem_filter.mp a.property).2
  choose y hy using hex
  let A' := I.attach.image y
  have hcard : A'.card ≤ A.card := calc
    A'.card ≤ I.attach.card := Finset.card_image_le
    _ = I.card := Finset.card_attach
    _ ≤ A.card := Finset.card_le_card (Finset.filter_subset _ _)
  have hcardR : (A'.card : ℝ) ≤ A.card := by exact_mod_cast hcard
  refine ⟨A', hcardR.trans hA, ?_, ?_⟩
  · intro a ha
    obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp ha
    exact hE (y i, w) (hy i).1
  · intro x hx
    obtain ⟨a, ha, hxa⟩ := hcov x hx
    have haI : a ∈ I := Finset.mem_filter.mpr ⟨ha, x, hx, hxa⟩
    let i : {a // a ∈ I} := ⟨a, haI⟩
    refine ⟨y i, Finset.mem_image.mpr ⟨i, Finset.mem_attach _ _, rfl⟩, ?_⟩
    simpa [mul_assoc] using reanchor_tube w x (y i) a hxa (hy i).2

/-- The two port estimates, followed by finite spatial localization, close
    the dyadic bridge. The resulting estimate is uniform over all directions. -/
theorem missing_dyadic_small_cap_bridge : DyadicSmallCapBridge := by
  intro k hk q t hq hq' ht ht' C hC R _hR ζ hζ
  obtain ⟨ε, hε, c, hc, d, hd, hg⟩ := bounded_dyadic_gain (R := R)
    (unit_dyadic_gain k hk q t hq hq' ht ht' C hC ζ hζ)
  exact ⟨1, by norm_num, ε, hε, c, hc, d, hd,
    fun N hN μ ν hl _w₀ E hE hcov _hcap => hg N hN μ ν hl E hE hcov⟩

end OAI.Falconer.LinearProjectionGainPartial

open Set MeasureTheory
open scoped ENNReal InnerProductSpace
open OAI.Falconer.LinearProjectionGainPartial

theorem solution_of_bridge
    (bridge : OAI.Falconer.LinearProjectionGainPartial.DyadicSmallCapBridge)
    (k : ℕ) (hk : 2 ≤ k) (q t : ℝ)
    (hq : (k : ℝ) - 1 ≤ q) (hq' : q ≤ (k : ℝ) - 1 / 2)
    (ht : (k : ℝ) - 1 / 2 < t) (ht' : t < (k : ℝ))
    (C : ℝ) (hC : 0 ≤ C) (R : ℝ) (hR : 0 ≤ R)
    (ζ : ℝ) (hζ : q = (k : ℝ) - 1 → 0 < ζ) :
    ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
      ∀ δ : ℝ, 0 < δ → δ < δ₀ →
      ∀ (μ : Measure (EuclideanSpace ℝ (Fin (k + 1))))
        (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1)),
      μ univ ≤ 1 → ν univ ≤ 1 →
      (∀ᵐ x ∂μ, ‖x‖ ≤ R) →
      (∀ x : EuclideanSpace ℝ (Fin (k + 1)), ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        μ (Metric.ball x r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ t)) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν (Metric.ball w r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ q)) →
      (q = (k : ℝ) - 1 →
        ∀ H : Submodule ℝ (EuclideanSpace ℝ (Fin (k + 1))),
        Module.finrank ℝ H = k → ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | Metric.infDist (w : EuclideanSpace ℝ (Fin (k + 1))) (H : Set _) ≤ r}
          ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ ζ)) →
      ∀ E : Set (EuclideanSpace ℝ (Fin (k + 1)) ×
        Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1),
      NullMeasurableSet E (μ.prod ν) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∃ A : Finset (EuclideanSpace ℝ (Fin (k + 1))),
          (A.card : ℝ) ≤ δ ^ (-q - ε) ∧
          ∀ x : EuclideanSpace ℝ (Fin (k + 1)), (x, w) ∈ E →
            ∃ a ∈ A,
              ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin (k + 1))))ᗮ.orthogonalProjectionOnto
                (x - a)‖ ≤ C * δ) →
      (μ.prod ν) E ≤ ENNReal.ofReal (δ ^ c) := by
  have hq0 : 0 ≤ q := by
    have hk0 : (2 : ℝ) ≤ k := by exact_mod_cast hk
    linarith
  have hcap := smallCapGain_of_dyadic hq0 hC
    (bridge k hk q t hq hq' ht ht' C hC R hR ζ hζ)
  obtain ⟨ε, hε, c, hc, δ₀, hδ₀, hgain⟩ := global_of_smallCapGain hcap
  refine ⟨ε, hε, c, hc, δ₀, hδ₀, ?_⟩
  intro δ hδ hδsmall μ ν hμ hν hs hμball hνball hplate E hE hcover
  exact hgain δ hδ hδsmall μ ν ⟨hμ, hν, hs, hμball, hνball, hplate⟩ E hE hcover


theorem solution
    (k : ℕ) (hk : 2 ≤ k) (q t : ℝ)
    (hq : (k : ℝ) - 1 ≤ q) (hq' : q ≤ (k : ℝ) - 1 / 2)
    (ht : (k : ℝ) - 1 / 2 < t) (ht' : t < (k : ℝ))
    (C : ℝ) (hC : 0 ≤ C) (R : ℝ) (hR : 0 ≤ R)
    (ζ : ℝ) (hζ : q = (k : ℝ) - 1 → 0 < ζ) :
    ∃ ε : ℝ, 0 < ε ∧ ∃ c : ℝ, 0 < c ∧ ∃ δ₀ : ℝ, 0 < δ₀ ∧
      ∀ δ : ℝ, 0 < δ → δ < δ₀ →
      ∀ (μ : Measure (EuclideanSpace ℝ (Fin (k + 1))))
        (ν : Measure (Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1)),
      μ univ ≤ 1 → ν univ ≤ 1 →
      (∀ᵐ x ∂μ, ‖x‖ ≤ R) →
      (∀ x : EuclideanSpace ℝ (Fin (k + 1)), ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        μ (Metric.ball x r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ t)) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν (Metric.ball w r) ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ q)) →
      (q = (k : ℝ) - 1 →
        ∀ H : Submodule ℝ (EuclideanSpace ℝ (Fin (k + 1))),
        Module.finrank ℝ H = k → ∀ r : ℝ, δ ≤ r → r ≤ 1 →
        ν {w | Metric.infDist (w : EuclideanSpace ℝ (Fin (k + 1))) (H : Set _) ≤ r}
          ≤ ENNReal.ofReal (δ ^ (-ε) * r ^ ζ)) →
      ∀ E : Set (EuclideanSpace ℝ (Fin (k + 1)) ×
        Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1),
      NullMeasurableSet E (μ.prod ν) →
      (∀ w : Metric.sphere (0 : EuclideanSpace ℝ (Fin (k + 1))) 1,
        ∃ A : Finset (EuclideanSpace ℝ (Fin (k + 1))),
          (A.card : ℝ) ≤ δ ^ (-q - ε) ∧
          ∀ x : EuclideanSpace ℝ (Fin (k + 1)), (x, w) ∈ E →
            ∃ a ∈ A,
              ‖(ℝ ∙ (w : EuclideanSpace ℝ (Fin (k + 1))))ᗮ.orthogonalProjectionOnto
                (x - a)‖ ≤ C * δ) →
      (μ.prod ν) E ≤ ENNReal.ofReal (δ ^ c) := by
  exact solution_of_bridge missing_dyadic_small_cap_bridge k hk q t hq hq' ht ht' C hC R hR ζ hζ
```