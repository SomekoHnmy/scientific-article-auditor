---
bibliography: references.bib
csl: vancouver.csl
link-citations: true
---

# Large language model–based auditing of scientific articles: protocol for tool development and a cross-sectional meta-epidemiological study of medical research articles

Hidehiro Someko, Keisuke Anan, Yuki Kataoka

- **Hidehiro Someko, MD**

  - ORCID: 0000-0002-7195-2055

  - Department of Internal Medicine, Nagoya Tokushukai General Hospital, 2-52 Kozojikitai, Kasugai, Aichi, 487-0016, Japan

  - Scientific Research Works Peer Support Group (SRWS-PSG), Osaka, Japan

- **Keisuke Anan, MD, DrPH**

  - ORCID: 0000-0002-2701-7334

  - Division of Respiratory Medicine, Saiseikai Kumamoto Hospital, 5-3-1 Chikami, Minami-ku, Kumamoto, 861-4193, Japan

  - Scientific Research WorkS Peer Support Group (SRWS-PSG), Osaka, Japan

- **Yuki Kataoka, MD, MPH, DrPH**

  - ORCID: 0000-0001-7982-5213

  - Center for Postgraduate Clinical Training and Career Development, Nagoya University Hospital, 65, Tsurumai-cho, Showa‑ku, Nagoya‑city, Aichi, Japan

  - Center for Medical Education, Graduate School of Medicine, Nagoya University, 65, Tsurumai-cho, Showa‑ku, Nagoya‑city, Aichi, Japan

  - Scientific Research Works Peer Support Group (SRWS-PSG), Osaka, Japan

  - Department of Internal Medicine, Kyoto Min-iren Asukai Hospital, Tanaka Asukai-cho 89, Sakyo-ku, Kyoto 606-8226, Japan

  - Department of Healthcare Epidemiology, Kyoto University Graduate School of Medicine / School of Public Health, Yoshida Konoe-cho, Sakyo-ku, Kyoto 606-8501, Japan

  - Department of International and Community Oral Health, Tohoku University Graduate School of Dentistry, 4-1, Seiryo-machi, Aoba-ku, Sendai, Miyagi, 980-8575, Japan

Correspondence: Hidehiro Someko, MD hidehirosomeko@gmail.com

## 1. Background

Science rests on the correctness of what is published. To safeguard that correctness, the publication process is built as a series of checks: authors verify their own manuscript, peer reviewers scrutinise it, and editorial staff check it again before publication [@GoldbeckWood1999]. Because of this layered structure, a published article is generally taken to be correct.

Research has shown that this expectation does not hold. Articles that have passed through every one of these checks are found, once published, to contain problems that the checks did not catch. These have been described under several names and studied by largely separate literatures: internal reporting discrepancies, defined as pairs of statements within a single manuscript that cannot both be true, which authors of systematic reviews encounter when extracting data [@Puljak2020]; numerical inconsistencies between an abstract and the body of the same article, reported in 18% to 68% of abstracts across six medical journals [@Pitkin1999] and confirmed repeatedly since [@Ward2004; @Fontelo2013; @Kamel2023; @Li2017]; spin, in which the reporting of outcomes and conclusions does not correspond to what the article itself reports [@Chiu2017]; and errors in figures, including internal contradictions, discrepancies with the article text, and visual distortion of numerical data, found in 40% of graphics in one emergency-medicine journal and reproduced in an audit of JAMA graphs [@Cooper2001; @Cooper2002]. Nor do the checks appear to be strengthenable by exhortation or expertise. A randomized trial found that instructing authors to verify their manuscripts did not prevent these defects [@Pitkin1998]. When 607 peer reviewers were each sent papers containing nine deliberately inserted major errors, they detected roughly three [@Schroter2008]; and when 260 readers were asked to look specifically for discrepancies in a clinical trial report, only 11.5% noticed more than a tenth of them, giving a 95% probability that any single alerted reader misses a given discrepancy [@Cole2015].

Large language models can, in principle, perform this checking at a scale that manual verification cannot reach, and across an entire article rather than one section of it. Evaluations of large language models for appraising published articles have so far concentrated on adherence to reporting checklists [@Sanmarchi2023; @Alharbi2024; @Chen2026; @Wrightson2025; @Srinivasan2025; @Forero2025; @Kataoka2026], a task requiring subjective judgement. The problems above are different in kind: each is settled by placing two locations in the same article side by side, and can therefore be adjudicated objectively. Outside medicine, an analogous approach has been used to quantify objective errors in published machine-learning papers [@Bianchi2025]. Whether large language models can detect such problems in medical research articles, and at what cost, are both unknown.

This study has two objectives. First, we will describe the frequency and severity of pipeline-detected, human-confirmed findings in published medical research articles, in top-ranked general medical journals and in openly licensed journal articles, across four domains: internal reporting discrepancies, graphical errors, spin, and citation errors. Second, we will evaluate whether low-cost detection configurations can reproduce the findings of a high-performance multi-model pipeline, and at what LLM API cost per article.

## 2. Methods

### 2.1 Study design

