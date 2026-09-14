# Ambient voice transcription in the emergency department: a stepped-wedge cluster randomised trial

> **SYNTHETIC DOCUMENT.** This article, its journal, its authors, its data and its
> references are entirely fictional. It exists only to demonstrate the benchmark schema.
> Errors have been planted in it deliberately; see `errors_planted.md`.

*Open Journal of Clinical Medicine Publication* 2025;14(3):210–224

Alex Demo, Bailey Sample, Casey Placeholder, Drew Example, Emery Mock

Correspondence: Alex Demo, Department of Emergency Medicine, Demo Central Hospital

Trial registration: Demo Trial Registry DEMO-TR-0001. Approved by the Demo Central Hospital Ethics Committee (reference DEMO-EC-0001).

## Abstract

**Background.** Documentation burden is a principal driver of emergency physician workload. Ambient voice transcription embedded in the electronic health record may reduce the time physicians spend documenting, but its effect on patient-facing metrics is unknown.

**Methods.** We conducted a stepped-wedge cluster randomised trial across 20 acute-care hospitals belonging to a single hospital group in Japan. Hospitals ranged from 100 to 500 beds and were distributed across all eight regions of the country. Hospitals were allocated to four clusters, and ambient transcription was activated in one cluster every two months between April 2023 and March 2024. The primary outcome was emergency department waiting time from arrival to first physician contact. Secondary outcomes were chart open-to-close time, the proportion of encounters in which the transcription feature was actually used, admission rate, and return to the same emergency department within seven days. Analyses used mixed-effects models with hospital as a random effect and calendar time as a fixed effect.

**Results.** We analysed 48,712 emergency department visits. Waiting time was significantly reduced in intervention periods compared with control periods (adjusted mean difference −4.7 minutes, 95% CI −9.1 to 0.3; p = 0.08). Chart open-to-close time fell by 8.4 minutes (95% CI −7.9 to −3.2). The transcription feature was used in 18,432 of 31,205 intervention-period encounters (62.1%). Admission rate and seven-day return rate did not differ between periods.

**Conclusions.** Ambient voice transcription substantially reduced documentation time in the emergency department and should be considered for wider adoption.

**Word count:** 248

## Introduction

Emergency physicians spend a substantial proportion of each shift on documentation rather than on direct patient care. Time–motion studies conducted in North American and Japanese emergency departments have consistently reported that between 30% and 45% of physician time is devoted to the electronic health record, and that this proportion has risen as record systems have accumulated mandatory fields [1,2]. The resulting burden has been linked to reduced time at the bedside, delayed disposition decisions, and physician burnout [3].

Ambient voice transcription, in which a microphone captures the clinical encounter and an automatic speech recognition system drafts the note, has been proposed as a remedy. Early single-centre evaluations in outpatient specialties reported reductions in documentation time of between five and twenty minutes per encounter [4,5]. Emergency departments differ from outpatient clinics in ways that may either amplify or negate this benefit: encounters are shorter and more frequently interrupted, ambient noise is higher, and several clinicians may contribute to a single record.

Evidence from emergency settings remains thin. Two before-and-after studies have reported favourable results, but both were conducted in single academic centres and neither adjusted for secular trends in department crowding [6,7]. No randomised evaluation has been published, and no study has reported whether the feature is actually used when it is available — a question that determines whether any measured effect reflects the technology or merely the attention that accompanies its introduction.

A further gap concerns who benefits. Documentation speed varies widely with experience: junior
physicians typically produce longer narrative notes and type more slowly than senior colleagues,
so any technology that removes typing from the task might be expected to help them
disproportionately. None of the published evaluations has stratified by training stage, and none
has examined whether benefit differs between smaller community hospitals and larger referral
centres, where case mix and departmental staffing differ substantially.

We therefore conducted a stepped-wedge cluster randomised trial across a national hospital group, in which ambient transcription was activated in successive clusters of hospitals at two-month intervals. We hypothesised that activation would shorten the interval from patient arrival to first physician contact, and that it would do so without increasing admission or return visits.

## Methods

### Design and setting

