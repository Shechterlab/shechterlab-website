---
title: Events
description: Symposia and meetings of the NYC Chromatin Club.
type: landing

# The events layout reads `.Params.reading_time` per page; the site-wide
# `hugoblox.content.reading_time` setting never reaches it. Cascade it so
# no symposium page advertises a "1 min read".
cascade:
  reading_time: false

sections:
  - block: markdown
    id: intro
    content:
      title: Events
      text: |
        The club's flagship event is the **annual summer symposium**, hosted on a rotating New York campus. Between symposia, the mailing list carries announcements and Zoom links for chromatin seminars across the participating institutions.
    design:
      spacing:
        padding: ['3rem', '0', '0.5rem', '0']

  - block: collection
    id: upcoming
    content:
      title: Upcoming
      subtitle: ''
      filters:
        folders:
          - events
        exclude_past: true
      sort_by: 'Date'
      sort_ascending: true
      count: 0
    design:
      view: card
      columns: 2
      show_read_time: false
      spacing:
        padding: ['0.5rem', '0', '2rem', '0']

  - block: collection
    id: past
    content:
      title: Past symposia and agendas
      subtitle: ''
      filters:
        folders:
          - events
        exclude_future: true
      sort_by: 'Date'
      sort_ascending: false
      count: 0
    design:
      view: card
      columns: 2
      # A symposium card should show the meeting's date, not "1 min read".
      show_read_time: false
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ['2rem', '0', '3rem', '0']
---
