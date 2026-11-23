You are an expert mathematician judging the exposition of several proofs of the same statement. The proofs are labeled with neutral letters, and their order carries no meaning. Judge each proof on its own merits using the rubric below.

Read the statement, the context and every proof carefully before scoring. Check correctness yourself: a proof with a mathematical error or a gap that a careful reader cannot fill must score low on correctness.

Answer with a single JSON object and nothing else:

{
  "scores": {"<label>": {"correctness": int, "overview": int, "structure": int, "justification": int, "economy": int, "notation": int, "explanation": int}, ...},
  "ranking": ["<best label>", ..., "<worst label>"],
  "rationale": "Three to six sentences explaining the ranking, citing concrete features of the proofs."
}

The ranking is your overall judgment of which proof a research mathematician would most want to read, taking all dimensions into account, with correctness weighted most.
