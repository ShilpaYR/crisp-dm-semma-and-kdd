# SEMMA — Step-by-Step Like I'm in 6th Grade

**Goal:** We want to guess something from data. For example, can we guess if a student will pass a class?

## S — Sample (Pick the data)
- Find the file (like `students.csv`) and put it in the `data/` folder.
- Open the notebook. Load the file. Look at the first 5 rows. Count how many rows and columns.
- Check: Are there empty cells? Are numbers actually numbers?

## E — Explore (Look around)
- Make simple charts: bars and histograms.
- Write down 3 things you notice. Example: "Students who study more hours tend to score higher."

## M — Modify (Clean and fix)
- Fill empty values (e.g., put the average for missing numbers).
- Turn words into numbers (like "yes"/"no" → 1/0).
- Create helpful features (like study_hours_per_week).

## M — Model (Teach the computer)
- Split data into train and test (like 80%/20%).
- Try a simple model first (like logistic regression). Then try one more (like random forest).
- Compare which is better using a score (like accuracy).

## A — Assess (Judge the result)
- Show a confusion matrix (which errors happen most).
- Explain what the score means in plain words.
- Say what you would change next time to improve.

**Finish line:** Save your best model (or the code) and write the Medium story using `medium_draft.md`.
