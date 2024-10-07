from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scripts.create_databases import upload_docx, upload_excel
from scripts.search_docx import search_docx
from scripts.search_excel import search_excel
from django.http import JsonResponse
import json
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def chatsynthify(request):
    return render(request, 'chat-synthify.html')

def openTickets(request):
    return render(request, 'open_tickets.html')

def myTickets(request):
    return render(request, 'my_tickets.html')

def sobre(request):
    return render(request, 'sobre.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        
        # Salva o arquivo em uma pasta temporária
        file_name = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(file_name)

        try:
            # Verifica a extensão do arquivo e salva na pasta correta (embeddings)
            if file_name.endswith('.docx'):
                upload_docx(file_path)  # Função de processamento do .docx
                destination_dir = os.path.join(settings.MEDIA_ROOT, 'db_docx')
            elif file_name.endswith('.xlsx'):
                upload_excel(file_path)  # Função de processamento do .xlsx
                destination_dir = os.path.join(settings.MEDIA_ROOT, 'db_excel')
            else:
                return JsonResponse({'error': 'Formato de arquivo não suportado.'}, status=400)

            # Move o arquivo para a pasta correta
            os.makedirs(destination_dir, exist_ok=True)
            os.rename(file_path, os.path.join(destination_dir, file_name))

            # Retorna uma resposta de sucesso
            return JsonResponse({'message': 'Upload feito com sucesso!'}, status=200)

        except Exception as e:
            # Retorna erro se algo deu errado durante o upload
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Nenhum arquivo enviado.'}, status=400)


def search_docs(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question', '')

        # Função de busca
        response, sources = search_docx(question)

        return JsonResponse({'response': response, 'sources': sources})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def search_tickets(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question', '')

        # Função de busca
        response, sources = search_excel(question)

        return JsonResponse({'response': response, 'sources': sources})
    return JsonResponse({'error': 'Invalid request'}, status=400)