import random as rand
class game:
    def play_game():
        score=0
        for i in range(3):
            numbers=[rand.randint(1,24) for i in range(3)]
            print(numbers)
            user_number=int(input("введите ваше число: "))
            if user_number in numbers:
                score+=1
            if score==1:
                print("Вы получили балл")
            elif score>=2:
                print("Вы выиграли ")
            else:
                print("Вы проиграли")
game.play_game()