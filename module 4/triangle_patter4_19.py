# stair_step_patter4_20
# This program displays a stair-step pattern

def main():
    num_steps=6
    for r in range(num_steps):
        for c in range(r):
            print(' ',end='')
        print('#')
main()
