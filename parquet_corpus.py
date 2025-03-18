import pandas as pd
import argparse
from tqdm import tqdm

def convert_parquet_to_txt(parquet_file, txt_file, text_column):
    # Leer el archivo parquet
    df = pd.read_parquet(parquet_file)
    
    # Verificar si la columna existe
    if text_column not in df.columns:
        raise ValueError(f"La columna '{text_column}' no existe en el archivo Parquet.")
    
    # Extraer el texto y guardarlo en un archivo .txt con barra de progreso
    with open(txt_file, 'w', encoding='utf-8') as f:
        for text in tqdm(df[text_column].dropna(), desc="Procesando filas", unit=" fila"):
            f.write(text + '\n')
    
    print(f"Conversión completada: {txt_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parquet", required=True, help="Ruta del archivo Parquet")
    parser.add_argument("-t", "--txt", required=True, help="Ruta del archivo de salida TXT")
    parser.add_argument("-c", "--column", required=True, help="Nombre de la columna que contiene el texto")
    args = parser.parse_args()
    
    convert_parquet_to_txt(args.parquet, args.txt, args.column)