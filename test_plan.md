# Test Plan

## Code Testing Explanation

Because the uses of `pygame` and mouse clicks this kind of visual interaction, using `pytest` is not practical. So I provide **three manual ways** to confirm the program works as expected.

### 1. Instruction and Input Screen Loads Properly

* When starts, it should first show a full-screen and ask the RA to type in a Participant ID.
* After ID imput and pressing ENTER, it should have a welcome screen with instructions
* If these above works well it means that:

  * `show_instructions()` works
  * `get_participant_code()` works

### 2. Trials Correctly and React to Clicks

* During the experiment after you press SPACE at the welcome page, trials should run one by one(total 20).
* Each trial should show only one red 'O' among other black letters.
* Clicking anywhere can advance the screen.
* If these above works well it means that:

  * `generate_objects()` works
  * `run_trial()` works

### 3. Data Saved and Analysis Displayed

* After all trials there should be a debriefing screen, if the RA presses ENTER:

  * A histogram of reaction times should appear (using `matplotlib`)
  * A `.csv` file should appear in the `data/` folder named after the participant
* If these above works well it means that:

  * `save_results_to_db()` works
  * `analyze_results()` works
