def user_score():
    score = int(input("Please enter a score: "))
    return(score)


def main():
    final_Score = user_score()
    print(final_Score)


main()