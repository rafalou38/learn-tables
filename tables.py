import random
import colorama
import msvcrt
import pickle
import os


if os.path.exists("sv.pkl"):
    with open("sv.pkl", "rb") as f:    
        nums = pickle.load(f)
else:
    nums = [2, 3, 4, 5, 6, 7, 8, 9]

queue = []

print("\033[2J", end="")
print("\033[0;0H", end="")

cursor = 0
while True:
    nmax = os.get_terminal_size().lines - 1
    for i in range(nmax):
        if(i == cursor):
            print("\033[1;36m", end="")

        print(f"[{'X' if i in nums else ' '}] " + str(i), end="\033[0m\n")
    print("\033[0;0H", end="")

    key = msvcrt.getch()

    if key == b'\xe0':  # Special keys (arrows, function keys, etc.)
        key = msvcrt.getch()
        if key == b'H':
            cursor = (cursor - 1) % nmax
        elif key == b'P':
            cursor = (cursor + 1) % nmax
    else:
        if key == b'\r':  # Enter key
            break
        elif key == b' ':
            if cursor in nums:
                nums.remove(cursor)
            else:
                nums.append(cursor)

with open("sv.pkl", "wb") as f:
    pickle.dump(nums, f)

while True:
    print("\033[2J", end="")
    for i in range(10):
        queue.append(
            (
                nums[random.randint(0, len(nums) - 1)],
                nums[random.randint(0, len(nums) - 1)],
            )
        )
    i = 0
    while len(queue) > 0:
        
        q = queue.pop(0)
        txt = f"[{str(len(queue) + 1).rjust(2)}] {q[0]} x {q[1]} = "

        print(
            "\033[0m" + txt,
            end="\033[1;36m",
        )
        try:
            r = input()
        except KeyboardInterrupt:
            print("\n\033[0mBye!")
            exit()
        

        print(f"\033[{len(txt)+len(r)}C\033[1A", end="")

        if r.strip() == "" or int(r) != q[0] * q[1]:
            print(f"\033[{len(r)}D" + colorama.Fore.RED + str(q[0] * q[1]))

            queue.append(q)
            queue.append(q)

            random.shuffle(queue)
        else:
            print(f"\033[{len(r)}D" + colorama.Fore.GREEN + r)
        i+=1
