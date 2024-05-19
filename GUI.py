from tkinter import scrolledtext, filedialog
from create_databases import upload_excel, upload_docx
from search_excel import search_excel
from search_docx import search_docx
import tkinter as tk
import speech_recognition as sr

# Criando a janela principal
window = tk.Tk()
window.title("Synthify")
window.geometry("1200x700")
window.configure(bg="#F6F7F9")

# Função para abrir a caixa de diálogo de seleção de arquivos
def upload_file():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Selecione um arquivo",
        filetypes=(("Todos os arquivos", "*.*"), ("Arquivos de texto", "*.txt"),)
    )
    if file_path:
        file_path_label.config(text=f"Arquivo selecionado: {file_path}\nArquivo carregado com sucesso.")
        if file_path.endswith(".xlsx"):
            upload_excel(file_path)
        elif file_path.endswith(".docx"):
            upload_docx(file_path)

# Função para fazer busca no histórico de tickets
def search_tickets():
    question = question_entry.get("1.0", tk.END).strip()
    result = search_excel(question)
    answer_text.delete("1.0", tk.END)
    answer_text.insert(tk.END, result[0])
    sources_text.delete("1.0", tk.END)
    sources_text.insert(tk.END, result[1])

# Função para fazer busca nas documentações
def search_documentation():
    question = question_entry.get("1.0", tk.END).strip()
    result = search_docx(question)
    answer_text.delete("1.0", tk.END)
    answer_text.insert(tk.END, result[0])
    sources_text.delete("1.0", tk.END)
    sources_text.insert(tk.END, result[1])

# Função para transcrever fala em texto
def speak_to_text():
    question_entry.delete("1.0", tk.END)
    question_entry.insert(tk.END, "Diga algo...")
    window.update_idletasks()  # Força a atualização da interface gráfica
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language="pt-BR")
            question_entry.delete("1.0", tk.END)
            question_entry.insert(tk.END, text)
            return text
        except sr.UnknownValueError:
            question_entry.delete("1.0", tk.END)
            question_entry.insert(tk.END, "Desculpe, não entendi o que você disse.")
        except sr.RequestError as e:
            question_entry.delete("1.0", tk.END)
            question_entry.insert(tk.END, f"Erro ao se conectar ao serviço de reconhecimento de fala; {e}")

# Função para limpar o texto de orientação na entrada da pergunta
def clear_placeholder(event):
    if question_entry.get("1.0", tk.END).strip() == default_text:
        question_entry.delete("1.0", tk.END)

# Texto padrão na entrada de pergunta
default_text = "Insira sua pergunta aqui ou clique em 'Pressione para Falar' para começar."

# Definições de estilo
bg_color = "#F6F7F9"
fg_color = "#000000"
button_color = "#4B00FF"
button_fg_color = "#FFFFFF"
entry_bg_color = "#FFFFFF"
entry_fg_color = "#000000"

# Função para criar botões com estilo uniforme
def create_button(text, command):
    return tk.Button(
        left_frame,
        text=text,
        font=("Arial", 12),
        bg=button_color,
        fg=button_fg_color,
        command=command,
        width=30,  # Largura do botão
        height=2,  # Altura do botão
        relief="flat",  # Remover bordas
        highlightthickness=0,
        bd=0
    )

# Layout
left_frame = tk.Frame(window, bg=bg_color)
left_frame.pack(side="left", fill="y")

logo_label = tk.Label(left_frame, text="Synthify", font=('Helvetica', 16, 'bold'), bg=bg_color, fg="#4B00FF")
logo_label.pack(pady=20)

# Criar botões com tamanhos e estilos uniformes
ask_button1 = create_button("Procurar nas documentações", search_documentation)
ask_button1.pack(anchor='w', padx=10, pady=10)

ask_button2 = create_button("Procurar no histórico de tickets", search_tickets)
ask_button2.pack(anchor='w', padx=10, pady=10)

ask_button3 = create_button("Procurar na internet", lambda: None)
ask_button3.pack(anchor='w', padx=10, pady=10)

speak_button = create_button("Pressione para falar", speak_to_text)
speak_button.pack(anchor='w', padx=10, pady=10)

upload_button = create_button("Enviar novo arquivo para a base", upload_file)
upload_button.pack(anchor='w', padx=10, pady=10)

user_info = tk.Frame(left_frame, bg=bg_color)
user_info.pack(side="bottom", fill="x", padx=20, pady=20)

user_label = tk.Label(user_info, text="👤 Shakshi Patel", font=("Arial", 12), bg=bg_color, fg=fg_color)
user_label.pack(anchor="w")

username_label = tk.Label(user_info, text="@shakshi123", font=("Arial", 10), bg=bg_color, fg=fg_color)
username_label.pack(anchor="w")

right_frame = tk.Frame(window, bg=bg_color)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

question_label = tk.Label(right_frame, text="Insira sua pergunta:", font=("Arial", 12), bg=bg_color, fg=fg_color)
question_label.pack(anchor="w", pady=10)
question_entry = tk.Text(right_frame, height=10, bg=entry_bg_color, fg=entry_fg_color)
question_entry.insert(tk.END, default_text)
question_entry.bind("<FocusIn>", clear_placeholder)
question_entry.pack(fill="x", pady=10)

answer_label = tk.Label(right_frame, text="Resposta:", font=("Arial", 12), bg=bg_color, fg=fg_color)
answer_label.pack(anchor="w", pady=10)

answer_text = scrolledtext.ScrolledText(right_frame, height=10, bg=entry_bg_color, fg=entry_fg_color)
answer_text.pack(fill="x", pady=10)

sources_label = tk.Label(right_frame, text="Fontes:", font=("Arial", 12), bg=bg_color, fg=fg_color)
sources_label.pack(anchor="w", pady=10)

sources_text = scrolledtext.ScrolledText(right_frame, height=5, bg=entry_bg_color, fg=entry_fg_color)
sources_text.pack(fill="x", pady=10)

file_path_label = tk.Label(right_frame, text="")
file_path_label.pack(anchor='center', padx=10, pady=10)

# Executar a janela principal
window.mainloop()
