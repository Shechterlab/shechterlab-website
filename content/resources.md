---
title: Resources
type: landing
sections:
  - block: markdown
    content:
      title: Resources
      text: |
        <nav style="display:flex;flex-wrap:wrap;justify-content:center;gap:0.5rem 1.25rem;margin-bottom:1rem;font-size:0.9rem;font-weight:600">
          <a href="#lab-wiki">Lab Wiki</a>
          <a href="#protocols">Protocols</a>
          <a href="#plasmids">Plasmids</a>
          <a href="#data">Data</a>
          <a href="#code">Code</a>
          <a href="#recombinant-proteins">Recombinant proteins</a>
          <a href="#equipment">Equipment</a>
          <a href="#deposited-structures">Structures</a>
          <a href="#deposited-em-maps">EM maps</a>
          <a href="#molecular-dynamics-simulations">MD simulations</a>
        </nav>

        <h2 id="lab-wiki">Lab Wiki</h2>

        Current lab members: internal protocols, onboarding checklists, and equipment SOPs live on the [Lab Wiki ↗](https://wiki.shechterlab.org). (Login required — ask David or a current member for access.)

        <h2 id="protocols">Protocols</h2>

        Selected protocols are below.

        - **EZ-MTase methyltransferase activity assay** — Burgos et al., 2017. The SAH deaminase plasmid (TM0936) is available from [DNASU](http://dnasu.org/DNASU/GetCloneDetail.do?cloneid=84735).
        - **Chromatin characterization in *Xenopus* egg extracts** — Wang, Onikubo & Shechter, *Cold Spring Harbor Protocols*, 2019.
        - Fractionated RNA-seq, CUT&RUN, ATAC-seq, and PRO-seq protocols from the lab_pipelines repository: [github.com/shechterlab](https://github.com/Shechterlab)

        <h2 id="plasmids">Plasmids</h2>

        Most lab constructs are available on [Addgene — Shechter Lab](https://www.addgene.org/David_Shechter/).

        <h2 id="data">Data</h2>

        Published datasets are deposited to [GEO](https://www.ncbi.nlm.nih.gov/geo/) and linked in the relevant publications.

        | Accession | Series |
        |---|---|
        | [GSE334611](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE334611) | PRMT5 Activity Sustains Histone Production to Maintain Genome Integrity — CUT&Tag (Roth et al.) |
        | [GSE333723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE333723) | The GNMT N-terminus Couples Folate Feedback to Methyl-donor Homeostasis |
        | [GSE301721](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301721) | PRMT5 Activity Sustains Histone Production to Maintain Genome Integrity — CUT&RUN (Roth et al.) |
        | [GSE275220](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275220) | Productive mRNA Chromatin Escape is Promoted by PRMT5 Methylation of SNRPB — PRO-seq, PRMT inhibition (15m/3hr) |
        | [GSE275217](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275217) | Productive mRNA Chromatin Escape is Promoted by PRMT5 Methylation of SNRPB — PRO-seq, PRMT inhibition + dexamethasone |
        | [GSE275215](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275215) | Productive mRNA Chromatin Escape is Promoted by PRMT5 Activity — cytoplasm/nucleoplasm/chromatin fractions |
        | [GSE275214](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275214) | Productive mRNA Chromatin Escape is Promoted by PRMT5 Activity — mRNA-seq, PRMT5/pICln/RIOK1/CoPR5 knockdown |
        | [GSE163421](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163421) | Type I and II PRMTs Inversely Regulate Post-Transcriptional Intron Detention (SKaTER-seq) |
        | [GSE158625](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158625) | Transcriptomic and Proteomic Regulation through Abundant, Dynamic, and Independent Arginine Methylation by Type I and Type II PRMTs |
        | [GSE80182](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80182) | A TGFβ-PRMT5-MEP50 Axis Regulates Cancer Cell Invasion (Chen et al. 2017) |

        Additional datasets from recent papers are linked in each publication entry.

        **Proteomics datasets** — mass spectrometry data from the lab is deposited to the [ProteomeXchange](http://www.proteomexchange.org) Consortium via the [PRIDE](https://www.ebi.ac.uk/pride/) partner repository, and older datasets to [Chorus](https://chorusproject.org).

        | Accession | Repository | Dataset |
        |---|---|---|
        | [PXD065294](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD065294) | PRIDE / ProteomeXchange | Total cell and fractionated LC-MS/MS — [Roth et al.](/publications/prmt5-histone-production-2025/) |
        | [PXD078525](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD078525) | PRIDE / ProteomeXchange | Proteomics — [Kraz et al.](/publications/gnmt-folate-methyl-donor-2026/) |
        | [PXD054308](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD054308) | PRIDE / ProteomeXchange | Total cell and fractionated LC-MS/MS — [DeAngelo et al.](/publications/productive-mrna-chromatin-escape-2025/) |
        | [CHORUS:1725](https://chorusproject.org) | Chorus | Total arginine analysis — [Maron et al., 2021](/publications/maron-prmts-iscience-2021/) |
        | [CHORUS:1671](https://chorusproject.org) | Chorus | PTMScan methylarginine — [Maron et al., 2021](/publications/maron-prmts-iscience-2021/) |

        **Metabolomics** — deposited to [MetaboLights](https://www.ebi.ac.uk/metabolights/).

        | Accession | Dataset |
        |---|---|
        | [MTBLS15161](https://www.ebi.ac.uk/metabolights/MTBLS15161) | [Kraz et al.](/publications/gnmt-folate-methyl-donor-2026/) |

        **Structural & biophysical data** — NMR chemical shifts deposited to the [BMRB](https://bmrb.io) and SAXS envelopes to [SASBDB](https://www.sasbdb.org).

        | Accession | Repository | Dataset |
        |---|---|---|
        | [BMRB 52244](https://bmrb.io/data_library/summary/index.php?bmrbId=52244) | BMRB | NMR chemical shifts — [Lorton et al.](/publications/h3r2-methylation-wdr5-switch-2020/) |
        | [BMRB 26809](https://bmrb.io/data_library/summary/index.php?bmrbId=26809) | BMRB | Npm tail domain chemical shifts — [Warren et al., 2017](/publications/nucleoplasmin-intramolecular-regulation-2017/) |
        | [SASDBY4](https://www.sasbdb.org/data/SASDBY4/) | SASBDB | SAXS envelope — [Warren et al., 2017](/publications/nucleoplasmin-intramolecular-regulation-2017/) |

        <h2 id="code">Code</h2>

        Analysis code, bioinformatics pipelines (RNA-seq, ATAC-seq, CUT&RUN, PRO-seq, fractionated proteomics), and reproducible workflows are maintained at [github.com/shechterlab](https://github.com/Shechterlab).

        <h2 id="recombinant-proteins">Recombinant proteins</h2>

        Purified recombinant proteins (PRMT5-MEP50 complex, nucleoplasmin, NPM1, NAP1, and others) are shared with collaborators on request.

        <h2 id="equipment">Lab equipment</h2>

        The lab occupies renovated space on the 3rd floor of the Forchheimer Building at Einstein — two adjoining rooms (~2,100 sq ft total) with bench positions for 12, a dedicated tissue culture room, and David's office next door.

        **In the lab:**

        - Two FPLC systems (AKTA Pure 25M, AKTA Purifier 10) plus an Agilent 1270 HPLC for small-molecule/peptide/histone purification
        - Keyence BZ-X810 automated fluorescence microscope (structured-illumination super-resolution, 4×–60× objectives)
        - GE LAS-4000 chemiluminescence/fluorescence imager for blots and gels
        - Reichert 2SPR (surface plasmon resonance) for binding studies
        - Sorvall XTR and X1R centrifuges, Beckman 22R chilled microcentrifuge
        - Nanodrop 2000C spectrophotometer; sonicator; Milli-Q water purification
        - Tissue culture hood, CO₂ incubators, and liquid-nitrogen cryostorage
        - −80°C and −30°C freezers on emergency power; Labconco lyophilizer/SpeedVac

        **Department and campus core access:** additional ultracentrifuges and PCR/qPCR instruments (QuantStudio 6 Pro), an Octet BLI system, a Malvern PEAQ-ITC, and — through Einstein's shared cores — mass spectrometry (Orbitrap Fusion Lumos, Orbitrap Exploris 480, timsTOF HT), solution NMR up to 900 MHz via the NY Structural Biology Center, in-house and synchrotron X-ray crystallography, cryo-EM, and an institutional HPC cluster.

        [Photos of lab &amp; department equipment →](/lab-life/#lab-dept-equipment)

        <h2 id="deposited-structures">Deposited structures</h2>

        Structures the lab has deposited to the [PDB](https://www.rcsb.org). "View structure" opens an interactive 3D viewer in a new tab; each card also links directly to its RCSB entry and, where applicable, the associated publication.

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;margin-top:1rem;font-size:0.85rem">
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">PRMT5–MEP50 complex</p>
            <img src="https://cdn.rcsb.org/images/structures/4g56_assembly-1.jpeg" alt="4G56 structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=4G56" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/4G56" target="_blank" rel="noopener" style="display:block">4G56 (RCSB) ↗</a>
            <a href="/publications/prmt5-mep50-structure-2013/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">GNMT</p>
            <img src="https://cdn.rcsb.org/images/structures/12yi_assembly-1.jpeg" alt="12YI structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=12YI" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/12YI" target="_blank" rel="noopener" style="display:block">12YI (RCSB) ↗</a>
            <a href="/publications/gnmt-folate-methyl-donor-2026/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">H2A–H2B histone chimera</p>
            <img src="https://cdn.rcsb.org/images/structures/6w4l_assembly-1.jpeg" alt="6W4L structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6W4L" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6W4L" target="_blank" rel="noopener" style="display:block">6W4L (RCSB) ↗</a>
            <a href="/publications/single-chain-h2a-h2b-structure-2020/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">WDR5 (apo)</p>
            <img src="https://cdn.rcsb.org/images/structures/6ofz_assembly-1.jpeg" alt="6OFZ structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6OFZ" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6OFZ" target="_blank" rel="noopener" style="display:block">6OFZ (RCSB) ↗</a>
            <a href="/publications/h3r2-methylation-wdr5-switch-2020/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">WDR5 + L-arginine</p>
            <img src="https://cdn.rcsb.org/images/structures/6oi0_assembly-1.jpeg" alt="6OI0 structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6OI0" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6OI0" target="_blank" rel="noopener" style="display:block">6OI0 (RCSB) ↗</a>
            <a href="/publications/h3r2-methylation-wdr5-switch-2020/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">WDR5 + monomethylarginine</p>
            <img src="https://cdn.rcsb.org/images/structures/6oi1_assembly-1.jpeg" alt="6OI1 structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6OI1" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6OI1" target="_blank" rel="noopener" style="display:block">6OI1 (RCSB) ↗</a>
            <a href="/publications/h3r2-methylation-wdr5-switch-2020/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">WDR5 + symmetric dimethylarginine</p>
            <img src="https://cdn.rcsb.org/images/structures/6oi2_assembly-1.jpeg" alt="6OI2 structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6OI2" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6OI2" target="_blank" rel="noopener" style="display:block">6OI2 (RCSB) ↗</a>
            <a href="/publications/h3r2-methylation-wdr5-switch-2020/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">WDR5 + H3R2 methylarginine peptide</p>
            <img src="https://cdn.rcsb.org/images/structures/6oi3_assembly-1.jpeg" alt="6OI3 structure preview" loading="lazy" onerror="this.style.display='none'" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?pdb=6OI3" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View structure ↗</a>
            <a href="https://www.rcsb.org/structure/6OI3" target="_blank" rel="noopener" style="display:block">6OI3 (RCSB) ↗</a>
            <a href="/publications/h3r2-methylation-wdr5-switch-2020/" style="display:block">Publication →</a>
          </div>
        </div>

        <h2 id="deposited-em-maps">Deposited EM maps</h2>

        Cryo-EM reconstructions of nucleoplasmin (egg, oocyte, and recombinant forms) deposited to the [EMDB](https://www.ebi.ac.uk/emdb). "View map" opens an interactive viewer in a new tab.

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;margin-top:1rem;font-size:0.85rem">
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">Nucleoplasmin (egg)</p>
            <img src="https://www.ebi.ac.uk/pdbe/static/entry/EMD-2866/400_EMD-2866.gif" alt="EMD-2866 map preview" loading="lazy" onerror="if(!this.dataset.f){this.dataset.f=1;this.src='https://www.ebi.ac.uk/emdb/images/entry/EMD-2866/400_EMD-2866.gif';}else{this.style.display='none';}" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?emdb=EMD-2866" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View map ↗</a>
            <a href="https://www.ebi.ac.uk/emdb/EMD-2866" target="_blank" rel="noopener" style="display:block">EMD-2866 (EMDB) ↗</a>
            <a href="/publications/nucleoplasmin-ptm-histone-sequestration-2015/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">Nucleoplasmin (oocyte)</p>
            <img src="https://www.ebi.ac.uk/pdbe/static/entry/EMD-2868/400_EMD-2868.gif" alt="EMD-2868 map preview" loading="lazy" onerror="if(!this.dataset.f){this.dataset.f=1;this.src='https://www.ebi.ac.uk/emdb/images/entry/EMD-2868/400_EMD-2868.gif';}else{this.style.display='none';}" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?emdb=EMD-2868" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View map ↗</a>
            <a href="https://www.ebi.ac.uk/emdb/EMD-2868" target="_blank" rel="noopener" style="display:block">EMD-2868 (EMDB) ↗</a>
            <a href="/publications/nucleoplasmin-ptm-histone-sequestration-2015/" style="display:block">Publication →</a>
          </div>
          <div style="border:1px solid #e2e8f0;border-radius:8px;padding:0.75rem;text-align:center">
            <p style="font-weight:600;margin-bottom:0.4rem">Nucleoplasmin (recombinant)</p>
            <img src="https://www.ebi.ac.uk/pdbe/static/entry/EMD-2869/400_EMD-2869.gif" alt="EMD-2869 map preview" loading="lazy" onerror="if(!this.dataset.f){this.dataset.f=1;this.src='https://www.ebi.ac.uk/emdb/images/entry/EMD-2869/400_EMD-2869.gif';}else{this.style.display='none';}" style="width:100%;border-radius:6px;margin-bottom:0.5rem;background:#f1f5f9">
            <a href="https://molstar.org/viewer/?emdb=EMD-2869" target="_blank" rel="noopener" style="display:block;margin-bottom:0.3rem">▶ View map ↗</a>
            <a href="https://www.ebi.ac.uk/emdb/EMD-2869" target="_blank" rel="noopener" style="display:block">EMD-2869 (EMDB) ↗</a>
            <a href="/publications/nucleoplasmin-ptm-histone-sequestration-2015/" style="display:block">Publication →</a>
          </div>
        </div>

        <h2 id="molecular-dynamics-simulations">Molecular dynamics simulations</h2>

        *(Links to the lab's deposited MD simulation data — placeholder pending final repository/accession details.)*
    design:
      spacing:
        padding: ['1.5rem', '0', '2rem', '0']
---
