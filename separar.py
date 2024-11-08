import pandas as pd

file_path = "LEAD-Limpo.csv"
df = pd.read_csv(file_path)


num_linhas = 20000

num_arquivos = len(df) // num_linhas + (1 if len(df) % num_linhas != 0 else 0)

for i in range(num_arquivos):

    df_part = df[i * num_linhas:(i + 1) * num_linhas]

    output_file = f"LISTA-PARTE-{i + 1}.csv"

    df_part.to_csv(output_file, index=False)
    print(f"Arquivo salvo: {output_file}")
