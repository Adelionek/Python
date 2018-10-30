#! python3
# randomQuizGenerator.py

import random

# the quiz data. Keys are states and values are capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\ Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West\ Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):

    #Creating quiz and answr fles

    quizFile = open('capitalquiz%s.txt' % (quizNum +1),'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum +1),'w')
    #header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)'% (quizNum+1))
    quizFile.write('\n\n')

    # Shuffle the order of states.
    states = list(capitals.keys())
    random.shuffle(states)

    # ODO: Loop through all 50 states, making a question for each

    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        "duplicating capitals"
        wrongAnswers = list(capitals.values())
        "deleting correct answer"
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        "choose 3 random answers"
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        "random answers, instead correct would be always D"
        random.shuffle(answerOptions)

        # Question and answer options
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1,states[questionNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

    # ODO: Write the answer key to a file
    answerKeyFile.write('%s. %s\n' % (questionNum +1,'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
