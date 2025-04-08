# Test Plan – Visual Attention Experiment

## Purpose

This file describes a complete test scenario for verifying the functionality of the Visual Attention Experiment program. The test covers the full user experience — from starting the program to completing trials and viewing results. It ensures that the experiment logic, timing, interaction, and data handling are all functioning as intended.

---

## Test Scenario: Full Experiment Run

### 1. Environment Setup

Before running the program, make sure the following packages are installed:

```bash
pip install pygame matplotlib psycopg2-binary
Make sure you also have a PostgreSQL database running with a table created using:

sql
复制
编辑
CREATE TABLE attention_results (
    id SERIAL PRIMARY KEY,
    participant_code VARCHAR(20),
    trial_num INT,
    target_position TEXT,
    click_position TEXT,
    correct BOOLEAN,
    reaction_time FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
You will need to edit the save_results_to_db() function to include your actual database credentials.

2. Running the Program
Run the Python script from the terminal:

bash
复制
编辑
python main.py
3. Expected User Flow
Instruction Screen
A Pygame window opens with instructions describing the task (e.g., “Click the red target letter…”).
User clicks anywhere to proceed.

Participant Code Entry
User is prompted to enter their participant code (e.g., "P001") using keyboard input.

Trial Execution

10 trials are shown, each with letters randomly placed.

One letter is red (the target).

User must click the red letter as fast as possible.

After each trial, the next begins automatically.

Post-Experiment Analysis

A matplotlib window displays a histogram of reaction times.

The terminal prints:

Average reaction time

Accuracy (percentage of trials where target was correctly clicked)

Data Storage

The results are stored in the PostgreSQL table attention_results.

You can manually verify this using SQL or a tool like pgAdmin.

Debrief Message

A final screen says “Thank you for participating.”

Sample Data
No input file is needed. All stimuli are generated randomly in the program.
If database storage is enabled, each row inserted will contain data like:

participant_code	trial_num	target_position	click_position	correct	reaction_time
P001	3	(115, 206)	(110, 200)	true	1.28
Evaluation Criteria
The program is considered to be functioning correctly if:

All screens render without error.

Trials can be completed with mouse clicks.

Reaction time is visibly different across trials.

Results plot is shown with valid histogram.

Average and accuracy statistics are printed.

Data is saved in the PostgreSQL database without error.
