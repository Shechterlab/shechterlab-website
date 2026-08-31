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
        Decoding the biochemistry behind cancer and ALS
      text: "The Shechter Lab at Albert Einstein College of Medicine in New York City studies how chemical modifications control chromatin and RNA processing: glutamylation of histone chaperones in NPM1-mutant leukemia, and arginine methylation of RNA-binding proteins in C9orf72 ALS."
      primary_action:
        text: Explore Research
        url: '/research'
        icon: hero/beaker
      secondary_action:
        text: View Publications
        url: '/publications'
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

  - block: markdown
    id: stats
    content:
      text: |
        <div class="stats-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));gap:1.5rem;max-width:80rem;width:100%;margin:0 auto">
          <a href="/history" class="stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:2rem;text-align:center;border:1px solid rgba(0,0,0,0.06);transition:box-shadow .2s">
            <div class="stat-num" data-count="17" style="font-size:2.75rem;font-weight:900;line-height:1">0</div>
            <div style="margin-top:0.5rem;font-weight:600">Years at Einstein</div>
            <div style="margin-top:0.4rem;font-size:0.8rem;opacity:0.65">Lab founded 2009 · Department of Biochemistry</div>
          </a>
          <a href="/research" class="stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:2rem;text-align:center;border:1px solid rgba(0,0,0,0.06);transition:box-shadow .2s">
            <div class="stat-num" data-count="2" style="font-size:2.75rem;font-weight:900;line-height:1">0</div>
            <div style="margin-top:0.5rem;font-weight:600">Molecular research areas</div>
            <div style="margin-top:0.4rem;font-size:0.8rem;opacity:0.65">Methylation and RNA processing · Glutamylation and chaperones — spanning 3 disease areas</div>
          </a>
          <a href="/people" class="stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:2rem;text-align:center;border:1px solid rgba(0,0,0,0.06);transition:box-shadow .2s">
            <div class="stat-num" data-count="50" data-suffix="+" style="font-size:2.75rem;font-weight:900;line-height:1">0</div>
            <div style="margin-top:0.5rem;font-weight:600">Trainees and mentees</div>
            <div style="margin-top:0.4rem;font-size:0.8rem;opacity:0.65">PhD, MD-PhD, postdoctoral, instructor, rotation, undergraduate, high-school</div>
          </a>
          <a href="https://scholar.google.com/citations?user=Mz9sZUoAAAAJ" class="stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:2rem;text-align:center;border:1px solid rgba(0,0,0,0.06);transition:box-shadow .2s">
            <div class="stat-num" data-count="30" data-prefix="h = " style="font-size:2.75rem;font-weight:900;line-height:1">h = 0</div>
            <div style="margin-top:0.5rem;font-weight:600">Google Scholar</div>
            <div style="margin-top:0.4rem;font-size:0.8rem;opacity:0.65">6000+ citations across original research and reviews</div>
          </a>
        </div>
        <style>
          .stat-card, .stat-card * { color: var(--hb-color-foreground, #111827) !important; }
          .stat-card:hover { box-shadow: 0 8px 20px rgba(0,0,0,0.12) !important; }
          .stat-card > div:first-child { color: var(--color-primary-600, #0f766e) !important; }
        </style>
        <script>
          (function () {
            var nums = document.querySelectorAll('.stat-num[data-count]');
            if (!nums.length) return;
            var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            function animate(el) {
              var target = parseInt(el.getAttribute('data-count'), 10);
              var prefix = el.getAttribute('data-prefix') || '';
              var suffix = el.getAttribute('data-suffix') || '';
              if (reduceMotion || isNaN(target)) {
                el.textContent = prefix + target + suffix;
                return;
              }
              var duration = 1200;
              var start = null;
              function step(ts) {
                if (!start) start = ts;
                var progress = Math.min((ts - start) / duration, 1);
                var eased = 1 - Math.pow(1 - progress, 3);
                el.textContent = prefix + Math.round(eased * target) + suffix;
                if (progress < 1) window.requestAnimationFrame(step);
              }
              window.requestAnimationFrame(step);
            }
            if ('IntersectionObserver' in window) {
              var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                  if (entry.isIntersecting) {
                    animate(entry.target);
                    observer.unobserve(entry.target);
                  }
                });
              }, { threshold: 0.4 });
              nums.forEach(function (el) { observer.observe(el); });
            } else {
              nums.forEach(animate);
            }
          })();
        </script>
    design:
      css_class: "bg-gradient-to-b from-primary-50 to-white dark:from-primary-900/20 dark:to-gray-800"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: research-areas
    id: disease-focus
    content:
      title: Disease Focus
      subtitle: Understanding disease mechanisms
      text: We start from mechanism — how the enzyme actually works — then ask whether that's what's driving disease, and whether it can be targeted.
      items:
        - name: C9orf72 ALS
          description: Arginine methylation shapes how RNA-binding proteins, stress granules, and nuclear transport behave. In C9orf72 ALS, we're asking whether PRMT inhibition — and PRMT-dependent control of TDP-43 cryptic exons — is a real therapeutic angle.
          image: research/als-motor-neuron.png
          topics:
            - C9orf72 ALS
            - TDP-43 cryptic exons
            - PRMT inhibitor biology
          cta:
            text: Read more
            url: /research/als
        - name: NPM1-mutant AML
          description: We found that TTLL4 glutamylates NPM1c, the mutant driver of this leukemia, changing how it associates with chromatin and reshaping the oncogenic transcriptional program. That makes TTLL4 a therapeutic target we're now pursuing directly.
          image: research/aml-blast-cells.png
          topics:
            - NPM1-mutant AML
            - TTLL4 glutamyltransferase
            - Target validation
          cta:
            text: Read more
            url: /research/aml
        - name: Aging and the methyl economy
          description: GNMT sits at the center of the methyl economy. With the Huffman and Gavathiotis labs, we're testing whether shifting methyl-donor flux through GNMT can move aging-related transcriptional and metabolic programs.
          image: research/methyl-cycle.png
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
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: research-areas
    id: research
    content:
      title: Research Areas
      subtitle: Post-translational modification of IDRs
      text: "Both grew out of the same question: what does a specific chemical modification actually do to a protein? We chase that from purified enzymes in a test tube through to cells and disease models."
      items:
        - name: Methylation, gene regulation, and RNA processing
          description: We study how PRMT5 methylates histones and splicing factors to control chromatin and mRNA processing, and how PRMT-dependent regulation may go wrong in C9orf72 ALS. GNMT sets the methyl-donor supply that all of this methylation draws on, tying the two together.
          image: research/methylation-rna.png
          topics:
            - PRMT5
            - GNMT and SAM homeostasis
            - Splicing and RNA processing
            - Histone gene regulation
            - C9orf72 ALS
          cta:
            text: Read more
            url: /research/arginine-methylation
        - name: Glutamylation and histone chaperones
          description: Histone chaperones use long, acidic, disordered stretches to mimic DNA and grab onto histones. We're working out how modifications like glutamylation tune that behavior — and what happens when it's hijacked in NPM1-mutant leukemia.
          image: research/chaperone-idr.png
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
      css_class: "bg-white dark:bg-gray-800"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: cta-image-paragraph
    content:
      items:
        - title: 'From mechanism to disease'
          text: |
            Two projects show how this works in practice. TTLL4-mediated glutamylation of NPM1c looks like a real vulnerability in NPM1-mutant AML, and we're testing whether PRMT-dependent control of TDP-43 cryptic exon splicing can be turned into a therapeutic angle in C9orf72 ALS. In both cases we started with the enzyme mechanism and only then went looking for the disease connection.
          image: research/ttll4-npm1-glutamylation-graphic.png
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
      spacing:
        padding: ["3rem", 0, "3rem", 0]

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

  - block: markdown
    id: funders
    content:
      title: Supported by
      text: |
        [NIH / NIGMS](https://www.nigms.nih.gov) &ensp;·&ensp; [NIH / NIA](https://www.nia.nih.gov) &ensp;·&ensp; [ALS Therapy Development Institute](https://www.als.net) &ensp;·&ensp; [Hevolution Foundation](https://hevolution.com) &ensp;·&ensp; [Irma T. Hirschl Trust](https://irmatrust.org) &ensp;·&ensp; [Montefiore Einstein Comprehensive Cancer Center](https://einsteinmed.edu/centers/cancer/) &ensp;·&ensp; [Einstein 2030 Fund](https://einsteinmed.edu)
    design:
      css_class: "text-center"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  - block: markdown
    id: collaborators
    content:
      title: Collaborators
      subtitle: ''
      text: |
        We work closely with [ALS Therapy Development Institute](https://www.als.net) (primary partner on C9orf72 ALS) and with colleagues at Einstein — [David Cowburn](https://einsteinmed.edu/faculty/12344/david-cowburn) (NMR), [Matthew Gamble](https://einsteinmed.edu/faculty/11838/matthew-gamble) (chromatin), [Charles Query](https://einsteinmed.edu/faculty/6996/charles-c-query) (splicing), [Simone Sidoli](https://einsteinmed.edu/faculty/16080/simone-sidoli) (proteomics), [Kira Gritsman](https://einsteinmed.edu/faculty/14128/kira-gritsman) (leukemia), [Seiya Kitamura](https://einsteinmed.edu/faculty/17244/seiya-kitamura) (chemical biology), and [Steven Almo](https://einsteinmed.edu/faculty/7091/steven-c-almo) (structural biology) — as well as [Jie Jiang](https://cellbio.emory.edu/jiang/index.html) (Emory, ALS).
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
      social:
        - icon: brands/orcid
          url: https://orcid.org/0000-0001-9388-6004
        - icon: brands/google-scholar
          url: https://scholar.google.com/citations?user=Mz9sZUoAAAAJ
      prospective:
        title: Get in touch
        text: Science, collaborations, and inquiries from prospective students and postdocs.
        button:
          text: Send a message
          url: /contact#inquiry
      map_url: https://maps.google.com/?q=Albert+Einstein+College+of+Medicine+1300+Morris+Park+Ave+Bronx+NY+10461
      show_form: false
    design:
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"
      spacing:
        padding: ["5rem", 0, "5rem", 0]
---
