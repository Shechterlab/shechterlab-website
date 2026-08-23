---
title: Resources
type: landing
sections:
  - block: markdown
    content:
      title: Resources
      text: |
        ## Lab Wiki

        Current lab members: internal protocols, onboarding checklists, and equipment SOPs live on the [Lab Wiki ↗](https://wiki.shechterlab.org). (Login required — ask David or a current member for access.)

        ## Protocols

        Selected protocols from the lab are available on [protocols.io](https://www.protocols.io/researchers/shechter-lab) and in the publications listed below. For additional protocols, email David.

        - **EZ-MTase methyltransferase activity assay** — Burgos et al., 2017. The SAH deaminase plasmid (TM0936) is available from [DNASU](http://dnasu.org/DNASU/GetCloneDetail.do?cloneid=84735).
        - **Chromatin characterization in *Xenopus* egg extracts** — Wang, Onikubo & Shechter, *Cold Spring Harbor Protocols*, 2019.
        - Fractionated RNA-seq, CUT&RUN, ATAC-seq, and PRO-seq protocols from the lab_pipelines repository: [github.com/shechterlab](https://github.com/Shechterlab)

        ## Plasmids

        Lab constructs are available upon request. Email David with the specific vector and insert you need. Selected plasmids will be deposited to [Addgene — Shechter Lab](https://www.addgene.org/David_Shechter/) as deposits are made; the PI page will activate once the first deposit is live.

        ## Data

        Published datasets are deposited to GEO and linked in the relevant publications. Direct links to selected datasets:

        - Chen et al. 2017: [GSE80182](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80182)

        Additional datasets from recent papers are linked in each publication entry.

        ## Code

        Analysis code, bioinformatics pipelines (RNA-seq, ATAC-seq, CUT&RUN, PRO-seq, fractionated proteomics), and reproducible workflows are maintained at [github.com/shechterlab](https://github.com/Shechterlab).

        ## Recombinant proteins

        Purified recombinant proteins (PRMT5-MEP50 complex, nucleoplasmin, NPM1, NAP1, and others) are shared with collaborators on request.

        ## Deposited structures

        Interactive viewers for structures the lab has deposited to the [PDB](https://www.rcsb.org). Each links through to its full RCSB entry (sequence, experimental data, citation) below the viewer.

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;margin-top:1.5rem">
          <div>
            <div id="pdb-viewer-4g56" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/4G56">4G56 ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6w4l" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6W4L">6W4L ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6oi0" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6OI0">6OI0 ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6oi1" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6OI1">6OI1 ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6oi2" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6OI2">6OI2 ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6oi3" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6OI3">6OI3 ↗</a></p>
          </div>
          <div>
            <div id="pdb-viewer-6ofz" style="width:100%;height:240px;border-radius:8px;overflow:hidden;background:#f8fafc"></div>
            <p style="text-align:center;margin-top:0.4rem;font-size:0.875rem"><a href="https://www.rcsb.org/structure/6OFZ">6OFZ ↗</a></p>
          </div>
        </div>

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pdbe-molstar@latest/build/pdbe-molstar-light.css">
        <script src="https://cdn.jsdelivr.net/npm/pdbe-molstar@latest/build/pdbe-molstar-plugin.js"></script>
        <script>
        document.addEventListener('DOMContentLoaded', function () {
          if (typeof PDBeMolstarPlugin === 'undefined') return;
          ['4g56','6w4l','6oi0','6oi1','6oi2','6oi3','6ofz'].forEach(function (id) {
            var el = document.getElementById('pdb-viewer-' + id);
            if (!el) return;
            new PDBeMolstarPlugin().render(el, {
              moleculeId: id,
              bgColor: { r: 248, g: 250, b: 252 },
              hideControls: true,
              hideCanvasControls: ['selection', 'animation', 'controls-info', 'controls-help', 'controls-full-screen'],
              sequencePanel: false,
              landscape: false
            });
          });
        });
        </script>

        ## Key tools we rely on

        | Tool | Use |
        |------|-----|
        | [Geneious](https://www.geneious.com) | DNA/protein sequence management |
        | [Benchling](https://www.benchling.com) | Molecular biology tools |
        | [LabArchives](https://www.labarchives.com) | Electronic lab notebooks |
        | [Prism](https://www.graphpad.com/features) | Statistics and plotting |
        | [UCSF Chimera](https://www.cgl.ucsf.edu/chimera/) | Structural visualization |
        | [Fiji/ImageJ](https://fiji.sc) | Image analysis |
        | [deeptools](https://deeptools.readthedocs.io) | ChIP/ATAC-seq analysis |
        | [DESeq2](https://bioconductor.org/packages/DESeq2) | RNA-seq differential expression |
---
