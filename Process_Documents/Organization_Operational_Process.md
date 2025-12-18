# {{PROJECT-FULLNAME}} Operational Process Document

```
Note: This document is a template that needs to be customized for your Organization.
Section notes should be deleted once customization is complete. Content in braces or italics denotes other areas for updating.
```
**{{DOCUMENT-STATUS}} version {{VERSION}}**
**Published on: {{PUBLICATION-DATE}}**

**Table of Contents**
1. [Introduction](#introduction)
2. [Governance](#governance)
   * [{{PROJECT-SHORTNAME}} Organizational Structure](#project-shortname-organizational-structure)
   * [Roles & Expectations](#membership-roles--expectations)
   * [Meeting Policies](#meeting-policies)
   * [Decision-Making](#decision-making-practices-and-consensus-guidelines)
3. [Specification Development and Release Management Process](#specification-development-and-release-management-process)
   * [Review and Approval Guidelines](#review-and-approval-guidelines)
   * [Roadmap and Release Planning](#roadmap-and-release-planning)
   * [Specification Development Lifecycle](#specification-development-lifecycle)
   * [Guidelines for {{PLATFORM}} Workflow (optional)](#guidelines-for-platform-workflow-optional)
4. [Publication and Collaboration Guidelines](#publication-and-collaboration-guidelines)
   * [Collaboration with other Standards Developing, Open Source, or Industry Organizations](#collaboration-with-other-standards-developing-open-source-or-industry-organizations)
   * [Notice Requirements and IPR Review Guidelines](#notice-requirements-and-ipr-policies)
5. [Additional Resources and Reference Materials](#additional-resources-and-reference-materials)
   * [Project Templates](#project-templates)
   * [Project Onboarding and Training](#project-onboarding-and-training)

## Introduction

This Operational Process Document is a living document that outlines the core procedures, roles, and decision-making processes that guide the day-to-day activities of the {{PROJECT-FULLNAME}} community. It is designed to promote transparency, accountability, and consistency in how the project operates, collaborates, and evolves over time.

Upon Approval of the Steering Committee, this document may be updated periodically to reflect the changing needs of the project and its participants. Updates should be proposed through the project’s defined decision-making process and tracked via version control.

## Governance

{{PROJECT-FULLNAME}} ({{PROJECT-SHORTNAME}}) is a Community Specification License project hosted by {{LEGAL-PARENT}}. Its Governance policy is as set forth in the GOVERNANCE.md file of the Project repositories. In the event of a conflict or inconsistency, the documents shall control in the following order of precedence (from highest to lowest): the terms of the Community Specification License, the {{LEGAL-PARENT}} Technical Project Charter and Series Agreement, and any policies or procedures adopted by the Project as outlined in this Process Document.

### {{PROJECT-SHORTNAME}} Organizational Structure

```
Note: Replace this example diagram with your own Organization organigram. 
```

<figure>
	<img src="images/organigram.svg" alt="{{PROJECT-SHORTNAME}} Organigram">
	<figcaption>{{PROJECT-SHORTNAME}} Organigram</figcaption>
</figure>

```
Note: The content in this section should not be an exhaustive description of each group, but rather a summary that provides pointers for newcomers or those looking for more information. 
```

#### Steering Committee *(JDF Projects Only)*

The Steering Committee is the body that is responsible for governing the Project, including approving Final Deliverables as a consensus product of the Working Groups. It also approves the formation of new project Working Groups or sub-committees.

**Steering Committee Composition**: 
```
Note: Refer to the Project Charter of the Membership Agreement packet to indicate how Steering Committee representatives are named, along with any supporting policies for participation and engagement.
```
**Steering Committee Meeting Information**: 

```
Note: Meetings should be held on a defined cadence, and ad-hoc meetings may be called with 7 or more days advance notice. Meeting notices must include an agenda with the topics to be discussed as well as any votes or resolutions to be taken during the meeting. Projects may adopt the degree of formality for meeting management that best suits their needs. Meeting minutes must be recorded and include the attendance and records of any votes or discussion outcomes.
```
**Steering Committee Mailing List Information**: _list information about SC mailing lists and who may post to them_

**Steering Committee Workspaces**: _list any tools or areas that SC representatives must be able to access_

#### Working Group(s)

The Project may have multiple Working Groups, and each Working Group will work within their defined scope on certain deliverables as set forth in its Working Group Charter. Changes to a Working Group Charter must be approved by the Steering Committee.

```
Note: This section should be updated each time a new Working or Sub-Working Group is added or removed.
```

* {{PROJECT-SHORTNAME}} has the following Working Groups:
  * Working Group Name 1
    * **Brief Description of Scope:**
    * **Link to Charter:**
    * **Link to Meeting Information:**
    * **Link to Mailing List Information:**
    * **Link to  Workspaces:**
    * **How to Join:**
  * Working Group Name 2
    * **Brief Description of Scope:**
    * **Link to Charter:**
    * **Link to Meeting Information:**
    * **Link to Mailing List Information:**
    * **Link to  Workspaces:**
    * **How to Join:**

#### Project Committee(s) *(Optional)*

```
Note: Projects may have one or more Committees to work in areas that support the technical development. Common examples include Marketing, Budget, and Events Committees. Committees do not produce technical deliverables and participation is often used as a benefit of Membership. This section should be updated each time a new Committee is added or removed.
```

{{PROJECT-SHORTNAME}} may establish one or more non-technical Committees to advance its work.

* {{PROJECT-SHORTNAME}} has the following Project Committees:
  * Committee 1
    * **Purpose of Committee/Key Responsibilities:**
    * **Link to Charter:**
    * **Link to Meeting Information:**
    * **Link to Mailing List Information:**
    * **Link to  Workspaces:**
    * **How to Join:**
  * Committee 2
    * **Purpose of Committee/Key Responsibilities:**
    * **Link to Charter:**
    * **Link to Meeting Information:**
    * **Link to Mailing List Information:**
    * **Link to  Workspaces:**
    * **How to Join:**

### Membership Roles & Expectations

#### {{PROJECT-SHORTNAME}} Membership

{{PROJECT-SHORTNAME}} Members are eligible Organizations that have signed the Membership Agreement at the Steering, General, or Contributor level. Members may appoint individual representatives from their Organization or Affiliate to participate in Working Groups and Committees. All Members and their selected representatives are expected to abide by the Code of Conduct, Contributing, Governance, and License policies as set forth in the [{{PROJECT-SHORTNAME}} Membership Agreement]({{MEMBERSHIP-AGREEMENT}}).

Trade Associations, Industry Forums, Standards Developing or Open Source organizations, and other Membership-based organizations are not eligible for Membership and should participate under the terms of a mutually-agreed MOU. Individuals are not eligible for Membership, but may make contributions to public repositories under the terms of that repository's open source license(s) and may be permitted to provide other contributions under the terms of the Non-Member Participation Agreement in the Membership Agreement (Appendix C). 

The table below summarizes the rights granted to each level for participation in the technical project, per the terms of the Project and Working Group charters. In addition to these rights, the Steering Committee may outline additional membership benefits, fees, or requirements for each level which can be found at {{PROJECT-URL}} if applicable. 

```
Note: Provide a description of the expectations for each participation level *as it pertains to the technical deliverables* - refer to the Membership Agreement to confirm the correct selections for your Project.
```

<table>
  <caption>Participation Levels</caption>
  <thead>
    <tr>
        <th></th>
        <th>Steering</th>
        <th>General</th>
        <th>Contributor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td colspan="5"><strong>Leadership</strong></td>
    </tr>
    <tr>
        <td>Eligible to lead Steering Committee</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Eligible to lead Working Group</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Eligible to lead Subcommittee or Technical Task Force</td>
        <td>Yes</td>
        <td>Task Forces only</td>
        <td>No</td>
    </tr>
    <tr>
        <td colspan="5"><strong>Participation</strong></td>
    </tr>
        <tr>
        <td>Eligible to join the Steering Committee</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Eligible to join Working Group(s) and Task Forces</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Select Working Groups and Task Forces</td>
    </tr>
    <tr>
        <td>Eligible to join Committee(s)</td>
        <td>Yes</td>
        <td>Marketing Committee only</td>
        <td>No</td>
    </tr>
    <tr>
        <td colspan="8"><strong>Contribution</strong></td>
    </tr>
    <tr>
        <td>Contribute to Working Groups</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Propose new Working Groups</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>May propose a Work Package or Feature</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
    </tr>   
    <tr>
        <td colspan="5"><strong>Decision-Making</strong></td>
    </tr>
    <tr>
        <td>Decides on Final Approval of Publications, Working Group formation, and/or Membership Agreement Changes</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Vote in a Supermajority vote</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
	      <td>Vote in an informal technical vote</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        <td colspan="5"><strong>Access to Meetings</strong></td>
    </tr>
    <tr>
        <td>Attend Work Group meetings (F2F, conference calls, interim)</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td colspan="5"><strong>Process Administration</strong></td>
    </tr>
    <tr>
        <td>May propose the creation of a Working Group</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>May appeal on technical issues</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>May appeal on procedural issues</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
  </tbody>
</table>

**Roles & Expectations**

All Working Group and Committee Participants are expected to: 
* Read and adhere to the Membership Agreement terms, Operational Process Document, and all applicable policies 
* Familiarize themselves with their own organization's internal policies for engagement with standards bodies
* Take the [Antitrust training][antitrust-training]
* Use the workspaces provided by the Project for the purposes of making contributions
* Participate in good faith in the consensus-seeking process
* Inform the Project of any issue that may arise.

Working Group and Committee Chairpersons are expected to: 
* Follow the guidelines listed above for Working Group and Committee Participants
* Take the [Leading Effective Working Group Meetings Training][leadership-training]
* Ensure fair, timely review and approval for group decision-making in the standards development process
* Publish Notices in a transparent and timely manner

The Specification Editor(s) are expected to:
* 

The Steering Committee Chairperson is expected to:
* Follow the guidelines listed above
* Counter-execute new Membership Agreements on behalf of the Project
* ...

### Meeting Policies

```
Note: The policies in this section should apply to all meetings in the organization. While the language provided describes general best practices, you can modify this section liberally to fit how your community prefers to meet.
```

{{PROJECT-SHORTNAME}} Working Groups and Committees have regular and ad hoc teleconference meetings. All teleconference meetings are subject to the organization's IPR and Antitrust policies and:

* Must be announced on the group Mailing List at least 7 days in advance and include any planned votes or notices
* Must be published to the Project Meeting Calendar
* Must use the Project's Agenda and Minutes templates and post them to the Group's shared meeting directory
* Must record attendance information, key issues discussed, proposed action items or motions, and outcomes of any vote or consensus decision.
* Shall be open to any eligible Working Group or Committee participant
* May include invited guests or Non-Member participants upon Working Group approval at the invitation of the Working Group Chair
* May be recorded by consent of the Working Group/Committee participants
* May not permit personal AI Notetaking tools
* May not be publicly broadcasted (e.g. through streaming services)

#### Meeting Agendas, Minutes, and other Collateral

* Agenda and Meeting Minutes templates can be found in the [Template directory][meeting-templates].
* Meeting materials for each Working Group and Committee are located in that group's repository. 
  * Meeting materials include the Agenda, Minutes, and any presentations or documents discussed.
  * Meeting materials generated with assistance from AI tools must be marked as such.
  * Meeting minutes should be reviewed and approved  
* The Project's Meeting Calendar is maintained by LFX Meetings
* To subscribe to the Meeting Calendar, [click here][project-calendar]
* To view past or upcoming meetings, access meeting recordings or calendar invites, go to [https://openprofile.dev]()

### Decision-Making Practices and Consensus Guidelines
{{PROJECT-SHORTNAME}} develops its specifications through voluntary consensus, meaning that:

* Participation is open to all interested stakeholders.
* Decisions are made by consensus. Consensus means substantial agreement, absent of sustained objection, not necessarily unanimity.
* The deliverable development process is transparent. Procedures are accessible and allow for input and review.
* There is a balance of interests, so no single group organization or stakeholder group dominates decision-making.
* There is due process, including mechanisms for notices and procedural appeals. Due process means that any party with a direct and material interest has a right to participate by: a) expressing a position and its basis, b) having that position considered, and c) having the right to appeal. Due process allows for equity and fair play. 

[Section x.x of the Membership Agreement]({{MEMBERSHIP-AGREEMENT}}) outlines the terms of decision-making. The remainder of this section is intended to provide guidance on the operational application of these terms. 

```
Note: The following sections can be tailored for your Project. For example, if your Project will do much of its development on GitHub, you may provide additional guidance for how Working Groups can use informal voting or input gathering with upvotes or emojis, or you might add additional responsibilities and expectations for Chairpersons.
```

#### General Approach to Decision-Making

* Working Groups and Committees seek consensus as the preferred decision-making method.
* Consensus does not require unanimity, but the agreement of all participants is preferred.
* If consensus cannot be reached, Working Group or Committee Chairpersons may use voting mechanisms as an alternative.
* Chairpersons must ensure decisions are made efficiently, without undue delay due to unavailable participants or contributions.
* Decisions may be made in real-time meetings or asynchronous forums meetings with equal merit.
* Where attendance or engagement is sparse when viewed from normal participation levels, potentially controversial proposals should be made available to the broader membership or given more time for review.

#### Consensus-Seeking Procedures

* Informal methods for gauging consensus are encouraged (e.g., show of hands, use of "+1" or voting on Pull Requests).
* Ensure all eligible Participants have had an opportunity to provide input.
* Related contributions should be considered together before resolution.
* Agreement SHOULD be sought in all Project forums, including asynchronous discussions (meetings, email discussions, chat tooling).
* Chairperson(s) must consider:
  * The dominant view of Working Group participants
  * The nature and strength of any objections
* Consensus shall not be considered achieved if there is a sustained objection from one or more participants.
* Chairperson(s) must document consensus decisions based on these criteria.

#### Chairperson Responsibilities in Decision-Making

Working Group and Committee Chairpersons must:
* Ensure timely progress on decisions, and provide notice for decisions requiring formal input from the Working Group or Committee.
* Ensure the maintenance and access of up-to-date project documentation (e.g., README, contributing guides, release plans).
* Apply a defined Review & Approval process to all contributions.
* Ensure opportunity for participation in the decision making process. 

Working Group and Committee Chairpersons should:
* Use project management tools and automation to facilitate collaboration - for example, using GitHub Labels to indicate the type of review assigned to pull requests.
* Conduct technical discussions within view of all Working Group Participants, for example using GitHub Issues and PRs (not 1:1 chat messages).
* Close contributions that:
  * Don’t follow project contribution and IPR rules
  * Don’t meet quality standards
  * Fall outside the scope of the Project
  
Working Group and Committee Chairpersons may:
* Delegate tasks to other Participants (including chairing meetings).
* Limit time spent on specific agenda items or proposals.
* Require new information before reopening previously tabled or resolved issues.
* Add or remove Non-Members (Invited Guests) from Working Group meetings or other project forums.

The lists above are exemplary and not exhaustive.

#### Mechanisms for Reaching Decisions

Proposals should be available for a defined comment period prior to calling for a decision. In non-real-time settings, consensus should be developed through review, comment, and acceptance of modifications. When discussion stalls or needs resolution, Working Group and Committee Chairpersons may:

* Issue a statement of perceived consensus (accepted if no objections arise)
* Assign Action Items with short timelines
* Direct invitation for objectors to withdraw sustained objections
* Use informal voting mechanisms (surveys, "upvotes", polls, etc)
* Use a formal ballot mechanism, whereby each eligible Member organization may submit a vote through their designated voting representative. 

#### Formal Decision-Making Requirements

Notice must be given for formal decisions, which may include:
* A pull request or document listed on an agenda
* Agenda item proposing next meeting dates
* Proposal circulated via mailing list
* Review & Comment periods via GitHub or other tools
* Electronic ballots for major decisions. Formal ballots are required for Adoption of Approved or Final Deliverables.

#### Communication and Reporting

* Progress and work status, including the outcome of any major decisions, should be regularly communicated through status updates, changelogs, reports or other means.
* All Participants should take care to abide by the Project's public disclosure policies. 
* Working Group and Committee Chairpersons are responsible for ensuring transparent and consistent communication with other Participants, particularly through the Project's primary workspace (e.g. GitHub and/or mailing lists).

#### Handling objections when seeking consensus

Sparsely attended meetings or forums should not be used to drive through proposals that would not have broad support. Care should also be taken when decisions need to be made during peak holiday periods. Dissent or objections should be recorded in the appropriate forum (e.g. the Project's minutes or via an alternative proposal in GitHub). In many cases, clearly documenting the concerns, basis for the objection, or alternatives proposed may be sufficient for the dissenting Participant(s) to not sustain their objection and move forward with the consensus decision (alternatively, "Disagree and commit"). Participants are discouraged from sustaining their objections when it is clear that they would be overruled by a vote were one to take place.

If the objection is sustained, further action is required to move forward - the Proposal may be withdrawn, amended, countered, or put to a formal vote. The Working Group or Committee Chairperson may propose a deadline for any actions in order to ensure the timely functioning of the group. Meeting summaries must include the outcome of the discussion and which Participant(s) are responsible for next actions. If there is insufficient time for review in a real-time meeting, non-real-time decision-making approaches should be used and documented for the group.  

#### Voting

In the case that a decision cannot be made by consensus, or in the case that a formal vote is required per the terms of the Membership Agreement, the following guidelines apply. 

**Phrasing Questions or Resolutions for Votes**
The Working Group Chairperson is responsible for ensuring all voting questions are clear, concise, and unambiguous. Collateral related to the vote question should be made available along with the text of the vote in advance. Questions should be phrased positively (e.g., “Shall the group…?”) and not in a negative form such as “The group shall not…”.

Examples of well-phrased questions:
* “Shall the group approve the Specification?”
* “Shall the liaison be approved?”
* “Shall the new Work Package be approved?”
* “Shall the existing Work Package be stopped?”

For decisions involving three or more options, the group should reduce the choices to two using informal voting techniques before proceeding to formal voting. Binary choices should be phrased clearly, e.g. “Shall the group approve Proposal A or Proposal B?.”

**Voting Methods**
Each eligible Member company is entitled to one vote, which should be issued by that Member's designated voting representative or their delegate.Members may change their vote during the voting period, however the last recorded vote is the one that counts.

Voting methods may include:
* Electronic voting via tools such as LFX, Doodle, OpaVote, or Email
* Show of hands
* Verbal roll call

Votes should be acknowledged to confirm receipt and participation, particularly those taken electronically. 

**Voting Period Requirements**
In-person meetings: A vote may be taken during an in-person meeting with a minimum 30 days prior written notice.
Teleconference meetings: Votes taken during teleconference require a minimum 7 days prior written notice.
Electronic voting: Votes taken via electronic means require no advance notice but must be open for no fewer than 7 days and utilize only "yes" or "no" question phrasing.

**Voting Results**
Results of all votes must be recorded in the meeting record for the Working Group or Committee. For votes that took place asynchronously through electronic ballot, the Chairperson should report the outcome of the vote at the next meeting. 

#### Appeals
Decisions may be appealed via a pull request or an issue, and that appeal will be considered by the Working Group Chairperson in good faith, who will respond in writing within a reasonable time.

## Specification Development and Release Management Process

Standards and specification development processes differ from open source development. In open source communities, contributions are made by forking a project and submitting a patch or pull request back to the project. The open source maintainer then decides whether to accept or reject that contribution, but in the meantime the Contributor is free to leverage the code with their own modifications. 

On the other hand, standards and specifications development efforts typically seek to drive interoperability or shared procedures across different implementations or technical stacks. Standardization activities require agreement of a much broader group of stakeholders and contributors, thus a more democratic approach to development is necessary. 

The review and approval process below outlines how all contributions are evaluated and either accepted or rejected by a Working Group. 

```
Note: This section should be modified to suit the preferred tools and workflows of the Project. We have provided an example based on a typical specification project that is developing collaboratively on GitHub. In lieu of PRs, for example, your project may have some other documentation such as an Architectural Decision Record or proposal template to communicate a desired change or addition. 
```

### Review and Approval Guidelines
<figure>
	<img src="images/R_A-1.svg" alt="Review & Approval">
	<figcaption>Illustration of the Review & Approval process</figcaption>
</figure>

The review period is the period of time during which the contribution will be under review before being merged. In order to advance work in a timely fashion, the Project has adopted guidelines for Working Group review periods:

* Non-substantive editorial changes - for example typo fixes and grammatical corrections, broken links and other simple tasks - may be adopted without Working Group review.
* Minor changes to specification text and errata require at least one full day for review. Examples include updates to non-normative sections and notes, edits to prose, or edits to draft spec text which is still in active development. 
* Major changes require at least 3 days for review. Examples of major changes include significant edits to a planned feature, significant revisions to a term or definition, or changes to existing normative behavior.
* New feature proposals require at least 5 days for review. New features are additions or amendments to expected behavior, which have not been previously been identified for the current draft or candidate release.

While Working Group Chairpersons and their authorized delegates are responsible for overseeing these review periods, all Working Group participants are expected to respect the review guidelines and participate in good faith. 

**Approval Criteria**
A contribution is considered approved and therefore it can be merged if:
  * The contribution has not received any sustained objections during the review period, AND
  * At least {{3}} reviewers have indicated that they agree with the contribution
  
**Comments and Objections**
Working Group Participants may raise comments or objections during the review & approval process.

Any Working Group Participant or authorized Non-Member stakeholder may comment on contributions. All comments should be taken into consideration, but they don't all have to be addressed; the contribution's author(s) or the Working Group Chairperson may exercise discretion when choosing to incorporate relevant comments. In any case, in order to merge the contribution at least {{3}} reviewers MUST indicate that they agree with the contribution. 

Only Working Group Participants may raise an objection to a contribution. Objections must be taken into consideration by the Working Group and contribution author(s). If a contribution receives an objection, it must be resolved with the objecting party through the consensus process. Sustained objections must be resolved by vote, unless the objecting party rescinds their objection. 

### Roadmap and Release Planning

```
Note: The language in this section - e.g. Milestones, Stories, Epics - comes from common software development methodologies. You are welcome to use language and patterns that are more familiar for your industry or participants. 
```

Each Working Group's Scope is defined in its Working Group Charter document, part of the Membership Agreement. The Scope typically envision a long term outcome, for which there will be many milestones along the way. Working Groups may collaborate on several different types of deliverables, depending on what was indicated in the Working Group Charter document: specifications, source code, data sets, or other technical documents.  The first task of any Working Group is to build agreement for what should be achieved at each milestone. From there, specification development is the process of continuous development and review until the Working Group agrees that its goals for the scope have been sufficiently met.

#### Work Packages
Work Packages define scope and expected deliverables to achieve an outcome. They translate end-user requirements into actionable tasks that can be researched and implemented into spec text, source code, datasets, supporting documentation, test suites, etc. in a transparent way. Work Packages are the building blocks for a roadmap to achieve these desired outcomes.

Release Planning is the process through which a single Work Package or a collection of Work Packages are identified for upcoming versions of the specification and/or any supporting reference software. 

Work Packages may be further broken down into Epics, Stories, and Tasks, depending on the size or complexity of the Work Package. This can be useful for translating user needs, business requirements, or customer requests that are not defined in detail.

Work Packages must be approved by the Working Group through the consensus process before they can be developed and included in an upcoming release.

<figure>
	<img src="images/breakdown.svg" alt="Construction of Work Packages">
	<figcaption>Work Package Illustration</figcaption>
</figure>

### Specification Development Lifecycle
If the Work Package and Release Roadmap describe what the Working Group will create together and when, the Specification Development Lifecycle describes how. The diagram below illustrates the phases through which the group's objectives and plans are translated into usable technical documents. 

<figure>
	<img src="images/life-cycle.svg" alt="Specification Development Lifecycle">
	<figcaption>Specification Development Lifecycle</figcaption>
</figure>

#### Draft Deliverable Development - Guidelines for [Appendix A Section 4.1]({{MEMBERSHIP-AGREEMENT}})

**Work Package Definition**
In this phase, the group defines the work to be done in a given Draft deliverable - described above as a Work Package. Any Member may submit a new Work Package proposal. The proposal is discussed and refined collaboratively, after which the Working Group decides to either approve or reject it. If approved, the Work Package moves to the Development phase.

**Specification Development**
Work Packages are implemented as a series of changes to the specification document(s). Specifications consist of one or more documents, packaged separately or together as needed. Contributors should take care to ensure that changes are complete. For example, if a Work Package requires a change to the spec text, that change may also need to be reflected in a conformance document, reference implantation, or non-normative example. 

* Requirements Document: Contains the business (non-technical) requirements, derived from the Use Cases described in this document.
* Architecture Document: Describes the system’s functional elements and their interfaces or reference points.
* Technical Specification Document(s): Defines the detailed requirements to be met by a material, design, product, or service. These documents clarify the system’s configuration and architecture.
* Supporting Document(s): Includes profile and conformance data, metadata, schemas, and other supplemental information.

**Consistency Review**
When the Specification Development stage is complete, or very near completion, the Working Group will formally review the document(s). The purpose of this review period is to catch any gaps, errors, or issues, and to submit comments. Consistency review may also be used for reviewing the specification materials through a specific perspective, for example for Security or Accessibility. Consistency review is a thorough process that takes some time - Working Groups should be sure to include at least a two week consistency review period in their release timelines. 

The Consistency Review period is also an appropriate time to address specification formatting comments or issues, as style or editorial guidelines have a tendency to drift during the Development phase.

#### Working Group Approval - Guidelines for [Appendix A Section 4.2]({{MEMBERSHIP-AGREEMENT}})
After the Consistency Review period concludes, the Working Group must address any comments raised during this period. When all comments have been addressed, the document(s) will be eligible to become a Working Group Approved Draft Deliverable per Section 4.1 of the Membership Agreement. 

#### Final Approval - Guidelines for [Appendix A Section 4.3]({{MEMBERSHIP-AGREEMENT}})
No sooner than 30 days after the the Working Group approves the document(s) as a Working Group Approved Draft Deliverable, the document(s) may be sent to the Steering Committee for Final Approval.

#### Publication - Guidelines for [Appendix A Section 4.4]({{MEMBERSHIP-AGREEMENT}})
Once the Steering Committee has approved a Final Deliverable, the document(s) will be published in the following manner: 

* To publish the document(s), the Maintainer will create a new Release Tag.
* A new Release Tag will be produce with the content in the "main" branch and stored in the Release section of the GitHub repository.
* Any announcements or notifications - be it through Project Mailing Lists, social media posts, newsletters, or other channels - should be coordinated by the Members.
* Any forums to collect public input or feedback on the material, such as through a release discussion in GitHub or other forum, should be created and monitored. 
* The input collected during the Maintenance phase may be used to improve the Technical Specifications as well as to collect business requirements for future releases.

### Guidelines for {{PLATFORM}} Workflow (optional)
```
Note: This section assumes that your project will leverage a git-based development methodology. Remove this section if your Project will not be using a git-based version control system for development (GitHub, Gitlab, etc). Consider amending this section to reflect any platform-specific development guidelines your project will need to ensure all Members are able to contribute and review materials in a consistent manner. 
```

<figure>
	<img src="images/dev-process.svg" alt="{{PROJECT-SHORTNAME}} Technical Specifications Development Phases">
	<figcaption>{{PROJECT-SHORTNAME}} Technical Specifications Development Phases</figcaption>
</figure>

The project has selected {{PLATFORM}} to maintain its source of truth for the specification development process. The diagram below illustrates how contributions and discussions proceed through the specification development lifecycle via {{PLATFORM}}. It may be amended from time to time as new efficiencies or features are developed.

#### {{PLATFORM}} Access Rights

The table below outlines permission levels in {{PLATFORM}} based on project role. Permission exceptions may be made on a case by case basis with Approval from the Working Group or Committee. Platform access should be audited on an annual basis.

```
Note: If you have added any additional Working Group or Committee Roles in the Roles and Expectations section, add them to the table. Customize the section GitHub Teams or other features.  
```

<table>
  <caption>{{PLATFORM}} Access Rights</caption>
  <thead>
    <tr>
	    <th>Role</th>
	    <th>Platform Permission Level</th>
      <th>Requirements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Working Group or Committee Participant</td>
      <td>May be added to the {{PLATFORM}} and Working Group or Committee repository or team at the <i>TRIAGE</i> level.</td>
      <td>Must complete Project Onboarding steps before permissions are granted. Must enable 2FA.</td>
   </tr>
    <tr>
      <td>Working Group or Committee Chairpersons</td>
      <td>Must be added to the {{PLATFORM}} and Working Group or Committee repository or team at the <i>WRITE</i> level. </td>
      <td>Must complete Project Onboarding steps before permissions are granted. Must enable 2FA. Must take {{PLATFORM}} Training.</td>
   </tr>
   <tr>
      <td>Editors</td>
      <td>Must be added to the {{PLATFORM}} and Working Group repository or team at the <i>MAINTAIN</i> level.</td>
      <td>Must complete Project Onboarding steps before permissions are granted. Must enable 2FA. Must take {{PLATFORM}} Training.</td>
   </tr>
      <tr>
      <td>Steering Committee Chairperson(s)</td>
      <td>Must be added to the {{PLATFORM}} at the <i>ADMINISTRATOR</i> level.</td>
      <td>Must complete Project Onboarding steps before permissions are granted. Must enable 2FA. Must take {{PLATFORM}} Training.</td>
   </tr>
   </tr>
      <td>Non-Members</td>
      <td>May be added to the {{PLATFORM}} at the <i>READ</i> level with Approval from the Working Group.</td>
      <td>Must enable 2FA. Must take {{PLATFORM}} Training.</td>
   </tr>
  </tbody>
</table>

#### {{PLATFORM}} Workflow Process

**Semantic Versioning Guidelines**
The project will follow [https://semver.org/]() guidelines to effectively track work and stage it for approval or advancement.

<figure>
	<img src="images/semantic-versioning.svg" alt="Semantic Versioning">
</figure>

<table>
  <thead>
    <tr>
	    <th>Field</th>
	    <th>Use</th>
	    <th>Description</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>X</td>
    <td><i>Major Version Indicator</i></td>
    <td>This mandatory field SHALL identify the major version of the document as determined by the Working Group.
      Major versions contain major feature additions; MAY contain incompatibilities with previous document or specification revisions; and MAY change, drop, or replace existing interfaces. Initial releases are “1.0”.
    </td>
  </tr>
  <tr>
    <td>Y</td>
    <td><i>Minor Version Indicator</i></td>
    <td>This mandatory field SHALL identify the minor version of the document. It is incremented every time a minor change is made to the approved document version. Minor versions MAY contain minor feature additions or clarifications, be compatible with the preceding Major_Minor specification revision, and MAY provide evolving interfaces. The initial minor release for any major release is “0”, i.e. 1.0</td>
   </tr>
   <tr>
    <td>Z</td>
    <td><i>Service Indicator</i></td>
    <td>Incremented every time a corrective update is made to the <strong>Approved</strong> (not draft) document version by the WG.
    This field is OPTIONAL, and SHALL be provided whenever a service release of the document is made. The first service indicator release SHALL be “.1” for any Major_Minor release. Service indicators are intended to be compatible with the Major_Minor release they relate to but add bug fixes. No new functions will be added through the release of Service Indicators.
    </td>
  </tr>
  </tbody>
</table>

**Contributions and Branching**

Contributions in the platform should follow [Trunk Based Development](https://trunkbaseddevelopment.com/) patterns (see diagram below). 

<figure>
	<img src="images/Git-Flow-2.svg" alt="Platform Workflow">
	<figcaption>Platform Workflow</figcaption>
</figure>

Working Groups and Committees should use the the following branching guidelines for their repositories:

<table>
  <caption>Branch Guidelines for Repositories</caption>
  <thead>
    <tr>
	    <th>Branch</th>
	    <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
	    <td><i>Rel vX.Y.Z</i></td>
      <td>Release tags contain all the different versions of the specifications that have been approved by the Working Group or Steering Committee. The name of the release tag will follow [Semantic Versioning](#semantic-versioning) principles.</td>
   </tr>
    <tr>
	    <td><i>main</i></td>
      <td>This branch contains the latest version of the Technical Specification approved by the Working Group. Its content will be moved into a release-tag, after the <strong>Consistency Review</strong> and Technical Steering Committee <strong>Ratification</strong> phases.</td>
   </tr>
  </tbody>
</table>

**Requirements for Issues, Pull Requests, Discussions, and Project Management Tracking**


## Publication and Collaboration Guidelines

```
Note: This section should be updated to reflect any project-specific practices or requirements for publishing Approved Working Group documents. If there are custom tools, for example tools that generate the documents in multiple formats, or tools that ensure specific editorial requirements are in place, those should be included below. 
```
Approved Final Deliverables must be published in {{PDF, LaTEX, MD, etc}} on the Project website and must follow the [specification template](). All published deliverables must:

* Include the Document status as either a Working Group Draft, Working Group Approved Draft, or Final deliverable
* Include the Legal Disclaimer (See Additional Resources and Reference Materials)
* Include the copyright notice (See Additional Resources and Reference Materials)
* Include the publication date
* Be published on a stable URL

Published Source Code materials must include:
* a LICENSE.md file in the source repository
* SPDX License Headers for each file - see [SPDX short-form license identifiers](https://spdx.dev/ids/)
* a shield.io badge for the license in the README, e.g. 

![APM license](https://img.shields.io/badge/License-MIT-brightgreen)

### Collaboration with other Standards Developing, Open Source, or Industry Organizations

**Memorandums of Understanding**
The Project welcomes opportunities to collaborate with other Member-based organizations under the terms of a mutually agreed Memorandum of Understanding (MOU). This section defines the requirements for defining and approving an MOU. 

All MOUs must:
* Originate on the {{PROJECT-SHORTNAME}}'s MOU template paper
* Include designated points of contact
* Include the scope and goals of the collaboration
* Indicate which specific Working Groups, Events, Meetings, or Deliverables will be involved
* Include a date by which the collaboration will be reviewed and renewed or terminated
* Go through legal review prior to signature

**Advancement of Deliverables**
A Final Deliverable may be adopted for publication by a national or international standards development organization. As this path may incur financial or maintenance costs for the organization, Steering Committee Approval is required. Additionally, Specifications intended to be advanced through the ISO / IEC JTC 1 PAS process must be approved by Joint Development Foundation Projects.  

### Notice Requirements and IPR Policies

#### Notice Requirements

**Types of Notices**

* IPR Review Period Notices
* Exclusion Notices
* Publication Notices
* Withdrawal Notices
* Security Disclosure
* Legal Notices

**Publishing Notices**
The Working Group Chairperson(s) is responsible for publishing notices.

#### IPR Policies
All Working Groups must adhere to the copyright and patent policies indicated in the Working Group Charter. Questions about these specific policies or questions about incorporating linked libraries, 3rd Party Software, License compatibility, or binary distributions should be addressed by the Working Group Member Participants and Member Legal Counsel. If the Working Group is unable to arrive at an answer, the Steering Committee may address the question or seek a legal opinion on behalf of {{PROJECT-SHORTNAME}}.

Working Groups may request a change to their patent or copyright policy. All changes must be reviewed and approved by the Steering Committee, and Notice must be provided to Joint Development Foundation Projects and all Members. Depending on the nature of the changes and the status of the Working Group's deliverables, licensing changes may result in the creation of a new Working Group. 

The Trademark Policy is located at {{TRADEMARK-POLICY-URL}}. The brand and logo usage guidelines are located at {{BRAND-FILES}}.

IPR and other Legal questions should be sent to {{ADMIN-CONTACT}}. 

## Additional Resources and Reference Materials

### Project Templates

* [Presentation Template][meeting-templates]
* [Specification Template][meeting-templates]
* [Agenda and Meeting Minutes Template][meeting-templates]

### Project Onboarding and Training

All Member Participants must familiarize themselves with the following materials: 

**Legal Disclaimer Text for Published Documents**
The legal disclaimer to insert in each publicly published document is:

```
© `{{PROJECT-FULLNAME}}` {{YEAR}}, All rights reserved.

“THESE MATERIALS ARE PROVIDED “AS IS.”  The parties expressly disclaim any warranties 
(express, implied, or otherwise), including implied warranties of merchantability, non-infringement, 
fitness for a particular purpose, or title, related to the materials. The entire risk as to 
implementing or otherwise using the materials is assumed by the implementer and user. 

IN NO EVENT WILL THE PARTIES BE LIABLE TO ANY OTHER PARTY FOR LOST PROFITS OR ANY FORM OF 
INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OF ANY CHARACTER FROM ANY CAUSES 
OF ACTION OF ANY KIND WITH RESPECT TO THIS DELIVERABLE OR ITS GOVERNING AGREEMENT, WHETHER 
BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND WHETHER OR NOT 
THE OTHER MEMBER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.”
```

**Project Copyright Notice**
The copyright notice to include on project deliverables is:

`Copyright Contributors to {{PROJECT-FULLNAME}}.`

[project-calendar]: https://calendar.projectname.org
[antitrust-training]: https://training.linuxfoundation.org/training/antitrust-laws-and-open-source-software-project-management-and-participation-lfc105/
[leadership-training]: https://training.linuxfoundation.org/training/leading-high-performance-working-group-meetings-lfc120/
[meeting-templates]: https://
