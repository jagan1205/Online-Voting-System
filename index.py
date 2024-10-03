candidates = {
    1: "Candidate A",
    2: "Candidate B",
    3: "Candidate C"
}

votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

def display_candidates():
    print("Candidates:")
    for num, name in candidates.items():
        print(f"{num}. {name}")

def cast_vote():
    try:
        choice = int(input("Enter the number of the candidate you want to vote for: "))
        if choice in candidates:
            selected_candidate = candidates[choice]
            votes[selected_candidate] += 1
            print(f"Your vote for {selected_candidate} has been recorded.")
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number.")

def display_results():
    print("\nVoting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

def main():
    while True:
        display_candidates()
        cast_vote()
        more_votes = input("Are there more votes? (yes/no): ").lower()
        if more_votes != 'yes':
            break
    display_results()


main()
