class GameMemory:

    def save_score(self, score):
        with open('score_history.txt', mode="w") as file:
            print(f"type of arg ", type(score))
            final_score = str(score)
            # if type(score) == 'string':
            print(f"type of final ", type(final_score))
            file.write(final_score)

    def read_score(self):
        with open('score_history.txt') as file:
            contents = int(file.read())
            print(f"Last recorded score {contents}")
            return contents
