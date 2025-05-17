# Visual Attention Experiment

**Course:** BCOG 200
**Author:** Joshua Zhao
**GitHub Repo:**[https://github.com/JJThomsonJZ/BCOG200-Project-Joshua-Z](https://github.com/JJThomsonJZ/BCOG200-Project-Joshua-Z)

## Overview

This is my last project for BCOG 200 which is an attention task in Python: participant attempts to find as fast as possible a red "O" letter amidst other black letters.The program tracks how quick people are at finding it and whether they click on the correct thing.

I was inspired by visual attention research in cognitive science and was interested in trying to make one myself.It also allowed me to get some experience in using Python with functions, Pygame, and Matplotlib.

## How It Works

1. **Participant No. Input** – RA will enter an ID that match the participant
2. **Welcome + Instructions** – show the task description
3. **Trials** * 20 – each trial shows letters and measures response
4. **Debriefing** – says thanks & simpely explain the experiment and ends the experiment
5. **Results + Graph** – after RA prerss "results" button shows reaction time and accuracy

## Code Structure (Main Functions)


| Function                                      | Description                                               |
| --------------------------------------------- | --------------------------------------------------------- |
| `get_participant_code(screen)`                | Lets the RA type in their ID                             |
| `show_instructions(screen)`                   | Shows instructions at the start (press space to begin)    |
| `generate_objects(num_objects, target_char)`  | Creates one red target and some distractors on the screen |
| `run_trial(screen, target_char, num_objects)` | Runs one trial and tracks how fast/correct the user is    |
| `run_experiment(screen, participant_code)`    | Runs multiple trials and saves the results                |
| `show_debrief(screen)`                        | the final thank-you screen                                |
| `analyze_results(results)`                    | Uses matplotlib to show a histogram and summary stats     |

## Data Storage

Results are saved automatically to a `.csv` file in the `data/` folder. the table look like this:


| Column Name       | Type      | Description                          |
| ----------------- | --------- | ------------------------------------ |
| id                | SERIAL    | Auto-generated row ID                |
| participant\_code | VARCHAR   | What the RA typed as ID             |
| trial\_num        | INT       | Which trial it was                   |
| target\_position  | TEXT      | Where the red “O” appeared         |
| click\_position   | TEXT      | Where the user clicked               |
| correct           | BOOLEAN   | True/False if they clicked correctly |
| reaction\_time    | FLOAT     | Time taken to click (in seconds)     |
| timestamp         | TIMESTAMP | Date/time of the trial               |

## How to Run (Multi-Platform)

This code should work on macOS, Windows, or Linux, as long as you have Python and the required packages.

### Step-by-step:

1. Make sure you have **Python 3.8 or newer** installed
2. Open your terminal or command prompt
3. Navigate to the project folder
4. Run this to install everything:
   ```bash
   pip install -r requirements.txt
   ```
5. Then run the experiment:
   ```bash
   python src/main.py
   ```

If you're on macOS and see a “pygame not found” error, you might need to use `python3` instead of `python`.

## Requirements

Listed in `requirements.txt`. The main ones are:

* `pygame`
* `matplotlib`
* `pandas`
* I ask chatGPT 4o how to use requirements.txt. here is the instructions - please ran this line:
  ```
  pip install -r requirements.txt
  ```

## Project Highlights

* Built from scratch using Python
* Interactive Pygame window with real-time mouse input
* Measures and saves reaction times
* Simple graph of performance shown at the end
* Designed to be reusable and expandable (can change number of trials, difficulty, etc.)

## References

Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).
*Methods for online testing of visual attention.*
Journal of Visualized Experiments: JoVE, (96), 52470.
[https://doi.org/10.3791/52470](https://doi.org/10.3791/52470)