This was a parallel-group cluster randomised trial conducted in 20 acute-care hospitals belonging to a single hospital group. Participating hospitals had between 100 and 500 inpatient beds and were distributed across all eight regions of Japan, from Hokkaido to Kyushu. All hospitals used the same commercial electronic health record and had emergency departments staffed continuously by physicians.

Each hospital's emergency department was staffed by a mixture of postgraduate year (PGY) 1–2 residents, who rotate through emergency medicine as part of general clinical training, and physicians in PGY 3–20 comprising subspecialty trainees and attending physicians. Staffing mix was recorded monthly for each hospital.

The trial protocol was registered in the Demo Trial Registry (DEMO-TR-0001) before the first cluster was activated and was approved by the Demo Central Hospital Ethics Committee (DEMO-EC-0001). The requirement for individual patient consent was waived because the intervention operated at the level of the documentation system rather than of patient care, and because only routinely collected data were analysed.

### Randomisation

The 20 hospitals were allocated to four clusters of five hospitals each. Allocation was performed by an independent statistician using a computer-generated sequence stratified by hospital size (fewer than 250 beds, 250 beds or more) and by annual emergency department census. Cluster assignment determined only the date on which the transcription feature was activated; no hospital was denied the intervention.

Blinding of clinicians was not possible, as activation of the feature was visible within the record interface. Outcome data were extracted from the record system by analysts who were unaware of cluster assignment.

### Intervention

Ambient voice transcription was activated as a configuration change within the existing electronic health record. Once active, a physician opening an encounter note could start transcription with a single control; the system then captured audio through the workstation microphone and generated a draft note, which the physician edited and signed. Physicians retained the option of typing the note in the conventional manner, and no target for uptake was set.

Each hospital received a one-hour training session delivered remotely in the week before activation, and a written quick-reference guide. No other component of the record system was altered during the trial.

### Study periods and eligibility

Recruitment ran from April 2023 to September 2024. Each hospital contributed control-period data from the start of the trial until its cluster was activated, and intervention-period data thereafter. All emergency department visits by patients aged 16 years or older were eligible. Visits by patients who left without being seen were excluded from the waiting-time analysis but retained for disposition outcomes.

### Data collection and quality assurance

All outcome data were extracted directly from the electronic health record by a single analytic
team using a fixed query specification written before the first cluster was activated. Extraction
covered the period from 1 April 2023 to 31 March 2024 inclusive. Timestamps for registration,
first physician contact, note opening and note signature are written automatically by the record
system and were not subject to manual entry.

Two quality checks were applied. First, encounters with a chart open-to-close time exceeding 480
minutes were reviewed individually, as these usually reflect a note left open at the end of a
shift rather than genuine documentation time; 214.5 such encounters were identified and truncated at
480 minutes. Second, hospital-months in which fewer than 50 encounters were recorded were examined
for extraction failure; none was found. Physician staffing mix was obtained from the group's
personnel system and linked to each hospital-month.

### Outcomes

The primary outcome was chart open-to-close time, defined as the interval in minutes between the physician first opening the encounter note and finally signing it, summed across all physicians contributing to the encounter.

Secondary outcomes were emergency department waiting time, defined as the interval from registration at the reception desk to the first documented physician contact; the proportion of encounters in which the transcription feature was used, determined from a flag written to the record whenever transcription was started; the proportion of visits ending in admission; and the proportion of patients returning to the same emergency department within seven days. Returns to a different hospital, including other hospitals in the group, were not counted.

### Statistical analysis

Analyses followed the intention-to-treat principle at the level of the hospital-month. All adults aged 18 years or older attending during the study window contributed to the primary analysis. Continuous outcomes were modelled with linear mixed-effects models including a random intercept for hospital, a fixed effect for calendar month to account for secular trend, and a fixed effect for intervention status. Binary outcomes were modelled with mixed-effects logistic regression using the same structure.

The trial was powered on the primary outcome. Assuming a control-period mean chart open-to-close time of 22 minutes with a between-hospital coefficient of variation of 0.15, 20 hospitals observed over twelve two-month steps provided 90% power to detect a difference of three minutes at a two-sided alpha of 0.05.

