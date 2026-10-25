# Lecture notes (short version, ~1000 words)

Zhu et al., *Science Translational Medicine* 16, eabo1997 (30 October 2024)

Timing: about 8 to 10 minutes at a normal pace.

---

## Slide 1. Title

Good morning, everyone. Today I'd like to introduce a paper called "Single-cell transcriptomic and proteomic analysis of Parkinson's disease brains." In one sentence, it is the first single-cell map of the Parkinson's disease prefrontal cortex. What makes it stand out is that, besides RNA, the authors also measured proteins and scored Lewy pathology in the same tissue.

---

## Slide 2. Background

Let's start with what we already know. PD is the second most common neurodegenerative disorder. Its established pathology has two parts: the loss of dopamine neurons in the substantia nigra, and the accumulation of misfolded alpha-synuclein inside neurons, forming Lewy bodies.

Over the past decade, however, it has become clear that PD is not purely a neuronal disease. Genetic and epidemiological evidence points to glial and immune pathways as well. The problem is that earlier bulk RNA-seq averages all cell types together, so it could not tell us how neurons and glia each change in PD. To solve this, the paper builds a single-cell map of PD cortex.

---

## Slide 3. Objectives

The overarching question is simple: which cell types, genes and cell-to-cell conversations change in late-stage PD cortex, and are those changes specific to PD?

To answer it, the paper has four aims, and the results follow the same order. First, build a cell-type atlas by single-nucleus RNA-seq of Brodmann area 9 from six PD donors and six controls. Second, anchor those changes to pathology and genetics: score alpha-synuclein pathology in the same tissue and correlate it with neuronal gene expression, and test whether PARK and GWAS genes change in specific cell types. Third, map ligand-receptor communication between neurons, glia and T cells, and in parallel profile the proteome and link protein modules back to cell types. Finally, ask whether PD and AD share a cellular signature.

Before the findings, let me briefly show how the data were generated.

---

## Slide 4. Methods

This slide shows the workflow. At the top, the samples: prefrontal cortex from 12 postmortem donors, six with late-stage PD and six sex- and age-matched controls.

For snRNA-seq, nuclei are isolated by sucrose-gradient ultracentrifugation and sequenced on the 10x Chromium platform. Reads are aligned to a GRCh38 pre-mRNA reference, because nuclear RNA is mostly unspliced, and nuclei with 200 to 7,000 genes are kept. The data are then log-normalised, integrated across donors, and clustered after PCA and UMAP into twelve clusters, which collapse into eight cell types by canonical markers. Differential expression uses a Wilcoxon rank-sum test per cell type, with log fold change above 0.25 and FDR below 0.05, followed by GO enrichment. Downstream, they add proportion tests, RNA velocity, CellPhoneDB for ligand-receptor inference, UTMOST for GWAS genes, and RNAscope validation in an independent cohort.

The second lane is proteomics. Label-free mass spectrometry quantifies about 2,500 proteins, tested with a two-sided t test at nominal P below 0.05 without correction. WGCNA then groups proteins into fourteen co-expression modules, and a Fisher exact test asks which cell-type markers each module contains.

The third lane is pathology: phospho-S129 alpha-synuclein staining, a Lewy body and neurite score per brain, and correlation of that score with chaperone expression in excitatory neurons.

---

## Slide 5. Result 1: the atlas

Here is the atlas. The UMAP of 77,384 nuclei shows eight populations, including a small cluster of brain-resident T cells. Importantly, PD and control nuclei overlap within each cluster, so clustering reflects cell identity rather than patient.

Then, the proportions shift in PD. While most types are stable, T cells increase about seven-fold, from 33 to 243 nuclei, at P equals 0.02, and microglia roughly double, although only at P equals 0.09. Both increases were confirmed by RNAscope.

Besides, the direction of change differs by cell type. Neurons have few DEGs and most go down: 79 percent in excitatory and 67 percent in inhibitory neurons, dominated by protein folding genes such as HSPB1, HSP90AB1 and DNAJB6. In other words, neurons are losing chaperone capacity. Glia, by contrast, mostly go up: astrocytes switch on metal-ion detoxification, microglia activate myeloid programs, and oligodendrocytes up-regulate protein-complex assembly.

So neurons go quiet while glia switch on. The next question is whether the neuronal change relates to the pathology itself.

---

## Slide 6. Result 2: pathology and communication

On the left, controls had essentially no Lewy pathology, whereas every PD brain had some, with scores from 0.1 up to about 12, significant at P equals 0.03. In the correlation panels, each point is a donor, and for most protein-folding genes in excitatory neurons, higher Lewy burden goes with lower expression, with HSP90AB1 the strongest at an R-squared of 0.74.

On the right, the matrix shows ligand-receptor interactions in PD minus controls. Almost the whole matrix is blue, meaning communication is globally reduced. The hardest-hit pair is excitatory neurons with astrocytes, where about a quarter of interactions are lost, including trophic signals such as EGFR with TGF-alpha. T cells, however, rewire rather than disconnect: restraining interactions are lost, while new Notch and TNF-receptor interactions with neurons appear. Taken together, supportive neuron-glia signalling fades while inflammatory signalling to T cells emerges.

---

## Slide 7. Result 3: proteomics and the AD comparison

On the left, 22 of 2,500 proteins differ, with glutathione metabolism up and ER-to-Golgi transport down. The more robust result comes from WGCNA: two modules, synaptic vesicle cycle and synapse organisation, rise in PD and are enriched for excitatory-neuron genes, which mirrors the up-regulated presynaptic pathways seen at the RNA level.

On the right, they compared with the Mathys 2019 AD dataset from the same region. The headline is zero shared DEGs in neurons. Overlap occurs only in glia: astrocytes share metal-ion detoxification, and microglia share an immune signature including APOE and SPP1. So neuronal vulnerability is disease-specific, whereas glial inflammation is a common denominator.

---

## Slide 8. Take-aways and critical appraisal

For the take-aways: first, this is the first single-cell atlas of PD prefrontal cortex, with paired proteomics and pathology, and the data are public. Second, neuroinflammation is cellular and specific, with more T cells and microglia. Third, excitatory neurons are the vulnerable population, and their chaperone loss scales with alpha-synuclein burden, making HSP90AB1 and DNAJB6 plausible targets. Fourth, neuron-astrocyte support is lost while neuron-T cell Notch signalling appears. Fifth, PD and AD diverge in neurons but converge in glia.

For critical thinking: first, six versus six is very small, so one donor with a score near 12 could drive the correlations, and the proteomic hits are uncorrected. Second, causality is unresolved: we cannot tell whether chaperone loss causes aggregation or follows it. Third, the tissue is end-stage, the investigators were not blinded, and T cells are a very small population.

That's all for my presentation. Thank you for listening.
