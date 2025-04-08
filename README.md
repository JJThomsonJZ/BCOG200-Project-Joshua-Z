## BCOG200 - Final Project: Visual Attention Experiment  
### Author: Joshua Zhao  

---

## Project Overview  

This project is a **visual attention experiment** designed to test how quickly and accurately people can identify a target object among several distractors. 
goal: to simulate the classic selective attention task and collect data on participants’ reaction times and accuracy.

I ues Python and these libraries to built the experiment:

- `pygame` 
- `matplotlib`

---

## How It Works  

Here’s a quick breakdown of how the experiment flows:

1. **Welcome + Instructions**
2. **Participant Code Input**
3. **Trials Begin** 
4. **Results + Analysis**
5. **Debriefing**

## Key Functions  

### `show_instructions(screen)`  
Instruction screen: task details & control instructions

### `get_participant_code(screen)`  
enter ID for data tie with session.

### `generate_objects(num_objects, target_char)`  
Randomly places distractors and one colored target on the screen. Returns their coordinates and labels.

### `run_trial(target_char, num_objects)`  
Runs a single trial: displays objects, tracks the user’s click, and measures how long they take. Also records whether they clicked the correct object.

### `run_experiment(screen, participant_code)`  
Runs a full experiment session (usually around 15–20 trials), collects data, and returns it.

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

---

## References  

This experiment was inspired by:  
Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).  
*Methods for online testing of visual attention*. *Journal of Visualized Experiments: JoVE*, (96), 52470.  
[https://doi.org/10.3791/52470](https://doi.org/10.3791/52470)

---
