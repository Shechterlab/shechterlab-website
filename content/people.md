---
title: People
type: landing
sections:

  - block: markdown
    content:
      title: The Lab
      text: |
        <div style="max-width:640px;margin:0 auto 1.5rem">
          <img src="/media/lab/lab-photo-2026.jpg" style="width:100%;border-radius:12px;box-shadow:0 4px 16px rgba(0,0,0,0.12)">
        </div>

        **Shechter Lab, 2026.** From left: Jacob Roth, Haeun Kim, Aliza Silverstein, Liana Valin, Subray Hegde, David Shechter, Isaac Kraz. Not pictured: additional collaborators and rotation students.

        [Lab History →](/history) &ensp;|&ensp; [Photo Archive →](/lab-life/archive)

        <nav style="display:flex;flex-wrap:wrap;justify-content:center;gap:0.5rem 1.5rem;margin-top:1.5rem;font-size:0.95rem;font-weight:600">
          <a href="#current">Current Lab Members</a>
          <a href="#alumni">Alumni</a>
          <a href="#rotation-summer-students">Rotation &amp; Summer Students</a>
        </nav>
    design:
      spacing:
        padding: ['2rem', '0', '0.5rem', '0']

  - block: team-showcase
    id: current
    content:
      title: Current Lab Members
      subtitle: ''
      user_groups:
        - Current
      sort_by: 'weight'
      sort_ascending: true
    design:
      show_role: true
      show_interests: true
      show_social: true

  - block: team-showcase
    id: alumni
    content:
      title: Alumni
      subtitle: 'Destinations are listed as of last contact and may not reflect current positions.'
      user_groups:
        - Alumni
      sort_by: 'weight'
      sort_ascending: true
    design:
      show_role: true
      show_interests: false
      show_social: false
      css_class: "bg-gray-50 dark:bg-gray-900"

  - block: markdown
    id: rotation-summer-students
    content:
      title: Rotation & Summer Students
      text: |
        Short-term trainees who have worked in the lab, listed by name only.

        **College / undergraduate summer students**

        *(Names to be added.)*

        **High school summer students**

        *(Names to be added.)*
    design:
      spacing:
        padding: ['0.5rem', '0', '2rem', '0']
---
