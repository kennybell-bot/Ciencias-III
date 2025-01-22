import json
from automaton_model import AFNLambdaAutomaton, AFNAutomaton, AFDAutomaton
from automaton_transformations import convert_afn_lambda_to_afn, convert_afn_to_afd
from automaton_visualization import draw_automaton

def load_automaton_from_json(file_path, automaton_type):
    with open(file_path, 'r') as file:
        data = json.load(file)
    if automaton_type == "AFN-λ":
        return AFNLambdaAutomaton(**data)
    elif automaton_type == "AFN":
        return AFNAutomaton(**data)
    elif automaton_type == "AFD":
        return AFDAutomaton(**data)
    else:
        raise ValueError("Tipo de autómata desconocido.")

# Cargar un AFN-λ desde JSON
automaton = load_automaton_from_json("afn.json", "AFN")
print(automaton.states)
print(automaton.alphabet)
print(automaton.transitions)
print(automaton.start_state)
print(automaton.final_states)
# Graficar el autómata
draw_automaton(automaton, "origen")

# Convertir AFN-λ a AFN
# afn = convert_afn_lambda_to_afn(afn_lambda)

# Convertir AFN a AFD
afd = convert_afn_to_afd(automaton)
print(afd.states)
print(afd.alphabet)
print(afd.transitions)
print(afd.start_state)
print(afd.final_states)

# Graficar el autómata
draw_automaton(afd, "convertido")
