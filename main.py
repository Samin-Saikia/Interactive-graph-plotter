import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import plotly.graph_objects as go
from plotly.offline import iplot

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Graph Plotter")
        self.entry_label = tk.Label(root, text="Enter equation (in terms of x):")
        self.entry_label.pack()
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        self.plot_button = tk.Button(root, text="Plot", command=self.plot_graph)
        self.plot_button.pack()
        self.quit = tk.Button(root, text="Quit", command=root.quit)
        self.quit.pack()

    def plot_graph(self):
        try:
            x = sp.symbols('x')
            eqn = self.entry.get()
            f = sp.sympify(eqn)
            lam_func = sp.lambdify(x, f, 'numpy')
            x_vals = np.linspace(-10, 10, 400)
            y_vals = lam_func(x_vals)

            fig = go.Figure(data=[go.Scatter(x=x_vals, y=y_vals, mode='lines')])
            fig.update_layout(title='Graph of ' + eqn,
                              xaxis_title='x',
                              yaxis_title='y')

            # For simplicity and compatibility, we'll save the plot to an HTML file and open it
            fig.write_html('graph.html', auto_open=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()