Prespecified subgroup analyses examined effect modification by physician postgraduate year (PGY 1–2 versus PGY 3–20), by hospital size, and by time of day. Subgroup results are presented in the supplementary appendix. No adjustment was made for multiple comparisons; subgroup findings are interpreted as exploratory.

## Results

### Hospitals and visits

All 20 randomised hospitals completed the trial and contributed data to the analysis. Hospital characteristics at baseline are shown in Table 1. Median bed count was 284 (interquartile range 196 to 372), and median annual emergency department census was 14,200 visits.

A total of 48,217 emergency department visits occurred during the study period, of which 17,012 fell in control periods and 31,205 in intervention periods. The distribution of visits across clusters and periods is shown in Table 2.

### Table 1. Baseline characteristics of participating hospitals

| Cluster | Hospitals | Median beds | Median annual ED census | Activation month |
| --- | --- | --- | --- | --- |
| 1 | 5 | 310 | 16,800 | June 2023 |
| 2 | 5 | 268 | 14,100 | August 2023 |
| 3 | 5 | 291 | 13,700 | October 2023 |
| 4 | 4 | 252 | 12,400 | December 2023 |
| Total | 19 | 284 | 14,200 | — |

### Table 2. Emergency department visits by period

| | Control periods | Intervention periods | Total |
| --- | --- | --- | --- |
| Visits, n | 17,012 | 31,205 | 48,217 |
| Patients aged 16–64, n | 10,884 | 19,703 | 30,587 |
| Patients aged 65 or older, n | 6,128 | 11,502 | 17,630 |
| Left without being seen, n (%) | 412 (2.4) | 690 (2.2) | 1,102 (2.3) |

### Primary outcome

Chart open-to-close time was shorter during intervention periods. The unadjusted mean was 21.6 minutes in control periods and 13.9 minutes in intervention periods. In the adjusted model, the mean difference was −8.4 minutes (95% CI −7.9 to −3.2).

### Secondary outcomes

Emergency department waiting time was significantly reduced in intervention periods compared with control periods, with an adjusted mean difference of −4.7 minutes (95% CI −9.1 to 0.3; p = 0.08).

The transcription feature was used in 18,432 of 31,205 intervention-period encounters (62.1%). Use varied considerably between hospitals, ranging from 31% to 84%, and was higher among PGY 1–2 residents than among PGY 3–20 physicians. Figure S2 in the supplementary appendix shows the distribution of use by hospital.

Admission rate was 24.1% in control periods and 23.8% in intervention periods (adjusted odds ratio 0.98, 95% CI 0.91 to 1.06). Return to the same emergency department within seven days occurred after 3.9% of control-period visits and 3.7% of intervention-period visits (adjusted odds ratio 0.96, 95% CI 0.86 to 1.07).

### Uptake over time

Use of the transcription feature rose over the first eight weeks after activation and then
plateaued. In the first two weeks after activation the feature was used in 38% of encounters,
rising to 54% in weeks three to four and to 63% by weeks seven to eight, after which the
hospital-level proportion changed by less than three percentage points in either direction.
This pattern was similar across all four clusters.

Staffing mix did not change materially during the trial. PGY 1–2 residents accounted for 31.6% of
documented encounters in control periods and 31.5% in intervention periods; the remainder were
documented by physicians in PGY 3–20.

### Subgroup analyses

Effect modification by postgraduate year was apparent for the primary outcome. Among PGY 1–2 residents the adjusted mean difference in chart open-to-close time was −11.2 minutes (95% CI −14.0 to −8.4), whereas among PGY 3–20 physicians it was −5.1 minutes (95% CI −7.3 to −2.9); the interaction term was statistically significant (p = 0.01). Results by hospital size and by time of day are shown in the supplementary appendix.

## Discussion

In this stepped-wedge cluster randomised trial across 20 hospitals, activation of ambient voice transcription was associated with a reduction of approximately eight minutes in the time physicians spent with the encounter note open. The effect on emergency department waiting time was smaller and did not reach conventional statistical significance. Admission and short-term return rates were unchanged, which argues against the possibility that faster documentation came at the cost of less thorough assessment.

