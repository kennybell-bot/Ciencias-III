from automaton_model import AFNLambdaAutomaton, AFNAutomaton, AFDAutomaton

def convert_afn_lambda_to_afn(automaton: AFNLambdaAutomaton) -> AFNAutomaton:
    """
    Convierte un AFN-λ a un AFN eliminando las transiciones λ.

    Args:
        automaton (AFNLambdaAutomaton): El autómata AFN-λ a convertir.

    Returns:
        AFNAutomaton: El autómata resultante sin transiciones λ.
    """
    # Clausura lambda: Calcula todos los estados alcanzables por λ desde un estado
    def lambda_closure(state):
        closure = {state}
        stack = [state]
        while stack:
            current = stack.pop()
            if 'λ' in automaton.transitions.get(current, {}):
                for next_state in automaton.transitions[current]['λ']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    # Crear nuevas transiciones sin λ
    new_transitions = {}
    for state in automaton.states:
        closure = lambda_closure(state)
        new_transitions[state] = {}

        for symbol in automaton.alphabet:
            if symbol == 'λ':
                continue
            destinations = set()
            for reachable in closure:
                if symbol in automaton.transitions.get(reachable, {}):
                    destinations.update(automaton.transitions[reachable][symbol])
            if destinations:
                new_transitions[state][symbol] = list(destinations)

    # Calcular los nuevos estados finales
    new_final_states = set(automaton.final_states)
    for state in automaton.states:
        if any(f in lambda_closure(state) for f in automaton.final_states):
            new_final_states.add(state)

    return AFNAutomaton(
        states=automaton.states,
        alphabet=[s for s in automaton.alphabet if s != 'λ'],
        transitions=new_transitions,
        start_state=automaton.start_state,
        final_states=list(new_final_states),
    )


def convert_afn_to_afd(automaton: AFNAutomaton) -> AFDAutomaton:
    """
    Convierte un AFN a un AFD utilizando el algoritmo de subconjuntos.

    Args:
        automaton (AFNAutomaton): El autómata AFN a convertir.

    Returns:
        AFDAutomaton: El autómata determinista resultante.
    """
    from collections import deque

    # Estado inicial del AFD
    start_closure = frozenset([automaton.start_state])
    queue = deque([start_closure])
    visited = {start_closure: "q0"}
    new_states = ["q0"]
    new_transitions = {}
    new_final_states = []
    state_counter = 1

    while queue:
        current_set = queue.popleft()
        current_label = visited[current_set]
        new_transitions[current_label] = {}

        for symbol in automaton.alphabet:
            destinations = set()
            for state in current_set:
                if symbol in automaton.transitions.get(state, {}):
                    destinations.update(automaton.transitions[state][symbol])

            if destinations:
                destination_closure = frozenset(destinations)
                if destination_closure not in visited:
                    new_label = f"q{state_counter}"
                    visited[destination_closure] = new_label
                    new_states.append(new_label)
                    queue.append(destination_closure)
                    state_counter += 1
                new_transitions[current_label][symbol] = visited[destination_closure]

        # Verificar si el estado actual contiene algún estado final del AFN
        if any(state in automaton.final_states for state in current_set):
            new_final_states.append(current_label)

    return AFDAutomaton(
        states=new_states,
        alphabet=automaton.alphabet,
        transitions=new_transitions,
        start_state="q0",
        final_states=new_final_states,
    )
