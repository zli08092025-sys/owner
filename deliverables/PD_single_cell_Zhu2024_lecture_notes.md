# Lecture notes: Single-cell transcriptomic and proteomic analysis of Parkinson's disease brains

Zhu et al., *Science Translational Medicine* 16, eabo1997 (30 October 2024)

Timing guide: about 15 to 18 minutes in total. Roughly 1.5 minutes for the title and background, 1.5 for objectives, 3.5 for methods, 2.5 for each results slide, and 2.5 for the conclusion, which leaves a few minutes for questions.

---

## Slide 1. Title

Good morning, everyone. Today I'd like to walk you through a paper that came out in *Science Translational Medicine* in October 2024, from Le Zhang, Sreeganga Chandra and David Hafler's groups at Yale. The title is "Single-cell transcriptomic and proteomic analysis of Parkinson's disease brains."

In one sentence, this is the first single-cell map of the Parkinson's disease prefrontal cortex. What makes it a little different from a typical atlas paper, though, is that the authors didn't stop at RNA. They also measured proteins and scored Lewy pathology in the very same pieces of tissue, so the three layers can be compared directly within each donor.

The cohort is small, just six patients with late-stage PD and six age-matched controls, and I'll come back to what that means at the end. But first, let me set up why this study was needed.

---

## Slide 2. Background

Let's start with what we already know about Parkinson's disease. It is the second most common neurodegenerative disorder, affecting roughly one million people in the United States and about six million worldwide. The textbook pathology has two parts: the loss of dopamine neurons in the substantia nigra, which you can see marked in the midbrain on the illustration, and the accumulation of misfolded alpha-synuclein inside neurons, forming the inclusions we call Lewy bodies.

So far, so familiar. However, two things have become clear over the past decade. First, PD is not purely a neuronal disease. Genetic and epidemiological evidence keeps pointing toward glial and immune pathways, and that is what we loosely call neuroinflammation. The problem is that most of that evidence comes from bulk tissue, where neurons, astrocytes, microglia and T cells are all averaged together. As a result, we don't actually know which cell types drive the inflammatory signal, or how much neurons versus glia contribute to sporadic disease.

Second, the cortex has been something of a blind spot. In late-stage PD, Lewy pathology spreads well beyond the midbrain into cortical areas, including the prefrontal cortex, and earlier bulk RNA-seq had flagged this region as abnormal. Yet, at the time this work was done, there was no single-cell map of PD cortex at all. Conveniently, single-nucleus RNA sequencing now makes frozen postmortem brain tractable, because nuclei survive freezing even when whole cells don't.

With that gap in mind, let's look at what the authors set out to do.

---

## Slide 3. Objectives

The overarching question is simple to state: which cell types, which genes, and which cell-to-cell conversations change in late-stage PD cortex, and are those changes specific to PD?

To answer it, the paper breaks into four aims, and I've organised the results slides to follow the same order.

The first aim is to build a cell-type atlas. That means single-nucleus RNA-seq of Brodmann area 9, the dorsolateral prefrontal cortex, from six PD donors and six controls, followed by identifying each cell type and its disease-associated genes and pathways.

The second aim is to anchor those transcriptional changes to something tangible. On one side, that's pathology: they stain the same tissue for phosphorylated alpha-synuclein, score the Lewy burden, and ask whether it correlates with gene expression in neurons. On the other side, it's genetics: they take the known PARK genes and GWAS risk loci and ask in which cell types those genes are actually changing.

The third aim moves from single cells to interactions and proteins. Using ligand-receptor inference, they map communication between neurons, glia and T cells, and in parallel they run mass spectrometry on the same donors and use co-expression network analysis to link protein modules back to cell types.

Finally, the fourth aim is comparative. Since PD and Alzheimer's disease are the two most common late-onset neurodegenerative disorders, and since a single-cell AD dataset from the same cortical region already existed, they ask whether the two diseases share a cellular signature.

Now, before we get to the findings, I want to spend a few minutes on how the data were generated and analysed, because several of the critical points at the end hinge on those choices.

---

## Slide 4. Methods and analysis workflow

