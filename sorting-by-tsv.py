import pandas as pd

df = pd.read_csv('aop_stacking_combo_amd_test_zhangyu.ea120.gemm_size.tsv', sep='\t')

sorted_df = df.sort_values(by='call_count', ascending=False)

print(sorted_df)

sorted_df.to_csv('sorted_data.tsv', sep='\t', index=False)
