# Create an empty list to store the vegetables
vegetables = []

# Function to add vegetables to the list
def add_vegetable():
    while True:
        vegetable = input("Masukkan nama sayuran (ketik 'stop' untuk berhenti): ")
        if vegetable.lower() == 'stop':
            break
        vegetables.append(vegetable)

# Function to search for a vegetable in the list
def search_vegetable():
    search_term = input("Masukkan nama sayuran yang ingin dicari: ")
    if search_term in vegetables:
        print(f"Sayuran '{search_term}' ditemukan!")
    else:
        print(f"Sayuran '{search_term}' tidak ditemukan.")

# Main program
print("Program Pencarian Sayuran")
print("-------------------------")

while True:
    print("1. Tambahkan sayuran")
    print("2. Cari sayuran")
    print("3. Keluar")
    choice = input("Pilih opsi: ")

    if choice == '1':
        add_vegetable()
    elif choice == '2':
        search_vegetable()
    elif choice == '3':
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")