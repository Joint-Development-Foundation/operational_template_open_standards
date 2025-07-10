## ✅ Getting Started Checklist

Preparing and approving operational procedures is an important step in fostering a culture of openness, trust, and collaboration within a community. This checklist helps you customize the default procedures in [`Organization Operational Process`](Organization_Operational_Process.md) to reflect the needs and aims of your project.

> 💡 Tip: Turn this file into a GitHub issue to track progress.

---

### 1. Initial Repository Setup & Hygiene

> 💡 Add a link to this repo in your GitHub Organization's README file for easy access

* [ ] Fork or copy this repository into your project’s GitHub organization
* [ ] Rename it to `{{PROJECT_NAME}}_Operational_Procedures` or similar
* [ ] Set the default branch (e.g., `main`) and enable branch protection and 2FA
* [ ] Set up DCO Bot (or CLA Bot, if applicable)
* [ ] Replace all instances of `{{PROJECT_NAME}}` with your actual project name
* [ ] Update links to canonical project documents in `index.yaml` if different from the defaults:

  * [ ] Project website
  * [ ] Link to Logo Artwork, Trademark and Brand Usage Guidelines
  * [ ] Code of Conduct
  * [ ] Membership agreement / How to join
  * [ ] Membership levels / benefits
  * [ ] Project and working group charters

---

### 2. Core Template Customization

* [ ] Document your project's organizational structure. For each committee, working group, task group, or interest group:

  * [ ] Add a short description of the group’s function or objective
  * [ ] Add a brief description of how to join
  * [ ] Include meeting cadence and calendar invite info
  * [ ] Include mailing list info and how to subscribe
  * [ ] Link to group-specific repos, file directories, chat channels, project boards, etc.
* [ ] Review the “Roles & Expectations” section and update as needed
* [ ] Review the Meeting Policy and update templates if needed
* [ ] Review and update the “Guidelines for Decision-Making” section:

  * Clarify how contributions to working groups are accepted and how work progresses (e.g., through PRs)
  * Working groups should document their process in a `CONTRIBUTING.md` file in each relevant repository
* [ ] Review the Specification Development and Release Management Process:

  * Ensure it reflects how your project collaborates across groups to produce deliverables
  * Document how work packages are created, assigned to releases or milestones, and reviewed
* [ ] Review the Access Rights table and update as needed
* [ ] Review the Git Development Flow section (if using git-based version control)
* [ ] Review the Publication and Advancement Guidelines:

  * Include links to relevant editorial tools or requirements from partner SDOs if applicable
* [ ] Review the Notice Requirements and IPR Review Guidelines
* [ ] Update the Additional Resources and Reference Materials section: 

  * The information in this section is non-normative but helpful to those following the Operational Process Document
* [ ] Remove unnecessary or inapplicable notes, sections, files or diagrams

---

### 3. Update Reference Diagrams

> 💡 Editable diagrams are in the `/Diagrams` directory (draw\.io format)

* [ ] Update the organization structure diagram (`organigram.svg`)
* [ ] Update the review & approval diagrams (`R_A-1.svg`, `R_A-2.svg`)
* [ ] Update the specification development process diagrams

---

### 4. Update Working Group Templates

> 💡 Create a Working Group Template repo to make it easier to launch new Working Groups on a common format

* [ ] Add status badges if using (e.g., license, build, last updated)
* [ ] Review and customize standard files per group:

  * [ ] `CONTRIBUTING.md`
  * [ ] `LICENSE.md`
  * [ ] `README.md`
* [ ] Update release planning documentation

---

### 5. Community Onboarding

> 💡 LFX tools help participants manage their calendar invites, mailing list subscriptions, votes, enrollment, track engagement, and other data. 

* [ ] Create GitHub teams and invite participants (if applicable)
* [ ] Update instructions on how contributors sign the license agreement
* [ ] Customize issue and PR templates and GitHub labels
* [ ] Consider adding workflow automations to support new contributor experience, triage, and project tracking
* [ ] Create a “New Contributor Onboarding” checklist
* [ ] Enable GitHub Discussions or Project Boards if using them

---

### 6. Final Review & Launch

* [ ] Review the updated `Organization_Operational_Process.md` with project stakeholders
* [ ] Tag an initial release (e.g., `v1.0.0`) and update `CHANGELOG.md`
* [ ] Obtain Steering Committee Approval to adopt/update document
* [ ] Update adoption date and publish the documents and notify your community
