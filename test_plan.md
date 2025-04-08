# Test Plan

## Test Scenario: Full Experiment Run

### 1. Environment Setup

Before running the program, make sure the following packages are installed:

```bash
pip install pygame matplotlib psycopg2-binary
```

---

### 2. Running the Program

Run the Python script from the terminal:

```bash
python main.py
```

### 3. Expected User Flow

1. **Instruction Screen**  

2. **Participant Code Entry**  

3. **Trial Execution**  
   - 10 trials are shown, each with letters randomly placed.
   - One letter is red (the target).
   - User must click the red letter as fast as possible.
   - After each trial, the next begins automatically.

4. **Post-Experiment Analysis**  
   - A matplotlib window displays a histogram of reaction times.
   - The terminal prints:
     - Average reaction time
     - Accuracy (percentage of trials where target was correctly clicked)

5. **Data Storage**  

6. **Debrief Message**  
---

## Sample Data

| participant_code | trial_num | target_position | click_position | correct | reaction_time |
|------------------|-----------|------------------|-----------------|---------|----------------|
| P001             | 3         | (115, 206)       | (110, 200)       | true    | 1.28           |

---

## Evaluation Criteria

The program is considered to be functioning correctly if:

- All screens render without error.
- Trials can be completed with mouse clicks.
- Reaction time is visibly different across trials.
- Results plot is shown with valid histogram.
- Average and accuracy statistics are printed.

---
