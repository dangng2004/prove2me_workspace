# Proof exposition pipeline

Turns several formal (Lean) proofs of the same statement into readable informal proofs, combines them into one, and has LLM judges rank all versions blind. Re-formalizations from [agent mode](../references/agent_mode.md) feed this pipeline: every theorem with two or more formalizations is a candidate.

```
Lean proofs ──extract──► informal versions ──combine──► combined proof
                                 │                            │
                                 └──────────── judge ◄────────┘  (blind ranking)
```

| Path | Contents |
|---|---|
| `scripts/proof_exposition.py` | `extract`, `combine`, `judge`, `table` subcommands (headless Codex / Claude) |
| `prompts/` | Prompts for each step, plus the exposition rubric the judges use |
| `lean/` | Lean sources the informal versions were extracted from |
| `results/exposition/<statement>/` | `statement.tex`, `context.tex`, `versions/*.tex`, judge outputs, ranking tables, logs |
| `pdf/` | `build_pdf.py` and the rendered original / rewrite / combined proofs |

Worked examples: Theorem 4.1 (`linear_projection_gain`) and Lemma 5.2 (`contact_interval`).

```bash
python3 exposition/scripts/proof_exposition.py --help
```
