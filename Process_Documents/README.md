# Open Standards Process Documents

This directory includes the core documents necessary to generate an operational procedures document for your Project or organization. 

1. **Getting Started**: Use the [initialization script](../Resources/initialization-script.py) and [Getting Started Checklist](../Resources/getting-started-checklist.md) to help modify and customize the [Operational Process Document](Organization_Operational_Process.md) in this directory. 
2. If needed, follow the instructions in the [Diagrams README](../Diagrams/README.md) to customize any diagrams you may need. Export your modified diagrams as .svg files and save them in the [/images](/Process_Documents/images/) directory.
3. Review the materials and suggestions in the [Resources](../Resources/) directory. Consider adapting and adopting these additional checklists and training materials to augment and support your community. 
4. Publish the customized Operational Process Document for your community, and follow your Operational Process to propose, approve, and publish modifications.

> 💡 **Tip:** Use a static site generator (like GitHub pages) to render your process document as an easy-to-read webpage.

## 🚀 How to Use the Initialization Script to Bootstrap

Simplified Directory structure:

```
project/
├── Resources/
│   └── initialization-script.py
└── Files/
    ├── index.md
    └── index.yaml
```

### 1. Open a terminal and navigate to the project root

```bash
cd path/to/project
```

This folder should contain both the `Resources` and `Process_Documents` directories.

---

### 2. Run the script to generate `index.md`

Use **python3** (or **py** on Windows):

```bash
python3 Resources/initialization-script.py Process_Documents/index.yaml Process_Documents/index.md
```

or on Windows:

```powershell
py Resources\initialization-script.py Process_Documents\index.yaml Process_Documents\index.md
```

This will:

* Load values from **Process_Documents/index.yaml**
* Generate **Process_Documents/index.md** with values applied