---
title: News
date: 2026-06-29
type: landing
sections:
  - block: markdown
    content:
      title: News
      text: What's happening in the lab — papers, people, talks, and grants.
    design:
      spacing:
        padding: ['2rem', '0', '0.5rem', '0']
  - block: collection
    id: news-recent
    content:
      title: ''
      subtitle: ''
      filters:
        folders:
          - news
        exclude_past: false
      sort_by: 'Date'
      sort_ascending: false
      publication_types: []
      featured_only: false
      offset: 0
      count: 20
    design:
      view: article-grid
      columns: 2
      spacing:
        padding: ['0.5rem', '0', '2rem', '0']
---
