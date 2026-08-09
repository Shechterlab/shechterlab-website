---
title: ''
date: 2026-06-28
type: landing

design:
  spacing: '5rem'

sections:
  - block: hero
    id: about
    content:
      title: |
        Decoding the protein chemistry behind cancer and ALS
      text: "The Shechter Lab at Albert Einstein College of Medicine studies how chromatin and RNA-processing proteins are chemically modified — and how that goes wrong in NPM1-mutant leukemia and C9orf72 ALS."
      primary_action:
        text: Explore Research
        url: '/research'
        icon: hero/beaker
      secondary_action:
        text: View Publications
        url: '#publications'
    design:
      background:
        image:
          filename: "lab/david-with-colleague.jpg"
          filters:
            brightness: 0.65
            contrast: 1.05
          parallax: false
          position: center 30%
          size: cover
        color: '#155e75'
        text_color_light: true
      spacing:
        padding: ['96px', '0', '96px', '0']
      no_padding: true

  - block: stats
    content:
      items:
        - statistic: "17"
          description: Years at Einstein
          sub_metric: Lab founded 2009 · Department of Biochemistry
          icon: hero/building-library
        - statistic: "4"
          description: Active research areas
          sub_metric: Methylation, chaperones, methyl economy, translational chromatin biology
          icon: hero/beaker
        - statistic: "30+"
          description: Trainees mentored
          sub_metric: PhD, MD-PhD, postdoctoral, instructor, undergraduate, high-school
          icon: hero/users
        - statistic: "h = 29"
          description: Google Scholar
          sub_metric: 6000+ citations across original research and reviews
          icon: hero/document-text
    design:
      layout: cards
      css_class: "bg-gradient-to-b from-primary-50 to-white dark:from-primary-900/20 dark:to-gray-800"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: research-areas
    id: research
    content:
      title: Research Areas
      subtitle: Mechanism first, disease relevance built in
      text: We focus on how chemically defined protein modifications reshape nuclear proteins, chromatin organization, RNA fate, and the cellular allocation of methylation potential.
      items:
        - name: Protein Arginine Methylation and Gene Regulation
          description: We define how PRMTs control chromatin, transcription, splicing, and transcript retention, with central work on PRMT5-dependent regulation of RNA processing and the discovery of GRIPPs as a chromatin-tethered mRNA reserve.
          icon: hero/document-text
          gradient: from-blue-400 to-indigo-600
          status: active
          topics:
            - PRMT5
            - Splicing and intron detention
            - GRIPPs and chromatin escape
            - Histone gene regulation
            - PRMT inhibitor biology
          cta:
            text: Read more
            url: /research/arginine-methylation
        - name: Histone Chaperones, Glutamylation, and Intrinsically Disordered Regions
          description: We define how acidic intrinsically disordered regions in histone chaperones encode DNA mimicry and chromatin assembly capacity, and how PTMs such as glutamylation tune those properties in normal physiology and disease.
          icon: hero/adjustments-horizontal
          gradient: from-fuchsia-400 to-rose-600
          status: active
          topics:
            - NPM1, NPM2, Nap1, PTMA
            - TTLL4 glutamyltransferase
            - Acidic disordered regions
            - Chromatin assembly
            - DNA mimicry
          cta:
            text: Read more
            url: /research/glutamylation-chaperones
        - name: The Methyl Economy of Cellular Proliferation
          description: We test the idea that proliferating cells solve an allocation problem for one-carbon methylation potential — tuning supply through GNMT and gating demand through PRMT5-dependent H4 methylation, which controls histone production and genome packaging.
          icon: hero/scale
          gradient: from-amber-400 to-orange-600
          status: active
          topics:
            - SAM and SAH homeostasis
            - GNMT and one-carbon flux
            - Histone supply and S-phase
            - Methyl-spending hierarchy
            - PEMT and NNMT
          cta:
            text: Read more
            url: /research/methyl-economy
        - name: Translational Chromatin Biology in Cancer, ALS, and Aging
          description: We connect mechanistic biochemistry to disease biology in NPM1-mutant AML, C9orf72 ALS, and aging-related methylation, working with chemistry, structural biology, and clinical collaborators to identify and validate targets.
          icon: hero/bolt
          gradient: from-emerald-400 to-teal-600
          status: active
          topics:
            - NPM1-mutant AML
            - C9orf72 ALS
            - PRMT inhibitor biology
            - Aging and one-carbon metabolism
            - Target validation
          cta:
            text: Read more
            url: /research/disease-mechanisms
      cta:
        text: Browse active projects
        url: /#projects
        icon: hero/arrow-right
    design:
      layout: cards
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"

  - block: cta-image-paragraph
    content:
      items:
        - title: 'A through-line from replication checkpoints to chromatin methylation'
          text: |
            Recent work in the lab shows how PRMT5 sustains S-phase histone production through H4 methylation, identifies GRIPPs as a class of chromatin-tethered incompletely spliced mRNA released post-transcriptionally on PRMT5 activity, and traces how the GNMT N-terminus couples folate feedback to SAM and SAH homeostasis. The common thread: how cells allocate a limited pool of methylation potential across competing reactions without losing control of proliferation.
          image: research/nucleosome-cartoon.jpg
          feature_icon: hero/check-circle
          features:
            - 'Biochemistry and enzymology linked to cell-based and genomic readouts'
            - 'Mechanistic focus on PTMs in charged and intrinsically disordered regions'
            - 'Disease-facing projects in AML, ALS, and aging'
          button:
            text: 'Featured projects'
            url: '/#projects'
        - title: 'Training and scientific culture'
          text: |
            The lab prioritizes rigorous mentorship, careful experimental design, and active participation in the chromatin community. This includes directing the graduate course *Gene Expression: Beyond the Double Helix*, founding and leading the [NYC Chromatin Club](https://www.nycchromatinclub.org/), co-organizing the Einstein Chromatin Club joint lab meetings since 2011, and a strong track record of trainee success from PhD students and MD-PhD trainees through to postdocs and undergraduates.
          image: lab/lab-photo-2026.jpg
          feature_icon: hero/users
          features:
            - 'Strong mentoring record across PhD, MD-PhD, postdoctoral, undergraduate, and high-school trainees'
            - 'Course leadership in Gene Expression: Beyond the Double Helix and the graduate curriculum'
            - 'Open, discussion-driven lab environment with deep biochemistry training'
          button:
            text: 'Join the lab'
            url: '/opportunities'
    design:
      css_class: "bg-white dark:bg-gray-800"

  - block: features
    id: values
    content:
      title: Lab Values
      subtitle: How we work
      text: ''
      items:
        - name: Mechanistic Curiosity
          description: We want to know how things actually work at the molecular level, not just that they happen.
          icon: hero/magnifying-glass
        - name: Biochemistry First
          description: In vitro reconstitution and quantitative enzymology tell us what's mechanistically possible before we interpret what's happening in cells and genomes.
          icon: hero/beaker
        - name: Integrative Thinking
          description: Molecular biology, genomics, structural biology, and metabolomics each catch something the others miss — we use whichever tool answers the question.
          icon: hero/puzzle-piece
        - name: Discovery with Purpose
          description: A new mechanism matters more when it connects to a disease context — cancer, ALS, or aging — where it can eventually be tested.
          icon: hero/light-bulb
        - name: Rigor, Reproducibility, and Openness
          description: Careful experimental design, and data and methods shared openly enough for others to build on.
          icon: hero/check-badge
        - name: Mentorship and Growth
          description: Independence and intellectual risk-taking, supported at every career stage from rotation student to postdoc.
          icon: hero/users
    design:
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"

  - block: team-showcase
    id: team
    content:
      title: Lab Members
      subtitle: ''
      text: 'A view of the current lab. For full current roster and alumni, see the [People page](/people).'
      sort_by: 'Params.last_name'
      sort_ascending: true
      cta:
        text: View full roster
        url: /people
        icon: user-group
    design:
      show_role: true
      show_organizations: false
      show_interests: true
      show_social: true
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: collection
    id: projects
    content:
      title: Featured Projects
      subtitle: ''
      text: ''
      filters:
        folders:
          - projects
      count: 0
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: publications
    content:
      title: Selected Publications
      text: 'A curated selection. The full bibliography is available in the [CV](/uploads/shechter-cv-2026.pdf).'
      filters:
        folders:
          - publications
        exclude_featured: false
      count: 8
    design:
      view: citation


  - block: logos
    id: funders
    content:
      title: Supported by
      subtitle: ''
      items:
        - name: NIH / NIGMS
          url: https://www.nigms.nih.gov
        - name: NIH / NIA
          url: https://www.nia.nih.gov
        - name: ALS Therapy Development Institute
          url: https://www.als.net
        - name: Hevolution Foundation
          url: https://hevolution.com
        - name: Irma T. Hirschl Trust
          url: https://irmatrust.org
        - name: Montefiore Einstein Cancer Center
          url: https://einsteinmed.edu/centers/cancer/
        - name: Einstein 2030 Fund
          url: https://einsteinmed.edu
    design:
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: markdown
    id: collaborators
    content:
      title: Collaborators
      subtitle: ''
      text: |
        We work closely with [ALS Therapy Development Institute](https://www.als.net) (primary partner on C9orf72 ALS) and with colleagues at Einstein — [Matthew Gamble](https://einsteinmed.edu/faculty/gamble) (chromatin), [Charles Query](https://einsteinmed.edu/faculty/query) (splicing), [Simone Sidoli](https://einsteinmed.edu/faculty/sidoli) (proteomics), [Kira Gritsman](https://einsteinmed.edu/faculty/gritsman) (leukemia), [Seiya Kitamura](https://einsteinmed.edu/faculty/kitamura) (medicinal chemistry), and [Steven Almo](https://einsteinmed.edu/faculty/almo) (structural biology) — as well as [Jie Jiang](https://www.emory.edu) (Emory, ALS) and [David Cowburn](https://einsteinmed.edu/faculty/cowburn) (NMR).
    design:
      spacing:
        padding: ["3rem", 0, "2rem", 0]

  - block: contact-info
    id: contact
    content:
      title: Contact
      subtitle: Get in touch about research, training, or collaboration
      visit_title: Visit
      connect_title: Connect
      address:
        lines:
          - Shechter Lab
          - Department of Biochemistry
          - Albert Einstein College of Medicine
          - Forchheimer 304
          - 1300 Morris Park Avenue
          - Bronx, NY 10461
      office_hours:
        - "By appointment"
      email: david.shechter@einsteinmed.edu
      phone: "+1 (718) 430-4120"
      social:
        - icon: brands/orcid
          url: https://orcid.org/0000-0001-9388-6004
        - icon: brands/google-scholar
          url: https://scholar.google.com/citations?user=Mz9sZUoAAAAJ
      prospective:
        title: Prospective lab members
        text: Rotation students, graduate applicants, postdocs, and collaborators are welcome to reach out.
        button:
          text: See opportunities
          url: /contact
      map_url: https://maps.google.com/?q=Albert+Einstein+College+of+Medicine+1300+Morris+Park+Ave+Bronx+NY+10461
      show_form: false
    design:
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"
      spacing:
        padding: ["5rem", 0, "5rem", 0]
---
