import pandas as pd

file_path = "lista.csv"

df = pd.read_csv(file_path)

df_filtrado = df.dropna(subset=["E-mail da Empresa"])

output_file = "CSV-Limpo.csv"
df_filtrado.to_csv(output_file, index=False)

print(f"Arquivo salvo: {output_file}")
