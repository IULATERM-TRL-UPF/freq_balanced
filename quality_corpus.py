import re
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import numpy as np
import nltk
from tqdm import tqdm
import os


# Cargar corpus línea por línea en modo streaming
def load_corpus(file_path):
    print("Cargando el corpus...")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# Procesar texto
def preprocess_text(text):
    return re.sub(r'[^a-záéíóúüñ ]', '', text.lower())

# Obtener stopwords por idioma
def get_stopwords(language):
    print(f"Obteniendo stopwords para el idioma: {language}")
    stopwords_dict = {
        'en': set(stopwords.words('english')),
        'es': set(stopwords.words('spanish')),
        'ca': set(stopwords.words('catalan'))
    }
    return stopwords_dict.get(language, set())

# Obtener frecuencias de palabras en chunks para optimizar memoria
def get_frequencies(file_path, stop_words):
    print("Calculando frecuencias de palabras...")
    word_counter = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f, desc="Procesando líneas", unit=" línea"):
            tokens = [word for word in word_tokenize(line.lower()) if word not in stop_words]
            word_counter.update(tokens)
    
    return word_counter

# Filtrar líneas según frecuencia y escribir en archivo en tiempo real
def filter_sentences(file_path, output_path, word_frequencies, stop_words, threshold=100):
    print("Filtrando líneas y escribiendo corpus filtrado...")
    total_lines = sum(1 for _ in open(file_path, 'r', encoding='utf-8'))
    
    with open(file_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in tqdm(infile, total=total_lines, desc="Procesando líneas", unit=" línea"):
            words = [word for word in word_tokenize(line.lower()) if word not in stop_words]
            if not all(word_frequencies[word] > threshold for word in words):
                outfile.write(line)
    
    print("Corpus filtrado guardado en:", output_path)

# Graficar distribuciones
def plot_frequencies(freq_dict, title, top_n=20):
    print(f"Generando gráfico: {title}")
    most_common = freq_dict.most_common(top_n)
    words, counts = zip(*most_common)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(words), y=list(counts))
    plt.xticks(rotation=45)
    plt.title(title)
    plt.show()

# Calcular media de frecuencias
def mean_frequency(freq_dict):
    return np.mean(list(freq_dict.values()))

# Ejemplo de uso
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", choices=["en", "es", "ca"], required=True, help="Idioma del corpus (en: inglés, es: español, ca: catalán)")
    parser.add_argument("-f", "--file", required=True, help="Ruta del archivo de texto del corpus")
    args = parser.parse_args()
    
    stop_words = get_stopwords(args.language)
    
    word_freqs = get_frequencies(args.file, stop_words)
    
    output_file = "filtered_corpus.txt"
    filter_sentences(args.file, output_file, word_freqs, stop_words)
    
    plot_frequencies(word_freqs, "Frecuencia de palabras")
    
    print("Media de frecuencia de palabras:", mean_frequency(word_freqs))
    print("Proceso completado.")