import random

def guessing_game():
    random_number = random.randint(1,100)

    while True:
        for guesses in range(7):
            print(f"남은 기회: ({1+6-guesses}) | ", end="")
            try:
                question = int(input(f"추측한 번호(1 ~ 100): "))
            except ValueError as e:
                print("{}는 숫자가 아닙니다".format(e))
                return

            try:
                if random_number < question:
                    print("\n[정답보다 큼]\n")
                elif random_number > question:
                    print("\n[정답보다 작음]\n")
                else:
                    print("\n[정답!]\n")
                    break
            except NameError as e:
                print("{}".format(e))
                break

        try:
            if random_number == question:
                print(f"이겼습니다! | 남은 횟수: ({6 - guesses})")
                break
            else:
                print(f"졌습니다! | 남은 횟수: ({6 - guesses}) | 정답: ({random})")
                break
        except NameError as e:
            print("{}".format(e))
            break


guessing_game()
