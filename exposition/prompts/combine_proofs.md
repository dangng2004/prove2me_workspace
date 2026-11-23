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
