import csv
import os
import subprocess
from tqdm import tqdm

file_name = "hipblaslt-bench-top100.txt"
output = "result.csv"

def read_csv_to_list(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = [str(row) for row in reader]
    return result

csv_data = read_csv_to_list(file_name)

with open(output, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    total_index = len(csv_data)
    progress_bar = tqdm(total=total_index)

    for row in csv_data:
        # m = row[0]
        # n = row[1]
        # k = row[2]

        # /root/hipBLASLt/build/release/clients/staging/hipblaslt-bench 
        # -f matmul --transA N --transB N 
        # -m 1 -n 10 -k 256 
        # --alpha 1 --a_type f16_r --lda 1 --b_type f16_r 
        # --ldb 256 --beta 0 --c_type f16_r --ldc 1 
        # --d_type f16_r --ldd 1 --compute_type f32_r

        # /root/rocblas/build/release/clients/staging/rocblas-bench 
        # -f gemm_ex --transposeA N --transposeB N -m 1 -n 10 -k 256 
        # --alpha 1 --a_type f16_r --lda 1 --b_type f16_r 
        # --ldb 256 --beta 0 --c_type f16_r --ldc 1 
        # --d_type f16_r --ldd 1 --compute_type f32_r 
        # --algo 0 --solution_index 0 --flags 0

        command_context = row.split(' ',1)[1]

        print("0", command_context)
        command_context = command_context.split(' ')[:-1]

        command_context = [item for item in command_context if item != ""]

        print("1", command_context)

        command  = ["/root/hipBLASLt-yangwen/build/release/clients/staging/hipblaslt-bench"]
        command += command_context
        # command += ["-f","matmul","--transA","N","--transB","N"]
        # command += ["-m",str(m)]
        # command += ["-n",str(n)]
        # command += ["-k",str(k)]
        # command += ["--alpha","1","--a_type","f16_r","--lda","1","--b_type","f16_r"]
        # command += ["--ldb","256","--beta","0","--c_type","f16_r","--ldc","1"]
        # command += ["--d_type","f16_r","--ldd","1","--compute_type","f32_r"]

        #command  = ["/root/rocblas/build/release/clients/staging/rocblas-bench"]
        #command += ["-f","gemm_ex","--transposeA","N","--transposeB","N"]
        #command += ["-m",str(m)]
        #command += ["-n",str(n)]
        #command += ["-k",str(k)]
        #command += ["--alpha","1","--a_type","f16_r","--lda","1","--b_type","f16_r"]
        #command += ["--ldb","256","--beta","0","--c_type","f16_r","--ldc","1"]
        #command += ["--d_type","f16_r","--ldd","1","--compute_type","f32_r"]
        #command += ["--algo", "0","--solution_index","0"," --flags"," 0"]


        #result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #result_stdout = result.stdout
        #result_solu = result_stdout.split(b"\n")[-2]
        #result_time = result_solu.split(b",")[-1]
        #result_time = result_time.decode('utf-8')
        #cur_row = [m , n, k, float(result_time)]
        #writer.writerow(cur_row)

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result)
        result_stdout = result.stdout
        result_solu = result_stdout.split(b"\n")[-2]
        result_time = result_solu.split(b",")[-1]
        result_time = result_time.decode('utf-8')
        cur_row = [row, float(result_time)]
        writer.writerow(cur_row)

        progress_bar.update(1)

    progress_bar.close()
