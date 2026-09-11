# Data dictionary — `benchmark_demo.csv`

One row per error record. 55 columns. Categorical columns are closed vocabularies: a value
outside the listed set is a schema violation.

## The counting unit

A record is **one disagreement** — the set of occurrences reporting the same quantity, or
asserting the same attribute, that do not agree with one another — not one pair of locations. A
value mistyped once and repeated in the abstract, the main text and a table is one record with
three sites, not three records. The set is established at adjudication against the version of
record; no automatic index is treated as authoritative.

This is the decision that shapes the whole file. Counting by location pairs makes the number of
records depend on how often an article repeats a quantity rather than on how many mistakes it
contains, and it discards the grouping irreversibly: a pairwise count can be computed from a site
list, but a site list cannot be recovered from pairs. Domain A in this demo has 9 records carrying,
between them, 19 conflicting pairs derived from the recorded sites.

## Article identity and characteristics

Repeated on every row belonging to the same article. A validation check should confirm that rows
sharing an `article_id` carry identical values here.

| Column | Type | Values / notes |
| --- | --- | --- |
| `article_id` | key | Stable internal identifier. |
| `pmid`, `doi`, `pmc_id` | text | Empty if not available. `pmc_id` is populated for Stratum 2 and is what the PDF versus PMC XML sub-analysis keys on. |
| `journal`, `issn` | text | As printed. |
| `pub_year`, `pub_month` | integer | Of the version of record. `pub_month` is left empty unless eligibility turns on it, as it can for an article published online in one year and in an issue the next. |
| `title` | text | As printed. |
| `authors` | text | `Family, Given; Family, Given` — Rayyan's convention. |
| `volume`, `issue`, `pages` | text | Of this article. The same three fields appear among the disagreeing fields recorded for a `citation_error`, where they describe a *reference* rather than the article itself. |
| `publisher` | text | Publisher of the version of record. |
| `language` | text | ISO 639-2 code. Non-English articles are excluded, so this should be `eng` throughout; it is recorded so that the exclusion is auditable rather than assumed. |
| `article_type` | **categorical** | `rct` · `cluster_rct` · `systematic_review` · `meta_analysis` · `cohort` · `case_control` · `cross_sectional` · `diagnostic_accuracy` · `other` |
| `collection` | **categorical** | `benchmark` (125-article development set) · `pilot` (20 stage-2 articles) · `main_study` (300-article main sample) |
| `stratum` | **categorical** | `1` · `2` · empty for benchmark articles, which come from neither stratum |
| `n_references` | integer | All entries in the reference list. |
| `n_references_checkable` | integer | Entries carrying a resolvable PubMed identifier or DOI. Denominator for the citation-error proportion; the difference from `n_references` is the not-checkable count the protocol requires to be reported alongside. |

These column names follow Rayyan's CSV import format, so a bibliographic export from a reference
manager or from Rayyan itself can be mapped onto them field by field without renaming. Rayyan's
`abstract` and `keywords` are omitted: they carry no benchmark information and would multiply the
size of the file. Rayyan's `location` is also omitted, as it means publisher location and would
collide with `siteN_location`.

## Record identity

| Column | Type | Values / notes |
| --- | --- | --- |
| `record_id` | key | Never reused, never renumbered. |
| `domain` | **categorical** | `internal_reporting_discrepancy` · `graphical_error` · `spin` · `citation_error` |
| `taxonomy_category` | **categorical** | Verbatim from Appendix 3 of the protocol. |
| `provenance` | **categorical** | Who first identified it — see below. |
| `source_report_id` | text | Which published report described it. Populated only when `provenance = source_reported`. |
| `detection_run_id` | text | Which run raised the flag. Empty for `source_reported` and `human_review`. |
| `n_sites` | integer | Number of populated site slots. Must equal the count of non-empty `siteN_location`. |
| `sites_truncated` | boolean | `TRUE` when the disagreement involves more locations than the six slots hold; the overflow is then listed in `note`. |

### `provenance`

| Value | Meaning |
| --- | --- |
| `source_reported` | Described in a published report before this study began. Benchmark articles only. These records are public **together with their labels**, so contamination of model training data cannot be excluded and performance on them should be reported separately. |
| `full_pipeline` | First raised by the full detection pipeline and confirmed on adjudication. |
| `low_cost_configuration` | First raised by a lower-cost configuration and missed by the full pipeline. Kept distinct because these records enter the reference standard after it was first assembled. |
| `human_review` | First identified by a rater who noticed it while adjudicating a different flag. |

