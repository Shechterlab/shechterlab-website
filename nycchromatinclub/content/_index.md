---
title: ''
date: 2026-08-30
type: landing

design:
  spacing: '5rem'

sections:
  # ------------------------------------------------------------------
  # Masthead. This is a `markdown` block rather than the `hero` block
  # because the club logo IS the headline — it carries the wordmark, the
  # skyline and all three brand colors — and the hero block has no slot
  # for a foreground logo, only a background image. Setting the logo as a
  # hero background would darken it behind an overlay and bury the
  # wordmark, so the masthead is hand-built here instead.
  # ------------------------------------------------------------------
  - block: markdown
    id: masthead
    content:
      title: ''
      text: |
        <div style="text-align:center;max-width:52rem;margin:0 auto">
          <img class="ncc-hero-logo" src="/media/logo/nyc-chromatin-club.png"
               alt="NYC Chromatin Club" width="1000" height="425">

          <p style="font-size:1.3rem;line-height:1.6;font-weight:500;margin:0 auto 1.75rem;max-width:40rem">
            The chromatin, epigenetics, and nuclear biology community of New York City — one symposium, many labs, five boroughs.
          </p>

          <p style="margin-bottom:1.75rem">
            <span class="ncc-datebadge">4th Annual Symposium &middot; Summer 2027 <span>· date to be announced</span></span>
          </p>

          <p style="display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap;margin:0">
            <a href="/join/"
               style="display:inline-block;padding:0.7rem 1.5rem;border-radius:0.5rem;background:var(--ncc-navy);color:#fff;font-weight:600;text-decoration:none">
              Join the mailing list
            </a>
            <a href="/events/symposium-2026/"
               style="display:inline-block;padding:0.7rem 1.5rem;border-radius:0.5rem;border:2px solid var(--ncc-navy);color:var(--ncc-navy);font-weight:600;text-decoration:none">
              The 2026 symposium
            </a>
          </p>
        </div>
    design:
      spacing:
        padding: ['4rem', '0', '2.5rem', '0']

  # ------------------------------------------------------------------
  # At-a-glance numbers. Hand-built rather than the `stats` block so the
  # cards can be links — each one goes somewhere useful.
  # ------------------------------------------------------------------
  - block: markdown
    id: at-a-glance
    content:
      text: |
        <div class="ncc-wide" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:1.25rem;max-width:72rem;margin:0 auto">
          <a href="/about/" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;text-align:center;border:1px solid rgba(0,0,0,0.06)">
            <div style="font-size:2.5rem;font-weight:800;line-height:1">2020</div>
            <div style="margin-top:0.4rem;font-weight:600">Founded</div>
            <div style="margin-top:0.35rem;font-size:0.8rem;opacity:0.65">Started as a virtual seminar series during the pandemic</div>
          </a>
          <a href="/about/#steering-committee" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;text-align:center;border:1px solid rgba(0,0,0,0.06)">
            <div style="font-size:2.5rem;font-weight:800;line-height:1">8</div>
            <div style="margin-top:0.4rem;font-weight:600">Institutions represented</div>
            <div style="margin-top:0.35rem;font-size:0.8rem;opacity:0.65">Columbia, Einstein, MSK, Mount Sinai, NYGC, NYU, Rockefeller, Weill Cornell</div>
          </a>
          <a href="/events/" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;text-align:center;border:1px solid rgba(0,0,0,0.06)">
            <div style="font-size:2.5rem;font-weight:800;line-height:1">3</div>
            <div style="margin-top:0.4rem;font-weight:600">Symposia held</div>
            <div style="margin-top:0.35rem;font-size:0.8rem;opacity:0.65">2024, 2025, 2026 — a full day of talks and posters each summer</div>
          </a>
          <a href="/join/" class="ncc-stat-card" style="display:block;text-decoration:none;background:var(--hb-color-background,#fff);border-radius:1rem;box-shadow:0 4px 12px rgba(0,0,0,0.06);padding:1.75rem;text-align:center;border:1px solid rgba(0,0,0,0.06)">
            <div style="font-size:2.5rem;font-weight:800;line-height:1">$0</div>
            <div style="margin-top:0.4rem;font-weight:600">Cost to join</div>
            <div style="margin-top:0.35rem;font-size:0.8rem;opacity:0.65">Mailing list, Slack, and every event — no membership fee</div>
          </a>
        </div>
    design:
      css_class: "bg-gradient-to-b from-primary-50 to-white dark:from-primary-900/20 dark:to-gray-800"
      spacing:
        padding: ['3rem', '0', '3rem', '0']

  # ------------------------------------------------------------------
  - block: features
    id: what-we-do
    content:
      title: What the club does
      text: 'The club exists to make a city full of chromatin labs behave like one department — so that a graduate student at Einstein knows what a postdoc at Rockefeller is working on, and can just email them.'
      items:
        - name: An annual symposium
          description: A full day of talks and posters each summer, hosted on a rotating campus. Speakers and posters are selected from submitted abstracts, so the program reflects what the community is actually doing this year.
          icon: hero/calendar-days
        - name: A platform for early-career scientists
          description: The club deliberately highlights graduate students, postdocs, and new investigators. Most symposium talks go to trainees and junior faculty rather than to established names.
          icon: hero/academic-cap
        - name: A year-round back channel
          description: A city-wide Slack forum for reagents, protocols, troubleshooting, instrument time, and job postings — plus a mailing list carrying seminar announcements and Zoom links from every participating institution.
          icon: hero/chat-bubble-left-right
    design:
      css_class: "bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"

  # ------------------------------------------------------------------
  - block: team-showcase
    id: keynotes-2026
    content:
      title: Most recent keynotes
      subtitle: '3rd Annual Symposium · Columbia University · July 21, 2026'
      text: ''
      user_groups:
        - 2026 Keynote Speakers
      sort_by: 'weight'
      sort_ascending: true
      cta:
        text: About the 2026 symposium
        url: /events/symposium-2026/
        icon: hero/arrow-right
    design:
      show_role: false
      show_organizations: true
      show_interests: true
      max_interests: 3
      show_social: false
      max_columns: 2
      align: center
      spacing:
        padding: ['3rem', '0', '3rem', '0']

  # ------------------------------------------------------------------
  - block: collection
    id: events
    content:
      title: Meetings
      subtitle: ''
      text: ''
      filters:
        folders:
          - events
      sort_by: 'Date'
      sort_ascending: false
      count: 6
    design:
      view: card
      columns: 2
      # A symposium card should show the meeting's date, not "1 min read".
      show_read_time: false
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ['3rem', '0', '3rem', '0']

  # ------------------------------------------------------------------
  - block: cta-card
    id: join-cta
    content:
      title: 'Chromatin in New York? Come join us.'
      text: 'Membership is free and open to anyone in the New York area working on chromatin, epigenetics, or nuclear biology — faculty, postdocs, students, and staff scientists alike. The 4th Annual Symposium lands in summer 2027 — sign up for the mailing list and the date, the abstract deadline, and seminar Zoom links will reach you first.'
      button:
        text: 'Join the mailing list'
        url: '/join/'
        icon: 'hero/envelope'
    design:
      # `gradient.start`/`end` are interpolated straight into a CSS
      # `linear-gradient()`, so they must be real CSS colors. Tailwind
      # tokens like `primary-700` (which the kit's own README suggests)
      # produce an invalid gradient that silently renders as nothing —
      # leaving this card's light text white-on-white. Use hex.
      card:
        css_class: 'cta-glassmorphism'
        text_color: 'light'
      background:
        gradient:
          start: '#003884'
          end: '#001b40'
          direction: 135
      spacing:
        padding: ['3rem', '0', '4rem', '0']
---
