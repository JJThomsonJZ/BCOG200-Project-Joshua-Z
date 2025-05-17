# Visual Attention Experiment

**Course:** BCOG 200
**Author:** Joshua Zhao
**Repository:** \[https://github.com/JJThomsonJZ/BCOG200-Project-Joshua-Z/tree/main]

## Overview

This experiment performs a visual selective attention task in Python. It collects the time taken and accuracy of subjects in being able to identify uniquely colored targets from distractors. The task is to replicate standard paradigms of cognitive psychology and record behavioral responses in reaction time and accuracy.

This project is written in Python and mainly uses:

* `pygame` for graphical stimulus presentation and user interaction
* `matplotlib` for data visualization and summary analysis

## How It Works

1. **Welcome Screen & Instructions** – Introduction to the task
2. **Participant Code Input** – Anonymous code entry to identify data
3. **Attention Trials** – Multiple trials with randomized target placement
4. **Results Summary** – Visualization of reaction times and summary stats
5. **Debriefing Screen** – Thank-you message and closing

## Code Structure

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

A cognitive science major who has an interest in attention processes can conduct this experiment with other classmates. Participants input an ID, do visual search trials, and get instant feedback in the form of graphs. One can then compare and analyze their respective outcomes to learn about visual processing dynamics.

## Data Storage

to store results, the table `attention_results` include:

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

>data is saved to `.csv` at data folder.

## Tools and Libraries Used

* Python 3.13
* Pygame
* Matplotlib
* Pandas
  
## Project Highlights

* Modular structure with well-defined functions
* Mouse click real-time stimulus interaction
* Immediate post-trial feedback
* Data visualization and accuracy tracking
* Extensibility for future additions (such as scaling difficulty, similarity of distractors)

## References

Yung, A., Cardoso-Leite, P., Dale, G., Bavelier, D., & Green, C. S. (2015).
*Methods for online testing of visual attention.* Journal of Visualized Experiments: JoVE, (96), 52470.
[https://doi.org/10.3791/52470](https://doi.org/10.3791/52470)
