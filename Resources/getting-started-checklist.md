## ✅ Getting Started Checklist

Preparing and approving operational procedures is an important step in fostering a culture of openness, trust, and collaboration within a community. This checklist helps you customize the default procedures in [Organization Operational Process](./Organization_Operational_Process.md) to reflect the needs and aims of your project.

> 💡 **Tip:** You can [turn this file into a GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/about-issues) to track your progress and assign tasks.

---

### 📌 How to Use This Checklist

- **Replace all placeholder text** such as `{{PROJECT_NAME}}`, `{{YEAR}}`, and `{{CONTACT_EMAIL}}` with your project’s information.  
- **Follow the links** to referenced documents for further details.
- **Check off each item** as you complete it to ensure no steps are missed.

---

### 1. Initial Repository Setup & Hygiene

> 💡 **Tip:** Add a link to this repo in your GitHub Organization's main README for easy access.

- [ ] Fork or copy this repository into your project’s GitHub organization  
  _Example: If your project is called “OpenData,” fork and rename to `OpenData_Operational_Procedures`._
- [ ] Rename the repository to `{{PROJECT_NAME}}_Operational_Procedures` or similar
- [ ] Set the default branch (e.g., `main`) and enable [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/about-protected-branches) and [2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication)
- [ ] Set up [DCO Bot](https://github.com/apps/dco) or CLA Bot if required
- [ ] Replace all instances of `{{PROJECT_NAME}}` with your actual project name (use a global find-and-replace or script)
- [ ] Update links to project documents in `index.yaml` if different from defaults:
    - [ ] Project website
    - [ ] Logo artwork, trademark & brand usage guidelines
    - [ ] Code of Conduct
    - [ ] Membership agreement / joining instructions
    - [ ] Membership levels / benefits
    - [ ] Project and working group charters

---

### 2. Core Template Customization

Document your project’s organizational structure by providing details for each committee, working group, task group, or interest group:
  - [ ] Add a short description of the group’s function/objective  
    _Example: “The Architecture WG maintains the technical architecture for the project.”_
  - [ ] Add joining instructions  
    _Example: “Anyone interested can join by emailing the chair at example@email.com.”_
  - [ ] Include meeting cadence and calendar invite info
  - [ ] Include mailing list info and subscription instructions
  - [ ] Link to group-specific repos, file directories, chat channels, or project boards

Review and update core sections:
- [ ] Update or add any roles or responsibilities important for your Project's context.
- [ ] Review the Meeting Policy and update templates if needed
- [ ] Clarify the “Guidelines for Decision-Making” section:
    - [ ] Document how contributions are accepted (e.g., via PRs)
    - [ ] Ensure each working group has a `CONTRIBUTING.md` in its repository
- [ ] Review the Specification Development and Release Management Process:
    - [ ] Document how work packages are created, assigned, and reviewed
- [ ] Update the Access Rights table as needed
- [ ] Review the Git Development Flow section (if using git-based version control)
- [ ] Update the Publication and Advancement Guidelines:
    - [ ] Link any relevant editorial tools or requirements from SDOs you may be working with
- [ ] Review the Notice Requirements and IPR Review Guidelines
- [ ] Update the Additional Resources and Reference Materials section
    - _Note: Information here is non-normative but helpful for users._
- [ ] Remove unnecessary or inapplicable notes, files, or diagrams

---

### 3. Update Reference Diagrams

> 💡 Editable diagrams are in the [`/Diagrams`](../Diagrams) directory (draw.io format).

- [ ] Update the organization structure diagram (`organigram.svg`)
- [ ] Update review & approval process diagrams (`R_A-1.svg`, `R_A-2.svg`)
- [ ] Update specification development process diagrams

---

### 4. Update Working Group Templates

> 💡 Consider creating a Working Group Template repo to make launching new groups easier.

- [ ] Add status badges (e.g., license, build, last updated) if using
- [ ] Review and customize standard files per group:
    - [ ] `CONTRIBUTING.md`
    - [ ] `LICENSE.md`
    - [ ] `README.md`
- [ ] Update release planning documentation

---

### 5. Community Onboarding

> 💡 [LFX tools](https://lfx.linuxfoundation.org/tools/) can help manage calendar invites, mailing lists, votes, onboarding, and engagement.

Set up GitHub (or GitLab, or version control tool of choice) community features:
- [ ] Create GitHub teams and invite participants
- [ ] Update instructions on how contributors sign the license agreement
- [ ] Customize issue and PR templates and labels
- [ ] Consider adding workflow automations for onboarding, triage, and project tracking
- [ ] Create a “New Contributor Onboarding” checklist
- [ ] Enable GitHub Discussions or Project Boards if using them

---

### 6. Final Review & Launch

- [ ] Review the updated [Organization_Operational_Process.md](./Organization_Operational_Process.md) with stakeholders
- [ ] Tag an initial release (e.g., `v1.0.0`) and update `CHANGELOG.md`
- [ ] Obtain Steering Committee approval to adopt/update document
- [ ] Update adoption date, publish the documents, and notify your community
- [ ] Solicit feedback from community members and iterate as necessary

---

## 📢 Feedback & Iteration

Continuous improvement helps everyone! Please [open an issue or PR](https://github.com/Joint-Development-Foundation/operational_template_open_standards/issues) to share feedback or improvements for this checklist.
