# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
from Bio import Entrez
import os
import csv
from datetime import datetime

Entrez.email = "thea.meimoun@weizmann.ac.il" 

def fetch_ncbi_records(term, number, database, file_format):
    search_handle = Entrez.esearch(db=database, term=term, idtype="acc", retmax=number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    total = search_results["Count"]

    file_names = []

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    for index, record_id in enumerate(ids):
        fetch_handle = Entrez.efetch(db=database, id=record_id, rettype=file_format, retmode="text")
        record = fetch_handle.read()
        fetch_handle.close()

        file_name = f"downloads/{term.replace(' ', '_')}_{index + 1}.{file_format.lower()}"
        with open(file_name, 'w') as file:
            file.write(record)
        file_names.append(file_name)

    return file_names, total

def log_search_details(date, term, number, total):
    log_file = 'search_log.csv'
    log_exists = os.path.isfile(log_file)

    with open(log_file, 'a', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        if not log_exists:
            log_writer.writerow(["date", "term", "max", "total"])
        log_writer.writerow([date, term, number, total])

def download_data():
    search_term = entry_search.get()
    num_records = entry_number.get()
    database = combo_db.get()
    file_format = combo_format.get()

    if not search_term or not num_records or not database or not file_format:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        num_records = int(num_records)
    except ValueError:
        messagebox.showerror("Error", "Number of records must be an integer")
        return

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        file_names, total = fetch_ncbi_records(search_term, num_records, database, file_format)
        log_search_details(current_date, search_term, num_records, total)

        messagebox.showinfo("Success", f"Data downloaded and saved as {', '.join(file_names)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("NCBI Data Downloader")

# Créer et placer les widgets
tk.Label(root, text="Search Term:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_search = tk.Entry(root, width=30)
entry_search.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Records:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_number = tk.Entry(root, width=30)
entry_number.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Database:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
combo_db = ttk.Combobox(root, values=["nucleotide", "protein"], width=27)
combo_db.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="File Format:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
combo_format = ttk.Combobox(root, values=["fasta", "gb"], width=27)
combo_format.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Download Data", command=download_data).grid(row=4, column=0, columnspan=2, pady=20)

# Lancer l'application
root.mainloop()
