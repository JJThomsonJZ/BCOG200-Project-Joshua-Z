## BCOG200-Final Project: Visual Attention Experiment

### by Joshua Zhao

## Description

This is a **visual attention test** which tests the response speed in the selection of a target object among distractors. The **reaction time** and **accuracy** are recorded to examine selective attention. The program is written in Python with `pygame` to create an interactive graphical user interface in which users mark a specific target (for example, a red "O" among random black letters). The outcome can be displayed with `matplotlib`.

## Functions

### **generate_objects(num_objects, target_char)**

* Produces a list of randomly dispersed letters with one letter in a different color as the target letter.

- Returns the object positions including the object being targeted.

### run_experiment()

- Opens the pygame window, draws the objects, and tracks the user choice.
- Traces response time and stores whether the user accurately identified the target.

### analyze_results()

- Uses `matplotlib` to plot a histogram of the reaction times.
- Computes average response time and reports noteworthy results.
