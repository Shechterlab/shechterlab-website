---
title: Contact
type: landing
sections:
  - block: markdown
    content:
      title: Contact
      text: |
        **Shechter Lab**
        [Department of Biochemistry](https://einsteinmed.edu/departments/biochemistry)
        Albert Einstein College of Medicine
        Forchheimer Building, Room 304
        1300 Morris Park Avenue
        Bronx, NY 10461

        **David Shechter, PhD**
        Professor of Biochemistry

        [Faculty page](https://www.einsteinmed.edu/faculty/1064/david-shechter/) &ensp;|&ensp; [ORCID 0000-0001-9388-6004](https://orcid.org/0000-0001-9388-6004) &ensp;|&ensp; [Google Scholar](https://scholar.google.com/citations?user=Mz9sZUoAAAAJ)

        <h2 id="inquiry">Inquiry</h2>

        Science, collaborations, reagents and data, or joining the lab.

        **Lab members:** [Lab Wiki ↗](https://wiki.shechterlab.org)

        <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thanks/" class="hb-form not-prose">
          <input type="hidden" name="form-name" value="contact">
          <p class="hb-form-hp" aria-hidden="true"><label>Leave this field empty: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>

          <div class="hb-form-row">
            <div>
              <label for="cf-name">Your name</label>
              <input type="text" id="cf-name" name="name" required autocomplete="name">
            </div>
            <div>
              <label for="cf-email">Your email</label>
              <input type="email" id="cf-email" name="email" required autocomplete="email">
            </div>
          </div>

          <div>
            <label for="cf-role">This is about…</label>
            <select id="cf-role" name="topic">
              <option>A question about the science</option>
              <option>A possible collaboration</option>
              <option>Reagents, plasmids, structures, or data</option>
              <option>Joining the lab — graduate student (MSTP / PhD)</option>
              <option>Joining the lab — postdoc</option>
              <option>Joining the lab — rotation or undergraduate student</option>
              <option>Teaching, seminars, or outreach</option>
              <option>Press or other</option>
            </select>
          </div>

          <div>
            <label for="cf-message">Message</label>
            <textarea id="cf-message" name="message" rows="7" required></textarea>
          </div>

          <button type="submit">Send message</button>
        </form>
---
