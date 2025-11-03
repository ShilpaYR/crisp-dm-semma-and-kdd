# Assignment 4: CRISP-DM, SEMMA, and KDD — Project Pack

**Due:** Sunday 11:59pm  
**Submission:** Website URL (link to your GitHub repo)

This repo contains three *separate* subprojects — one per methodology — each using a *different* dataset:

- **CRISP-DM** → Suggested dataset: *Walmart Sales Forecasting* (Kaggle) or similar retail sales dataset.
- **KDD** → Suggested dataset: *Telco Customer Churn* (Kaggle).
- **SEMMA** → Suggested dataset: *Student Performance* (UCI) or an education outcomes dataset.

> You can replace with other datasets (Kaggle / Papers With Code) if you prefer. Just update the `README.md` in that subfolder.

## What’s inside

- `CRISP-DM/`, `KDD/`, `SEMMA/` — Each has:
  - `README.md` with step-by-step tasks and deliverables
  - `checklist.md` for grading-aligned self-audit
  - `critique_prompts.md` — ready-to-copy prompts for Claude / GPT‑5 as a **world‑renowned methodology critic**
  - `medium_draft.md` — structured outline to turn into a Medium article
  - `notebook.ipynb` — starter Colab-ready notebook scaffold
  - `data/` — put your raw files here
- `requirements.txt` — common Python libs (feel free to add/change)
- `.gitignore` — ignore data and environment clutter

## How to use

1. **Pick/Download the dataset** for each subproject (three different datasets). Place CSV/JSON/Parquet in that subproject’s `data/` folder.
2. Open the matching **`notebook.ipynb` in Colab** (Upload or open from GitHub) and follow the TODOs.
3. After each phase, **copy a critique prompt** from `critique_prompts.md` and paste into Claude/GPT‑5. Apply fixes, repeat until strong.
4. Export artifacts (diagrams, charts, metrics) and update **`README.md` + `medium_draft.md`**.
5. Record a **YouTube walkthrough** using the `README.md` as your script.
6. Push everything to GitHub and submit your repo URL.

---

**Tip (optional):** Explore automation helpers like [open-interpreter](https://github.com/KillianLucas/open-interpreter) and [MetaGPT](https://github.com/geekan/MetaGPT) to plan and script repeated tasks. If you dockerize, note Python deps in a `Dockerfile` and keep notebooks portable.

**Reminder:** You must still **verify/validate** any model/code that an AI system generates and ensure the final work is *yours*.
