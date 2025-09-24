# Data Science Institute (DSI) - Learning Repository

This repository contains coursework and projects for data science learning, covering Python, SQL, Excel, and exploratory data analysis.

## Environment Setup

This repo uses a **hybrid virtual environment approach**:
- **Base environment** (`.venv/`) for common data science packages
- **Project-specific environments** for projects with unique dependencies

### Quick Setup

```bash
# Create and activate base environment
python3 -m venv .venv
source .venv/bin/activate

# Install common packages
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
```

### Daily Usage

```bash
# For most work (notebooks, data analysis, homework)
source .venv/bin/activate

# For existing projects with their own environment
cd project_folder/
source .venv/bin/activate
```

### Creating New Project Environment (One-time Setup)

```bash
# Only when starting a NEW project that needs unique dependencies
cd new_project_folder/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # if requirements.txt exists
```

### When to Create Project Environment
- Projects with unique dependencies (like game frameworks)
- Projects that conflict with base environment packages
- Production-ready applications

**Note**: Pre-commit hooks run from DSI/ level and work regardless of active environment.
