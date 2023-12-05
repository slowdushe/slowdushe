import csv

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            print(f"Fayl topilmadi: {self.file_path}")
            return None

def main():
   
    file_reader = FileReader("descriptions.csv") 

    
    data = file_reader.read_data()

    if data:
       
        csv_file_path = "output.csv" 
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["name", "price", "description"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

         
            writer.writeheader()

            
            for row in data:
                writer.writerow(row)

        print(f"Ma'lumotlar CSV fayliga saqlandi: {csv_file_path}")

if __name__ == "__main__":
    main()
