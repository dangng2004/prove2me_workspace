You are given a Lean 4 formalization of a mathematical result and the result's statement in the paper it comes from. Write the proof that the Lean code carries out as an informal proof in LaTeX, the way it would appear in a mathematics paper.

Rules:

- Follow the Lean proof's own route: the same constructions, the same order of steps, the same case splits and the same intermediate claims. Do not substitute a different or better argument, and do not import ideas from the paper's proof that the Lean proof does not use.
- Results that the Lean file imports without proof (theorems it uses as black boxes) should be stated briefly and cited as lemmas, as a paper cites earlier results. Helper lemmas proved inside the file should be proved if they carry mathematical content, and summarized in a sentence if they are routine bookkeeping.
- Leave out Lean-specific matters (coercions, casts, `ENNReal` versus real arithmetic, measurability side conditions that are automatic in ordinary mathematics) unless they correspond to a genuine mathematical point.
- Write ordinary mathematical prose. Do not mention Lean, tactics, or names of Lean declarations.

Output only the LaTeX body of the proof, starting with `\begin{proof}` and ending with `\end{proof}`, preceded if needed by short `\begin{lemma}...\end{lemma}` statements of the cited black-box results. Use only standard LaTeX and amsmath macros.
