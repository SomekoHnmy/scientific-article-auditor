# Data dictionary — benchmark schema

Categorical columns are closed vocabularies: a value outside the listed set is a schema violation.

## Files

| File | One row per | Released |
| --- | --- | --- |
| `articles_demo.csv` | article in any collection, whether or not anything was found in it | yes |
| `records_demo.csv` | error record (a finding, or a flag judged not to be one) | yes |
| `source_reports_demo.csv` | published report that contributed benchmark records | yes |
| detection log: `runs`, `flags`, `configurations`, `prices` | see [Detection log](#detection-log) | with the study manuscript; kept locally until then |

Articles and records are joined on `article_id`; records and source reports on `source_report_id`. For release,
records are also written out as a single flat file with the article columns repeated on every record, so that it
can be read without joining. The articles file is released alongside it, because an article with no record is
absent from the flat file but still belongs in every article denominator.

The demo documents are `demo_fictitious_article.md` and `demo_fictitious_supplement.md`. `DEMO-EHR-01` is the
only article with a full text; the other articles and records E17–E18 are stubs that show table structure only.

## The counting unit

A record is **one disagreement** — the set of occurrences reporting the same quantity, or asserting the same
attribute, that do not agree with one another — not one pair of locations. A value mistyped once and repeated in
the abstract, the main text and a table is one record with three sites, not three records. The set is established
at adjudication against the version of record; no automatic index is treated as authoritative.

Some internal reporting discrepancies are established by a single statement that contradicts the definition of what
it reports, such as a fractional count of patients or a proportion above 100%. Such a record has one site. A
statement whose parts contradict each other within one sentence or one table cell, such as a point estimate outside
the interval printed beside it, is also one site.

Counting by location pairs would make the number of records depend on how often an article repeats a quantity
rather than on how many mistakes it contains, and it discards the grouping irreversibly: a pairwise count can be
computed from a site list, but a site list cannot be recovered from pairs.

## Articles

| Column | Type | Values / notes |
| --- | --- | --- |
| `article_id` | key | Stable internal identifier. |
| `pmid`, `doi`, `pmc_id` | text | Empty if not available. `pmc_id` is populated for Stratum 2 and is what the PDF versus PMC XML sub-analysis keys on. |
| `journal`, `issn` | text | As printed. |
| `pub_year`, `pub_month` | integer | Of the version of record. `pub_month` is left empty unless eligibility turns on it. |
| `title` | text | As printed. |
| `authors` | text | `Family, Given; Family, Given` — Rayyan's convention. |
| `volume`, `issue`, `pages` | text | Of this article. |
| `publisher` | text | Publisher of the version of record. |
| `language` | text | ISO 639-2 code. Non-English articles are excluded, so this should be `eng` throughout; it is recorded so that the exclusion is auditable. |
| `article_type` | **categorical** | `rct` · `cluster_rct` · `systematic_review` · `meta_analysis` · `cohort` · `case_control` · `cross_sectional` · `diagnostic_accuracy` · `other` |
| `collection` | **categorical** | `benchmark` (124-article development set) · `pilot` (20 stage-2 articles) · `main_study` (300-article main sample) |
| `stratum` | **categorical** | `1` · `2` · empty for benchmark articles, which come from neither stratum |
| `n_supplement_files` | integer | Supplementary files the publisher provides, including any removed before processing. |
| `removed_supplements` | text | Supplementary files or sections removed before processing because they are trial protocols, statistical analysis plans, or records of amendments: `supplement_2 (trial protocol); supplement_3 (statistical analysis plan)`. Empty if none. |
| `n_references` | integer | All entries in the reference list. |
| `n_references_checkable` | integer | Entries carrying a resolvable PubMed identifier or DOI. Denominator for the citation-error proportion. |
| `primary_outcome` | text | The primary outcome, identified by the rule in Appendix 3: the outcome the Methods call primary; failing that, the one on which the sample size was calculated; failing that, the one named in the stated aim. Several are separated by `; `. Empty while `spin_assessability` is `pending` or when none can be identified. |
| `primary_outcome_quote` | text | The sentence that identifies the primary outcome, verbatim: the Methods sentence naming it as primary if there is one, otherwise the sentence giving the basis of the sample size calculation, otherwise the stated aim. Which step of the rule applied is read from the quotation. |
| `primary_outcome_result` | text | For each primary outcome, in the order of `primary_outcome`, `significant` or `not significant`, optionally followed by the P value or interval, separated by `; `. The basis for `spin_assessability`. |
| `spin_assessability` | **categorical** | `assessable` · `assessable_partial` · `not_assessable` · `pending`. Whether the article meets the spin applicability gate (Appendix 3); `assessable_partial` when several primary outcomes are named and only some are statistically significant, so that only two strategies are assessed. Where sections designate different primary outcomes, the Methods designation governs, as stated in the note to Appendix 3. |
| `spin_assessability_reason` | text | The basis for the judgement. Empty while `pending`. |
| `spin_verdict` | **categorical** | `present` · `absent` · empty unless `assessable` or `assessable_partial`. The supporting quotations are the sites of the article's spin record. |
| `note` | text | |

The bibliographic column names follow Rayyan's CSV import format, so an export from a reference manager or from
Rayyan can be mapped onto them field by field. Rayyan's `abstract`, `keywords` and `location` are omitted.

## Source reports

| Column | Type | Values / notes |
| --- | --- | --- |
| `source_report_id` | key | Referenced by `records.source_report_id`. |
| `pmid`, `doi` | text | Of the report. |
| `citation` | text | Full reference. |
| `domains_examined` | **categorical**, `;`-separated | Values of `domain` that the report looked for. |
| `scope` | **categorical** | The part of each article the report examined: `abstract_vs_full_text` · `abstract_conclusion` · `full_text` · `figures` · `other` (described in `note`) |
| `n_articles`, `n_records` | integer | Contributed to the benchmark. |
| `note` | text | |

A benchmark article carries only what its source report looked for, plus whatever the pipeline flagged and
adjudication confirmed. The absence of a record outside `domains_examined` and `scope` is not evidence that the
article is free of such defects.

## Records

### Identity and classification

| Column | Type | Values / notes |
| --- | --- | --- |
| `article_id` | key | Joins to the articles file. |
| `record_id` | key | Never reused, never renumbered. |
| `domain` | **categorical** | `internal_reporting_discrepancy` · `graphical_error` · `spin` · `citation_error` · `other_within_article_concern` |
| `taxonomy_code` | **categorical** | The code of the category in Appendix 3 (`A01` … `D04`), or `X00` for an other within-article concern. The first letter must match `domain`. |
| `taxonomy_category` | text | The category name. Must match the name Appendix 3 gives for `taxonomy_code` after normalization (below). For `X00`, a short free-text description of the concern. |
| `provenance` | **categorical** | Who first identified it — see below. |
| `source_report_id` | text | Populated only when `provenance = source_reported`. |
| `n_sites` | integer | Number of populated site slots. Must equal the count of non-empty `siteN_document`. |
| `sites_truncated` | boolean | `TRUE` when the record involves more locations than the six slots hold; the overflow is then listed in `note`. |
| `mismatched_fields` | **categorical**, `;`-separated | `volume` · `issue` · `pages` · `year` · `journal` · `authors` · `title`. Only for `D04` (Bibliographic field error); empty otherwise. An entry with several disagreeing fields is still one record. |

**Codes.** The code, not the name, identifies a category. A code keeps its meaning when the category is renamed, for
example at peer review, and is never reused; a category that is split or merged receives a new code and the old one
is retired.

**Normalization** before comparing names: Unicode NFKC; lower case; hyphen, non-breaking hyphen, figure dash, en
dash, em dash and minus sign all read as `-`; curly quotation marks and apostrophes read as straight ones; runs of
whitespace collapse to one space. Differences that disappear under these rules are not violations.

**Other within-article concerns** (`X00`) are adjudicated like any record but never enter the primary or secondary
outcomes or sensitivity. They carry no severity. A residual category inside a domain, such as `A12` Other numerical
discrepancy, is a different thing: it belongs to its domain and is counted with it.

### `provenance`

| Value | Meaning |
| --- | --- |
| `source_reported` | Described in a published report before this study began. Benchmark articles only. These records are public **together with their labels**, so contamination of model training data cannot be excluded and performance on them should be reported separately. |
| `full_pipeline` | First raised by the full detection pipeline. |
| `low_cost_configuration` | First raised by a lower-cost configuration and missed by the full pipeline. Kept distinct because these records enter the reference standard after it was first assembled. |
| `human_review` | First identified by a rater who noticed it while adjudicating a different flag. |

Which runs raised a record is not stored here: every original flag is kept in the detection log with the
`record_id` it was grouped into.

### Sites — where the defect is

Six slots, each with four columns. Unused slots are empty.

| Column | Type | Values / notes |
| --- | --- | --- |
| `siteN_document` | **categorical** | `main` · `supplement_1`, `supplement_2` … numbered in the publisher's order of supplementary files, counting any that were removed so that the numbers do not shift. For a record retrieved in a citation check: `pubmed` · `crossref` · `openalex`. |
| `siteN_page` | integer | Physical page of that PDF file, counting from 1 — not the journal's printed page number, which supplementary files lack. Empty for a retrieved record. Recorded on the version of record even for flags raised from PMC XML. **In this demo** the documents are Markdown, so the column holds line numbers instead (`L21`, `L73-L74`). |
| `siteN_object` | text | `title` · `abstract` · `introduction` · `methods` · `results` · `discussion` · `table_2` · `figure_1` · `figure_S2` · `reference_4` …, optionally narrowed with a colon: `table_1:Total`, `figure_S2:caption`, `figure_S1:y_axis`. For a retrieved record, the identifier that was resolved: `doi:10.0000/demo.4104`. |
| `siteN_quote` | text | The content **as printed**, and nothing else, separated by semicolons where a site carries several printed items. Never empty. For a graphic this is the text printed in it — axis title, tick labels, data labels, legend — not a description of what the graphic looks like; the geometry that makes it an error belongs in `note`. For a retrieved record it is the record the catalogue returned. |

Arity is constrained by domain:

| Domain | Permitted `n_sites` |
| --- | --- |
| `internal_reporting_discrepancy` | 1 or more |
| `graphical_error` | exactly 1 |
| `spin` | 1 or more — each supporting quotation is a site |
| `citation_error` | 2, or 3 when a PubMed identifier and a DOI in the same entry resolve to different publications |
| `other_within_article_concern` | 1 or more |

For `citation_error`, **site 1 is always the entry as printed and sites 2 and 3 are the records retrieved for its
identifiers**. For the other domains no site is privileged: which of several disagreeing occurrences is wrong is
usually not determinable.

The sites of a record are the locations identified at adjudication. They need not be every place in the article
where the quantity or attribute is printed.

### Adjudication

| Column | Type | Values / notes |
| --- | --- | --- |
| `rater1`, `rater2` | text | Initials. Empty when that judgement has not been made. |
| `raterN_decision` | **categorical** | `confirmed` · `not_a_finding` · `rounding_sensitive` |
| `raterN_severity` | **categorical** | `minor` · `major` · `not_graded` (spin) · empty when not confirmed and for `X00` |
| `raterN_reason` | **categorical** | Only when the decision is `not_a_finding`: `rounding_compatible` · `reconciled_in_article` · `not_in_version_of_record` · `extraction_error` · `parsing_error` · `ocr_error` · `representation_error` · `unit_conversion` · `omission_misread` · `misread_table_structure` · `out_of_scope_document` · `outside_definition` · `other` — defined below |
| `discussion_outcome` | **categorical** | `resolved` · `unresolved` · empty when the raters agreed or discussion has not yet taken place |
| `consensus_decision`, `consensus_severity`, `consensus_reason` | **categorical** | The judgement the raters agreed in discussion, in full, including when only severity was in dispute. Only when `discussion_outcome = resolved`. Same sets as the rater columns. |
| `third_rater` | text | Initials. Only when discussion did not resolve the disagreement. |
| `third_rater_decision`, `third_rater_severity`, `third_rater_reason` | **categorical** | Same sets as the rater columns. |

The two raters' judgements are recorded as made and never overwritten by a later step. For flags raised by a
detection run and for records identified in human review, rater 1 and rater 2 judge independently. For
`source_reported` records, rater 1 (HS) checks the reported error against the version of record and rater 2
verifies that judgement.

Two judgements **agree** when decision and severity are the same. Different rejection reasons alone are not a
disagreement.

**Rejection reasons.** Each applies to a flag or reported error judged `not_a_finding`.

| Value | The apparent defect is not a finding because |
| --- | --- |
| `rounding_compatible` | the values are compatible under ordinary rounding at their displayed precision (protocol Section 2.4) |
| `reconciled_in_article` | the article itself explains the apparent difference, for example 44 patients enrolled of whom 42 took part |
| `not_in_version_of_record` | the error reported in a source report, or cited by a flag, cannot be found in the version of record, for example because a corrected or different version was read |
| `extraction_error` | the extraction tool misread characters or values |
| `parsing_error` | structuring the extracted content (paragraphs, reading order, footnote links) attached a value to the wrong place |
| `ocr_error` | text recognition misread characters or values printed in an image |
| `representation_error` | another representation of the article, such as PMC XML, differs from the version of record |
| `unit_conversion` | the values express the same quantity in different units or scales |
| `omission_misread` | one location merely omits a value, and the omission was read as a disagreement, for example a subgroup count taken for the total |
| `misread_table_structure` | the rows, columns, headers or footnotes of a table were matched incorrectly |
| `out_of_scope_document` | it rests on a trial protocol, statistical analysis plan or record of amendments that should have been removed before processing |
| `outside_definition` | it is of a kind the definition excludes (protocol Section 2.4): detectable only by statistical recomputation or by reconstructing values from the geometry of a graphic, or a question of methodological appropriateness or another out-of-scope construct |
| `other` | none of the above applies; the reason is given in `note` |

### Resolution

| Column | Type | Values / notes |
| --- | --- | --- |
| `resolved_status` | **categorical** | `candidate` · `pending_second_rater` · `pending_discussion` · `pending_third_rater` · `confirmed` · `not_a_finding` · `rounding_sensitive` |
| `resolved_severity` | **categorical** | `minor` · `major` · `not_graded` · empty unless `confirmed` |
| `resolved_reason` | **categorical** | The rejection reason when `not_a_finding`; empty otherwise |
| `note` | text | Reasoning, arithmetic, overflow sites. Never the quoted content itself. |

The three `resolved_*` columns are **derived** and can be recomputed from the adjudication columns:

1. No judgement from rater 1 → `candidate`.
2. No judgement from rater 2 → `pending_second_rater`.
3. The two agree → their decision and severity, with rater 1's reason.
4. They disagree and `discussion_outcome = resolved` → the `consensus_*` values.
5. They disagree and discussion has not taken place → `pending_discussion`.
6. Discussion was `unresolved` and the third rater has judged → the `third_rater_*` values.
7. Otherwise → `pending_third_rater`.

## Scoring a detector against these records

Two sensitivity definitions are reported in the protocol:

- **lenient** — the configuration flags the record at one or more of its sites
- **strict** — the configuration flags every one of its sites

Both are defined against the sites recorded, not against every place the quantity is printed, so they compare a
configuration with what the full pipeline and adjudication located. In both, the configuration's flag must concern
the same disagreement, which is decided when the flag is adjudicated. The two coincide for records with one site.

## Detection log

The detection log is kept locally while the study runs and released as tables with the study manuscript. Raw model
requests and responses are kept but not released.

**`runs`** — one row per run of one model under one set of conditions on one article.

| Column | Notes |
| --- | --- |
| `run_id` | key |
| `article_id` | |
| `model`, `model_version` | As reported by the provider. |
| `conditions` | The value of every varied condition, including prompt version and input format (`pdf_bundle` · `pmc_xml`). |
| `repetition` | 1, 2, 3 … |
| `started_at`, `finished_at` | ISO 8601 with time zone. |
| `status` | `completed` · `failed` · `retried` |
| `input_tokens`, `cached_input_tokens`, `output_tokens`, `reasoning_tokens` | Summed over every billed API call in the run, including retried calls. |
| `price_id` | Joins to `prices`. |

**`flags`** — one row per flag as the model returned it, before deduplication. Flags are never deleted or
overwritten; deduplication only fills `record_id`.

| Column | Notes |
| --- | --- |
| `flag_id` | key |
| `run_id` | |
| `article_id`, `domain`, `taxonomy_code`, `taxonomy_category` | The name as the model gave it and the code it maps to after normalization. |
| `siteN_document`, `siteN_page`, `siteN_object`, `siteN_quote` | As the model gave them, in the same format as the records. |
| `record_id` | The record the flag was grouped into. Every flag has one, including flags whose record was judged not a finding. |

**`configurations`** — one row per evaluated configuration.

| Column | Notes |
| --- | --- |
| `config_id` | key |
| `description` | |
| `run_ids` | `;`-separated. A configuration that can be assembled from runs executed for the full pipeline lists those runs and is not executed again. |
| `combination` | `union` · `intersection` — how the flags of its runs are combined. |

**`prices`** — one row per price schedule applied.

| Column | Notes |
| --- | --- |
| `price_id` | key |
| `model` | |
| `schedule` | `standard` · `batch` · other provider-specific schedules |
| `input_per_million`, `cached_input_per_million`, `output_per_million` | In the currency charged. |
| `currency`, `effective_date` | |

Cost per article for a configuration is the sum, over its runs, of token counts multiplied by the prices actually
applied.

## A note on matching detector output to these records

There is no occurrence identifier. Matching is on the site columns. This is deliberate: an identifier minted by
this study's pipeline means nothing to anyone else's detector, so a benchmark that relied on it would be usable only
from inside this project. Document, page, object and verbatim quotation are portable.
