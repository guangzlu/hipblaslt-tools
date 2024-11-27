import pandas as pd

file_name = "no-graph-rocblas_log_tf218_fuel-0_noautotune.stats.csv"
output_file_path = "hipblaslt-bench-top100.txt"

df = pd.read_csv(file_name)
total_count = df["call_count"].sum()
print("total_count is, ", total_count)

#get top 100 hipblaslt-bench commands and sum call count:
df_head_100 = df.head(100)
head_100_count = df_head_100["call_count"].sum()
print("head_100_count is, ", head_100_count, "ratio to total is", (head_100_count/total_count))

#output top 100 hipblaslt-bench commands to txt:
df_head_100_commands = df_head_100["hipblaslt-bench"]
df_head_100_commands.to_csv(output_file_path, index=False)

