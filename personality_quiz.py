soccer_points = 0
track_points = 0
basketball_points = 0
# Start of quiz
answer1 = input ("Do you like team sports or solo sports? ")
if answer1 == "team sports" or answer1 == "Team sports" or answer1 == "team" or answer1 == "Team":
    soccer_points += 1
    basketball_points += 1
elif answer1 == "solo sports" or answer1 == "Solo sports" or answer1 == "solo" or answer1 == "Solo":
    track_points += 1
answer2 = input ("Do you like outdoor sports or indoor sports? ")
if answer2 == "outdoor" or answer2 == "Outdoor":
    soccer_points += 2
    track_points += 1
elif answer2 == "indoor" or answer2 == "Indoor":
    basketball_points += 1
answer3 = input ("Do you prefer sports where you use your hands or legs? ")
if answer3 == "hands" or answer3 == "Hands":
    basketball_points += 1
    track_points += .5
elif answer3 == "legs" or answer3 == "Legs":
    soccer_points += 1
    track_points += 1
answer4 = input ("What do you like watching more the World Cup, the Olympics, or the NBA? ")
if answer4 == "the world cup" or answer4 == "The World Cup" or answer4 == "world cup" or answer4 == "World Cup":
    soccer_points += 1
if answer4 == "Olympics" or answer4 == "olympics" or answer4 == "the olympics" or answer4 == "The Olympics":
    track_points += 1
    soccer_points += .5
if answer4 == "NBA" or answer4 == "nba":
    basketball_points += 1
answer5 = input ("Which sport do you like more soccer, track, or basketball? ")
if answer5 == "soccer" or answer5 == "Soccer":
    soccer_points += 2
if answer5 == "basketball" or answer5 == "Basketball":
    basketball_points += 2
if answer5 == "track" or answer5 == "Track":
    track_points += 2
if soccer_points > track_points and soccer_points > basketball_points:
    print ("You are a soccer player!")
elif track_points > soccer_points and track_points > basketball_points:
    print ("You are a track and field runner!")
elif basketball_points > soccer_points and basketball_points > soccer_points:
    print ("You are basketball player!")