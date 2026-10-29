import random
import time

creepyMessages = [
    "It can see you.",
    "Do you hear the screams?",
    "I don't know what that is.",
    "The radio screams an inhuman tune.",
    "It's already gotten to our minds."
]

for attempt in range(1, 11):
    print(f"Attempt {attempt}/10:")
    index = random.randint(0, 5)
    
    try:
        print(f"  {creepyMessages[index]}")
    except IndexError:
        print("  ERROR: Something is trying to communicate.")
    finally:
        print("  The computer sees and hears your every move.")
    
    time.sleep(1)
    print()