import random


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
    
for quizNum in range(5):
    quizFile = open('quiz%s.txt' % (quizNum + 1), 'w')
    ansFile = open('ans%s.txt' % (quizNum +1), 'w')    

    #Quiz header
    quizFile.write('Name:\nNumber:\nDate:\n\n')
    quizFile.write(' ' * 20 + 'Geography Quiz Form %s\n\n\n' % (quizNum + 1))
    
    #Shuffle states
    states = list(capitals.keys())
    random.shuffle(states)

    #write questions and answers
    for quesNum in range(50):
        correctAns = capitals[states[quesNum]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        ansOptions = wrongAns + [correctAns]
        random.shuffle(ansOptions)

        quizFile.write('%s. Which is the capital of %s?\n' % (quesNum+1, states[quesNum]))
        for option in range(len(ansOptions)):
            quizFile.write(' ' +  'ABCD'[option] + '. ' + ansOptions[option] + '\n')
        quizFile.write('\n')

        ansFile.write('%s %s\n' % (quesNum + 1, 'ABCD'[ansOptions.index(correctAns)]))

    quizFile.close()
    ansFile.close()
