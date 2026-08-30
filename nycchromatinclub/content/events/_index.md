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

  # The "next symposium" notice is a markdown block rather than a
  # `collection` with `exclude_past: true`, because an empty collection
  # still renders its heading — a bare "Upcoming" with nothing under it
  # reads as a broken page rather than as "not announced yet".
  #
  # TODO (organizers): once the 2027 date is set, create
  # content/events/symposium-2027/index.md and replace this whole block
  # with the collection below, which will then populate itself:
  #
  #   - block: collection
  #     id: upcoming
  #     content:
  #       title: Upcoming
  #       filters:
  #         folders: [events]
  #         exclude_past: true
  #       sort_by: 'Date'
  #       sort_ascending: true
  #       count: 0
  #     design:
  #       view: card
  #       columns: 2
  - block: markdown
    id: upcoming
    content:
      title: Next symposium
      text: |
        The **4th Annual NYC Chromatin Club Symposium** is planned for summer 2027. The date, the host campus, and the abstract deadline are announced on the mailing list first.

        [Join the mailing list →](/join/)
    design:
      spacing:
        padding: ['0.5rem', '0', '2rem', '0']

  - block: collection
    id: past
    content:
      title: Past symposia
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
