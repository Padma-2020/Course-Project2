letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combine list letters & points to form dictionary
letters += [letter.lower() for letter in letters]
points *=2
print(letters)
print(points)
letters_to_points = {letter:point for letter, point in zip(letters, points)}
#print(letters_to_points)
letters_to_points[" "] = 0
print(letters_to_points)
def score_word(word):
  score = 0
  for letter in word:
    score += letters_to_points.get(letter)
  return score  
brownie_points = score_word('brownie')
print(brownie_points)
player_to_words = {'player1': ['BLUE','TENNIS', 'EXIT'], 'wordnerd' : ['earth', 'eyes', 'machine'], 'LexiCon': ['eraser', 'belly', 'husky'], 'ProfReader': ['zap','coma', 'period']}
player_to_points  = {}
for player, words in player_to_words.items():
  player_points =0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points  
print(player_to_points)
def play_word(player, word):
  player_to_words[player].append(word)
play_word('wordnerd', 'TRUE')
play_word('ProfReader', 'complete')
play_word('player1', 'win')
print(player_to_words)
#update_point_total 
def update_point_totals():
  for player, words in player_to_words.items():
    player_score = 0
    for word in words:
      player_score += score_word(word)
      player_to_points[player] = player_score
play_word('player1', 'square')
update_point_totals()
print(player_to_points)
