meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("Apa yang harus kita lakukan jika kata itu ditemukan?")
else:
    print("Apa yang harus kita lakukan jika kata itu tidak ditemukan?")
