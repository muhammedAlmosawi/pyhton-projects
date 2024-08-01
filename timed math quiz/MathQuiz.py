import ProblemsRNG
from inputimeout import inputimeout
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
games_played = 0
player_score = 0
timer_run_out_counter = 0
if __name__ == "__main__":
    print("make sure after the expression appears that you answer in less than 10 seconds or the timer will run out!!!!!")
    time.sleep(2)       #always remember that sleep() is measured in seconds
    while True:
        stop_condition = input("if you want to stop type (Q) if not then type any other letter: ").lower()
        if stop_condition == "q":
            break

        games_played += 1


        the_expression, correct_answer = ProblemsRNG.random_generator()
        print(f"your question is {the_expression}")
        
        try:
            input_start = time.time()
            user_answer = int(inputimeout(prompt="enter the correct answer: ", timeout=10))       
                    #here the timeout is measured in seconds
            input_end = time.time()
        except:
            print("you are waaaaaaaaaaaaaaaaaaaay too slow")
            timer_run_out_counter += 1
            continue

        if user_answer == correct_answer:
                time_elapsed = int(input_end - input_start)
                print(f"congrats you entered the correct answer in {time_elapsed} seconds")
                player_score += 1
        else:
            print("you answered in time but you are a failure")
            player_score -= 1

        
    print(f"you played {games_played} time(s)")
    print(f"your final score is {player_score}")
    print(f"the timer has ran out {timer_run_out_counter} time(s)")