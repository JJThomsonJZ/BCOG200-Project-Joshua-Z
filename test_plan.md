# Test Plan

## Code Testing Explanation

Because this project uses `pygame` and graphical user interactions (like mouse clicks), standard unit testing using `pytest` is not practical. Instead, I provide **three manual ways** to confirm the program works as expected.

### 1. Instruction and Input Screen Loads Properly

* When the program starts, it should first show a full-screen welcome screen with instructions.
* After pressing SPACE, it should ask the RA to type in a Participant ID.
* If these screens appear and can be interacted with (ID typed in, ENTER works), that confirms:

  * `show_instructions()` function works
  * `get_participant_code()` function works

### 2. Trials Display Correctly and React to Clicks

* During the experiment phase, 20 trials should run one by one.
* Each trial should show exactly **one red 'O'** among **other black letters**.
* Clicking the red "O" or anywhere else should advance the screen.
* This confirms:

  * `generate_objects()` generates letters correctly
  * `run_trial()` responds to mouse clicks and records correct data

### 3. Data is Saved and Analysis is Displayed

* After all trials and the debriefing screen, if the RA presses ENTER:

  * A histogram of reaction times should appear (using `matplotlib`)
  * A `.csv` file should appear in the `data/` folder named after the participant
* This confirms:

  * `save_results_to_db()` works correctly
  * `analyze_results()` runs and displays results