This slide looks busy, so let me walk through it lane by lane, from top to bottom.

At the top, the samples. Twelve postmortem donors, prefrontal cortex BA9, six with late-stage PD and six sex- and age-matched controls with a mean age of about 76. All three data streams below come from these same twelve brains, which is the real strength of the design.

The first lane is the single-nucleus RNA-seq pipeline. Nuclei are isolated from frozen tissue by sucrose-gradient ultracentrifugation, then loaded on the 10x Chromium platform and sequenced to roughly 100,000 reads per nucleus. One detail worth noting is the alignment step: they built a custom pre-mRNA reference. The reason is that nuclear RNA is largely unspliced, so a standard transcriptome reference would throw away most of the reads. After quality control, keeping nuclei with between 200 and 7,000 genes to remove debris and doublets, they end up with 77,384 nuclei.

Then comes the Seurat workflow. Each sample is log-normalised and the top 2,000 highly variable genes are selected. Next, and this is important, all twelve donors are integrated using anchor-based integration. In practice, that means the algorithm finds pairs of similar cells across samples and uses them to align the datasets, which removes donor and batch effects while preserving shared biology. After PCA and UMAP they obtain twelve clusters, which they collapse into eight major cell types using canonical markers. Differential expression is then run per cell type with a Wilcoxon rank-sum test, requiring a log fold change above 0.25 and an FDR below 0.05, and pathways are summarised with GO enrichment.

Below that, a row of downstream analyses: proportion tests, variance partitioning, RNA velocity with scVelo, ligand-receptor inference with CellPhoneDB, a GWAS-to-cell-type method called UTMOST, and RNAscope in situ hybridisation on an independent cohort for validation.

The second lane is proteomics. Label-free mass spectrometry on the same tissue quantifies about 2,500 proteins. Differential abundance uses a two-sided t test, and here I should flag that they report nominal P below 0.05 without multiple-testing correction. They then run WGCNA, which clusters proteins into co-expression modules, fourteen in this case, and tests each module for enrichment of cell-type marker genes with a Fisher exact test. That is how a bulk protein measurement gets attributed back to a cell type.

The third lane is pathology: phospho-S129 alpha-synuclein immunohistochemistry, a Lewy body and neurite count per brain, a t test between groups, and then correlation of that score with chaperone gene expression in excitatory neurons.

So why these particular statistics? Briefly: the Wilcoxon test is non-parametric, which suits sparse, zero-inflated single-cell counts, and it is also what the AD atlas used, so the later comparison is like-for-like. FDR control is needed because thousands of genes are tested per cell type. For proteins, log intensities are roughly normal, so a t test is reasonable, but with six versus six nothing survives correction, which the authors acknowledge. And the permutation test inside CellPhoneDB builds an empirical null by shuffling cell labels, so it needs no distributional assumption.

With the pipeline in hand, let's turn to what they found.

---

## Slide 5. Result 1: the atlas

Here is the atlas. On the left, the UMAP of all 77,384 nuclei, coloured by cell type. You can see the eight major populations: excitatory and inhibitory neurons, oligodendrocytes, OPCs, astrocytes, microglia, endothelial cells and, importantly, a small cluster of brain-resident T cells. One reassuring point is that when the same plot is coloured by donor or by disease status, PD and control nuclei overlap within each cluster, so the clustering is driven by cell identity rather than by patient. The variance partition analysis backs this up: cell type explains more than half of the expression variance, donor explains under six percent, and post-mortem interval, age and sex each explain less than half a percent.

Now, what changes in PD? First, proportions. The middle panel shows that most cell types are stable. However, T cells increase about seven-fold, from 33 to 243 nuclei, and that is significant at P equals 0.02. Microglia also roughly double, although that only reaches P equals 0.09, and oligodendrocytes decrease. The microglial and T cell increases were confirmed with RNAscope on independent sections, so they don't rest on the sequencing alone.

Second, the direction of transcriptional change. Look at the table on the right. Neurons have relatively few differentially expressed genes, and most of them go down: 79 percent of excitatory and 67 percent of inhibitory neuron DEGs are down-regulated, and the down-regulated pathways are dominated by protein folding and the unfolded protein response, genes like HSPB1, HSP90AB1, DNAJB6 and HSPA1A. In other words, neurons seem to be losing chaperone capacity.

