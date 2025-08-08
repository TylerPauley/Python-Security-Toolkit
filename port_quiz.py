import random

# Dictionary of various common ports and their services. Can easily be added to
port_services = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    993: 'IMAP over SSL',
    995: 'POP3 over SSL',
    3389: 'RDP',
    3306: 'MySQL',
    1433: 'MSSQL',
    1521: 'Oracle DB',
    8080: 'HTTP Proxy',
}

# Function that creates multiple-choice questions
def create_multiple_choice(correct_answer, options):
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    return options

# Function that handles "What's Port X?" questions
def guess_service_by_port(port, correct_answers, total_answers):
    correct_service = port_services[port]
    incorrect_services = random.sample(
        [service for p, service in port_services.items() if p != port], 3
    )
    options = [correct_service] + incorrect_services
    options = create_multiple_choice(correct_service, options)
    
    answer = int(input("Your answer: "))
    total_answers += 1
    if options[answer - 1] == correct_service:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect! Port {port} is used for {correct_service}.\n")

    return correct_answers, total_answers

# Function that handles "What port is service Y on?" questions
def guess_port_by_service(service, correct_answers, total_answers):
    correct_port = [port for port, serv in port_services.items() if serv == service][0]
    incorrect_ports = random.sample(
        [port for port, serv in port_services.items() if serv != service], 3
    )
    options = [correct_port] + incorrect_ports
    options = create_multiple_choice(correct_port, options)
    
    answer = int(input("Your answer: "))
    total_answers += 1
    if options[answer - 1] == correct_port:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect! {service} runs on port {correct_port}.\n")

    return correct_answers, total_answers

def port_guesser_game():
    correct_answers = 0
    total_answers = 0

    while True:
        question_type = random.choice(["port", "service"])
        
        if question_type == "port":
            port = random.choice(list(port_services.keys()))
            print(f"\nWhat service runs on port {port}?")
            correct_answers, total_answers = guess_service_by_port(port, correct_answers, total_answers)
        else:
            service = random.choice(list(port_services.values()))
            print(f"\nWhat port does {service} run on?")
            correct_answers, total_answers = guess_port_by_service(service, correct_answers, total_answers)
        
        # Breaks the script if total_answers / correct_answers is left at 0. Added this to get around that issue.
        if total_answers > 0:
            percentage_score = (correct_answers / total_answers) * 100
            print(f"\nYour score: {correct_answers}/{total_answers} correct.")
            print(f"Your percentage score: {percentage_score:.2f}%")
        
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print(f"Thanks for playing!\nYou got {percentage_score:.2f}% correct! Your final score was {correct_answers}/{total_answers}")
            break

if __name__ == "__main__":
    port_guesser_game()
