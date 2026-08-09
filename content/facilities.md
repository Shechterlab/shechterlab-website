---
title: 'Lab Environment & Contact'
date: 2026-06-28
type: landing

design:
  spacing: '4rem'

sections:
  - block: hero
    content:
      title: |
        A mechanistic biochemistry lab in the Bronx
      text: |
        The Shechter Lab is based in the Department of Biochemistry at Albert Einstein College of Medicine. Our work spans biochemical reconstitution, quantitative enzymology, chromatin biology, RNA processing, structural and biophysical analysis, and disease-focused molecular investigation.
      primary_action:
        text: Contact the lab
        url: '#contact'
        icon: hero/envelope
      secondary_action:
        text: View opportunities
        url: '/opportunities'
        icon: hero/user-plus
    design:
      background:
        image:
          filename: "lab/lab-instrumentation.jpg"
          filters:
            brightness: 0.75
            contrast: 1.0

  - block: markdown
    content:
      title: 'Research environment'
      text: |
        The lab combines biochemical and mechanistic work with cell-based and genome-wide approaches. Typical project directions include enzyme mechanism, substrate recognition, chromatin-associated regulation, RNA maturation and retention, and therapeutic target validation.

        We benefit from the broader Einstein ecosystem including the Montefiore-Einstein Comprehensive Cancer Center, the Data Science Institute, and strong neighboring expertise in chromatin, cancer biology, chemical biology, structural biology, metabolism, and graduate training. The lab plays an active role in the Einstein Chromatin Club joint lab meetings since 2011 and the founding and ongoing leadership of the [NYC Chromatin Club](https://www.nycchromatinclub.org/).
    design:
      columns: '1'

  - block: features
    content:
      title: Current strengths
      text: ''
      items:
        - name: Mechanistic biochemistry
          description: In vitro reconstitution and enzymology used to establish causal molecular models for PRMT, TTLL, and GNMT biology.
          icon: hero/beaker
        - name: Chromatin and RNA integration
          description: Projects connect PTMs to chromatin assembly, transcription, splicing, and transcript fate, including the GRIPP chromatin reserve.
          icon: hero/document-text
        - name: Translation to disease
          description: Active work in NPM1-mutant AML, C9orf72 ALS, and aging-related metabolism, with chemistry and clinical collaborators.
          icon: hero/bolt
        - name: Training culture
          description: Mentorship, careful experimental design, and a discussion-driven environment across PhD, MD-PhD, postdoctoral, undergraduate, and high-school trainees.
          icon: hero/academic-cap
    design:
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"

  - block: markdown
    content:
      title: 'Downloads'
      text: |
        - [PI Curriculum Vitae (PDF)](/uploads/shechter-cv-2026.pdf)
        - [NIH biosketch (PDF)](/uploads/shechter-biosketch-2026.pdf)
    design:
      columns: '1'

  - block: contact-info
    id: contact
    content:
      title: Contact the Shechter Lab
      subtitle: ''
      visit_title: 'Address'
      connect_title: 'Email'
      address:
        lines:
          - Shechter Lab
          - Department of Biochemistry
          - Albert Einstein College of Medicine
          - Forchheimer 304
          - 1300 Morris Park Avenue
          - Bronx, NY 10461
      office_hours:
        - 'By appointment'
      email: 'david.shechter@einsteinmed.edu'
      phone: '+1 (718) 430-4120'
      social:
        - icon: brands/orcid
          url: https://orcid.org/0000-0001-9388-6004
      map_url: 'https://maps.google.com/?q=Albert+Einstein+College+of+Medicine+1300+Morris+Park+Ave+Bronx+NY+10461'
    design:
      css_class: "dark bg-gray-900 text-white"
---
