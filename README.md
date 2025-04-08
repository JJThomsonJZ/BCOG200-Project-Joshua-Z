## BCOG200 - Final Project: Visual Attention Experiment

### Author: Joshua Zhao

---

## Description

This is a **visual attention test** that measures the response speed and accuracy of selecting a target object among distractors. The task simulates the classic selective attention experiment. Participants must find a specific target (e.g., red "O") among distractors (e.g., black "X", "T", etc.).

The program is written in Python and uses:

- `pygame`
- `matplotlib`
- `psycopg2`

Experimental Flow:

1. Instruction Screen

2. Participant ID Input

3. Multiple Trials

4. Result Analysis

5. End of Experiment Debriefing

---

## Function/Method Overview

### `show_instructions(screen)`
Use pygame to display a full-screen instructions panel. Explain the task and controls before starting.

### `get_participant_code(screen)`
Prompt the user to enter a participant code, which will be tied to all saved trial data.

### `generate_objects(num_objects, target_char)`
- Randomly generate distractor letters and one colored target letter.
- Place them at random screen coordinates.
- Return a list of objects and their locations.

### `run_trial(target_char, num_objects)`
- Display a visual trial on the screen.
- Capture the participant's clicks and measure response times.
- Return correctness and reaction times.

### `run_experiment(screen, principal_code)`
- Run a random series of trials (e.g. 10-20).
- Collect and return trial data.

### `save_results_to_db(data, principal_code)`
- Insert results into a PostgreSQL table using `psycopg2`.
- Ensure each trial is associated with a participant.

### `analyze_results(results)`
- Display a reaction time histogram using `matplotlib`.
- Compute and print the average response time and accuracy.

### `show_debrief(screen)`
- Display a thank you screen at the end of an experiment session.

---

## Example Use Case

A cognitive science student is conducting a study of visual attention. Participants start the experiment, read the instructions, enter a participant code, and complete 15 trials. Afterwards, their results (response times and accuracy) are saved in a database and visualized as a histogram.

---

## Input and Output Data Formats

This experiment **does not require any external input files**. All visual objects are generated procedurally on each trial.

If connected to a PostgreSQL database, the output table `attention_results` has the following structure:

| Column name | Type | Description |
|---------------------|-------------|---------------------------------------|
| `id` | SERIAL | Primary key |
| `participant_code` | VARCHAR | Participant ID entered by the user |
| `trial_num` | INT | Trial sequence number |
| `target_position` | TEXT | Position of the red target |
| `click_position` | TEXT | Position clicked by the user |
| `correct` | BOOLEAN | Whether the user clicked the target |
| `reaction_time` | FLOAT | Response time (seconds) |
| `timestamp` | TIMESTAMP | Automatically generated |

---

## Technologies used

- Python 3.x
- pygame
- matplotlib
- psycopg2 + PostgreSQL

---

## Citations

Inspired by:
Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).
*Methods for online testing of visual attention*. *Journal of Visualized Experiments: JoVE*, (96), 52470.
https://doi.org/10.3791/52470
