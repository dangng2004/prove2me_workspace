You are given a proof of a statement, in LaTeX. It is the original proof from the paper.

Write a new proof of the statement that is clearer and more legible than the given proof, judged by the rubric below.

Rules:

- Your proof must be correct and complete. It may cite only results stated in the provided context.
- Do not simply polish the wording. Rethink the exposition: improve its structure, overview, explanations and local justifications wherever that makes the proof simpler, clearer or more rigorous.
- You may restructure freely: add an overview, split the proof into claims, reorder steps, rename notation, or remove material that does not help the reader.
- Write in ordinary mathematical prose for a research mathematician.

Output exactly two blocks:

<proof>
The LaTeX proof, starting with `\begin{proof}` and ending with `\end{proof}`. You may put short lemma statements or a one-paragraph overview before it. Do not mention the source proof in this block.
</proof>
<notes>
A short list of what you changed and why.
</notes>