Glia, by contrast, do the opposite. Astrocytes and microglia carry the largest numbers of DEGs, and theirs are mostly up. Astrocytes switch on metal-ion detoxification genes such as the metallothioneins, microglia activate myeloid differentiation and hematopoiesis programs including FOS, STAT3 and RUNX1, and oligodendrocytes up-regulate protein-complex assembly. Even the T cells show enrichment for IL7R, IL15, CD28 and ZAP70, which suggests an active rather than a bystander population.

So the headline from this first result is an inverse pattern: neurons go quiet while glia and immune cells switch on. The natural next question is whether the neuronal change has anything to do with the pathology itself, and that brings us to the second result.

---

## Slide 6. Result 2: pathology correlation and cell-cell communication

Let's take the left half first. The authors stained the same prefrontal sections for phospho-S129 alpha-synuclein and counted Lewy bodies and Lewy neurites. As expected, controls had essentially none, whereas every PD brain had some, with scores ranging from 0.1 all the way up to about 12. That difference is significant at P equals 0.03, but notice the wide spread between PD donors. That spread is actually useful, because it lets them ask whether more pathology means more transcriptional change.

And it does, at least for chaperones. In the correlation panels, each point is a donor, and the y axis is the pathology score. For most of the protein-folding genes in excitatory neurons, higher Lewy burden goes with lower expression. HSP90AB1 is the strongest, with an R-squared of 0.74, followed by HSPA1A at 0.61, DNAJA4 at 0.58 and HSPB1 at 0.47. Interestingly, HSPA4L, which encodes a disaggregase, is the one that does not correlate, and the authors read that as the disaggregation machinery not being induced to compensate. Equally interesting, inhibitory neurons show the same trend but far more weakly, which fits the long-standing observation that Lewy bodies form mainly in excitatory neurons.

They also looked at the known PD genes. SNCA and LRRK2 are up in PD, and LRRK2 in particular is highest in microglia and OPCs, which echoes earlier findings in blood monocytes. On the other hand, PRKN, PINK1, GBA and PARK7 are down in excitatory neurons, so the direction of change is broadly consistent with the loss-of-function genetics.

Now, moving to the right half: cell-cell communication. This matrix shows, for every pair of cell types, the number of ligand-receptor interactions in PD minus the number in controls, as inferred by CellPhoneDB. The striking thing is that almost the whole matrix is blue. Communication is globally reduced in PD. The hardest-hit pair is excitatory neurons with astrocytes, where roughly a quarter of the interactions are lost, including trophic signals such as EGFR with TGF-alpha and betacellulin, TYRO3 with GAS6, and the SIRPA-CD47 "don't eat me" signal.

T cells, however, behave differently. Rather than simply disconnecting, they rewire. Interactions that restrain immune activation, such as CD74 with APP and the CX3CR1-CX3CL1 axis, are lost in PD, while new Notch and TNF-receptor interactions with neurons appear. Taken together, the picture is that supportive neuron-glia signalling fades while inflammatory signalling to T cells emerges.

That is the RNA story. The third result asks whether the proteins agree, and whether any of this is unique to PD.

---

## Slide 7. Result 3: proteomics, WGCNA and the comparison with AD

Starting on the left with the proteome. From about 2,500 quantified proteins, 22 came out as differentially abundant at a nominal P below 0.05, with CDH2, GSTT1 and N4BP1 among those going up and SEC13, BRCC3 and NDRG2 among those going down. At the pathway level, glutathione metabolism is up, which fits an oxidative-stress response, whereas branched-chain amino acid catabolism and ER-to-Golgi transport are down. Again, I'd remind you these are uncorrected P values, so treat the individual proteins as candidates rather than established findings.

