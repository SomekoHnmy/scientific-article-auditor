# scientific-article-auditor

Large language model–based auditing of published medical research articles for **within-article reporting defects**: internal reporting discrepancies, graphical errors, spin, and citation errors.

> **Status: protocol stage.** This repository holds the prespecified study protocol and a synthetic demonstration of the benchmark schema. No detection code, results, or annotations of real articles have been released yet. Amendments to the protocol are recorded in the commit history with their dates.

## Contents

| Path | What it is |
| --- | --- |
| [`protocol/protocol.md`](protocol/protocol.md) | Study protocol |
| [`protocol/protocol-full.md`](protocol/protocol-full.md) | Full protocol, expanding the Background and Methods |
| `protocol/references.bib`, `protocol/vancouver.csl` | Bibliography and citation style |
| [`protocol/figures/`](protocol/figures/) | Study workflow figure and its draw.io source |
| [`protocol/build.py`](protocol/build.py) | Builds Word versions of the protocol |
| `protocol/reference.docx` | Word styles and page setup used by the build |
| [`prompt/base_prompt.txt`](prompt/base_prompt.txt) | Base detection prompt (Appendix 2 of the protocol) |
| [`benchmark/schema/`](benchmark/schema/) | Synthetic article with planted errors, showing how findings are recorded |

## Building the protocol

```sh
python protocol/build.py
```

This needs pandoc 3 on `PATH`, or its location in the `PANDOC` environment variable. It writes `protocol.docx` and `protocol-full.docx` to `protocol/build/`, which is not tracked. It stops if `prompt/base_prompt.txt` no longer matches Appendix 2 of the protocol.

## Benchmark schema demonstration

The article, supplement, journal, authors, identifiers, and references in [`benchmark/schema/`](benchmark/schema/) are **entirely fictional**. Errors were planted in them deliberately so that the schema can be shown on concrete cases; nothing there describes real research.

- [`data_dictionary.md`](benchmark/schema/data_dictionary.md) — every table and column, with permitted values, and the detection log released with the study manuscript
- [`articles_demo.csv`](benchmark/schema/articles_demo.csv) — one row per article, including articles with no record
- [`records_demo.csv`](benchmark/schema/records_demo.csv) — one row per error record
- [`source_reports_demo.csv`](benchmark/schema/source_reports_demo.csv) — the published reports benchmark records come from, and what each examined
- [`errors_planted.md`](benchmark/schema/errors_planted.md) — the answer key

The benchmark and main-study article lists described in Appendix 4 of the protocol will be added under `benchmark/`. Full texts of the articles will not be redistributed; each article is identified by its PubMed identifier and digital object identifier.

## Licence

- Protocol text, figures, prompt, and data: [CC BY 4.0](LICENSE).
- Code, currently `protocol/build.py`: [MIT](LICENSE-CODE).
- `protocol/vancouver.csl` comes from the Citation Style Language project and remains under CC BY-SA 3.0.

## Authors

Hidehiro Someko, Keisuke Anan, Yuki Kataoka