## Sites — where the defect is

Six slots. Unused slots are empty. Arity is a property of the record and is constrained by domain:

| Domain | Permitted `n_sites` |
| --- | --- |
| `internal_reporting_discrepancy` | 2 or more |
| `graphical_error` | exactly 1 |
| `spin` | exactly 1 |
| `citation_error` | 2, or 3 when a PubMed identifier and a DOI in the same entry resolve to different publications |

A validation script should enforce this. A generic six-slot layout otherwise invites the reading
that any record may be folded into up to six locations, which is true only for Domain A.

What a site *is* follows from `domain` and, for citation errors, from position. There is no role
column: for Domain A every site is one of the disagreeing occurrences and none is privileged,
since which of them is wrong is usually not determinable; Domain B has the graphic; Domain C has
the article. For `citation_error`, **site 1 is always the entry as printed and sites 2 and 3 are
the records retrieved for its identifiers** — the only case where sites differ in kind, and
position carries it.

| Column | Type | Values / notes |
| --- | --- | --- |
| `siteN_location` | text | Where in the document; for a retrieved record, which catalogue. Markdown line numbers stand in here for page and bounding box. |
| `siteN_quote` | text | The content **as printed**, and nothing else, separated by semicolons where a site carries several printed items. Never empty. For a graphic this is the text printed in it — axis title, tick labels, data labels, legend — not a description of what the graphic looks like; the geometry that makes it an error (equal spacing, a bar ending short of its label) is an observation and belongs in `note`. For a retrieved record it is the record the catalogue returned. Keeping quotation and explanation apart is what allows automatic matching against a pipeline flag. |

## Adjudication

Each rater's independent judgement is recorded before any resolution. During collection the two
raters enter judgements separately so that neither sees the other's; the merged result appears here.

| Column | Type | Values / notes |
| --- | --- | --- |
| `rater1`, `rater2` | text | Initials. Empty when that judgement has not been made. |
| `raterN_decision` | **categorical** | `confirmed` · `not_a_finding` · `rounding_sensitive` |
| `raterN_severity` | **categorical** | `minor` · `major` · `not_graded` (spin) · empty when not confirmed |
| `raterN_reason` | **categorical** | Only when the decision is `not_a_finding`: `rounding_compatible` · `extraction_error` · `parsing_error` · `ocr_error` · `representation_error` · `unit_conversion` · `omission_misread` · `misread_table_structure` · `out_of_scope_document` · `other` |
| `discussion_outcome` | **categorical** | `resolved` · `unresolved` · empty when the raters agreed |
| `third_rater` | text | Initials. Only when discussion did not resolve the disagreement. |
| `third_rater_decision`, `third_rater_reason` | **categorical** | Same sets as the rater columns. |

## Resolution

| Column | Type | Values / notes |
| --- | --- | --- |
| `resolved_status` | **categorical** | `candidate` · `pending_second_rater` · `confirmed` · `not_a_finding` · `rounding_sensitive`. **Derived** from the adjudication columns and recomputable from them. |
| `resolved_severity` | **categorical** | `minor` · `major` · `not_graded` · empty |
| `note` | text | Reasoning, arithmetic, overflow sites. Never the quoted content itself. |

## Scoring a detector against this file

Because sites are recorded rather than decomposed, two sensitivity definitions are available and
both are reported in the protocol:

- **lenient** — the configuration flags the discrepancy at any recorded site
- **strict** — the configuration flags every recorded site

The two coincide outside Domain A, whose findings are the only ones occupying more than one
location in the article itself.

## What this file does not carry

`coverage_demo.csv` records what was examined. A domain examined and found clean produces no row
here, and silence would otherwise be ambiguous between "clean" and "never looked at".

## A note on matching detector output to these records

There is no occurrence identifier. Matching is on `siteN_location` and `siteN_quote`. This is
deliberate: an identifier minted by this study's pipeline means nothing to anyone else's detector,
so a benchmark that relied on it would be usable only from inside this project. Location and
verbatim quotation are portable.
