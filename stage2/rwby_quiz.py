from os import system
import platform
import textwrap

def start_game():
    blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

    paragraphs = [
                    "Team RWBY is led by ___1___ Rose, the other members " + \
                    "being Weiss Schnee, Blake Belladonna, and Yang Xiao " + \
                    "Long. ___2___ and Ruby are sisters. They attend " + \
                    "___3___ Academy, with the headmaster being Professor " + \
                    "___4___.",

                    "Ruby's semblance is ___1___, leaving a trail of rose " + \
                    "petals behind her. Blake creates ___2___ of herself " + \
                    "that can take on different properties, like ice or " + \
                    "fire. Pyrrha Nikos' semblance is ___3___, which Ruby " + \
                    "mistakenly thought was the ability to control ___4___. ",

                    "Ruby's weapon is named ___1___ Rose and is a giant " + \
                    "scythe as well as a sniper rifle. ___2___ is Weiss's " + \
                    "weapon and resembles a fencing sword. Blake wields " + \
                    "___3___ ___4___, which is a dual sword and gun " + \
                    "combination, with a ribbon that allows it to be swung " + \
                    "around. The gun-firing gauntlets that Yang has are " + \
                    "called ___5___ ___6___."

                ]
    answers = [
                ["Ruby", "Yang", "Beacon", "Ozpin"],

                ["speed", "shadows", "polarity", "poles"],

                ["Crescent", "Myrtenaster", "Gambol", "Shroud", "Ember", \
                 "Celica"]
              ]

    print_title()
    difficulty_level = getDifficulty() - 1

    level_paragraph = paragraphs[difficulty_level]
    level_answers = answers[difficulty_level]
    play_round(level_paragraph, level_answers, blanks)



def clear_screen():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

# Major help from GlassGiant.com
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

def getDifficulty():
    user_input = raw_input("Select your difficulty. [1 = Easy, 2 = Medium, 3 " +
                           "= Hard]: ")

    while user_input != "1" and user_input != "2" and user_input != "3":
        print "" # blank line
        user_input = raw_input("Try again: ")

    return int(user_input)

def play_round(paragraph, answers, blanks):
    index = 0

    for answer in answers:
        print_paragraph(paragraph)
        get_answer(answer, index)

        blank = blanks[index]
        paragraph = paragraph.replace(blank, answer)
        index += 1

    print_paragraph(paragraph)
    print "" # blank line
    print "You got it!"

def print_paragraph(paragraph):
    width = 60

    clear_screen()
    print textwrap.fill(paragraph, width=width)

def get_answer(answer, index):
    blank_number = str(index + 1)
    print "" # blank line
    user_input = raw_input("For blank #" + blank_number + ": ")

    while user_input != answer:
        print "" # blank line
        user_input = raw_input("Try again: ")


start_game()