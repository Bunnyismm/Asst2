# CS 1430 Assignment 2: The Cost of College

Build a menu-driven Python program that takes a yearly college cost and a credit load, then shows what that money works out to per semester, per month, per class day, per credit, and per CS 1430 class period.

**The full instructions are in the Assignment 2 student guide on Canvas.** This page is a quick reference.

## The one rule

Your wording and menu design are yours. Your numbers must be exact, to the cent.

## What's in this repo

| File | What it is for | Do you edit it? |
|---|---|---|
| `main.py` | Your program. All of your Python goes here. | **Yes.** The only Python file you edit. |
| `check.py` | Tests your work and writes `SUBMISSION.txt`. | No. Never. |
| `AI_NOTES.md` | Your structured AI review. | Yes. Writing, not code. |
| `README.md` | This page. | No. |
| `.gitignore`, `.gitattributes` | Git housekeeping. | No. |

## Inside main.py

- **Constants** at the top. Use them in your math. Do not change them.
- **Five function stubs.** Each one returns `0` right now. Replace that with the real calculation.
- **`main()`** with the menu loop started for you. Add the two input prompts, your menu, and a branch for each choice.
- **Launch lines** at the bottom. Leave them exactly as they are.

## The menu contract

- Ask for the **total cost for one year**, then the **credits this semester**, once each, before the menu.
- Keys **1** to **5** show the five results, in any order you like.
- Key **6** runs your Worth It? extension. `check.py` does not test option 6; it is graded from your slide deck.
- **Q** quits.

## Commands

```
git clone https://github.com/YOUR-USERNAME/Assignment2.git C:\CS1430\Assignment2
python main.py
python check.py
git add .
git commit -m "describe what you changed"
git push
```

## Checking your work

Run `python check.py` as often as you like. If anything says **FAIL**, fix only the first FAIL and run it again.

`check.py` is worth **40 of the 50 points**: 6 for each of the five functions, and 10 for the program itself. Every run writes `SUBMISSION.txt` into this folder with your points so far. Your points count only when the Git and GitHub checks pass, meaning your work is committed and pushed. Do not edit `SUBMISSION.txt` by hand.

The other **10 points** are for your Worth It? extension (menu option 6), graded from your slide deck.

## Turning it in

1. Commit and push your final `main.py` and `AI_NOTES.md`.
2. Run `python check.py` one last time, after your final push.
3. Upload `SUBMISSION.txt` and `AI_NOTES.md` to Assignment 2 in Canvas.
4. Answer the reflection questions and the debugging record in Canvas.
5. Submit your slide deck with your Worth It? screenshots and math explanation.
