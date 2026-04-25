import re 

def extract_data(file_content):
    months = {
        "janeiro": "01",
        "fevereiro": "02",
        "marco": "03",
        "abril": "04",
        "maio": "05",
        "junho": "06",
        "julho": "07",
        "agosto": "08",
        "setembro": "09",
        "outubro": "10",
        "novembro": "11",
        "dezembro": "12"
    }
    file_content = file_content.upper()

    # Tipo de termo(substituição, devolução ou declaração) do arquivo
    if "SUBSTITUI" in file_content:
        file_type = "Termo de substituição"
    elif "DEVOLU" in file_content:
        file_type = "Termo de devolução"
    elif "DECLARA" in file_content:
        file_type = "Termo de declaração"
    elif "ALVARA" in file_content:
        file_type = "Alvará de Soltura"
    else:
        file_type = "Unknow file"

    # Data de emissão no documento
    date_match = re.search(
        r"(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})",
        file_content.lower())
    
    date = date_match.group(0) if date_match else None

    if date_match:
        day, written_month,year = date_match.groups()
        month = months.get(written_month, "00")
        date = f"{day.zfill(2)}.{month}.{year}"
    else:
        date = "."

    # Nome do monitorado/vítima
    name_match = re.search(
        r"MONITORADO[:\-]?\s*([A-Z\s]+)(?:PROCESSO|$)",
        file_content)
    
    name = name_match.group(1).strip() if name_match else None

    if name:
        name = name.split("PROCESSO")[0].strip()

    return file_type, name, date

def clean_text(file_content):
    file_content = file_content.upper()
    file_content = file_content.replace("\n", " ")
    file_content = re.sub(r"\s+", " ", file_content)
    return file_content