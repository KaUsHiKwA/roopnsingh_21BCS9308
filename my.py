import pygame
import matplotlib.pyplot as plt
import random
from pygame.locals import *


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr, j, j + 1
            else:
                yield arr, j, j
        if not swapped:
            break


def visualize_pygame(arr):
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bubble Sort Visualization")

    bar_width = width // len(arr)
    max_value = max(arr)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    speed_value = 50  # Initial speed (lower value = faster)
    slider_x = 10
    slider_y = height - 50
    slider_width = 150
    slider_height = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slider_x <= event.pos[0] <= slider_x + slider_width and \
                   slider_y <= event.pos[1] <= slider_y + slider_height:
                    speed_value = (event.pos[0] - slider_x) * 100 // slider_width

        screen.fill((0, 0, 0))
        delay = 100 - speed_value  # Map speed_value to delay

        for state, idx1, idx2 in bubble_sort(arr.copy(), delay):
            for i, val in enumerate(state):
                bar_height = (val / max_value) * height
                x = i * bar_width
                y = height - bar_height
                color = (255, 0, 0)
                if i == idx1 or i == idx2:
                    color = (0, 255, 0)
                if i >= len(arr) - i:
                    color = (0, 0, 255)
                pygame.draw.rect(screen, color, (x, y, bar_width - 1, bar_height))

        # Draw speed slider
        pygame.draw.rect(screen, (100, 100, 100), (slider_x, slider_y, slider_width, slider_height))
        pygame.draw.circle(screen, (255, 255, 255), (slider_x + speed_value * slider_width // 100, slider_y + slider_height // 2), 8)
        speed_text = font.render(f"Speed: {speed_value}", True, (255, 255, 255))
        screen.blit(speed_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def visualize_matplotlib(arr):
    plt.figure(figsize=(10, 5))
    plt.title("Bubble Sort Visualization")
    plt.xlabel("Element Index")
    plt.ylabel("Value")

    for state, idx1, idx2 in bubble_sort(arr.copy()):
        plt.cla()
        plt.bar(range(len(arr)), state, color='lightgray')
        plt.bar([idx1, idx2], [state[idx1], state[idx2]], color='green')
        for i in range(len(arr) - 1, len(arr) - len(state), -1):
            plt.bar(i, state[i], color='blue')
        plt.pause(0.1)

    plt.show()

def generate_random_data(size):
    return [random.randint(1, 100) for _ in range(size)]

# Choose either Pygame or Matplotlib
use_pygame = True

if use_pygame:
    data_size = 20
    data = generate_random_data(data_size)
    visualize_pygame(data)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    data = generate_random_data(data_size)
                    visualize_pygame(data)

else:
    while True:
        data_size = 20
        data = generate_random_data(data_size)
        visualize_matplotlib(data)

        input("Press Enter to generate new data...")