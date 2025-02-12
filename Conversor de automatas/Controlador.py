from Adapter import AdaptadorDiagrama
from automaton_model import Automaton, AFDAutomaton, AFNAutomaton, AFNLambdaAutomaton
from automaton_transformations import convert_afn_lambda_to_afn, convert_afn_to_afd

class Controlador:
    
    def adaptar_diagrama(self, automata, tipo_ingresado, tipo_conversion):
        adaptador = AdaptadorDiagrama()
        nodos, adyacencias, alfabeto, estado_inicial, estados_finales = adaptador.obtener_nodos_y_adyacencias(automata)
        print("Estados:", nodos)
        print("Conexiones:", adyacencias)
        print("Alfabeto:", alfabeto)
        print("Estado inicial:", estado_inicial)
        print("Estados finales:", estados_finales)

        # Inicializar el autómata según el tipo ingresado
        if tipo_ingresado == "AFN-λ":
            automaton = AFNLambdaAutomaton(nodos, alfabeto, adyacencias, estado_inicial, estados_finales)
        elif tipo_ingresado == "AFND":
            automaton = AFNAutomaton(nodos, alfabeto, adyacencias, estado_inicial, estados_finales)
        elif tipo_ingresado == "AFD":
            automaton = AFDAutomaton(nodos, alfabeto, adyacencias, estado_inicial, estados_finales)
        else:
            raise ValueError(f"Tipo de autómata ingresado desconocido: {tipo_ingresado}")

        # Validar el autómata ingresado
        try:
            automaton.validate()
            print(f"El autómata {tipo_ingresado} es válido.")
        except ValueError as e:
            print(f"Error de validación del autómata {tipo_ingresado}: {e}")
            return None

        # Convertir el autómata al tipo deseado
        if tipo_conversion == "AFN-λ":
            if isinstance(automaton, AFNLambdaAutomaton):
                converted_automaton = automaton
            else:
                raise ValueError("No se puede convertir a AFN-λ desde el tipo ingresado.")
        elif tipo_conversion == "AFND":
            if isinstance(automaton, AFNLambdaAutomaton):
                converted_automaton = convert_afn_lambda_to_afn(automaton)
            elif isinstance(automaton, AFNAutomaton):
                converted_automaton = automaton
            else:
                raise ValueError("No se puede convertir a AFND desde el tipo ingresado.")
        elif tipo_conversion == "AFD":
            if isinstance(automaton, AFNLambdaAutomaton):
                afn_automaton = convert_afn_lambda_to_afn(automaton)
                converted_automaton = convert_afn_to_afd(afn_automaton)
            elif isinstance(automaton, AFNAutomaton):
                converted_automaton = convert_afn_to_afd(automaton)
            elif isinstance(automaton, AFDAutomaton):
                converted_automaton = automaton
            else:
                raise ValueError("No se puede convertir a AFD desde el tipo ingresado.")
        else:
            raise ValueError(f"Tipo de conversión desconocido: {tipo_conversion}")

        # Validar el autómata convertido
        try:
            converted_automaton.validate()
            print(f"El autómata convertido a {tipo_conversion} es válido.")
        except ValueError as e:
            print(f"Error de validación del autómata convertido a {tipo_conversion}: {e}")

        # Imprimir el autómata convertido para verificar
        print("Autómata Finito Convertido:")
        print("Estados:", converted_automaton.states)
        print("Alfabeto:", converted_automaton.alphabet)
        print("Estado Inicial:", converted_automaton.start_state)
        print("Estados Finales:", converted_automaton.final_states)
        print("Transiciones:", converted_automaton.transitions)

        return converted_automaton
