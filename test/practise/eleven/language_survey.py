from survey import AnonymouSurvey


question = "What language did you first learn to speak?"
my_suyvey = AnonymouSurvey(question)

my_suyvey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_suyvey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_suyvey.show_results()
