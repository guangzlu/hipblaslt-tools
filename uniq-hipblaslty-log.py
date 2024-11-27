import json
import pandas as pd

file_name = "tf218-mi308-noxla-hipblaslt-41steps-dand451.log"
output_name = "tf218-mi308-noxla-hipblaslt-41steps-dand451.stats."

#def remove_duplicate_lines(input_text):
#    # Split the input text into lines
#    lines = input_text.split('\n')
#    print("len of original is ", len(lines))
#    # Use a set to track unique lines
#    unique_lines = set()
#    # List to store the result
#    result = []
#    for line in lines:
#        if line not in unique_lines:
#            unique_lines.add(line)
#            result.append(line)
#    print("len of uniq set is ", len(unique_lines))
#    # Join the result list into a single string with newline characters
#    return '\n'.join(result)

def get_list_from_str(input_str):
    return_list = input_str.split('\n')
    return return_list


with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

#output_text = remove_duplicate_lines(content)

all_list  = get_list_from_str(content)
#uniq_list = get_list_from_str(output_text)

call_count = {}
for call in all_list:
    if call in call_count:
        call_count[call] += 1
    else:
        call_count[call] = 1

print("all_list len is ", len(all_list))
#print("uniq_list len is ", len(uniq_list))
print("len of call_count is", len(call_count))

#with open('output.json', 'w', encoding='utf-8') as file:
#    json.dump(call_count, file, ensure_ascii=False, indent=4)

df = pd.DataFrame.from_dict(call_count, orient='index').reset_index()
df.columns = ['hipblaslt-bench', 'call_count']
df_sorted = df.sort_values(by='call_count', ascending=False)
print(df_sorted)

df_first_1000 = df_sorted.head(1000)

#sorted_result = []
#for index, row in df_first_1000.iterrows():
#    sorted_result.append(row['Key'])
#
#out_str = '\n'.join(sorted_result)

#output_txt_name= output_name + '.txt'
#with open(output_txt_name , 'w', encoding='utf-8') as file:
#    file.write(out_str)
#print(output_text)

output_file_path = output_name + '.csv'
df_first_1000.to_csv(output_file_path, index=False, encoding='utf-8')

row_count = df.shape[0]
print(" unique blaslt call amount is ", row_count)
#with open('output.txt', 'w', encoding='utf-8') as file:
#    file.write(output_text)
#print(output_text)
