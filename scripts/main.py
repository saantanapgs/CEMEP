import os
import re
import shutil
from pdf2image import convert_from_path
from extract_data import extract_data, clean_text
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

directory = "Scan"

for files in os.listdir(directory):
    if files.lower().endswith(".pdf"):
        pdf_path = os.path.join(directory, files)
        print(f"\nProcessando o arquivo: {files}")

        # Convertendo de PDF para imagem para que o OCR consiga transformar em texto
        try:
            images = convert_from_path(pdf_path)
        except:
            print(f"Erro ao abrir o arquivo: {files}")
            continue

        full_text = ""

        # Converte de imagem para string
        for img in images:
            try:
                img = img.convert("RGB")  
                file_content = pytesseract.image_to_string(img, lang="por")
                full_text += file_content + "\n"
            except:
                print(f"Erro no OCR do arquivo: {files}")
                continue

        # Limpando o conteúdo da extração do OCR
        cleaned_text = clean_text(full_text)

        # Extraindo dados
        file_type, name, date = extract_data(cleaned_text)

        if name and date:
            new_file_name = f"{file_type.upper()} - {name} - {date}"
            file_extension = ".pdf"

            # Limpando caracteres inválidos
            new_file_name = re.sub(r'[\\/*?:"<>|]', "", new_file_name)

            final_name = f"{new_file_name}{file_extension}"
            final_path = os.path.join(directory, final_name)

            # Loop para garantir que arquivos tenham nomes únicos
            counter = 1
            while os.path.exists(final_path):
                final_name = f"{new_file_name} ({counter}){file_extension}"
                final_path = os.path.join(directory, final_name)
                counter += 1

            os.rename(pdf_path, final_path)

            print(f"Renomeado para: {final_name}")

            # Nome do monitorado(a) limpo
            cleaned_name = re.sub(r'[\\/*?:"<>|]', "", name)

            # Jogando o arquivo na pasta do monitorado(a)
            base_dir = r"C:\ATIVOS_TESTE"
            
            # Iniciliazando variável da pasta a ser pesquisada através do nome do monitorado(a)
            folder_found = None

            # Loop para procurar pasta com o nome do monitorado(a)
            for folder in os.listdir(base_dir):
                folder_path = os.path.join(base_dir, folder)

                if os.path.isdir(folder_path):
                    if cleaned_name.lower() in folder.lower():
                        folder_found = folder_path
                        break

            if folder_found:
                file_name = os.path.basename(final_path)
                destination_path = os.path.join(folder_found, file_name)

                # Loop para garantir que arquivos tenham nomes únicos
                cont = 1
                while os.path.exists(destination_path):
                    name_whitout_ext, ext = os.path.splitext(file_name)
                    new_name = f"{name_whitout_ext} {cont}{ext}"
                    destination_path = os.path.join(folder_found, new_name)
                    cont += 1

                shutil.move(final_path, folder_found)

                print(f"Movido para: {folder_found}")
            else:
                print(f"Pasta do monitorado(a): {cleaned_name} não encontrada.")

        else:
            print(f"ERRO ao extrair dados do arquivo: {files}")