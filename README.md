# Operational Template for Open Standards Projects

This repository provides a customizable set of documents and templates to help open standards projects establish clear, transparent, and sustainable practices for day-to-day project operations. These templates encourage projects to adopt procedural guidelines that ensure fairness, openness, and due process as promoted by the [American National Standards Institute's Essential Requirements](https://ansi.org/american-national-standards/ans-introduction/essential-requirements) and the [World Trade Organization's Principles for the Development of International Standards, Guides and Recommendations](https://www.wto.org/english/tratop_e/tbt_e/principles_standards_tbt_e.htm).

This material is further designed to be compatible with projects using governance structures established in the [Community Specification License](https://communityspec.dev) and/or the [Joint Development Foundation Membership Agreement](https://jointdevelopment.org) version 5 or higher. Whether you're starting a new Joint Development Foundation project or refining your existing governance, this template offers a practical starting point for defining how your community collaborates.

---

## 🚀 Quick Start

1. **Fork this repository** into your organization or working group’s GitHub account.
2. **Rename your fork** to reflect your project name (e.g., `myproject-operational-process-document`).
3. **Customize the templates**:
    - Replace placeholders like `{{PROJECT_NAME}}`, `{{YEAR}}`, and `{{CONTACT_EMAIL}}`.
    - Use our [Getting Started Checklist](./Process_Documents/getting-started-checklist.md) to tailor the information for your project.
4. **Commit your changes** and share with your stakeholders for review.

> 💡 **Tip:** Search for `{{` in the repo to find all fields needing customization. You can speed this up by using a find-and-replace tool or by running a simple setup script (see below for an example).

---

## 📁 What’s Included

| File/Directory                                  | Description                                                                 |
|-------------------------------------------------|-----------------------------------------------------------------------------|
| `/Process_Documents/`                           | Core templates for project operations                                       |
| `/Diagrams/`                                   | Editable diagram sources (draw.io format)                                   |
| `.github/`                                     | Optional GitHub configurations like issue templates and contribution guides |
| `README.md`                                    | Overview and guidance for customizing the repo                              |
| `LICENSE`                                      | Open source license under which the templates are shared                    |
| `index.yaml`                                   | Canonical links and references for your project                             |
| `getting-started-checklist.md`                  | [Checklist for adapting these templates](./Process_Documents/getting-started-checklist.md) |
| `Glossary.md` / `Glossary & Terms`              | Informational document containing terms common in standards development     |

---

## 🧰 Key Templates

- **Project Charter:** Defines the project's scope, mission, and structure.
- **Governance Model:** Outlines decision-making, voting, and membership rules.
- **Participation Guidelines:** Sets expectations for contributors and stakeholders.
- **Change Process:** Documents how proposals and updates are introduced and approved.

---

## 👥 Who Should Use This

- **New JDF Projects or affiliated projects** looking to establish operational clarity
- **Working groups** developing technical specifications or open standards
- **Maintainers and coordinators** formalizing governance and participation processes

---

## 🛠 Tips for Customization

- **Find placeholders:** Search for `{{` to quickly find all template fields.
- **Use scripts:** For bulk replacement, try a script like this:
    ```bash
    #!/bin/bash
    # Example: Replace all occurrences of {{PROJECT_NAME}} in all markdown files
    find . -name "*.md" -exec sed -i '' 's/{{PROJECT_NAME}}/MyProjectName/g' {} +
    ```
- **Keep up to date:** Regularly check for updates or improvements to these templates and keep your project’s copies in sync.
- **Cross-link:** Update all internal links after renaming or moving files and directories.
- **Remove what you don’t need:** Delete any template files, diagrams, or notes that don’t apply to your project.

---

## 📢 Example Implementations

- [UXL Foundation Operational Procedures](https://github.com/uxlfoundation/uxl_operational_procedures)

---

## 🤝 Contributing

We welcome contributions to improve the clarity, accessibility, and utility of these templates.

- Please open an [issue](https://github.com/Joint-Development-Foundation/operational_template_open_standards/issues) or [pull request](https://github.com/Joint-Development-Foundation/operational_template_open_standards/pulls) if you have suggestions or improvements.
- If you find an issue that needs to be addressed, please open an issue so we can continue to build a better template together.
- This project operates under a [Code of Conduct](./.github/CODE_OF_CONDUCT.md).

---

## 📄 License

This template is shared under the [Creative Commons Attribution 4.0 International License](./LICENSE).

---

<!--
TEMPLATE: Replace all `{{PLACEHOLDER}}` values before using in your project.
If you have feedback or improvements, please contribute them upstream!
-->