Cross-sectional meta-epidemiological study of published medical research articles, with a nested comparison of detection configurations. A within-article reporting defect as defined in Section 2.4 is the target condition. Defects will be ascertained by the detection pipeline (Section 2.5) with human confirmation of every flag it raises (Section 2.4); the sensitivity of that pipeline is not estimated, so the frequencies it yields are lower bounds. In the nested comparison (Section 2.6) each lower-cost configuration is the index test and the confirmed findings of the full pipeline are the reference standard; that comparison will be reported in accordance with the STARD-AI statement where applicable [@Sounderajah2025]. This protocol will be maintained in a public repository (https://github.com/SomekoHnmy/scientific-article-auditor). Any amendments will be incorporated into the repository as they are made, with the date and content of each change documented in the version history.

![Study workflow](figures/detection-pipeline-flowchart.jpg)

**Figure 1.** Study workflow. From each stratum 160 eligible articles are drawn; ten per stratum are set aside for the development pilot, and the remaining 300 form the main sample. One detection pipeline is built on the 125-article benchmark, frozen, checked for false positives on the 20 set-aside articles, and then applied to the main sample. Every flag it raises on those 300 articles is confirmed by two raters; the confirmed findings are the descriptive result, and those in a random subsample of 50 articles serve as the reference standard against which lower-cost configurations are evaluated.

### 2.2 Sampling frame and eligibility

We will sample articles from two strata defined by rule.

**Stratum 1 (top-ranked journals).** Original research articles published in 2025 in the ten highest-ranked eligible journals after excluding Nature Reviews Disease Primers, based on Journal Impact Factor in the Journal Citation Reports category “Medicine, General & Internal” [@Clarivate2025]. The input is the publisher’s version-of-record PDF; author manuscripts deposited in PubMed Central are not used, since they may differ from the version of record in layout and content.

**Stratum 2 (open-access benchmark stratum).** Original research articles, including systematic reviews, published in 2025 in MEDLINE-indexed journals, whose full text is available in the PubMed Central Open Access subset under a CC BY or CC0 license. No impact-factor cutoff is applied; the MEDLINE restriction sets the editorial standard. The licence restriction allows the annotated full texts to be redistributed as a public benchmark (Section 2.11). No more than 10 articles per journal will be included (the per-journal cap). Articles in this stratum are available both as a publisher PDF and as PMC XML, so 30 of them, randomly selected, will additionally be processed from their PMC XML in an input-format sub-analysis (Section 2.8). Stratum 1 has no XML counterpart, so the sub-analysis is confined to this stratum.

**Exclusion criteria (both strata):** animal-only studies, narrative reviews, case reports, letters and research letters, study protocols, articles retracted as of the search date, and articles published in languages other than English.

Operationalization of eligibility. Article retrieval will be implemented through the NCBI E-utilities and PMC APIs. The full PubMed search strategies for both strata are given in **Appendix 1**.

Licence is not expressible as a PubMed query; retrieved PMCIDs will be passed to the PMC OA Web Service (oa.fcgi) or matched against the PMC OA file list, and only records whose licence field indicates CC BY or CC0 retained. The per-journal cap is applied after this step. Retraction status will be rechecked when eligibility is finalized.

Two criteria cannot be expressed reliably in either API and will be applied by manual screening: (i) animal-only studies, and (ii) study protocols not indexed under "Clinical Trial Protocol"[pt]. The number of records screened and excluded at each step will be reported in a flow diagram.

Within each stratum, candidate records will be drawn in a reproducible random order without replacement and screened sequentially. An ineligible record, or in Stratum 2 a record drawn after its journal has reached the per-journal cap, will be skipped and replaced by the next draw. Drawing continues until 160 eligible articles have been accepted in each stratum. Ten per stratum will then be selected at random, assigned to the stage 2 pilot (Section 2.5), and excluded from the main sample; the remaining 150 per stratum constitute the main sample of 300 articles. The main-sample size was determined by feasibility of human adjudication. Because the number of flags per article at the prevalence of the study population is not known in advance, this size may be revised once stage 2 has estimated it; any revision will be fixed and recorded before the main study begins, and the sample size used will be reported.

The strata will be sampled in priority order, with Stratum 1 completed before Stratum 2. If an article selected for Stratum 2 has already been included in Stratum 1, it will be retained in Stratum 1, excluded from Stratum 2, and replaced by the next eligible Stratum 2 draw.

### 2.3 Article processing

The input for each article is the publisher's version-of-record PDF, which is the canonical source for both strata, and comprises the full text together with those supplementary materials that report results or describe the methods as actually applied; how it is divided across calls is one of the conditions in Section 2.5. Trial protocols, statistical analysis plans, and records of amendments supplied as supplementary materials will be removed before processing, identified from the file name where the publisher supplies them as separate files and from section headings where they are bound into a combined file, and the documents removed from each article will be recorded. A difference between such a plan and the report may reflect a legitimate amendment rather than a defect in reporting (Section 2.4). Each PDF will be processed once using the Adobe PDF Extract API. The canonical article bundle will comprise the structured JSON output with reading order and page coordinates, tables represented as both machine-readable CSV files and PNG renditions, extracted figure images, and the associated captions and surrounding text. Table-footnote markers and their footnote text will be linked where recoverable, and the table PNG and original PDF retained for verification. Extracted figure images will be supplied to a multimodal model, with the use of an additional OCR transcript varied as described in Section 2.5.

The reference list is parsed separately. For every entry carrying a PubMed identifier or a digital object identifier, the record for that identifier will be retrieved from PubMed, Crossref, and OpenAlex and supplied with the canonical bundle alongside the entry as printed; entries without a resolvable identifier will be marked not checkable. This retrieval is deterministic and is performed once, before detection, so that models compare a claimed record against a retrieved one without querying any service at inference time.

### 2.4 Target condition and adjudication of flags

This section defines the target condition — the within-article reporting defect — and the procedure by which candidate flags are confirmed against it. Because the procedure is applied only to flagged items, it establishes that a flag is a defect but never that no defect exists elsewhere in an article, so the frequencies reported in Section 2.7 are lower bounds.

**Operational definition of the target condition.** The target condition is a **within-article reporting defect**: a defect in reporting that can be established from the article’s own content — its abstract, main text, tables, figures, and those supplementary materials that report results or describe the methods as actually applied (Section 2.3) — or, for its reference entries, by resolving the identifiers it gives against public bibliographic catalogues. Four constructs qualify, and are defined in the taxonomy below: a pair of statements within the article that could not both be true, after allowing for rounding (see “Conditions not counted as a finding” below); an error determinable from a graphic alone; reporting that could distort the interpretation of the article’s own results; and a bibliographic claim about one of the article’s own reference entries that the catalogues contradict. Defects requiring judgement about the substance of an external source are outside the definition. A flag that adjudication confirms to be such a defect is a **confirmed finding**, and an article meets the target condition when it carries at least one.

**Taxonomy of within-article reporting defects.** The prespecified taxonomy comprises four top-level domains. Classification is by **type of discrepancy**; the location of the conflicting statements is recorded separately as an attribute of each finding, using the location scheme of Puljak et al. [@Puljak2020] extended to cover supplementary materials. Each confirmed finding receives exactly one category. The full classification, with the source of each category, is given in **Appendix 3**.

1. **Internal reporting discrepancies.** Pairs of statements within the same article that could not both be true [@Francis2013], termed internal reporting discrepancies by Puljak et al. [@Puljak2020]. Categories are numerical and non-numerical. A discrepancy between a figure and the text or a table belongs to this domain, not to the graphical domain, following Puljak et al. [@Puljak2020] and the internal/external distinction of Cooper et al. [@Cooper2001].

2. **Graphical errors.** Errors determinable from the graphic alone, without comparison against text or tables [@Cooper2001]. Graphic-design quality judgements — labelling completeness, visual clarity, adherence to graphing conventions, redundancy, and data density — are excluded.

3. **Spin.** Specific reporting that could distort the interpretation of results and mislead readers [@Boutron2010], restricted to strategies determinable by rule. The domain is assessable when the article has an identifiable primary or main result and that result is not statistically significant; it is not restricted by study design, so systematic reviews and observational studies are assessable. Categories are drawn from Boutron et al. [@Boutron2010] and, for the systematic-review setting, from Yavchitz et al. [@Yavchitz2016] in the seven-item form used by Nascimento et al. [@Nascimento2020]. Articles that do not meet this condition will be recorded as not assessable for this domain.

4. **Citation errors.** Defects in the bibliographic claims the article makes about its own reference entries, established by resolving the PubMed identifiers and digital object identifiers it gives against PubMed, Crossref, and OpenAlex [@Topaz2026]. Only entries carrying a resolvable identifier are checked; entries without one, such as books, websites, and grey literature, are recorded as not checkable and the proportion so excluded is reported. Google Scholar is not queried, as it offers no programmatic interface, which makes the count of non-existent references conservative. The counting unit is the reference entry, and each entry receives at most one category, the most severe that applies.

Defects established from the article’s own content but outside these four domains will be retained as **Other within-article concerns** for exploratory reporting, and excluded from completeness and sensitivity calculations. Methodological appropriateness, risk of bias, reporting-guideline adherence, plagiarism, registry discrepancies, discrepancies between the report and its trial protocol, statistical analysis plan, or record of amendments, raw-data errors, and whether a cited work supports the claim made of it are outside scope: each requires judgement about the substance of an external source, or a different evaluative construct. Recurring findings may inform future expansion of the taxonomy but will not be promoted into the prespecified domains after the main study begins.

**Conditions not counted as a finding.** The following are excluded from the definition:

*Rounding.* Compatibility will first be assessed from the intervals implied by the displayed precision. Under rounding to nearest, a value represents an interval extending half a unit of its last reported digit on either side, so “28%” spans 27.5% to 28.5%; under truncation toward zero the interval is one-sided and one unit wide. Values are rounding-compatible when the intervals or deterministic calculations they imply intersect under a standard convention: 17/60 = 28.33…% is compatible with “28%”.

A discrepancy that ordinary rounding cannot reconcile will not be dismissed merely because it is no more than one unit in the last reported digit. If only an undocumented double-rounding path could explain it, it is classified as **rounding-sensitive/indeterminate**; a double-rounding path supported by quantities and calculation steps in the article instead establishes compatibility. Each candidate is therefore classified as (i) a confirmed finding, (ii) rounding-compatible and so not a finding, or (iii) rounding-sensitive/indeterminate. Only (i) contributes to the primary outcome; (iii) is reported separately as an exploratory outcome.

*Statistical recomputation.* Discrepancies detectable only by recomputing statistics from reported quantities (e.g., recalculating a p-value from a test statistic and degrees of freedom) are outside the definition.

*Graphical estimation.* A value not printed in the article may not be reconstructed from the geometry of a graphic: not from the position of a plotted point relative to axis ticks, from bar height, from a box and its boundaries, or from an error bar and the axis scale. Values printed in a figure, caption, or legend remain eligible, as do symbols defined there; a defined significance symbol may be checked against a reported p-value or confidence interval. Comparing a printed value against its own plotted position is permitted: a bar explicitly labelled 60% that terminates below the displayed 50% tick is a confirmed finding, since no value has to be assigned to the bar. Where the plotted position is too imprecise to establish a contradiction without estimating the underlying value, the candidate will not be confirmed.

**Severity grading.** Each confirmed finding in the internal-reporting-discrepancy and graphical-error domains will be graded on a binary scale. A confirmed citation error is graded major when the source the entry describes cannot be identified from the entry as printed, and minor otherwise; a non-existent reference is always major. Confirmed spin is not graded.

- **Minor:** under either of the conflicting candidate statements, the direction, statistical interpretation, and stated conclusions of the article are unchanged.

- **Major:** under at least one of the conflicting candidate statements, the direction or statistical interpretation of a reported result, or a conclusion stated in the article or abstract, could change.

**Adjudication procedure.** Each pooled flag will be independently assessed by two of the study raters (HS, [initials to be added]), blinded to which model(s), condition(s), and run(s) produced it. Adjudication will be performed against the version-of-record PDF, not the Adobe extraction or another transformed representation. For a flag generated in the input-format sub-analysis (Section 2.2), raters will additionally inspect the original PMC XML with its linked tables and figures, to determine whether the candidate arose from the XML representation. A discrepancy present only because the XML, extraction, parsing, OCR, or another format conversion differs from the version-of-record PDF will be recorded as an input-processing or representation error, not as a finding in the source article. Each flag will first be classified as a confirmed finding, rounding-sensitive/indeterminate, or not a finding; a standardized rejection-reason field will separately identify extraction, parsing, OCR, and representation errors, and flags resting on a trial protocol, statistical analysis plan, or record of amendments that was not removed under Section 2.3; such flags are not findings. Confirmed findings in the internal-reporting-discrepancy and graphical-error domains will then be graded as minor or major. Spin is adjudicated once per article as present or absent, and is not graded. Disagreements will be resolved through discussion; if consensus cannot be reached, a third rater (YK) will make the final determination. No inter-rater kappa statistic is planned.

**Defects noticed outside the flagged set.** A rater who notices a defect while adjudicating a different flag will record it as a finding in its own right, adjudicate it by the same procedure, and mark its provenance as identified by human review rather than by a detection run. Such findings contribute to the primary outcome. Their number will be reported separately, by domain, so that the figure obtained from pipeline-detected findings alone remains recoverable. Raters will not read articles in full in search of further defects; the intent is only that a defect seen in passing is not discarded.

### 2.5 Index test

To detect within-article reporting defects (Section 2.4), a detection pipeline is assembled from several large language models, each applied to every article under a set of varied conditions, with all of their output pooled as a union. Its components are specified in this section and are fixed before the main study by the development stages below.

The primary detection pipeline will consist of three frontier LLMs:

- GPT-5.6 (sol; OpenAI)

- Claude Fable 5 (Anthropic)

- A leading open-weight vision-language model (provisionally Qwen3.8-27B; Alibaba)

An open-weight model is included so that the pipeline can be re-executed with fixed model weights after proprietary model versions are deprecated, addressing reproducibility concerns. Because open-weight model rankings change rapidly, the specific model is defined by rule rather than by name. On the date the pipeline is frozen, we will select the highest-ranked model on a named public leaderboard that satisfies all of the following: weights permanently downloadable from a public repository under a licence permitting redistribution of derived annotations, such as Apache 2.0 or MIT; native vision-language capability, which is required both for the figure conditions below and for the graphical-error domain of the taxonomy (Section 2.4); a context window at least as long as the largest article bundle in the sample; and availability from at least two independent commercial inference providers, so that the study can be re-executed without self-hosting. Where candidates are otherwise comparable, a model that can be run on a single accelerator will be preferred, because it can be re-executed by a reader without cluster infrastructure. The model selected, the leaderboard consulted, and the date of selection will be recorded, and the selection may be revised if the leaderboard changes before the main study begins.

#### Conditions to be varied.

The conditions below will be varied and reported. The list is a prespecified starting set rather than a closed one: further conditions may be introduced during development, and every condition tried will be reported with its retention decision.

1. Prompt wording — alternative formulations of the base prompt, differing in how the domains are framed and in how the model is instructed to search. Candidate formulations are developed during the staged plan and are subject to the same retention rule as the other conditions, so more than one may be carried into the main study.

1. Reasoning effort — minimal (or disabled where the model permits) versus high.

1. Code execution — with and without access to a code execution tool. Where enabled, the tool is available for arithmetic on quantities explicitly reported in the article: percentages against their numerator and denominator, subcomponents against a stated total, a point estimate against its own interval, and the interval arithmetic required to apply the rounding tolerance. Statistical recomputation remains outside the definition (Section 2.4).

1. Input granularity — the whole article in a single call versus section-by-section calls with a final cross-referencing pass.

1. Supplement handling — main text and supplementary materials together versus processed separately with a cross-referencing pass.

1. Figure handling — an extracted figure image supplied directly to a multimodal model versus the same image supplied together with a machine-generated OCR transcript. In both conditions, checking is limited to values, labels, and symbols explicitly printed in the figure, caption, or legend, and to the position of plotted elements relative to the displayed axes. A printed value may be checked against its own plotted position; a value that is not printed may not be reconstructed from graphical geometry (Section 2.4).

1. Repetition — model output varies between runs, so each condition will be run three times per article.

#### Prompt.

The prompt operationalizes the construct defined in Section 2.4: it states the definition of a within-article reporting defect in each of the four domains, mirrors the conditions that are not counted as a finding so that models do not generate flags that adjudication would systematically reject, enumerates the locations where the same quantity or the same attribute is reported more than once in a medical research article, and specifies a structured output that allows each flag to be located and adjudicated. The full text of the base prompt is given in **Appendix 2** and is also held as a versioned file in the study repository. Candidate formulations will be developed during development and compared as a varied condition. The version or versions retained for the main study will be frozen before it begins, tagged in the repository, and reported by identifier.

#### Flag pooling and deduplication.

Flags produced by all runs, models, and evaluated conditions will be pooled as a union. Each flag will receive a flag ID and will retain the quoted values or statements, their locations, the relationship being checked, the domain, and the model and run that produced it.

The counting unit differs by domain. For internal reporting discrepancies, the counting unit is a single disagreement: the set of occurrences reporting the same quantity, or asserting the same attribute, that do not agree with one another, however many locations they span. The set is established at adjudication against the version-of-record PDF. A value mistyped once but repeated in the abstract, the main text and a table is one finding at three locations, not three findings, and the locations are recorded against it. Two flags are duplicates when they concern the same disagreement, whatever subset of its locations each cites. Counting this way keeps the number of findings a property of the article rather than of how often it repeats a quantity, and a pairwise count can be derived from the recorded locations where one is wanted; the reverse derivation is not possible. For graphical errors, the unit is an error determinable from a single graphic. For spin, the unit is the article: any spin flag from any model, condition, or run places the article in the pooled union, without counting or deduplication. For citation errors, the unit is the reference entry. Duplicates in the counted domains will be merged into a single flag, recording which models, conditions, and runs produced it, and the union of the locations they cite. A configuration that flags a discrepancy at one of its locations and a configuration that flags it at all of them contribute the same finding; the difference between them is preserved in the recorded locations and is reported in Section 2.6. Deduplication will be performed by one investigator before adjudication; uncertain cases will be retained as separate flags and resolved during adjudication. Adjudication results and rejection reasons will be stored against the flag ID.

#### Pipeline development.

Conditions will be compared during development: detection yield, flag counts, precision, and LLM API cost (Section 2.6) will be tabulated per condition. A condition that contributes confirmed findings found by no other condition will be retained for the main study; a condition that contributes none will be dropped. The per-condition tabulation and the retention decision for every condition, including those dropped, will be reported.

The pipeline will be developed in two stages before the main study. Stage 1 uses an externally assembled benchmark of articles with previously reported errors; stage 2 uses articles drawn from the study's own sampling frame.

**Stage 1: benchmark development (125 articles).** We have assembled a benchmark of 125 published articles in which errors have already been reported in the peer-reviewed literature, together with 140 item-level error records drawn from those reports. The benchmark spans three of the four domains: 88 records of internal reporting discrepancies, 38 of spin, and 14 of graphical errors. No benchmark record is a citation error, so recall in that domain cannot be developed against previously reported cases; citation errors confirmed during stage 1 will be added to the benchmark as records discovered in this study. Its sources include the abstract-versus-full-text assessment of Kamel and El-Sobky [@Kamel2023], the DAMASCENE within-report discrepancy catalogue [@Nowbar2014], the data-extraction discrepancies of Puljak et al. [@Puljak2020], and the 30 reports selected as containing spin in the abstract conclusion for the SPIIN trial [@Boutron2014]. The full list, with the source that reported each error, is released as described in Section 2.11 and identified in Appendix 4.

The pipeline will be run on these articles under every condition, and every flag will be adjudicated as in Section 2.4, including flags that do not correspond to a previously reported error. Confirmed findings of this kind are expected, since most source reports examined only one domain or one part of the article. They will be added to the benchmark as additional item-level records, marked as discovered in this study rather than reported in the source literature, so that the benchmark used for the retention decision and for the configuration evaluation of Section 2.6 reflects everything confirmed to be present. The number of records added in this way will be reported, by domain. Candidates that are not confirmed will be categorized as rounding-compatible, rounding-sensitive/indeterminate, unit conversion, omission misread as a discrepancy, misread table structure, out-of-scope document, or other, and this classification will inform refinement of the prompt's exclusion clauses.

All 125 articles are used for development, with no subset held out, so performance measured on this benchmark is **not reported as an estimate of pipeline accuracy**. Two further properties would make such an estimate unsafe in any case: every article was selected because an error had already been found in it, so the prevalence of findings far exceeds that of the study population; and several source reports are public together with their labels, including the SPIIN supplement and the DAMASCENE dataset, so contamination of model training data cannot be excluded. Clean estimates come only from stage 2 and the main study.

**Stage 2: pilot in the study population (20 articles).** The benchmark articles are error-enriched and predate the sampling frame, so configurations retained in stage 1 will be re-checked against the study's own population. This stage also gives the only estimate of flags per article at the prevalence of the study population, on which the feasibility of the planned adjudication depends. The retained conditions (Section 2.5) will be applied to the 10 articles per stratum set aside at sampling (Section 2.2), which are drawn by the same procedure as the main sample and excluded from it. Stage 2 will fix, before the main study: (i) which conditions are retained; (ii) the final base prompt; (iii) the final deduplication rule; and (iv) promotion of recurring types from the residual "other" categories of Appendix 3 to named taxonomy categories.

**The main study.** The retained conditions are applied to all sampled articles as described in Sections 2.3 to 2.6.

Articles and adjudications from stages 1 and 2 will not contribute to the primary estimates. The adjudicated findings assembled in stage 1 will be reported separately and released with the benchmark (Section 2.11).

### 2.6 Low-cost configuration evaluation

Each lower-cost configuration is an index test, evaluated against the confirmed findings of the full pipeline (Sections 2.4–2.5), which serve as the reference standard for this comparison. The comparison is run on a random subsample of the main sample, 25 articles per stratum and 50 in total, drawn after the main-study run so that the full pipeline has already been applied to them; restricting it to a subsample bounds the cost of running many configurations and of adjudicating the flags they add. The configurations evaluated include at minimum:

- the open-weight model alone, at a single run and at three runs;

- each frontier model alone, single run;

- smaller or cheaper model tiers of the frontier vendors, single and multiple runs;

- unions and intersections across the cheaper configurations.

The open-weight configuration is listed first because it is the only one a reader can re-execute with fixed weights after proprietary model versions are deprecated (Section 2.5).

All flags generated by the evaluated low-cost configurations, including flags absent from the initial frontier-model union, will undergo the same blinded human adjudication. Confirmed novel flags will be added to the finalized candidate-union benchmark before recall is calculated for every configuration.

The unit of sensitivity differs by domain, following the counting rule in Section 2.5. Each confirmed finding in the internal-reporting-discrepancy, graphical-error and citation-error domains contributes one unit. For spin, each article that meets the assessability condition and carries confirmed spin contributes one unit, which a configuration recalls by flagging spin in that article. The denominator of overall sensitivity is therefore the number of confirmed findings in the three counted domains plus the number of articles with confirmed spin.

Sensitivity is reported in two forms. Under the **lenient** definition a configuration recalls an internal reporting discrepancy when it flags it at any of the locations recorded for that finding; under the **strict** definition it must flag every recorded location. The lenient figure is the primary one, because it measures whether the defect would be brought to a reader’s attention at all; the strict figure is reported alongside and measures completeness of localisation. The two coincide for the other three domains, whose findings occupy a single location.

For each configuration we will report sensitivity against the reference standard, overall and by domain, precision (percentage of the configuration’s flags that are confirmed), and LLM API cost per article calculated from input and output token use at the price applicable on the execution date. Adobe extraction charges, code-execution charges, local or self-hosted compute costs, and human time are excluded from this metric. Input and output token counts will be reported separately; a model run without a token-based price will have its monetary cost reported as not applicable. Configurations will be compared as a sensitivity–LLM-API-cost trade-off. A configuration is classified adequate when the lower bound of the 95% interval for its overall sensitivity is at least 0.8, inadequate when the upper bound falls below 0.8, and indeterminate when the interval spans 0.8. No per-domain threshold and no precision threshold are set. Because overall sensitivity depends on the domain composition of the reference standard, it will be interpreted alongside the per-domain figures rather than on its own.

### 2.7 Outcomes of the descriptive analysis

**Primary outcome.** The percentage of articles containing at least one within-article reporting defect confirmed on adjudication (Section 2.4), in any of the four domains, reported per stratum. Almost all such findings will have been detected by the pipeline; the few identified by a rater in passing are included and are also counted separately.

**Secondary outcomes.** The percentage of articles with at least one confirmed finding in each domain separately, with spin reported over the articles that meet its assessability condition; the percentage of confirmed findings graded major; the number of confirmed findings per article in the three counted domains, summarized as the median and interquartile range; the distribution by location (within main text, between main text and supplementary materials, within supplementary materials); the distribution by taxonomy category; the number of rounding-sensitive/indeterminate candidates; and, for citation errors, the per-article proportion of checked reference entries carrying a confirmed defect — the number of such entries divided by the number of entries checked in that article — summarized across articles as the median and interquartile range, with the proportion of entries not checkable reported alongside.

### 2.8 Statistical analysis

Proportions whose denominator is an article — the primary outcome and the percentages by domain — will be reported per stratum with 95% Wilson score intervals, which have better coverage than the Wald interval at proportions near 0 or 1. Each stratum is sampled at random from a frame far larger than the sample, so no finite population correction is applied. The primary outcome remains an observed lower-bound frequency rather than an estimate corrected for defects the pipeline missed; its interval covers sampling error only and not the incompleteness of detection.

Several quantities have a finding or a flag, not an article, as their denominator, and these are clustered within articles: an article carrying five confirmed findings contributes five correlated observations. Intervals for them will therefore be obtained by a nonparametric bootstrap that resamples articles with replacement, with 2000 replicates, reported as percentile intervals. This applies to the percentage of confirmed findings graded major, to the sensitivity and precision of each detection configuration (Section 2.6), and to the per-article proportion of reference entries carrying a confirmed citation error.

Detection configurations will be compared as paired differences computed on the same articles, with intervals from the same article-level bootstrap. Medians and interquartile ranges are descriptive summaries and will be reported without intervals. No interval will be adjusted for multiplicity; all are interpreted descriptively rather than as hypothesis tests.

The input-format sub-analysis introduced in Section 2.2 will compare detection performance between the publisher PDF and the PMC XML of the same 30 Stratum 2 articles, to quantify the effect of input format. Flags arising only from the XML representation are identified during adjudication (Section 2.4) and are reported separately from findings in the source article.

### 2.9 Dissemination of findings

Authors and editorial offices will not be contacted about individual confirmed findings. The study estimates how often such findings occur and how well they can be detected automatically; it is not a correction exercise, and notification at this scale would introduce an uncontrolled co-intervention part-way through data collection.

Findings will be disseminated in aggregate through the study manuscript and, at item level, through the annotated benchmark described in Section 2.11, which identifies each article by digital object identifier.

The study analyses published documents only, involves no human participants or personal data, and does not require research ethics review.

### 2.10 Technical implementation

- **Input processing:** version-of-record PDFs (Strata 1 and 2) will be processed once through the Adobe PDF Extract API, following the previously established pipeline [@Kataoka2026]. The canonical bundle will include structured JSON, table data in CSV format with corresponding PNG renditions, recoverable links between table-footnote markers and footnote text, extracted figure images, captions, surrounding text, reading order, and page coordinates; PMC XML will be retrieved through the NCBI OA web service only for the Stratum 2 input-format sub-analysis and supplied directly, with its native structure and links to tables and figures preserved, without first converting it to PDF or passing it through the Adobe extraction pipeline. The version-of-record PDF remains the canonical source for source-level adjudication.

- **Bibliographic verification:** reference entries will be resolved through the NCBI E-utilities, the Crossref REST API, and the OpenAlex API. Retrieved records, the query date, and the API versions will be stored with the canonical bundle so that the comparison can be re-executed.

- **Languages/libraries:** Python (pydantic, typer, pandas, numpy, scikit-learn, httpx).

- **Model access and execution:** all runs will be executed programmatically as batch jobs from a Python script against the vendors' APIs, not through interactive chat interfaces. The code execution tool will be enabled or disabled according to the assigned condition; when enabled, computation is performed within the provider's sandbox during inference. All requests, responses, tool invocations, model versions, parameters, timestamps, and token counts will be logged.

### 2.11 Data and code availability

- **Stratum 2 benchmark:** full texts (CC BY / CC0) with item-level annotations of all adjudicated flags will be publicly released. A randomly selected subset of 30 articles will be withheld from public release and retained privately, to permit future contamination-controlled evaluation of models trained after the benchmark’s publication.

- **Stratum 1:** an annotation-only layer (DOI, location, conflicting values, adjudication, severity) will be released; full texts cannot be redistributed.

- **Development benchmark:** the 125-article benchmark and the findings adjudicated on it in stage 1 (Section 2.5) will be released as an annotation layer keyed to PubMed identifiers and digital object identifiers, recording for each item the domain, taxonomy category, and the published report in which the error was originally described. Full-text PDFs will not be redistributed, because many of the articles are subscription content.

- **Code:** the full pipeline, prompts, merging rules, and analysis code will be released in a public repository.

---

# Appendices

Appendices 1 to 3 are reproduced below. Appendix 4 is held as a separate file in the study repository, for the reasons given there.

## Appendix 1. PubMed search strategies

Both strategies will be executed through the NCBI E-utilities `esearch` endpoint against PubMed. The date of execution and the number of records retrieved will be recorded.

**Stratum 1 (top-ranked journals).**

```text
("Lancet"[jour]
OR "N Engl J Med"[jour]
OR "JAMA"[jour]
OR "BMJ"[jour]
OR "Mil Med Res"[jour]
OR "JAMA Intern Med"[jour]
OR "Lancet Digit Health"[jour]
OR "Ann Intern Med"[jour]
OR "EClinicalMedicine"[jour]
OR "J Transl Int Med"[jour]
)
AND 2025[dp]
AND english[lang]
NOT ("Case Reports"[pt] OR Letter[pt] OR Comment[pt] OR Editorial[pt]
     OR (Review[pt] NOT systematic[sb]) OR News[pt]
     OR "Published Erratum"[pt] OR "Clinical Trial Protocol"[pt]
     OR Retraction of Publication[pt] OR Retracted Publication[pt])
```

**Stratum 2 (open-access benchmark stratum).**

```text
2025[dp] AND medline[sb] AND "pmc open access"[filter] AND english[lang]
NOT ("Case Reports"[pt] OR Letter[pt] OR Comment[pt] OR Editorial[pt]
     OR (Review[pt] NOT systematic[sb]) OR News[pt]
     OR "Published Erratum"[pt] OR "Clinical Trial Protocol"[pt]
     OR Retraction of Publication[pt] OR Retracted Publication[pt])
```

License status is not expressible as a PubMed query and is resolved after retrieval, as described in Section 2.2.

## Appendix 2. Base detection prompt

This is the base prompt as of protocol publication. Wording may be refined during the pilot study and will be frozen before the main study; the frozen version will be tagged in the study repository, which also holds this text as a versioned file.

```text
You are checking a medical research article for defects that can be
established from the article itself, together with the bibliographic
records supplied for its reference entries. Use no other outside
information.

Report findings in four domains.

DOMAIN A - INTERNAL REPORTING DISCREPANCIES
A pair of statements anywhere in the article (abstract, main text, tables,
figures, or supplementary materials reporting results or methods) that could
not both be true.

Numerical: contradictory values for the same quantity; a numerator and
denominator inconsistent with the reported percentage; a sum of
subcomponents inconsistent with the reported total; a point estimate lying
outside its own reported interval; a significance statement inconsistent
with the reported p-value or interval; a fractional count of an indivisible
unit; a value outside the defined range of a scale or proportion; a unit or
order-of-magnitude discrepancy for the same quantity; an unexplained change
in denominator between analyses; identical results reported for
contradictory sample sizes; contradictory results reported for identical
sample sizes.

Non-numerical: contradictory statements about the study design (randomised
or not, controlled or not, blinded or not), the recruitment period, the
eligibility criteria, the methods used (for example which databases were
searched), a categorical attribute of the same subject or group, or which
outcome is designated primary.

A discrepancy between a figure and the text or a table belongs to this
domain, not to Domain B.

DOMAIN B - GRAPHICAL ERRORS
Errors established from a graphic alone, without comparing it to the text or
tables: legend text contradicting axis labels; axis values that do not
correspond to the actual distance along the axis; a printed value that
contradicts its own plotted position; a plotted length or area not in
proportion to the underlying data; a scale that is interrupted or does not
follow a linear or logarithmic progression.

DOMAIN C - SPIN
Reporting that could distort the interpretation of the article's own
results. Assess this domain only if the article has an identifiable primary
or main result AND that result is not statistically significant. If it does
not, report Domain C as "not assessable" and give the reason. If the article
names different primary outcomes in different sections, use the one named in
the Methods to decide assessability.

If assessable, report spin as present or absent for the article as a whole,
with the supporting quotations. Do not enumerate or count separate spin
items. Spin includes: claiming equivalence or no difference from a
nonsignificant result; claiming efficacy without stating the nonsignificant
primary result; acknowledging the nonsignificant primary result but
emphasising the treatment's benefit or other significant results; focusing
on significant secondary outcomes, subgroup analyses, within-group
comparisons, or a modified analysis population; ruling out an adverse event
on a nonsignificant result; comparing against a group external to the study;
and concluding for a specific intervention that was not evaluated separately
from its class.

DOMAIN D - CITATION ERRORS
For each reference entry carrying a PubMed identifier or a digital object
identifier, the bundle supplies the record retrieved for that identifier from
PubMed, Crossref, and OpenAlex. Compare the entry as printed against the
retrieved record. Report an entry when:
- the retrieved record is a different publication from the one the entry
  describes;
- the PubMed identifier and the digital object identifier in the same entry
  resolve to different publications;
- the title claimed by the entry matches no retrieved record and its
  identifiers resolve to unrelated publications;
- the retrieved record is the publication the entry describes, but the volume,
  issue, page range, year, journal name, or author list disagrees with it.

Do not flag differences that are formatting alone: abbreviated journal names,
truncated or informally shortened titles, "et al" standing in for a full author
list, or differences in punctuation, capitalization, or diacritics. Do not judge
whether a cited work supports the claim made of it. Entries without a resolvable
identifier are not checked.

DO NOT FLAG
- Differences compatible under ordinary rounding based on the displayed
  precision. If ordinary rounding cannot reconcile the values but an
  undocumented double-rounding path could plausibly explain the discrepancy,
  report the item and label it `rounding_sensitive`; do not discard it.
- Issues requiring statistical recomputation from reported quantities (e.g.,
  recalculating a p-value from a test statistic and degrees of freedom).
  Deterministic checking is limited to addition, subtraction, multiplication,
  and division of quantities explicitly reported in the article.
- Disagreements with external sources or with your own knowledge, other
  than the supplied bibliographic records used in Domain D. In particular, do not judge
  the risk of bias or the certainty of the evidence.
- Differences between the article and a trial protocol, statistical analysis
  plan, or record of amendments, if one is included. Planned and reported
  methods can differ legitimately.
- Values that are not printed in the article. Do not reconstruct a value from
  the position of a point relative to axis ticks, the height of a bar, the
  position of a box or whisker, or the endpoints of an error bar. You MAY
  compare a value that IS printed against where its element sits on the
  displayed axis; a bar labelled 60% that ends below the 50% tick is a valid
  finding, because no value has to be assigned to the bar.
- Graphic design quality. Cluttered layouts, undefined abbreviations,
  unconventional plot styles, decorative elements, and redundancy between a
  figure and the text are not errors.

Verify each value and each statement independently. Do not assume that a
quantity is correct because the authors reported it, and do not accept a
stated result without checking it against the values it is derived from.
Examine every table, figure, and explicitly reported quantity in the
article; do not sample, and do not stop early on long articles.

Report every finding. For Domain A and Domain B, provide:
1. The conflicting values or statements, quoted exactly as they appear
2. The location of each (section, table, or figure)
3. The domain and the taxonomy category
4. A brief explanation of why both cannot be correct
5. Candidate status: `inconsistency_candidate` or `rounding_sensitive`

For Domain C, provide the assessability judgement, the verdict (spin present
or absent), and the quotations supporting it.

For Domain D, provide the reference number as printed, the taxonomy category,
the field or fields that disagree, the entry as printed, and the retrieved
record.

If you find no findings in a domain, state this explicitly for that domain.
```

## Appendix 3. Taxonomy of within-article reporting defects

Classification is by **type of discrepancy**, not by location. Categories are intended to be mutually exclusive: each confirmed finding receives exactly one item from this table. Where the conflicting statements sit is recorded separately as an attribute of the finding, using the location scheme of Puljak et al. extended to cover supplementary materials, as is the article section in which spin occurs.

Domain names and the groupings within a domain occupy the left column alone. Category names are verbatim from their source except where the Source column marks an operationalization.

| Item | Definition | Source of concept |
| --- | --- | --- |
| **A. Internal reporting discrepancies** — pairs of statements within the same article that could not both be true (Francis 2013), termed internal reporting discrepancies by Puljak 2020. |  |  |
| *A1 — Numerical* |  |  |
| Contradictory values for the same quantity | The same quantity is reported with two different values in two places. No computation is required to establish the conflict. | Francis 2013, Discussion p.3396 (*internal contradiction*) |
| Numerator and denominator inconsistent with the reported percentage | A reported percentage cannot be obtained from the count and denominator reported for it. | Operationalization of Francis 2013 *faulty calculation* |
| Sum of subcomponents inconsistent with the reported total | The reported components of a total do not add to the total as reported. | Francis 2013 *faulty calculation*; examples in Puljak 2020, Table 1 |
| Point estimate outside its own reported interval | A reported point estimate lies outside the confidence interval reported for it. | Operationalization of Francis 2013 *faulty calculation* |
| Significance statement inconsistent with the reported p-value or interval | A statement that a result is or is not statistically significant contradicts the p-value or interval reported for it at the stated threshold. | Francis 2013, Discussion p.3396 (*erroneous statistical inference*) |
| Fractional count of an indivisible unit | A count of discrete entities is reported as a non-integer. | Francis 2013, Abstract (*fractional numbers of patients*, *fractional numbers of coronary arteries*) |
| Value outside the defined range of a scale or proportion | A value falls outside the range the scale or proportion admits. | Francis 2013, Abstract (*a patient with a negative NYHA class*) |
| Unit or order-of-magnitude discrepancy for the same quantity | The same quantity is reported in incompatible units or at an incompatible magnitude. | Francis 2013, Abstract (*million-fold differences in cell counts*) |
| Unexplained change in denominator between analyses | The analysed population changes between analyses without the change being stated or accounted for. | Francis 2013, Abstract (*possible silent patient deletions*) |
| Identical results reported for contradictory sample sizes | The same result is reported for two different stated sample sizes. | Francis 2013, Abstract (verbatim) |
| Contradictory results reported for identical sample sizes | Different results are reported for the same stated sample size. | Francis 2013, Abstract (verbatim) |
| Other numerical discrepancy | Residual category for a numerical pair that cannot both be true and matches no item above. | — |
| *A2 — Non-numerical* |  |  |
| Contradictory study design designation | The article does not consistently state whether the study was randomised, whether it was open-controlled or blinded placebo-controlled, or whether it had a control group at all. | Francis 2013, Table 1 (*Design discrepancies*) and Abstract |
| Contradictory recruitment period | Recruitment start or end dates differ between statements. | Francis 2013, Table 2 (*Recruitment discrepancies*) |
| Contradictory eligibility criteria | Inclusion or exclusion criteria differ between statements. | Francis 2013, Table 2 (*Recruitment discrepancies*) |
| Contradictory methods description | A described method differs between sections, for example the set of databases stated to have been searched. | Puljak 2020, Table 1 (abstract-text example) |
| Contradictory categorical attribute of the same subject or group | A non-numerical attribute assigned to the same subject or group differs between statements. | Francis 2013, Abstract (*sex reclassification*) |
| Outcome designated primary in one section and secondary in another | The designation of an outcome as primary or secondary is not consistent across Methods, Results, Abstract and Conclusions. Classified here, not as spin, because it is a factual contradiction rather than an interpretive strategy. | Operationalization; the requirement that the primary outcome be clearly identified is a precondition of Boutron 2010 |
| Other non-numerical discrepancy | Residual category for a non-numerical pair that cannot both be true and matches no item above. | — |
| **B. Graphical error** — errors determinable from the graphic alone, without comparison against text or tables. Corresponds to Cooper 2001, Section I (internal characteristics). A discrepancy between a figure and the text or a table is *not* classified here; it belongs to Domain A, following Cooper 2001, Section II (*Inconsistency of graphic with text*) and Puljak 2020 (*Text-figure discrepancies*). |  |  |
| Legend text contradicts axis labels | What the legend states is incompatible with how the axes are labelled. | Cooper 2001, Table 1 (*Internal contradiction*, first clause) |
| Axis values do not correspond to the actual distance along the axis | The printed axis values are not consistent with the spacing of the axis on which they appear. | Cooper 2001, Table 1 (*Internal contradiction*, second clause) |
| Printed value contradicts its own plotted position | A value printed on a plotted element is incompatible with where that element sits against the displayed axis, for example a bar labelled 60% terminating below the displayed 50% tick. Confirmed only where the contradiction is unambiguous without reconstructing the underlying value from geometry. | Operationalization; extends Cooper 2001 *Internal contradiction* |
| Plotted length or area not in proportion to the underlying data | Lengths or areas used to represent quantities are not proportional to those quantities. Most often arises when dimensions not required to portray the data are added. | Cooper 2001, Table 1 (*Numeric distortion*, first clause) |
| Scale interrupted or not following a linear or logarithmic progression | The scale has interruptions, or its progression is neither linear nor logarithmic. | Cooper 2001, Table 1 (*Numeric distortion*, second clause) |
| Other graphical error | Residual category for an error determinable from the graphic alone that matches no item above. | — |
| **C. Spin** — specific reporting that could distort the interpretation of results and mislead readers (Boutron 2010). Restricted here to strategies determinable by rule. **Applicability gate**: the article has an identifiable primary or main result, and that result is not statistically significant.\* The gate is not restricted by study design; systematic reviews and observational studies are assessable. Articles failing the gate are recorded as not assessable for this domain. Categories are collapsed across article sections; the section in which the strategy occurs is recorded as an attribute. |  |  |
| Claiming equivalence or no difference for a statistically nonsignificant result | A nonsignificant result is reported or interpreted as demonstrating equivalence, comparable effectiveness, or absence of a difference, where the trial was not designed to assess equivalence or noninferiority. | Boutron 2010, Table 2 (*Claiming equivalence for statistically nonsignificant results*; *Reporting of statistically nonsignificant outcome as if the trial were an equivalence trial*) |
| Claiming efficacy without consideration of the statistically nonsignificant primary outcome | Efficacy is asserted while the nonsignificant primary outcome result is not stated. | Boutron 2010, Table 2 |
| Acknowledging the nonsignificant primary outcome but emphasizing the beneficial effect of the treatment | The nonsignificant primary outcome result is stated, but the treatment is nonetheless presented as beneficial. Includes a recommendation to use the treatment in clinical practice. | Boutron 2010, Table 2 |
| Acknowledging the nonsignificant primary outcome but emphasizing other statistically significant results | The nonsignificant primary outcome is stated, but the emphasis is placed on other significant results. | Boutron 2010, Table 2 |
| Focus on statistically significant secondary outcomes | Reporting or interpretation centres on significant secondary outcomes. | Boutron 2010, Table 2 |
| Focus on statistically significant subgroup analyses | Reporting or interpretation centres on significant subgroup findings. | Boutron 2010, Table 2 |
| Focus on statistically significant within-group comparison | Reporting or interpretation centres on significant change from baseline within one or both groups rather than on the between-group comparison. Includes the case where both groups are declared effective on this basis. | Boutron 2010, Table 2 (merges *Focus on statistically significant within-group comparison*, *Focus on overall within-group improvement*, and *Conclusion focusing on within-group assessment*) |
| Focus on a statistically significant modified population of analyses | Reporting or interpretation centres on a modified analysis population, such as a per-protocol analysis, in which the result is significant. | Boutron 2010, Table 2 |
| Ruling out an adverse event on a statistically nonsignificant result | A nonsignificant safety result is interpreted as demonstrating absence of harm, or safety is claimed on the basis of a nonsignificant result. | Boutron 2010, Table 2 (merges the Discussion and Conclusions rows); Yavchitz 2016, as operationalized in Nascimento 2020, item 4 |
| Comparison with the placebo group of another trial | The experimental group is compared against a group external to the trial in order to support a claim of benefit. | Boutron 2010, Table 2 |
| Conclusion extrapolates the findings to a different intervention | The conclusion claims efficacy of one specific intervention although the review or study evaluated a class of several interventions and did not evaluate that intervention separately. | Yavchitz 2016, as operationalized in Nascimento 2020, item 7 |
| **D. Citation errors** — defects in the bibliographic claims the article makes about its own references, established by resolving the identifiers it gives against public bibliographic catalogues (PubMed, Crossref, OpenAlex). Only entries carrying a resolvable PubMed identifier or digital object identifier are checked; entries without one, such as books, websites, and grey literature, are recorded as not checkable. The counting unit is the reference entry, and each entry receives at most one category, the most severe that applies. |  |  |
| Non-existent reference | The title claimed by the entry matches no record in any catalogue searched, and any identifier it carries resolves to an unrelated publication. | Topaz 2026 (operationalization) |
| Conflicting identifiers within one entry | The PubMed identifier and the digital object identifier given in the same entry resolve to different publications. | Topaz 2026 (operationalization) |
| Identifier–record mismatch | The identifier resolves to a publication other than the one the entry describes. | Topaz 2026 (operationalization) |
| Bibliographic field error | The identifier resolves to the publication the entry describes, but one or more fields disagree with the retrieved record. The disagreeing fields (volume, issue, pages, year, journal, authors, title) are recorded as an attribute. | — |

\* **Contested primary outcome.** Where the article designates different primary outcomes in different sections, the designation given in the Methods governs the gate; the discrepancy itself is recorded separately as an internal reporting discrepancy. This affects the gate only when one designation is statistically significant and the other is not.

## Appendix 4. Benchmark and development article lists

These lists are held as separate machine-readable files in the study repository rather than reproduced here, because they are tabular data that will grow as the study proceeds and are intended for reuse.

The repository will hold:

- the development benchmark used in stage 1 (Section 2.5): 125 articles carrying 140 item-level records of errors already reported in the peer-reviewed literature, comprising 88 records of internal reporting discrepancies, 38 of spin, and 14 of graphical errors. Each record is keyed to a PubMed identifier and a digital object identifier, and names the published report in which the error was originally described. Contributing sources include the abstract-versus-full-text assessment of Kamel and El-Sobky [@Kamel2023], the DAMASCENE within-report discrepancy catalogue [@Nowbar2014], the data-extraction discrepancies of Puljak et al. [@Puljak2020], and the 30 reports selected as containing spin in the abstract conclusion for the SPIIN trial [@Boutron2014], for which the supplement additionally provides each abstract with spin alongside a rewritten version without spin;
- the adjudications made on that benchmark in stage 1, recording for each flag its domain, taxonomy category, and outcome;
- the main-study article lists for both strata, with adjudicated item-level annotations, released as specified in Section 2.11.

Full-text PDFs of these articles will not be redistributed. Many are published under subscription terms that do not permit redistribution, and the lists identify every article unambiguously by PubMed identifier and digital object identifier, so that a reader with access can retrieve them.

## Funding

The application programming interface fee was supported by a JSPS Grant-in-Aid for Scientific Research (Grant No. 25K13585) provided to Y.K. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## References

::: {#refs}
:::
