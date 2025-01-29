import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from automaton_model import AFNLambdaAutomaton, AFNAutomaton, AFDAutomaton
from automaton_transformations import convert_afn_lambda_to_afn, convert_afn_to_afd
from automaton_visualization import draw_automaton

class AutomatonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Autómatas")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Variables
        self.file_path = None
        self.automaton = None
        self.automaton_type = None

        # UI
        self.create_widgets()

    def create_widgets(self):
        """Crea los elementos de la interfaz gráfica."""
        tk.Label(self.root, text="Convertidor de Autómatas", font=("Arial", 16, "bold")).pack(pady=10)

        self.label_file = tk.Label(self.root, text="No se ha seleccionado un archivo", fg="gray")
        self.label_file.pack()

        tk.Button(self.root, text="Cargar Archivo JSON", command=self.load_json, bg="#3498db", fg="white").pack(pady=10)
        self.btn_draw = tk.Button(self.root, text="Visualizar Autómata", command=self.draw_automaton, state=tk.DISABLED)
        self.btn_draw.pack(pady=5)

        self.btn_convert_afn_lambda = tk.Button(self.root, text="Convertir AFN-λ → AFN", command=self.convert_to_afn, state=tk.DISABLED)
        self.btn_convert_afn_lambda.pack(pady=5)

        self.btn_convert_afn = tk.Button(self.root, text="Convertir AFN → AFD", command=self.convert_to_afd, state=tk.DISABLED)
        self.btn_convert_afn.pack(pady=5)

    def load_json(self):
        """Carga un archivo JSON con un autómata."""
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not self.file_path:
            return
        
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            
            if "λ" in str(data["transitions"]):
                self.automaton_type = "AFN-λ"
                self.automaton = AFNLambdaAutomaton(**data)
            elif any(isinstance(v, list) for state in data["transitions"].values() for v in state.values()):
                self.automaton_type = "AFN"
                self.automaton = AFNAutomaton(**data)
            else:
                self.automaton_type = "AFD"
                self.automaton = AFDAutomaton(**data)
            
            self.label_file.config(text=f"Archivo cargado: {os.path.basename(self.file_path)} ({self.automaton_type})", fg="black")
            self.update_buttons()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")

    def update_buttons(self):
        """Habilita o deshabilita botones según el tipo de autómata."""
        self.btn_draw.config(state=tk.NORMAL)

        if self.automaton_type == "AFN-λ":
            self.btn_convert_afn_lambda.config(state=tk.NORMAL)  # Habilitar AFN-λ → AFN
            self.btn_convert_afn.config(state=tk.DISABLED)  # AFN → AFD deshabilitado hasta que se haga la primera conversión
        elif self.automaton_type == "AFN":
            self.btn_convert_afn_lambda.config(state=tk.DISABLED)  # AFN-λ → AFN ya no aplica
            self.btn_convert_afn.config(state=tk.NORMAL)  # AFN → AFD habilitado
        elif self.automaton_type == "AFD":
            self.btn_convert_afn_lambda.config(state=tk.DISABLED)  # No se puede convertir más
            self.btn_convert_afn.config(state=tk.DISABLED)  # No hay más conversiones posibles

    def draw_automaton(self):
        """Dibuja el autómata cargado."""
        if self.automaton:
            draw_automaton(self.automaton, "origen")
            messagebox.showinfo("Éxito", "El autómata original se ha guardado como 'origen.png'.")

    def convert_to_afn(self):
        """Convierte un AFN-λ a un AFN y lo visualiza."""
        if self.automaton_type == "AFN-λ":
            self.automaton = convert_afn_lambda_to_afn(self.automaton)
            self.automaton_type = "AFN"  # Ahora es un AFN
            draw_automaton(self.automaton, "convertido")
            messagebox.showinfo("Conversión Exitosa", "El autómata se ha convertido a AFN y guardado como 'convertido.png'.")
            self.update_buttons()  # Actualizar botones

    def convert_to_afd(self):
        """Convierte un AFN a un AFD y lo visualiza."""
        if self.automaton_type == "AFN":
            self.automaton = convert_afn_to_afd(self.automaton)
            self.automaton_type = "AFD"  # Ahora es un AFD
            draw_automaton(self.automaton, "convertido")
            messagebox.showinfo("Conversión Exitosa", "El autómata se ha convertido a AFD y guardado como 'convertido.png'.")
            self.update_buttons()  # Actualizar botones

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomatonApp(root)
    root.mainloop()
