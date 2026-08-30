---
title: Join
type: landing

sections:
  - block: markdown
    id: intro
    content:
      title: Join the club
      text: |
        Membership is free and open to anyone in the New York area working on chromatin, epigenetics, or nuclear biology. There is no application — sign up for the mailing list and you are in.
    design:
      spacing:
        padding: ['3rem', '0', '0.5rem', '0']

  # The kit's `cta-button-list` block renders icon + label only — it drops
  # a `description`, which is most of the value here — so these three
  # channel cards are hand-built.
  - block: markdown
    id: channels
    content:
      text: |
        <div class="ncc-wide" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));gap:1.25rem;max-width:72rem;margin:0 auto">
          <a href="mailto:info@nycchromatinclub.org?subject=Subscribe%20to%20the%20NYC%20Chromatin%20Club%20mailing%20list" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;border:1px solid rgba(0,0,0,0.06);border-top:4px solid var(--ncc-orange)">
            <div style="font-size:1.15rem;font-weight:700">Mailing list</div>
            <div style="margin-top:0.5rem;font-size:0.92rem;opacity:0.8">Symposium announcements, abstract deadlines, and seminar Zoom links. A few messages a month, no more.</div>
          </a>
          <a href="#slack" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;border:1px solid rgba(0,0,0,0.06);border-top:4px solid var(--ncc-navy)">
            <div style="font-size:1.15rem;font-weight:700">Slack forum</div>
            <div style="margin-top:0.5rem;font-size:0.92rem;opacity:0.8">Where the between-meeting conversation happens — reagents, protocols, troubleshooting, instrument time, and job postings.</div>
          </a>
          <a href="https://x.com/nycchromatin" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;border:1px solid rgba(0,0,0,0.06);border-top:4px solid var(--ncc-gray)">
            <div style="font-size:1.15rem;font-weight:700">@nycchromatin on X</div>
            <div style="margin-top:0.5rem;font-size:0.92rem;opacity:0.8">Announcements and symposium photos.</div>
          </a>
        </div>
    design:
      spacing:
        padding: ['0.5rem', '0', '2rem', '0']

  - block: markdown
    id: slack
    content:
      title: The Slack forum
      text: |
        The club runs a Slack workspace for the city's chromatin labs. It is the fastest way to find someone who has already run the experiment you are about to start — or who has a spare aliquot of the antibody you need.

        <!--
          TODO (organizers): paste the Slack invite link below, replacing this
          paragraph and the comment. Slack invite links expire, so if you would
          rather not maintain one here, leave the mailto: request in place —
          it routes people to whoever is holding the workspace admin.
        -->

        To get an invite, [email the organizers](mailto:info@nycchromatinclub.org?subject=NYC%20Chromatin%20Club%20Slack%20invite) from your institutional address.
    design:
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']

  - block: markdown
    id: sponsors
    content:
      title: Sponsoring the symposium
      text: |
        The symposium is free to attend because host institutions and commercial sponsors cover the venue, the catering, and the poster printing. Sponsors get signage, a table at the poster session, and acknowledgement in the program.

        If your company would like to sponsor, [get in touch](mailto:info@nycchromatinclub.org?subject=NYC%20Chromatin%20Club%20sponsorship) and the committee will send the current options.
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']

  - block: contact-info
    id: contact
    content:
      title: Contact
      subtitle: ''
      visit_title: 'Where we meet'
      connect_title: 'Get in touch'
      address:
        lines:
          - 'The symposium rotates between New York campuses.'
          - '2026: Columbia University Irving Medical Center'
          - '2025: Albert Einstein College of Medicine'
      email: info@nycchromatinclub.org
      social:
        - icon: brands/x
          url: https://x.com/nycchromatin
      show_form: false
    design:
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ['2.5rem', '0', '3rem', '0']
---
