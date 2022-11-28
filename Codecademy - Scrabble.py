# In this project, we are going to process some data playing with scrabble

# Here are the 2 lists of data
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combine 2 lists into a dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}

# Add one item, if there is blank then its point is 0
letter_to_points[" "] =0

# Define a function named score_word, give a parameter named word
# Use for loop to receive the total score of a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# create a variable and set it equal to score_word("BROWNIE"). Let's test!
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Create a dictionary include players and words
player_to_words = {
"player":["BLUE","TENNIS","EXIT"],
"wordNerd":["EARTH","EYES","MACHINE"],
"LexiCon":["ERASER","BELLY","HUSKY"],
"Prof Reader":["ZAP","COMA","PERIOD"]
}

# set a new player_to_points equal 0
player_to_points = {}

# create for loop and use .item() to get both keys and vlues
# set player and words as the key and values in the player_to_words dictionary
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  # take the keys from player_to_words and set it as keys for player_to_points
  player_to_points[player] = player_points 
print(player_to_points)