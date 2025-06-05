"""crie uma lista de questões com 5 perguntas e 4 possiveis resposta,
Cada pergunta deve ter uma resposta correta
Cada resposta correta deve valer 1 ponto
Esse quiz será de várias capitais do mundo
"""

questions = [
    
    {
        "question": "Qual é a capital da França?",
        "answers": {"a":"Paris", "b":"Londres","c":"Berlim","d":"Madri"},
        "correct_answer": "Paris"
    },
    {
        "question": "Qual é a capital do Japão?",
        "answers": {"a":"Tóquio", "b":"Seul","c":"Pequim","d":"Bangkok"},
        "correct_answer": "Tóquio"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "answers": {"a":"Brasília", "b":"Rio de Janeiro","c":"São Paulo","d":"Salvador"},
        "correct_answer": "Brasília"
    },
    {
        "question": "Qual é a capital da Itália?",
        "answers": {"a":"Roma", "b":"Milão","c":"Veneza","d":"Florença"},
        "correct_answer": "Roma"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "answers": {"a":"Canberra", "b":"Sydney","c":"Melbourne","d":"Brisbane"},
        "correct_answer": "Canberra"
    }
]

# escreva uma função que recebe a questão e as exibe para o usuario.
#Ela retorna a respostya do usuário e valida se a resposta é valida ou se ela é um erro.

# def show_question(question):
#     print(question["question"])
#     for key, value in question["answers"].items():
#         print(f"{key}: {value}")
    
#     user_answer = input("Digite a letra da sua resposta: ").strip().lower()
    
#     while user_answer not in question["answers"].keys():
#         print("Resposta inválida. Tente novamente.")
#         user_answer = input("Digite a letra da sua resposta: ").strip().lower()
#     return user_answer

"""
 escreva uma função que recebe a questão e as exibe para o usuario.
 Ela retorna a respostya do usuário e valida se a resposta é valida ou se ela é um erro.
 Ser o usuario não responder em 10 segundos, a fução deve retornar que o tempo acabou.
 Usando a biblioteca treading, voce pode criar uma thead que conta  10 segundos e, 
 se o usuario não responder, a thread interrompe a execução e retorna que o tempo acabou.
"""
import threading

def show_question(question):
    print(question["question"])
    for key, value in question["answers"].items():
        print(f"{key}: {value}")
    
    user_answer = None  # Variável para armazenar a resposta do usuário
    
    def get_user_answer():
        user_answer = input("Digite a letra da sua resposta: ").strip().lower()


    thread = threading.Thread(target=get_user_answer)
    thread.daemon = True  # Permite que a thread seja encerrada quando o programa principal terminar
    thread.start()a
    thread.join(timeout=5)  # Aguarda até 10 segundos pela resposta do usuário
    if user_answer == "":
        print("Tempo esgotado! Você não respondeu a tempo.")
        return None
    while user_answer not in question["answers"].keys():
        print("Resposta inválida. Tente novamente.")
        user_answer = input("Digite a letra da sua resposta: ").strip().lower() 
    return user_answer

   

#escreva uma função recebe a respósta do usuário e a resposta correta



def check_answer(user_answer, question):
    return question["answers"][user_answer] == question["correct_answer"]

def main():
    score = 0
    for question in questions:
        user_answer = show_question(question)
        if check_answer(user_answer, question):
            print("Resposta correta!")
            score += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {question['correct_answer']}")
    

    """Adicione um sistema de feedback ao usuário ao final do quiz,
    entre 0 e 30 por cento:"Você precisa estudar mais"
    entre 40 e 70 por cento: "Bom trabalho, mas ainda há espaço para melhorias"
    entre 80 e 100 por cento: "Excelente trabalho, você é um expert!"
    """
    if score/len(questions) <= 0.3:
        print("Você precisa estudar mais.")
    elif score/len(questions) <= 0.7:
        print("Bom trabalho, mas ainda há espaço para melhorias.")
    else:
        print("Excelente trabalho, você é um expert!")

    print(f"Sua pontuação final é: {score}/{len(questions)}")


if __name__ == "__main__":
    main()