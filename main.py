# python3

def parallel_processing(n, m, data):
    output = []
    arr = [0]*n
    time = 0
    i = 0
    for elements in data:
        i = 0
        while i != n:
            if arr[i] == time:
                arr[i] = arr[i] + elements
                output.append([i,time])
                break
            elif i == n-1: 
                time += 1
                i = 0
            else:
                i += 1
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    input_string = input("Enter thread and job count: ")
    n,m = input_string.split()
    n = int(n)
    m = int(m)
    data = list(map(int, input().split()))
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
          print(i, j)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

    
