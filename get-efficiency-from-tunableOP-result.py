import re

file_name = "tunableop_results0.csv" 

line_list = []
with open(file_name, 'r') as file:
    for line in file:
        line_list.append(line.strip())

result_list = line_list[5:]
tflops_result_list = []

for single_str in result_list:
    if "GemmStridedBatchedTunableOp_Half" in single_str:
        if "Rocblas" in single_str:
            library = "Rocblas"
        elif "Hipblaslt" in single_str:
            library = "Hipblaslt"
        else:
            library = "unknown"
        single_str_list = re.split('_|,', single_str)
        m = int(single_str_list[4])
        n = int(single_str_list[5])
        k = int(single_str_list[6])
        batch_size = int(single_str_list[8])
        run_time = round(float(single_str_list[-1]), 6)
        tflops = m * n * k * 2 * batch_size
        TFlopS = tflops / run_time / 1000000000
        print("library ", library , ", m ", m, ", n ", n, ", k ", k, ", batch ", batch_size, ", time ", run_time* 1000 , ", TFlopS ", TFlopS)

    if "GemmTunableOp_Half" in single_str:
        #single_str = "GemmTunableOp_Half_TN,tn_1280_1_1280,Gemm_Rocblas_621288271,0.0123716"
        if "Rocblas" in single_str:
            library = "Rocblas"
        elif "Hipblaslt" in single_str:
            library = "Hipblaslt"
        else:
            library = "unknown"
        single_str_list = re.split('_|,', single_str)
        m = int(single_str_list[4])
        n = int(single_str_list[5])
        k = int(single_str_list[6])
        batch_size = 1
        run_time = round(float(single_str_list[-1]), 6)
        tflops = m * n * k * 2
        TFlopS = tflops / run_time / 1000000000
        print("library ", library , ", m ", m, ", n ", n, ", k ", k, ", batch ", batch_size, ", time ", run_time* 1000 , ", TFlopS ", TFlopS)



