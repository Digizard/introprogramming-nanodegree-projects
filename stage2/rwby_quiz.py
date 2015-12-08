##
# rwby_quiz.py
# This is a fill-in-the-blank quiz game with the items based on the RWBY series.

# Import needed modules
from os import system
import platform
import textwrap

# Setup necessary data for quiz
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

levels = [
			# Easy
			{
				"paragraph": "Team RWBY is led by ___1___ Rose, the other " + \
							 "members being Weiss Schnee, Blake Belladonna," + \
							 " and Yang Xiao Long. ___2___ and Ruby are " + \
							 "sisters. They attend ___3___ Academy, with " + \
							 "the headmaster being Professor ___4___.",
				"answers":	["Ruby", "Yang", "Beacon", "Ozpin"]
			},

			# Medium
			{
				"paragraph": "Ruby's semblance is ___1___, leaving a trail " + \
							 "of rose petals behind her. Blake creates " + \
							 "___2___ of herself that can take on different" + \
							 " properties, like ice or fire. Pyrrha Nikos' " + \
							 "semblance is ___3___, which Ruby mistakenly " + \
							 "thought was the ability to control ___4___. ",
				"answers":  ["speed", "shadows", "polarity", "poles"]
			},

			# Hard
			{
				"paragraph": "Ruby's weapon is named ___1___ Rose and is a " + \
							 "giant scythe as well as a sniper rifle. " + \
							 "___2___ is Weiss's weapon and resembles a " + \
							 "fencing sword. Blake wields ___3___ ___4___, " + \
							 "which is a dual sword and gun combination, " + \
							 "with a ribbon that allows it to be swung " + \
							 "around. The gun-firing gauntlets that Yang " + \
							 "has are called ___5___ ___6___.",
				"answers": ["Crescent", "Myrtenaster", "Gambol", "Shroud",
							"Ember", "Celica"]
			}
		 ]


##
# Sets up paragraphs to be filled in, as well as the answers. Then the game gets
# going.
def start_game():

    # Starting screen
    print_title()
    difficulty_level = getDifficulty() - 1

    # Let the quiz begin!
    level_paragraph = levels[difficulty_level]["paragraph"]
    level_answers = levels[difficulty_level]["answers"]
    play_level(level_paragraph, level_answers, blanks)


##
# Clear the window of all text.
def clear_screen():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

##
# Outputs the "title screen" to the window. Much thanks to GlassGiant.com.
def print_title():
    clear_screen()
    print """
      ,:=,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM?~,
     ,:=ZM,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+~,
     :=$MMM,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+:,
    ,~?MMMMM,?MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM$=,
    :=NMMMMMM, =MMMMMMMMM   IM MMMMM DD``?MM MM MMMMM?~,
   ,~+MMMMMMMM     OMMMMM MM MM M`NM MM -IMMMN MMMMMMZ=,
   ,~7MMMMMMMM      MMMMM  MMMM $ D IMM _`MMM MMMMMMMM=:
   :=8MMMMMMMD      MMMMM MD MMN MM MMM  .NM MMMMMMMMM+:,
   :=MMMMMMMMMM      7MMM MMMMMMMMMMMMMMMMMMMMMMMMMMMM+~,
   :=MMMMMMMMMMN     :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+:,
   :=8MMMMMMMMMM   +D  ZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+:,
   ,~7MMMMMMMM     MMM ,MM?ZMMMMMMMMMMMMMMMMMMMMMMMMMM=:
   ,~+MMMMM=       :MMM  MMMM+    ~+IDMMMMMMMMMMMMMMM$=,
    :=NMM:          MMMM  ZMMMMM         ~===IDMMMMMM?~,
    ,~?MMMD          MMMMN,MMMMMMM  ,
     ,=7MMMM~        ,MMMMM,MMMMMM   8=
      :=ZMMMM  M  $MMMMMMMMM, MMD     MM8
      ,:=OMMM  M  MMMMMMMMM,  ~M,   M:MMMMM7=
       ,:=7MM  M  MMMMMM:    =~  ::MMMMMMMMMMM?
         :~?M  M? :MMMM+    ~    ,MMMMMMMMMMMMM7
          ,:=  MM  MM          , MMMMMMMMMMMMO+
    """

##
# Asks user to choose difficulty level and returns selection.
# @return int - Number 1, 2, or 3 depending on user choice.
def getDifficulty():
    user_input = raw_input("Select your difficulty. [1 = Easy, 2 = Medium, 3 " +
                           "= Hard]: ")

    # If the user didn't make a valid choice, have them try again
    while user_input not in ["1", "2", "3"]:
        print "" # blank line
        user_input = raw_input("Try again: ")

    return int(user_input)

##
# Runs the quiz with the given level data
# @param paragraph - String containing blanks to be filled for quiz.
# @param answers   - List of strings containing the solution for each blank.
# @param blanks    - List of all numbered blanks that could exist in paragraph.
def play_level(paragraph, answers, blanks):
    # Try to get user to fill in each blank.
    for answer in answers:
    	index = answers.index(answer)
        print_paragraph(paragraph)
        get_answer(answer, index)

        blank = blanks[index]
        paragraph = paragraph.replace(blank, answer)

    # When user wins
    print_paragraph(paragraph)
    print "" # blank line
    print "You got it!"

##
# Output the quiz text so that it wraps at a certain width on a clean screen.
# @param paragraph - String of text to be output.
def print_paragraph(paragraph):
    width = 60

    clear_screen()
    print textwrap.fill(paragraph, width=width)

##
# Ask user for answer, repeating request if user is incorrect.
# @param answer - String of answer user needs to input.
# @param index  - The index number of the answer in its list.
def get_answer(answer, index):
    blank_number = str(index + 1)
    print "" # blank line
    user_input = raw_input("What should go in blank #" + blank_number + "?: ")

    # If user guesses wrong, have them try again.
    while user_input != answer:
        print "" # blank line
        user_input = raw_input("Try again: ")


# Run the game
start_game()