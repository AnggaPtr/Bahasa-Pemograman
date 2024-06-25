def binary_search(arr,x):
    
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        
        if arr[mid] < x:
            low = mid + 1
            
            
        elif arr[mid] > x:
            high = mid - 1
            
            
        else:
            return mid
        
        
    return - 1

def main():
    
    arr = list(map(int,input("Masukan Daftar Elemen Yang SUdah Terurut (Pisahkan Dengan Spasi): ").split()))
    
    
    x = int(input("Masukan Elemen Yang Akan Dicari: "))
    
    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen Ditemukan Pada Indeks {result}")
    else:
        print("Elemen Tidak Ditemukan Dalam Dafatr.")
    
    
if __name__ == "__main__":
    main()    