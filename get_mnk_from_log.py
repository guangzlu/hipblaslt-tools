file_name = "model3-hipblaslt-bench-top100.txt" 

log_list = []
with open(file_name, 'r') as file:
    for line in file:
        log_list.append(line.strip())

NN_list = []
NT_list = []
TN_list = []
TT_list = []

for line in log_list:
    line_list = line.split(" ")

    m = line_list[4]
    n = line_list[6]
    k = line_list[8]

    batch_count = line_list[36]

    if( "--transA N --transB N" in line ):
        NN_list.append([m,n,batch_count,k])
    elif( "--transA N --transB T" in line ):
        NT_list.append([m,n,batch_count,k])
    elif( "--transA T --transB N" in line ):
        TN_list.append([m,n,batch_count,k])
    elif( "--transA T --transB T" in line ):
        TN_list.append([m,n,batch_count,k])

    #print ("- Exact: [ ", m, " , " , n , " , " , batch_count, "," , k , "]" )

print("NN list :")
for size in NN_list:
    print ("- Exact: [ ", size[0], " , " , size[1] , " , " , size[2], "," , size[3] , "]" )

print("NT list :")
for size in NT_list:
    print ("- Exact: [ ", size[0], " , " , size[1] , " , " , size[2], "," , size[3] , "]" )

print("TN list :")
for size in TN_list:
    print ("- Exact: [ ", size[0], " , " , size[1] , " , " , size[2], "," , size[3] , "]" )

print("TT list :")
for size in TN_list:
    print ("- Exact: [ ", size[0], " , " , size[1] , " , " , size[2], "," , size[3] , "]" )








