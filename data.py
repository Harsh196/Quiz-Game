# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to "
#              "eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament,"
#              " you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
question_data = {
    "Film": {
        "Questions": [
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "The movie &quot;The Nightmare before Christmas&quot; was all done with physical objects.",
                "correct_answer": "True", "incorrect_answers": ["False"]
            },
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039; The Aviator.",
                "correct_answer": "False", "incorrect_answers": ["True"]
            },
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "The film &quot;2001: A Space Odyssey&quot; was released on December 31st, 2000.",
                "correct_answer": "False", "incorrect_answers": ["True"]
            },
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies "
                            "Interstellar and The Martian.",
                "correct_answer": "True", "incorrect_answers": ["False"]
            },
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "In the original script of &quot;The Matrix&quot;, the machines used humans as additional "
                            "computing power instead of batteries.",
                "correct_answer": "True", "incorrect_answers": ["False"]},
            {
                "category": "Entertainment: Film",
                "type": "boolean",
                "difficulty": "easy",
                "question": "Ewan McGregor did not know the name of the second prequel film of Star Wars during and after "
                            "filming.",
                "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
             "question": "Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during "
                         "the filming of Star Wars.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
             "question": "In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate "
                         "the blood in the famous shower scene from ",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
             "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
             "question": "&quot;Minions&quot; was released on the June 10th, 2015.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
        ]
    },
    "Science": {
        "Questions": [
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "The Neanderthals were a direct ancestor of modern humans.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "The planet Mars has two moons orbiting it.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Steel is an alloy of Iron and Carbon.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Shrimp can swim backwards.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Type 1 diabetes is a result of the liver working improperly.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "Sound can travel through a vacuum.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
             "question": "&quot;Tachycardia&quot; or &quot;Tachyarrhythmia&quot; refers to a resting heart-rate "
                         "near or "
                         "over 100 BPM.",
             "correct_answer": "True", "incorrect_answers": ["False"]}
        ]
    },
    "Music": {
        "Questions": [
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "The music video to The Buggle&#039;s &quot;Video Killed the Radio Star&quot; was the first music video to broadcast on MTV.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "Eurobeat is primarily an Italian genre of music.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "The alternative rock band, They Might Be Giants, released their album &#039;Flood&#039; in 1990. ",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "The song &quot;Stronger Than You&quot; is a single by Estelle, who played Garnet in Steven Universe.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "Stevie Wonder&#039;s real name is Stevland Hardaway Morris.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "Scatman John&#039;s real name was John Paul Larkin.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "Michael Jackson wrote The Simpsons song &quot;Do the Bartman&quot;.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "In 1993, Prince changed his name to an unpronounceable symbol because he was unhappy with his contract with Warner Bros.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "The 2011 movie &quot;The Adventures of Tintin&quot; was directed by Steven Spielberg.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
             "question": "John Williams composed the music for &quot;Star Wars&quot;.", "correct_answer": "True",
             "incorrect_answers": ["False"]}
        ]
    },
    "General Knowledge": {
        "Questions": [
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Gumbo is a stew that originated in Louisiana.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
             "question": "Cucumbers are usually more than 90% water.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Bulls are attracted to the color red.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "The color orange is named after the fruit.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "You can legally drink alcohol while driving in Mississippi.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "hard",
             "question": "In Scandinavian languages, the letter &Aring; means river.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
             "question": "Albert Einstein had trouble with mathematics when he was in school.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
             "question": "Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
             "correct_answer": "False", "incorrect_answers": ["True"]}
        ]
    },
    "Random": {
        "Questions": [
            {"category": "Entertainment: Board Games", "type": "boolean", "difficulty": "medium",
             "question": "In the game &quot;Racko&quot; you may pick up ANY card from the discard pile.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Nutella is produced by the German company Ferrero.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
             "question": "The word &quot;news&quot; originates from the first letters of the 4 main directions on a "
                         "compass (North, East, West, South).",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
             "question": "TF2: Sentry rocket damage falloff is calculated based on the distance between the sentry "
                         "and the enemy, not the engineer and the enemy",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard",
             "question": "Throughout the entirety of &quot;Dragon Ball Z&quot;, Goku only kills two characters: a "
                         "miniboss named Yakon and Kid Buu.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "The name of the attack &quot;Kamehameha&quot; in Dragon Ball Z was named after a famous "
                         "king of Hawaii.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese "
                         "and Italian. ",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
             "question": "In Riot Games &quot;League of Legends&quot; the name of Halloween event is called &quot;The "
                         "Reckoning&quot;.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "easy",
             "question": "Tokyo is the capital of Japan.", "correct_answer": "True", "incorrect_answers": ["False"]}
        ]
    },
    "Maths": {
        "Questions": [
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
             "question": "The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its "
                         "first publisher, Sun Tzu.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
             "question": "A universal set, or a set that contains all sets, exists.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
             "question": "111,111,111 x 111,111,111 = 12,345,678,987,654,321", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
             "question": "The binary number &quot;101001101&quot; is equivalent to the Decimal number &quot;334&quot;",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
             "question": "Zero factorial is equal to zero. ", "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
             "question": "A &#039;Multimillion&#039; is a real number.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
             "question": "L&#039;H&ocirc;pital was the mathematician who created the homonymous rule that uses "
                         "derivatives to evaluate limits with indeterminations.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
             "question": "The sum of any two odd integers is odd.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
             "question": "You can square root a negative number with an imaginary number &quot;i&quot;.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
             "question": "A scalene triangle has two sides of equal length.", "correct_answer": "False",
             "incorrect_answers": ["True"]}
        ]
    },
    "Television": {
        "Questions": [
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
             "question": "The television show Doctor Who first aired in 1963.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
             "question": "In Battlestar Galactica (2004), Cylons were created by man as cybernetic workers and soldiers.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
             "question": "Bob Ross was a US Air Force pilot.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "hard",
             "question": "The Klingon home planet is Qo&#039;noS.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
             "question": "Klingons respect their disabled comrades, and those who are old, injuried, and helpless.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
             "question": "Klingons express emotion in art through opera and poetry.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
             "question": "In &quot;Star Trek&quot;, Klingons respect William Shakespeare, they even suspect him having a Klingon lineage.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
             "question": "In &quot;Star Trek&quot;, Klaang is a typical Klingon male.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
             "question": "In &quot;Star Trek&quot;, Klingons are aliens.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
             "question": "In &quot;Doctor Who&quot;, the Doctor gets his TARDIS by stealing it.",
             "correct_answer": "True", "incorrect_answers": ["False"]}
        ]
    },
    "Mythology": {
        "Questions": [
            {"category": "Mythology", "type": "boolean", "difficulty": "easy",
             "question": "In Norse mythology, Thor once dressed as a woman.", "correct_answer": "True",
             "incorrect_answers": ["False"]}, {"category": "Mythology", "type": "boolean", "difficulty": "easy",
                                               "question": "According to Greek Mythology, Zeus can control lightning.",
                                               "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "medium",
             "question": "According to Norse mythology, Loki is a mother.", "correct_answer": "True",
             "incorrect_answers": ["False"]}, {"category": "Mythology", "type": "boolean", "difficulty": "medium",
                                               "question": "The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.",
                                               "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "hard",
             "question": "Rannamaari was a sea demon that haunted the people of the Maldives and had to be appeased monthly with the sacrifice of a virgin girl.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "medium",
             "question": "In Greek mythology, Hera is the goddess of harvest.", "correct_answer": "False",
             "incorrect_answers": ["True"]}, {"category": "Mythology", "type": "boolean", "difficulty": "easy",
                                              "question": "According to Greek Mythology, Atlas was an Olympian God.",
                                              "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "medium",
             "question": "The Roman god &quot;Jupiter&quot; was first known as &quot;Zeus&quot; to the Greeks.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "easy",
             "question": "A wyvern is the same as a dragon.", "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Mythology", "type": "boolean", "difficulty": "hard",
             "question": "Janus was the Roman god of doorways and passageways.", "correct_answer": "True",
             "incorrect_answers": ["False"]}
        ]
    },
    "Geography": {
        "Questions": [
            {"category": "Geography", "type": "boolean", "difficulty": "easy",
             "question": "Greenland is almost as big as Africa.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "There are no roads in\/out of Juneau, Alaska.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "Vietnam is the only country in the world that starts with V. ", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "Gothenburg is the capital of Sweden.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "There exists an island named &quot;Java&quot;.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "The capital of the US State Ohio is the city of Chillicothe.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "easy",
             "question": "St. Louis is the capital of the US State Missouri.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "medium",
             "question": "Japan has left-hand side traffic.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Geography", "type": "boolean", "difficulty": "easy",
             "question": "New Haven is the capital city of the state of Connecticut in the United States.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Geography", "type": "boolean", "difficulty": "hard",
             "question": "The two largest ethnic groups of Belgium are Flemish and Walloon. ", "correct_answer": "True",
             "incorrect_answers": ["False"]}
        ]
    },
    "Vehicles": {
        "Questions": [
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "The Chevrolet Corvette has always been made exclusively with V8 engines only.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "easy",
             "question": "The full English name of the car manufacturer BMW is Bavarian Motor Works",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "When BMW was established in 1916, it was producing automobiles.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "Arriva is owned by the Deutsche Bahn.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "Ferrari has never made a V10 engine for any of its cars.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "Bugatti was an Italian car manufacturer.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "The majority of Subaru vehicles are made in China.", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "easy",
             "question": "BMW M GmbH is a subsidiary of BMW AG that focuses on car performance.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "hard",
             "question": "The term &quot;GTO&quot; was originated by Ferrari?", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
             "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
             "correct_answer": "True", "incorrect_answers": ["False"]}
        ]
    },
}
