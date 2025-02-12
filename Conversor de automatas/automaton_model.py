class Automaton:
    """
    Clase base para representar un autómata.
    """
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def validate(self):
        """
        Valida que el autómata sea coherente.
        """
        if self.start_state not in self.states:
            raise ValueError("El estado inicial no está en los estados del autómata.")
        for state in self.final_states:
            if state not in self.states:
                raise ValueError(f"El estado final '{state}' no está en los estados del autómata.")
        for state, transitions in self.transitions.items():
            if state not in self.states:
                raise ValueError(f"El estado '{state}' en las transiciones no está definido.")
            for symbol in transitions:
                if symbol not in self.alphabet:
                    raise ValueError(f"El símbolo '{symbol}' en las transiciones no está en el alfabeto.")
        return True


class AFNLambdaAutomaton(Automaton):
    """
    Representa un AFN-λ.
    """
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        super().__init__(states, alphabet, transitions, start_state, final_states)
        self.alphabet.append("λ")  # Incluye λ como símbolo


class AFNAutomaton(Automaton):
    """
    Representa un AFN.
    """
    pass  # Usa la lógica básica de la clase Automaton


class AFDAutomaton(Automaton):
    """
    Representa un AFD.
    """
    def validate(self):
        """
        Valida que las transiciones del AFD sean determinísticas.
        """
        super().validate()
        for state, transitions in self.transitions.items():
            for symbol, destinations in transitions.items():
                if len(destinations) > 1:
                    raise ValueError(
                        f"El AFD tiene transiciones no determinísticas desde el estado '{state}' con símbolo '{symbol}'."
                    )
        return True
