import pygame
import time
import random
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

# ----------------------------
# Instruction-related Functions
# ----------------------------

def show_instructions(screen):
    font = pygame.font.SysFont(None, 36)
    screen.fill((255, 255, 255))
    lines = [
        "欢迎参加视觉注意力实验！",
        "任务说明：请在多个字母中尽快点击红色的 'O' 字母。",
        "按任意键开始。"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (100, 100 + i * 40))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False


def get_participant_code(screen):
    return str(random.randint(1000, 9999))  # 可拓展为更复杂的 ID 系统


def show_debrief(screen):
    font = pygame.font.SysFont(None, 36)
    screen.fill((255, 255, 255))
    text = font.render("谢谢参与！实验结束。", True, (0, 0, 0))
    screen.blit(text, (250, 250))
    pygame.display.flip()
    time.sleep(3)

# ----------------------------
# Stimulus & Trial Generation
# ----------------------------

def generate_objects(num_objects, target_char):
    positions = []
    labels = []
    for _ in range(num_objects):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        positions.append((x, y))
        labels.append(chr(random.randint(65, 90)))  # A-Z distractors
    target_index = random.randint(0, num_objects - 1)
    positions[target_index] = (random.randint(50, 750), random.randint(50, 550))
    labels[target_index] = target_char
    return positions, labels, target_index


def run_trial(screen, target_char="O", num_objects=10):
    font = pygame.font.SysFont(None, 48)
    screen.fill((255, 255, 255))
    positions, labels, target_index = generate_objects(num_objects, target_char)
    for i, (x, y) in enumerate(positions):
        color = (255, 0, 0) if labels[i] == target_char else (0, 0, 0)
        text = font.render(labels[i], True, color)
        screen.blit(text, (x, y))
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


def run_experiment(screen, participant_code, num_trials=10):
    results = []
    for i in range(num_trials):
        trial_result = run_trial(screen)
        trial_result["participant_code"] = participant_code
        trial_result["trial_num"] = i + 1
        results.append(trial_result)
    return results

# ----------------------------
# Data Analysis
# ----------------------------

def analyze_results(results):
    rts = [r["reaction_time"] for r in results]
    accuracy = sum(1 for r in results if r["correct"]) / len(results)
    plt.hist(rts, bins=10, color='skyblue', edgecolor='black')
    plt.title("Reaction Time Distribution")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
    print(f"Average RT: {sum(rts)/len(rts):.2f}s, Accuracy: {accuracy*100:.1f}%")


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

# ----------------------------
# Main Program Entry Point
# ----------------------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Visual Attention Experiment")

    show_instructions(screen)
    participant_code = get_participant_code(screen)
    results = run_experiment(screen, participant_code)
    save_results_to_db(results, participant_code)
    analyze_results(results)
    show_debrief(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
