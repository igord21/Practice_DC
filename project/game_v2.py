'''Guess the Number Game'''
''' The computer conceives and guesses the number itself.'''


import numpy as np
def random_predict(number: int=1) -> int:
    """Random number guessing
    Args:
        number (int, optional): The number to guess. Defaults to 1.
    Returns:
        int: Number of tries
    """
    count = 0
    lastdict_number = 101
    ferstdict_number = 1

    while True:
        count += 1
        predict_number = np.random.randint(
            ferstdict_number, lastdict_number)  # estimated number
        # half of the range where the guessed number falls
        half_number = int(
            (lastdict_number - ferstdict_number)/2) + ferstdict_number
        if number == predict_number:
            break  # exit the cycle if you guessed
        if number > half_number:
            ferstdict_number = half_number - 1
        else:
            lastdict_number = half_number + 1

    return count


def score_game(random_predirect) -> int:
    """For how many attempts, on average, in 1,000 approaches does our algorithm guess
    Args:
        random_predirect ([type]): guessing function
    Returns:
        int: average number of attempts
    """
    count_ls = []  # list to save the number of attempts
    # np.random.seed(1) # fixing the seat for reproducibility
    random_array = np.random.randint(
        1, 101, size=(1000))  # puzzled list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # find the average number of attempts

    print(
        f'Your algorithm guesses the number in an average of : {score} tries')
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