The more robust result comes from the network analysis. WGCNA organised the proteome into fourteen modules, each labelled by its top GO term in the colour bar you see on the dendrogram. Two of those modules, M1 synaptic vesicle cycle and M2 synapse organisation, have higher eigengene expression in PD, and when the authors tested which cell-type markers they contain, both were enriched for excitatory-neuron genes such as HPCA, NPTX1 and SYN2. That matters because it mirrors what they saw at the RNA level, where presynaptic assembly and axonogenesis were the top up-regulated pathways in neurons, and RNA velocity had independently flagged SYN2. So two different molecular layers point to the same synaptic remodelling in excitatory neurons.

Now to the right half, the comparison with Alzheimer's disease. They used the Mathys et al. 2019 single-nucleus dataset from the prefrontal cortex, 24 AD cases and 24 controls, and processed it with the same differential expression settings. The headline is in the first two rows of the table: zero shared differentially expressed genes in excitatory or inhibitory neurons. Not a reduced overlap, but none at all, even though 138 genes overlap across all cell types combined.

Where, then, is the overlap? It is in glia. Astrocytes share the metal-ion detoxification response, metallothioneins again, microglia share an immune activation signature including APOE, SPP1 and APOC1, and oligodendrocytes share a handful of genes. The bar chart shows the top shared pathways, and you can see they are all about cadmium, copper and zinc responses in astrocytes and interferon and innate immune regulation in microglia.

The proteome tells the same story in a different way. Against an AD proteomic dataset from the same region, only a single protein, CDH2, overlaps, yet 12 up- and 17 down-regulated pathways are shared, mostly cytoskeletal transport and ER-to-Golgi trafficking.

So the message of this slide is that neuronal vulnerability appears to be disease-specific, whereas glial inflammation looks like a common denominator across the two diseases.

---

## Slide 8. Take-aways and critical appraisal

Let me pull this together, and then I'd like to spend the remaining time on what I think we should question.

On the left are the five things I would take away. First, this is the first single-cell atlas of PD prefrontal cortex, and crucially it comes with paired proteomics and pathology from the same donors, and all of the data are public on GEO and PRIDE. Second, neuroinflammation in PD is cellular and specific: more T cells, more microglia, defined activation programs in each glial type, and LRRK2 sitting in microglia and OPCs. Third, excitatory neurons are the vulnerable population, and their loss of chaperones scales with alpha-synuclein burden, which makes HSP90AB1 and DNAJB6, both known to restrain alpha-synuclein aggregation, plausible therapeutic targets. Fourth, neuron-astrocyte support is lost while neuron-T cell Notch signalling appears. And fifth, PD and AD diverge in neurons but converge in glia.

That said, there are several points I think deserve discussion, and these are on the right.

The first is sample size. Six versus six is very small for a human cohort. The pathology correlations, in particular, rest on six PD data points, and if you look back at the scatter plots, one donor with a score near 12 sits far from the others and could be driving several of those R-squared values. Likewise, the proteomic hits are uncorrected and the authors themselves say they need replication.

The second point is more technical but, in my view, the most important: pseudoreplication. The Wilcoxon test treats every nucleus as an independent observation, so a cell type with 20,000 nuclei is tested as if it had 20,000 samples, when in reality there are twelve biological replicates. That inflates significance, and it means the 806 DEGs would almost certainly shrink under a donor-level pseudobulk analysis. The variance partition result is reassuring about batch effects, but it does not fix this issue.

Third, correlation is not causation. Is the loss of chaperones a cause of aggregation, or is it a late consequence of neurons that are already dying? The study validates expression changes with RNAscope, which is good, but there is no functional experiment.

Fourth, some design limits: the tissue is late-stage and end-stage, the investigators were not blinded, T cells are a very small population of fewer than 300 nuclei, WGCNA was run on PD and control samples pooled together, and the AD comparison crosses different cohorts, slightly different regions, BA9 versus BA10, and different pipelines.

Finally, what would I do next? Larger cohorts analysed with pseudobulk mixed models, inclusion of early-stage or incidental Lewy body cases to separate cause from consequence, spatial transcriptomics to place the T cells and the lost astrocyte contacts in context, and, most directly, perturbing HSP90AB1 or DNAJB6 in neuron-glia co-cultures to test whether chaperone loss actually accelerates alpha-synuclein aggregation.

With that, I'll stop here. Thank you, and I'm happy to take questions.
