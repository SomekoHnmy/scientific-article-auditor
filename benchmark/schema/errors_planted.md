# Planted errors — answer key

Defects were planted in `article.md` and `supplement.md`. Counting one record per disagreement, they form **16
records** (E01–E16) for the article `DEMO-EHR-01` in `records_demo.csv`. Records E17 and E18 belong to stub articles
with no full text and are explained at the end. Line numbers refer to the markdown files as committed; `S:`
prefixes `supplement.md`.

| ID | Domain | Code | Category | Sites | Where | What is wrong |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | A | A01 | Contradictory values for the same quantity | 3 | L21, L105, L121 | Total visits 48,712 in the abstract, 48,217 in Results and Table 2 |
| E02 | A | A02 | Numerator/denominator vs percentage | 2 | L134, S:L43 | 18,432/31,205 = 59.1%, printed as 62.1%; the supplement caption carries the correct value |
| E03 | A | A01 | Contradictory values for the same quantity | 3 | L48, L103, L115 | 20 hospitals in the text, Table 1 totals 19 (5+5+5+4) |
| E04 | A | A04 | Point estimate outside its own interval | 2 | L128, L21 | −8.4 with CI −7.9 to −3.2, printed in both places |
| E05 | A | A05 | Significance statement vs p-value | 2 | L132, L21 | "significantly reduced", CI −9.1 to 0.3, p = 0.08 |
| E06 | A | A13 | Contradictory study design designation | 3 | L1, L19, L48 | Stepped-wedge in the title and abstract, parallel-group in the Methods |
| E07 | A | A14 | Contradictory recruitment period | 3 | L19, L68, L73–74 | To March 2024, to September 2024, extraction to 31 March 2024 |
| E08 | A | A15 | Contradictory eligibility criteria | 2 | L68, L93 | Aged 16+ vs adults 18+ |
| E09 | A | A18 | Primary outcome designated differently | 2 | L19, L87 | Waiting time vs chart open-to-close time |
| E10 | B | B02 | Axis values vs distance along the axis | 1 | S:L21–31 | Ticks 0,10,20,40,80 at equal spacing, axis labelled linear |
| E11 | B | B03 | Printed value vs its own plotted position | 1 | S:L50 | H11 printed 41%, bar ends below the 40% gridline |
| E12 | C | C04 | Nonsignificant primary acknowledged, other significant results emphasised | 2 | L23, L181 | Conclusion recommends adoption, in the abstract and the Discussion |
| E13 | D | D03 | Identifier–record mismatch | 2 | L188 | Reference 4 DOI resolves to an unrelated paper |
| E14 | D | D04 | Bibliographic field error | 2 | L190 | Reference 6 year and page range disagree with the record |
| E15 | D | D01 | Non-existent reference | 2 | L192 | Reference 8 title matches no catalogue record |
| E16 | A | A06 | Fractional count of an indivisible unit | 1 | L80 | 214.5 encounters |

## What the counting rule does here

Under the earlier pair rule these defects produced more records than there are mistakes: the visit total split into
abstract–Results and abstract–Table, the broken interval split into abstract and Results, and so on. Counting one
record per disagreement keeps one record per mistake, and the pairs remain computable from the recorded sites.

E02 shows why the change matters beyond bookkeeping. The printed 62.1% disagrees with its own numerator and
denominator *and* with the supplementary caption, which carries the arithmetically correct 59.1%. As one record with
two sites the shape of the mistake is visible: a single wrong number, with the correct value printed elsewhere.

E16 shows the other side of the rule. A fractional count of encounters is wrong on its face, so the record has one
site and there is no second location to invent.

## Domain assignment

E02 involves a figure caption but is Domain A, because establishing it requires comparing the caption against the
body text. E10 and E11 are Domain B because each is determinable from the graphic alone.

## Adjudication paths

| Record | Path |
| --- | --- |
| most | Both raters agree; resolved directly. |
| E03 | Both confirmed, severity differed (major vs minor); discussion agreed on major (`consensus_*`). |
| E09 | Decisions differed (confirmed vs not a finding); discussion agreed it is a finding (`consensus_*`). |
| E07 | Decisions differed and discussion did not resolve it; the third rater decided (`third_rater_*`). |
| E08 | One rater only: `pending_second_rater`. |
| E17 | Both raters rejected it as rounding-compatible: `not_a_finding`. |
| E18 | A `source_reported` record: HS checked it against the version of record and rater 2 verified the judgement. |

`E11` carries `provenance = low_cost_configuration`, `E14` carries `human_review`, and `E18` carries
`source_reported`, so every provenance value appears.

## Stub articles

`articles_demo.csv` also holds three articles without full text, so that the articles file can show what a
records file cannot:

- `DEMO-STUB-02` raised no flag and has no record, but still counts in every article denominator. Its trial protocol
  and statistical analysis plan were removed before processing (`removed_supplements`), and it is not assessable
  for spin.
- `DEMO-STUB-03` has one record, E17, judged not a finding, so the article does not meet the target condition. It is
  assessable for spin and spin is absent.
- `DEMO-BENCH-04` is a benchmark article contributed by the fictional source report `SR-DEMO-01`, which compared
  abstracts with full texts only. Its spin assessment is still pending.

## A known inconsistency, left in place

E12 (spin) was recorded on the basis of the abstract's designation of the primary outcome (waiting time, p = 0.08),
and `DEMO-EHR-01` is marked assessable on the same basis. The protocol's rule for contested primary outcomes is that
the Methods designation governs. The Methods names chart open-to-close time, which is reported as significant, so
under that rule this article would be **not assessable** for spin and E12 would not exist.

The demo is left as it stands because the dependency is worth seeing: whether an article is eligible for spin
assessment can turn on a Domain A defect recorded elsewhere in the same file (E09).
