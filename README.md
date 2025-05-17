# Visual Attention Experiment

**Course:** BCOG 200 – Brain and Cognitive Science
**Author:** Joshua Zhao
**Repository:** \[https://github.com/JJThomsonJZ/BCOG200-Project-Joshua-Z]

## Overview

This project implements a visual selective attention experiment in Python. The experiment tests how quickly and accurately participants can identify a uniquely colored target among a field of distractors. The goal is to simulate classic paradigms in cognitive psychology and collect behavioral data on reaction time and accuracy.

This project is written in Python and uses:

* `pygame` for graphical stimulus presentation and user interaction
* `matplotlib` for data visualization and summary analysis

## How It Works

The program walks participants through a series of trials in which they must find and click on a target object as quickly and accurately as possible. The experiment includes:

1. **Welcome Screen & Instructions** – Introduction to the task
2. **Participant Code Input** – Anonymous code entry to identify data
3. **Attention Trials** – Multiple trials with randomized target placement
4. **Results Summary** – Visualization of reaction times and summary stats
5. **Debriefing Screen** – Thank-you message and closing

## Code Structure

The experiment is organized with modular functions to ensure clarity and reuse:

| Function                                     | Description                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------- |
| `show_instructions(screen)`                  | Displays task instructions using Pygame                                          |
| `get_participant_code(screen)`               | Prompts user for a participant ID                                                |
| `generate_objects(num_objects, target_char)` | Generates coordinates and symbols for the target and distractors                 |
| `run_trial(target_char, num_objects)`        | Executes a single visual trial and records click accuracy and timing             |
| `run_experiment(screen, participant_code)`   | Loops through all trials and compiles performance data                           |
| `analyze_results(results)`                   | Uses matplotlib to display reaction time histograms and compute average accuracy |
| `show_debrief(screen)`                       | Displays end-of-experiment message                                               |

## Sample Use Case

A cognitive science student interested in attentional mechanisms can run this experiment with classmates. Each participant enters an ID, completes visual search trials, and receives immediate feedback via graphs. Their results can then be compared and interpreted to understand visual processing dynamics.

## Data Storage (Optional)

If using a database to store results, the table `attention_results` may include:

| Column Name       | Type      | Description                                    |
| ----------------- | --------- | ---------------------------------------------- |
| id                | SERIAL    | Auto-incremented ID                            |
| participant\_code | VARCHAR   | User-entered participant ID                    |
| trial\_num        | INT       | Trial number                                   |
| target\_position  | TEXT      | Coordinates of the target                      |
| click\_position   | TEXT      | Where the user clicked                         |
| correct           | BOOLEAN   | Whether the user clicked on the correct object |
| reaction\_time    | FLOAT     | Time taken in seconds                          |
| timestamp         | TIMESTAMP | When the trial occurred                        |

> In the version submitted here, data is stored in memory and optionally saved to `.csv`.

## Tools and Libraries Used

* Python 3.x
* Pygame
* Matplotlib
* (Optional: SQLite3 or Pandas for saving/analyzing data)

## Project Highlights

The project emphasizes:

* Modular design with clearly defined functions
* Real-time stimulus interaction via mouse clicks
* Immediate post-trial feedback
* Data visualization and accuracy tracking
* Extensible design for future additions (e.g., difficulty scaling, distractor similarity)

## References

Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).
*Methods for online testing of visual attention.* Journal of Visualized Experiments: JoVE, (96), 52470.
[https://doi.org/10.3791/52470](https://doi.org/10.3791/52470)
