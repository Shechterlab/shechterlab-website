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
        - statistic: "16"
          description: Years at Einstein
          sub_metric: Joined November 2009 · Department of Biochemistry
          icon: hero/building-library
        - statistic: "2"
          description: Molecular research areas
          sub_metric: Methylation and RNA processing · Glutamylation and chaperones — spanning 3 disease areas
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
      subtitle: Two molecular research areas
      text: Both areas start from the same question — how a specific chemical modification changes what a protein does — and follow it from purified enzymes into cells and disease models.
      items:
        - name: PRMTs, GNMT, and Methylation in Gene Regulation and RNA Processing
          description: We study how PRMT5 methylates histones and splicing factors to control chromatin and mRNA processing, and how PRMT-dependent regulation may go wrong in C9orf72 ALS. GNMT sets the methyl-donor supply that all of this methylation draws on, tying the two together.
          icon: hero/document-text
          gradient: from-blue-400 to-indigo-600
          status: active
          topics:
            - PRMT5
            - GNMT and SAM homeostasis
            - Splicing and RNA processing
            - Histone gene regulation
            - C9orf72 ALS
          cta:
            text: Read more
            url: /research/arginine-methylation
        - name: Glutamylation, Histone Chaperones, and Intrinsically Disordered Regions
          description: Histone chaperones use long, acidic, disordered stretches to mimic DNA and grab onto histones. We're working out how modifications like glutamylation tune that behavior — and what happens when it's hijacked in NPM1-mutant leukemia.
          icon: hero/adjustments-horizontal
          gradient: from-fuchsia-400 to-rose-600
          status: active
          topics:
            - NPM1, NPM2, Nap1, PTMA
            - TTLL4 glutamyltransferase
            - Acidic disordered regions
            - Chromatin assembly
            - NPM1-mutant AML
          cta:
            text: Read more
            url: /research/glutamylation-chaperones
      cta:
        text: Browse active projects
        url: /#projects
        icon: hero/arrow-right
    design:
      layout: cards
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"

  - block: research-areas
    id: disease-focus
    content:
      title: Disease Focus
      subtitle: Three diseases, one question each
      text: In each case we start from an enzyme we understand mechanistically and ask whether that mechanism is actually driving disease — and whether it's a target.
      items:
        - name: C9orf72 Amyotrophic Lateral Sclerosis
          description: Arginine methylation shapes how RNA-binding proteins, stress granules, and nuclear transport behave. In C9orf72 ALS, we're asking whether PRMT inhibition — and PRMT-dependent control of TDP-43 cryptic exons — is a real therapeutic angle.
          icon: hero/beaker
          gradient: from-sky-400 to-blue-600
          status: active
          topics:
            - C9orf72 ALS
            - TDP-43 cryptic exons
            - PRMT inhibitor biology
          cta:
            text: Read more
            url: /research/als
        - name: NPM1-Mutant Acute Myeloid Leukemia
          description: We found that TTLL4 glutamylates NPM1c, the mutant driver of this leukemia, changing how it associates with chromatin and reshaping the oncogenic transcriptional program. That makes TTLL4 a therapeutic target we're now pursuing directly.
          icon: hero/bolt
          gradient: from-emerald-400 to-teal-600
          status: active
          topics:
            - NPM1-mutant AML
            - TTLL4 glutamyltransferase
            - Target validation
          cta:
            text: Read more
            url: /research/aml
        - name: Aging and One-Carbon Metabolism
          description: GNMT sits at the center of the methyl economy. With the Huffman and Gavathiotis labs, we're testing whether shifting methyl-donor flux through GNMT can move aging-related transcriptional and metabolic programs.
          icon: hero/clock
          gradient: from-amber-400 to-orange-600
          status: active
          topics:
            - GNMT
            - One-carbon metabolism
            - Dietary restriction
          cta:
            text: Read more
            url: /research/aging
      cta:
        text: Browse active projects
        url: /#projects
        icon: hero/arrow-right
    design:
      layout: cards
      css_class: "bg-white dark:bg-gray-800"

  - block: cta-image-paragraph
    content:
      items:
        - title: 'From enzyme mechanism to leukemia and ALS'
          text: |
            Two projects show how this works in practice. TTLL4-mediated glutamylation of NPM1c looks like a real vulnerability in NPM1-mutant AML, and we're testing whether PRMT-dependent control of TDP-43 cryptic exon splicing can be turned into a therapeutic angle in C9orf72 ALS. In both cases we started with the enzyme mechanism and only then went looking for the disease connection.
          image: research/nucleosome-cartoon.jpg
          feature_icon: hero/check-circle
          features:
            - 'Disease-facing projects in AML, ALS, and aging'
            - 'Biochemistry and enzymology linked to cell-based and genomic readouts'
            - 'Mechanistic focus on PTMs in charged and intrinsically disordered regions'
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

  - block: team-showcase
    id: team
    content:
      title: Lab Members
      subtitle: ''
      text: 'A view of the current lab. For full current roster and alumni, see the [People page](/people).'
      sort_by: 'weight'
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

  - block: collection
    id: projects
    content:
      title: Featured Projects
      subtitle: ''
      text: ''
      filters:
        folders:
          - projects
        featured_only: true
      count: 0
    design:
      view: date-title-summary

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