The magnitude of the documentation effect is consistent with the upper end of the range reported from outpatient settings [4,5], which is perhaps surprising given the noisier and more fragmented environment of the emergency department. One explanation is that the marginal value of transcription is greatest for long free-text narratives, which remain common in emergency notes despite the proliferation of structured fields.

The gradient across postgraduate year deserves comment. Junior residents, who type more slowly and who write longer narrative notes, gained roughly twice as much as senior physicians. If this pattern is general, the case for ambient transcription may be strongest in teaching hospitals with large junior cohorts.

Uptake was incomplete. Nearly four in ten eligible encounters were documented conventionally even after activation, and use varied more than twofold between hospitals. We did not collect qualitative data on the reasons, but informal feedback pointed to microphone placement in shared work areas and to concern about transcription accuracy for medication names.

Our findings sit alongside a small but growing literature on ambient documentation. The two
before-and-after emergency department studies reported reductions of six and eleven minutes
respectively [6,7], both larger than the effect we observed for waiting time and broadly
consistent with what we observed for documentation time. Neither adjusted for secular trends, and
in a stepped-wedge design the calendar-time term absorbs a portion of the apparent benefit that an
uncontrolled before-and-after comparison would attribute to the intervention. That our adjusted
estimate remains substantial is therefore reassuring.

The absence of a detectable effect on waiting time merits attention. Documentation is only one
component of the interval between arrival and first physician contact, and in most participating
departments that interval is dominated by triage capacity and by the availability of a free
cubicle. A saving of eight minutes per note, distributed across a shift, may simply be too small
relative to those constraints to move an arrival-to-contact metric. It may also be redeployed to
other tasks rather than to seeing the next patient sooner.

This trial has several limitations. First, it was conducted within a single hospital group using a single record system, and the findings may not transfer to other systems. Second, return visits were ascertained only at the index hospital; patients returning elsewhere were not captured, which will have biased the return rate downwards to an unknown degree. Third, waiting time depends heavily on department crowding, which we adjusted for only through a calendar-time term. Fourth, the trial could not be blinded, and physicians aware of being studied may have altered their documentation behaviour.

Ambient voice transcription substantially reduced documentation time in the emergency department without measurable harm to patient-facing outcomes, and should be considered for wider adoption.

## References

1. Hartwell PN, Iwasaki M, Dube A. Time allocation among emergency physicians: a multicentre time–motion study. *Demo Journal of Emergency Systems* 2021;9(4):220–228. doi:10.0000/demo.4101
2. Okabe S, Lindqvist H. Documentation load and the electronic record: a decade of change. *Demo Review of Health Informatics* 2022;7(2):88–97. doi:10.0000/demo.4102
3. Vasquez-Arnal T, Chen W, Ferreira L. Documentation burden and burnout among emergency clinicians. *Open Journal of Clinical Medicine Publication* 2020;9(1):15–23. doi:10.0000/demo.4103
4. Delacroix M, Nwosu B. Ambient documentation in ambulatory care: a pragmatic evaluation. *Demo Journal of Digital Medicine* 2023;5(3):141–150. doi:10.0000/demo.4104
5. Stein AR, Kobayashi J, Oyelaran F. Speech recognition drafting and clinician time: a prospective cohort. *Demo Journal of Digital Medicine* 2023;5(11):610–618. doi:10.0000/demo.4105
6. Ferrand C, Takeda M. Before-and-after evaluation of ambient scribing in an academic emergency department. *Demo Acute Care Reports* 2024;12(6):301–309. doi:10.0000/demo.4106
7. Bergstrom L, Adeyemi O, Park J. Ambient transcription and throughput in emergency care: a single-centre study. *Demo Acute Care Reports* 2024;12(9):455–462. doi:10.0000/demo.4107
8. Maruyama T, Silva RP. Cluster randomised designs for health information technology evaluation. *Demo Journal of Trial Methodology* 2019;3(2):55–64. doi:10.0000/demo.4108
