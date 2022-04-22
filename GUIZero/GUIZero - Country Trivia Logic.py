from guizero import App, Text, Box, PushButton, TextBox
from textwrap import wrap


f = open('countries2.txt')
countries = [_.lower() for _ in f.read().split('\n')]
f.close()

answers = [
    ['India', 'Sri Lanka', 'China', 'United Arab Emirates', 'Kyrgyzstan', 'Oman'],
    ['Morocco', 'Madagascar', 'Nigeria', 'Djibouti', 'Chad', 'Togo'],
    ['Spain', 'Iceland', 'Russia', 'United Kingdom', 'Estonia', 'France'],
    ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Peru', 'Suriname'],
    ['Mexico', 'Cuba', 'United States', 'Canada', 'Guatemala', 'Panama']
]

hints = {
    'A1': 'Each country in column C is the most populated on its row and on its continent',
    'A2': 'Canada is adjacent to Brazil',
    'A3': 'All South American countries appear in alphabetical order',
    'A4': "An 'O' country can be found at either F1 or E3",
    'A5': '',
    'B1': '',
    'B2': 'Panama is in the same column as Togo',
    'B3': 'Every 4-letter country from the Americas is in this quiz',
    'B4': 'If Guatemala is in this quiz, then so is Madagascar',
    'B5': 'The only 1-syllable country starting with S is in this quiz, but not adjacent to Suriname',
    'C1': 'Suriname is in F4, Bahrain is not in this quiz',
    'C2': 'There are exacly two countries in this row that start with M',
    'C3': "Two 'United _____' countries are in column D",
    'C4': 'Find Morocco at A2 and Iceland at B3',
    'C5': 'Every country in column B (except for one) has zero land borders',
    'D1': "Three countries in row 5 have a capital that ends with 'City'",
    'D2': 'If Finland is in this quiz, then so is El Salvador',
    'D3': 'Every column has just 1 country that begins with the letter of its column',
    'D4': 'Mexico is in the same diagonal as Kyrgyzstan',
    'D5': 'There is only one island in this row',
    'E1': 'There are exactly two 2-word countries',
    'E2': '',
    'E3': 'There is a 3-syllable country in F5',
    'E4': 'Two of the three 4-letter African countries are in this quiz',
    'E5': '',
    'F1': 'No country with more than 4 words in its name is in this quiz',
    'F2': '',
    'F3': "The world's most southern-reaching country is in D4",
    'F4': 'Every row represents a unique continent, and only contains countries from that continent',
    'F5': ''
}

def get_coordinates(x, y):
    return ['A', 'B', 'C', 'D', 'E', 'F'][y] + str(x + 1)

def check():
    answer.value = answer.value.replace(' ', '')
    if answer.value.lower() in countries and squares[activated[0]][activated[1]].bg == 'blue':
        if answer.value.lower() == answers[activated[0]][activated[1]].lower().replace(' ', ''):
            squares[activated[0]][activated[1]].bg = None
            answer.value = ''
        else:
            answer.value = ''
            square_text.value = 'You lose'
            answer.disable()

def activate(x, y):
    global activated
    if answer.enabled:
        activated = [x, y]
        square_text.value = get_coordinates(x, y)

def clear_board():
    new_board = [[None for a in range(6)] for b in range(5)]
    for p in range(6):
        Text(
            board,
            text=['A', 'B', 'C', 'D', 'E', 'F'][p],
            grid=[p + 1, 0]
        )
    for x in range(5):
        Text(
            board,
            text=str(x + 1),
            grid=[0, x + 1]
        )
        for y in range(6):
            button = PushButton(
                board,
                text=answers[x][y] + '\n' + '\n'.join(wrap(hints[get_coordinates(x, y)], 20)),
                command=activate,
                args=[x, y],
                grid=[y + 1, x + 1]
            )
            button.text_color = 'blue'
            button.bg = 'blue'
            new_board[x][y] = button
    return new_board
            
app = App('Country Trivia Logic')

board = Box(app, layout='grid')
squares = clear_board()
squares[0][0].bg = None

Text(app, '\n\n')

activated = [1, 0]
square_text = Text(app, 'A2', size=15)
answer = TextBox(app, command=check)

app.set_full_screen()
app.display()
