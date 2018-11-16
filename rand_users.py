from random import choice, choices
import yaml


class GenerateRandom:

    def __init__(self):
        pass

    class GameofThrones:

        def __init__(self):
            self.data = None
            with open('data/game_of_thrones.yml', 'r') as file:
                self.data = yaml.load(file)['en']['faker']['game_of_thrones']

        def character(self):
            return choice(self.data['characters'])

        def characters(self, cant=-1):
            characters = self.data['characters']
            if cant > 0:
                if cant > len(characters):
                    return None
                return choices(characters, k=cant)
            return characters

    class LeagueofLegends:

        def __init__(self):
            self.data = None
            with open('data/league_of_legends.yml', 'r') as file:
                self.data = yaml.load(file)['en']['faker']['games']['league_of_legends']

        def champion(self):
            return choice(self.data['champion'])

        def champions(self, cant=-1):
            champions = self.data['champions']
            if cant > 0:
                if cant > len(champions):
                    return None
                return choices(champions, k=cant)
            return champions

    class Witcher:

        def __init__(self):
            self.data = None
            with open('data/witcher.yml', 'r') as file:
                self.data = yaml.load(file)['witcher']

        def character(self):
            return choice(self.data['characters'])

        def characters(self, cant=-1):
            characters = self.data['characters']
            if cant > 0:
                if cant > len(characters):
                    return None
                return choices(characters, k=cant)
            return characters
