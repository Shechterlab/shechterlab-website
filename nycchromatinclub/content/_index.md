---
title: ''
date: 2026-08-30
type: landing

design:
  spacing: '5rem'

sections:
  # ------------------------------------------------------------------
  # Hero.
  #
  # Modelled on the premium conference template's hero-with-stats: a
  # full-bleed coloured field, big left-aligned display type, and the
  # numbers sitting INSIDE the hero rather than in a band underneath. The
  # earlier draft was a centred logo on white, which read as a lab page —
  # this site should not look like shechterlab.org.
  #
  # The background is generated from the club logo's own skyline (see
  # assets/media/hero-skyline.build.py) so the art is the brand, not stock
  # photography. The wordmark is a white knockout of the same logo, minus
  # its skyline, which would otherwise be drawn twice.
  # ------------------------------------------------------------------
  - block: markdown
    id: hero
    content:
      title: ''
      text: |
        <div class="ncc-hero ncc-wide">
          <img class="ncc-hero-wordmark" src="/media/logo/wordmark-white.png"
               alt="NYC Chromatin Club" width="1503" height="145">

          <p class="ncc-hero-kicker">Founded 2020 &middot; Eight institutions &middot; Five boroughs</p>

          <h1 class="ncc-hero-title">4th Annual<br>Symposium</h1>

          <p class="ncc-hero-sub">Summer 2027 &middot; New York City</p>

          <p class="ncc-hero-lead">
            A full day of chromatin science &mdash; two keynotes, selected talks and a poster
            session, with the program built from submitted abstracts. Free at the door,
            lunch included.
          </p>

          <p class="ncc-hero-actions">
            <a class="ncc-hero-btn ncc-hero-btn-primary" href="/join/">Join the mailing list</a>
            <a class="ncc-hero-btn ncc-hero-btn-ghost" href="/events/symposium-2026/">See the 2026 program</a>
          </p>

          <dl class="ncc-hero-stats">
            <div><dt>Symposia</dt><dd>3</dd></div>
            <div><dt>Institutions</dt><dd>8</dd></div>
            <div><dt>Cost to attend</dt><dd>$0</dd></div>
            <div><dt>Founded</dt><dd>2020</dd></div>
          </dl>
        </div>
    design:
      background:
        image:
          filename: 'hero-skyline.jpg'
          size: cover
          position: center
          parallax: false
        text_color_light: true
      spacing:
        padding: ['0', '0', '0', '0']
      no_padding: true

  # ------------------------------------------------------------------
  # Countdown to the next symposium, in the position the premium
  # conference template puts it: immediately under the masthead, before
  # anything else competes for attention.
  #
  # `date` is deliberately EMPTY. The 2027 date is not fixed, and a
  # countdown ticking against a made-up target is worse than no countdown
  # — the block renders `fallback_text` instead of zeroes until a real
  # date is set here. Set it to e.g. '2027-07-20 09:00:00' and the digits
  # appear on their own.
  # ------------------------------------------------------------------
  - block: countdown
    id: countdown
    content:
      date: ''
      # Deliberately NOT repeating the hero's headline, which sits
      # directly above this band.
      title: 'Save the date'
      text: ''
      fallback_text: 'The 2027 date is being set now — it goes to the mailing list first.'
      elapsed_text: 'The symposium is under way — see you there.'
      text_after: 'Free to attend, as always.'
      button:
        text: 'Get symposium announcements'
        url: '/join/'
    design:
      css_class: "bg-primary-800"
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']

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
  # ------------------------------------------------------------------
  # Agenda. The premium conference template renders the running order
  # straight on the landing page from a CSV; here the full agendas live
  # on each symposium page (so past programs stay with their meeting) and
  # the home page links through to them.
  # ------------------------------------------------------------------
  - block: markdown
    id: agenda
    content:
      title: Agenda
      text: |
        The program is built from **submitted abstracts** — two keynotes, selected talks, and a poster session over lunch. Every symposium keeps its own running order, so past agendas stay online:

        - [**2027 — 4th Annual**](/events/symposium-2027/) · summer, date to be announced · registration and abstracts open in the spring
        - [**2026 — 3rd Annual**](/events/symposium-2026/) · Columbia University Irving Medical Center · [agenda](/events/symposium-2026/#agenda)
        - [**2025 — 2nd Annual**](/events/symposium-2025/) · Albert Einstein College of Medicine · [agenda](/events/symposium-2025/#agenda)
        - [**2024 — 1st Annual**](/events/symposium-2024/) · the first in-person meeting
    design:
      spacing:
        padding: ['3rem', '0', '1rem', '0']

  - block: collection
    id: meetings
    content:
      title: ''
      subtitle: ''
      text: ''
      filters:
        folders:
          - events
      sort_by: 'Date'
      sort_ascending: false
      count: 4
    design:
      view: card
      columns: 2
      show_read_time: false
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ['2rem', '0', '3rem', '0']

  # ------------------------------------------------------------------
  # Sponsors, given a slot on the landing page rather than only living
  # on /sponsors/ — sponsors are what keeps the day free at the door, and
  # prospective ones need to see that the club puts them in front of the
  # whole audience.
  # ------------------------------------------------------------------
  - block: sponsors
    id: sponsors
    content:
      mode: current
      title: Sponsors
      text: 'The symposium is free to attend because sponsors cover the room, the catering and the poster boards.'
      empty_text: |
        Sponsors for 2027 are being lined up now — [your company could be here](/sponsors/).
    design:
      spacing:
        padding: ['3rem', '0', '2rem', '0']

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
