import json
from automaton_model import AFNLambdaAutomaton, AFNAutomaton, AFDAutomaton
from automaton_transformations import convert_afn_lambda_to_afn, convert_afn_to_afd


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
print(automaton.transitions)

# Convertir AFN a AFD
afd = convert_afn_to_afd(automaton)
print(afd.states)
print(afd.transitions)
