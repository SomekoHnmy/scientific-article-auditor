# Planted errors — answer key

Defects were planted in `article.md` and `supplement.md`. Counting one record per disagreement, they form **15 records** in `benchmark_demo.csv`. Line numbers refer to the markdown files
as committed; `S:` prefixes `supplement.md`.

| ID | Domain | Category | Sites | Where | What is wrong |
| --- | --- | --- | --- | --- | --- |
| E01 | A | Contradictory values for the same quantity | 3 | L21, L105, L121 | Total visits 48,712 in the abstract, 48,217 in Results and Table 2 |
| E02 | A | Numerator/denominator vs percentage | 3 | L134, S:L43, S:L47–52 | 18,432/31,205 = 59.1%, printed as 62.1%; the supplement caption carries the correct value |
| E03 | A | Contradictory values for the same quantity | 3 | L48, L103, L115 | 20 hospitals in the text twice, Table 1 totals 19 (5+5+5+4) |
| E04 | A | Point estimate outside its own interval | 2 | L128, L21 | −8.4 with CI −7.9 to −3.2, printed in both places |
| E05 | A | Significance statement vs p-value | 2 | L132, L21 | "significantly reduced", CI −9.1 to 0.3, p = 0.08 |
| E06 | A | Contradictory study design designation | 3 | L1, L19, L48 | Stepped-wedge in the title and abstract, parallel-group in the Methods |
| E07 | A | Contradictory recruitment period | 3 | L19, L68, L74 | To March 2024, to September 2024, extraction to 31 March 2024 |
| E08 | A | Contradictory eligibility criteria | 2 | L68, L93 | Aged 16+ vs adults 18+ |
| E09 | A | Primary outcome designated differently | 2 | L19, L87 | Waiting time vs chart open-to-close time |
| E10 | B | Axis values vs distance along the axis | 1 | S:L31–37 | Ticks 0,10,20,40,80 at equal spacing, axis labelled linear |
| E11 | B | Printed value vs its own plotted position | 1 | S:L51 | H11 printed 41%, bar ends below the 40% gridline |
| E12 | C | Nonsignificant primary acknowledged, other significant results emphasised | 1 | L23, L169 | Conclusion recommends adoption |
| E13 | D | Identifier–record mismatch | 2 | L188 | Reference 4 DOI resolves to an unrelated paper |
| E14 | D | Bibliographic field error | 2 | L190 | Reference 6 year and page range disagree with the record |
| E15 | D | Non-existent reference | 2 | L192 | Reference 8 title matches no catalogue record |

## What the counting rule does here

Under the earlier pair rule these same defects produced 20 records: the visit total split into
abstract–Results and abstract–Table, the broken interval split into abstract and Results, and so
on. Counting one record per disagreement gives 9 Domain A records carrying 19 conflicting pairs
between them, and the pairs remain computable from the recorded sites.

E02 shows why the change matters beyond bookkeeping. The printed 62.1% disagrees with its own
numerator and denominator *and* with the supplementary caption, which carries the arithmetically
correct 59.1%. Under the pair rule these were two records in two different places in the file, one
classified as an arithmetic error and one as a text–figure discrepancy, and nothing connected
them. As one record with three sites the shape of the mistake is visible: a single wrong number,
with the correct value printed elsewhere in the same paper.

## Domain assignment

E02 involves a figure caption but is Domain A, because establishing it requires comparing the
caption against the body text. E10 and E11 are Domain B because each is determinable from the
graphic alone.

## Records that are not simply "confirmed"

`E07` shows a disagreement that survived discussion. HS read the abstract's dates as describing
activation months rather than the recruitment window and judged it not a finding; KA judged it a
genuine discrepancy; discussion did not resolve it; YK decided. All four steps are in the row.

`E08` shows a record judged by one rater only, with `resolved_status = pending_second_rater`.

`E11` carries `provenance = low_cost_configuration` and `E14` carries `human_review`, so that
all but one of the provenance values appear in the file. `source_reported` does not appear
because this is a main-study article, for which no prior report exists.

## A known inconsistency, left in place

E12 (spin) was recorded on the basis of the abstract's designation of the primary outcome
(waiting time, p = 0.08). The protocol has since acquired a rule for contested primary outcomes:
the Methods designation governs. The Methods names chart open-to-close time, which is reported as
significant, so under the current rule this article would be **not assessable** for spin and E12
would not exist.

The demo is left as it stands because the dependency is worth seeing: whether an article is
eligible for spin assessment can turn on a Domain A defect recorded elsewhere in the same file
(E09).
