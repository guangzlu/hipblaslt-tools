import json
import pandas as pd

file_name = "tf218-mi308-noxla-hipblaslt-41steps-dand451.log"
output_name = "tf218-mi308-noxla-hipblaslt-41steps-dand451.stats."

def get_list_from_str(input_str):
    return_list = input_str.split('\n')
    return return_list


with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

all_list  = get_list_from_str(content)

call_count = {}
for call in all_list:
    if call in call_count:
        call_count[call] += 1
    else:
        call_count[call] = 1

print("all_list len is ", len(all_list))
print("len of call_count is", len(call_count))

df = pd.DataFrame.from_dict(call_count, orient='index').reset_index()
df.columns = ['hipblaslt-bench', 'call_count']
df_sorted = df.sort_values(by='call_count', ascending=False)
print(df_sorted)

df_first_1000 = df_sorted.head(1000)

output_file_path = output_name + '.csv'
df_first_1000.to_csv(output_file_path, index=False, encoding='utf-8')

row_count = df.shape[0]
print(" unique blaslt call amount is ", row_count)

