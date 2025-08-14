class VotingSystem:
    def __init__(self):
        self.__candidates = {}

    def add_candidate(self, name):
        if name not in self.__candidates:
            self.__candidates[name] = 0
        else:
            print(f"{name} is already in the list.")

    def remove_candidate(self, name):
        if name in self.__candidates:
            del self.__candidates[name]
        else:
            print(f"{name} not found.")

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1
        else:
            print(f"{name} not found.")

    def display_the_winner(self):
        if not self.__candidates:
            print("No candidates available.")
            return

        winner = max(self.__candidates, key=self.__candidates.get)
        print(f"The winner is {winner} with {self.__candidates[winner]} votes.")

    def display_all(self):
        for name, votes in self.__candidates.items():
            print(f"{name}: {votes} votes")



vs = VotingSystem()
vs.add_candidate("Mohamed")
vs.add_candidate("Ali")
vs.vote_to_candidate("Mohamed")
vs.vote_to_candidate("Mohamed")
vs.vote_to_candidate("Ali")
vs.display_all()
vs.display_the_winner()