import random
def messages():
    answers = ['я вас не понимаю','i don\'t understand you','non capisco', 'Je ne comprends pas']
    a = answers[random.randint(0, len(answers)-1)]
    return a
hellowords = ['привет','ку','здарова','здравствуйте','салам', 'всем привет']
def answer():
    answers = ['Еу','Всем хай','Привет', 'Ciao','Hello']
    a = answers[random.randint(0, len(answers)-1)]
    return a