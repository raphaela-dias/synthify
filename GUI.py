from tkinter import scrolledtext
from tkinter import filedialog
from create_databases import upload_excel, upload_docx
from search_excel import search_excel
from search_docx import search_docx
import tkinter as tk

# Criando a janela principal
window = tk.Tk()
window.title("Synthify")

# Função para abrir a caixa de diálogo de seleção de arquivos
def upload_file():
  """Abre uma caixa de diálogo para o usuário escolher um arquivo e exibe o caminho do arquivo."""
  file_path = filedialog.askopenfilename(
    initialdir="/",
    title="Selecione um arquivo",
    filetypes=(("Todos os arquivos", "*.*"), ("Arquivos de texto", "*.txt"),)
  )
  if file_path:
    # Exibe o caminho do arquivo selecionado
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

def search_documentation():
  question = question_entry.get("1.0", tk.END).strip()
  result = search_docx(question)
  answer_text.delete("1.0", tk.END)
  answer_text.insert(tk.END, result[0])
  sources_text.delete("1.0", tk.END)
  sources_text.insert(tk.END, result[1])
  


# Campo de entrada da pergunta
question_label = tk.Label(window, text="Insira sua pergunta:")
question_label.pack()
question_entry = tk.Text(window, height=3)
question_entry.pack()

# Criando um frame para os botões
button_frame = tk.Frame(window)
button_frame.pack()

# Botões para enviar a pergunta
ask_button1 = tk.Button(button_frame, text="Enviar novo arquivo para a base", command=upload_file)
ask_button1.pack(side="left", padx=10)

ask_button2 = tk.Button(button_frame, text="Procurar nas documentações", command= search_documentation)
ask_button2.pack(side="left", padx=10)

ask_button3 = tk.Button(button_frame, text="Procurar no histórico de tickets", command=search_tickets)
ask_button3.pack(side="left", padx=10)

ask_button4 = tk.Button(button_frame, text="Procurar na internet")
ask_button4.pack(side="left", padx=10)

# Rótulo para exibir o caminho do arquivo selecionado
file_path_label = tk.Label(window, text="")
file_path_label.pack()

# Área de exibição da resposta
answer_label = tk.Label(window, text="Resposta:")
answer_label.pack()
answer_text = scrolledtext.ScrolledText(window, height=10)
answer_text.pack()

# Área de exibição das fontes
sources_label = tk.Label(window, text="Fontes:")
sources_label.pack()
sources_text = scrolledtext.ScrolledText(window, height=5)
sources_text.pack()

# Executar a janela principal
window.mainloop()