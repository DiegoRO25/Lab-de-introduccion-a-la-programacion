from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

USUARIO = "admin"
CONTRASENA = "admin2026"

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Flask</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .card {
            background: white;
            padding: 32px;
            border-radius: 14px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            width: 340px;
        }
        h2 {
            margin: 0 0 20px;
            text-align: center;
            color: #111827;
        }
        label {
            display: block;
            margin: 12px 0 6px;
            color: #374151;
            font-weight: bold;
        }
        input {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            outline: none;
        }
        input:focus {
            border-color: #2563eb;
        }
        button {
            width: 100%;
            margin-top: 18px;
            padding: 12px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            background: #1d4ed8;
        }
        .error {
            margin-top: 12px;
            color: #dc2626;
            text-align: center;
            font-size: 14px;
        }
        .success {
            text-align: center;
            color: #16a34a;
            font-size: 14px;
        }
        .logout {
            display: inline-block;
            margin-top: 18px;
            text-decoration: none;
            background: #dc2626;
            color: white;
            padding: 10px 14px;
            border-radius: 8px;
            font-weight: bold;
        }
        .center {
            text-align: center;
        }
    </style>
</head>
<body>
    {% if session.get("autenticado") %}
        <div class="card center">
            <h2>Sesión iniciada</h2>
            <p class="success">Bienvenido, administrador.</p>
            <p>Usuario autenticado: admin</p>
            <a class="logout" href="{{ url_for('logout') }}">Cerrar sesión</a>
        </div>
    {% else %}
        <form class="card" method="post">
            <h2>Iniciar sesión</h2>
            <label>Usuario</label>
            <input type="text" name="usuario" required>
            <label>Contraseña</label>
            <input type="password" name="contrasena" required>
            <button type="submit">Ingresar</button>
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
        </form>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "").strip()

        if usuario == USUARIO and contrasena == CONTRASENA:
            session["autenticado"] = True
            return redirect(url_for("login"))

        return render_template_string(LOGIN_HTML, error="Usuario o contraseña incorrectos.")

    return render_template_string(LOGIN_HTML, error=None)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

##tkinter
import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Login Tkinter")
        self.root.geometry("360x220")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f7fb")

        self.usuario_correcto = "admin"
        self.contrasena_correcta = "admin2026"

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        frame = tk.Frame(self.root, bg="#ffffff", padx=25, pady=25)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(
            frame,
            text="Iniciar sesión",
            font=("Arial", 16, "bold"),
            bg="#ffffff",
            fg="#1f2937"
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        tk.Label(
            frame,
            text="Usuario",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#374151"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entry_usuario = tk.Entry(frame, width=24, font=("Arial", 11))
        self.entry_usuario.grid(row=1, column=1, pady=5)

        tk.Label(
            frame,
            text="Contraseña",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#374151"
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.entry_contrasena = tk.Entry(frame, width=24, font=("Arial", 11), show="*")
        self.entry_contrasena.grid(row=2, column=1, pady=5)

        boton = tk.Button(
            frame,
            text="Ingresar",
            width=18,
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.validar_login
        )
        boton.grid(row=3, column=0, columnspan=2, pady=(18, 0))

        self.entry_usuario.bind("<Return>", self.validar_login_evento)
        self.entry_contrasena.bind("<Return>", self.validar_login_evento)

    def validar_login_evento(self, event: tk.Event) -> None:
        self.validar_login()

    def validar_login(self) -> None:
        usuario = self.entry_usuario.get().strip()
        contrasena = self.entry_contrasena.get().strip()

        if usuario == self.usuario_correcto and contrasena == self.contrasena_correcta:
            messagebox.showinfo("Acceso concedido", "Bienvenido, administrador.")
            self.mostrar_panel()
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")

    def mostrar_panel(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#ffffff", padx=30, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Sesión iniciada",
            font=("Arial", 18, "bold"),
            bg="#ffffff",
            fg="#111827"
        ).pack(pady=(0, 10))

        tk.Label(
            frame,
            text="Usuario autenticado: admin",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#4b5563"
        ).pack(pady=(0, 15))

        tk.Button(
            frame,
            text="Cerrar sesión",
            width=18,
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.reiniciar
        ).pack()

    def reiniciar(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
        self._crear_interfaz()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
