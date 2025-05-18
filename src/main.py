import pygame
import time
import random
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

def show_instructions(screen):
    font = pygame.font.SysFont(None, 36) # did a small study on pygame through https://www.pygame.org/docs/ref/font.html
    screen.fill((255, 255, 255)) # white

    lines = [
        "Welcome to the Visual Attention Experiment!",
        "Task: Find and click the red 'O' as fast as you can.",
        "Press SPACEBAR when you're ready."
    ]

    screen_width, screen_height = screen.get_size()
    y = (screen_height - len(lines) * 50) // 2  # center lines

    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))  # black
        rect = text.get_rect(center=(screen_width // 2, y + i * 50))
        screen.blit(text, rect)

    pygame.display.flip()
    # for this part I did a quick search: How do I wait for a pressed key?
    # stackoverflow save me again: https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


def get_participant_code(screen):
    font = pygame.font.SysFont(None, 36)
    input_text = ""
    active = True

    while active:
        screen.fill((255, 255, 255))
        prompt = font.render("Enter Participant ID and press ENTER:", True, (0, 0, 0))
        prompt_rect = prompt.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))
        screen.blit(prompt, prompt_rect)

        input_render = font.render(input_text, True, (0, 0, 255))
        input_rect = input_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 10))
        screen.blit(input_render, input_rect)

        # for the next part that all related to display, I use https://www.pygame.org/docs/ref/display.html to did a "crashcourse"
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # actually I try to ues tkinter at first but seems like tkinter and pygame tend to conflict on macOS for some reason
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text != "":
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    return input_text.strip()

def show_debrief(screen):
    font = pygame.font.SysFont(None, 36)
    screen.fill((255, 255, 255))

    lines = [
        "Thanks for participating!",
        "This experiment performs a visual selective attention task in Python.",
        "It collects the time taken and accuracy of subjects in being able to identify uniquely colored targets from distractors.",
        "The task is to replicate standard paradigms of cognitive psychology and",
        " record behavioral responses in reaction time and accuracy.",
        "Now RA can press ENTER to finish and view results."
    ]

    screen_width, screen_height = screen.get_size()
    y = (screen_height - len(lines) * 50) // 2

    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))
        rect = text.get_rect(center=(screen_width // 2, y + i * 50))
        screen.blit(text, rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

def generate_objects(num_objects, target_char, screen):
    width, height = screen.get_size()
    margin = 50
    positions = []
    labels = []

    for _ in range(num_objects):
        x = random.randint(margin, width - margin)
        y = random.randint(margin, height - margin)
        # at first I didn't do 'if chr(c) != target_char' which there are always several 'O' on the screen 
        # so for this specific bug I asked chatGPT 4o to help me out and 'if chr(c) != target_char' is the result
        label = random.choice([chr(c) for c in range(65, 91) if chr(c) != target_char])
        positions.append((x, y))
        labels.append(label)

    target_index = random.randint(0, num_objects - 1)
    positions[target_index] = (random.randint(margin, width - margin), random.randint(margin, height - margin))
    labels[target_index] = target_char

    return positions, labels, target_index

def run_trial(screen, target_char="O", num_objects=20):
    font = pygame.font.SysFont(None, 48)
    screen.fill((255, 255, 255))

    positions, labels, target_index = generate_objects(num_objects, target_char, screen)

    for i, (x, y) in enumerate(positions):
        color = (255, 0, 0) if labels[i] == target_char else (0, 0, 0)
        letter = font.render(labels[i], True, color)
        screen.blit(letter, (x, y))

    pygame.display.flip()

    start_time = time.time()
    clicked_pos = None
    correct = False

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                waiting = False

    rt = time.time() - start_time
    tx, ty = positions[target_index]
    cx, cy = clicked_pos

    if abs(cx - tx) < 30 and abs(cy - ty) < 30:
        correct = True

    return {
        "target_position": (tx, ty),
        "click_position": (cx, cy),
        "correct": correct,
        "reaction_time": rt,
        "timestamp": datetime.now().isoformat()
    }

def run_experiment(screen, participant_code, num_trials=20):
    results = []
    for i in range(num_trials):
        result = run_trial(screen)
        result["participant_code"] = participant_code
        result["trial_num"] = i + 1
        results.append(result)
    return results

def save_results_to_db(results, participant_code):
    if not os.path.exists("data"):
        os.makedirs("data")
    filename = f"data/{participant_code}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["participant_code", "trial_num", "target_position", "click_position", "correct", "reaction_time", "timestamp"])
        for r in results:
            writer.writerow([
                r["participant_code"],
                r["trial_num"],
                r["target_position"],
                r["click_position"],
                r["correct"],
                r["reaction_time"],
                r["timestamp"]
            ])

def analyze_results(results):
    rts = [r["reaction_time"] for r in results]
    accuracy = sum(1 for r in results if r["correct"]) / len(results)
    plt.hist(rts, bins=10, color="skyblue", edgecolor="black")
    plt.title("Reaction Time Distribution")
    plt.xlabel("Time (s)")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()
    print("Average RT:", round(sum(rts)/len(rts), 2), "s")
    print("Accuracy:", round(accuracy * 100, 1), "%")

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Visual Attention Experiment")

    participant_code = get_participant_code(screen)
    show_instructions(screen)
    results = run_experiment(screen, participant_code)
    save_results_to_db(results, participant_code)
    show_debrief(screen)
    analyze_results(results)
    pygame.quit()

if __name__ == "__main__":
    main()
