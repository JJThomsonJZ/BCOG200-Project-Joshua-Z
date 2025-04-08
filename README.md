## BCOG200 - Final Project: Visual Attention Experiment  
### Author: Joshua Zhao  

---

## Project Overview  

This project is a **visual attention experiment** designed to test how quickly and accurately people can identify a target object (like a red "O") among several distractors (like black "X"s or "T"s). The goal is to simulate the classic selective attention task and collect data on participants’ reaction times and accuracy.

The experiment is built using Python and makes use of the following libraries:

- `pygame` (for graphics and interaction)  
- `matplotlib` (for data visualization)  
- `psycopg2` (to connect to a PostgreSQL database)  

---

## How It Works  

Here’s a quick breakdown of how the experiment flows:

1. **Welcome + Instructions** — A screen explains the task and how to interact with the program.  
2. **Participant Code Input** — Each user enters a unique code so their data can be saved properly.  
3. **Trials Begin** — The user completes multiple rounds of the attention task.  
4. **Results + Analysis** — The program shows a graph of the user’s reaction times and provides feedback.  
5. **Debriefing** — A final screen thanks the participant and ends the session.

---

## Key Functions  

### `show_instructions(screen)`  
Displays an instruction screen with task details and control instructions using pygame.

### `get_participant_code(screen)`  
Lets the participant enter a unique ID to tie all trial data to their session.

### `generate_objects(num_objects, target_char)`  
Randomly places distractors and one colored target on the screen. Returns their coordinates and labels.

### `run_trial(target_char, num_objects)`  
Runs a single trial: displays objects, tracks the user’s click, and measures how long they take. Also records whether they clicked the correct object.

### `run_experiment(screen, participant_code)`  
Runs a full experiment session (usually around 15–20 trials), collects data, and returns it.

### `save_results_to_db(data, participant_code)`  
Saves all results to a PostgreSQL table using `psycopg2`. Each trial includes reaction time, accuracy, and other relevant info.

### `analyze_results(results)`  
Generates a histogram of reaction times using `matplotlib`, and calculates summary stats like average time and accuracy.

### `show_debrief(screen)`  
Shows a closing screen thanking the participant for completing the experiment.

---

## Sample Use Case  

Imagine a cognitive science student wants to explore how visual attention works. They run this experiment with a few classmates. Each participant enters their ID, reads the instructions, completes the trials, and sees their performance visualized in a graph. Their results are saved to a database for later analysis.

---

## Data and Storage  

No external files are required — everything is generated during runtime.  

If using the database option, the `attention_results` table looks like this:

| Column name        | Type     | Description                               |
|--------------------|----------|-------------------------------------------|
| `id`               | SERIAL   | Auto-incremented primary key              |
| `participant_code` | VARCHAR  | The participant’s entered ID              |
| `trial_num`        | INT      | The trial number in sequence              |
| `target_position`  | TEXT     | Coordinates of the target object          |
| `click_position`   | TEXT     | Coordinates of where the participant clicked |
| `correct`          | BOOLEAN  | Whether the participant found the target  |
| `reaction_time`    | FLOAT    | Time taken to respond (in seconds)        |
| `timestamp`        | TIMESTAMP| When the trial was completed              |

---

## Tools and Libraries Used  

- Python
- pygame  
- matplotlib  
- psycopg2 (for PostgreSQL database connection)

---

## References  

This experiment was inspired by:  
Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).  
*Methods for online testing of visual attention*. *Journal of Visualized Experiments: JoVE*, (96), 52470.  
[https://doi.org/10.3791/52470](https://doi.org/10.3791/52470)

---
