import sys
import csv

checksum = False

ingredients = {
	"ayam_paha_fillet":[0,"gram"],
	"ayam_utuh_boiler":[0,"gram"],
	"kaki_ayam":[0,"gram"],
	"cumi":[0,"gram"],
	"udang_kulit_pancet_31_40":[0,"gram"],
	"udang_kupas_71_90":[0,"gram"],
	"kepiting_soka":[0,"gram"],
	"sapi":[0,"gram"],
	"ayam_kampung":[0,"ekor"],
	"gurame":[0,"ekor"],
	"kerapu":[0,"ons"],
}

def main():
	parse_csv()
	print("")
	output()
	print("\nALWAYS CROSS-CHECK THE QUANTITY SOLD ON THE RAW FILE AND THE ONE DISPLAYED ABOVE.\n")
	detect_error()

def parse_csv():
	with open(sys.argv[1]) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    for row in csv_reader:
	    	if len(row) < 14:
	    		continue
	    	elif len(row) == 35 or len(row) == 46:
	    		print(row[1] + ": " + row[2])
	    		add_ingredient(row[1],row[2])
	    	else:
	    		print(row[13] + ": " + row[14])
	    		add_ingredient(row[13],row[14])

def detect_error():
	if checksum == True:
		print("WARNING: BUGS MAY BE PRESENT!")

def add_ingredient(product_id, quantity_sold):
	global checksum
	if (product_id.isdigit() == True) or (product_id == "STotal") or (product_id == "Bill  Discount") or (product_id == "GTotal") or (product_id == "Page 1 of ") or (product_id == "PLU / Item Category Report") or (product_id == "PLUNumber") or (product_id == "Name") or (product_id == "Sold") or (product_id == "%") or (product_id == "ItemSales") or (product_id == "TotDisc") or (product_id == "FOC") or (product_id == "Revenue") or (product_id == "Voids") or (product_id == "Rfnds") or (product_id == "DINE IN") or (product_id == "TAKE AWAY"):
		checksum = True
	if (quantity_sold.isdigit() == False) or (int(quantity_sold) == 0) or (int(quantity_sold) > 5000) or (len(str(quantity_sold)) > 5):
		checksum = True

	if product_id == "Lumpia Buah Udang":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 86)
	elif product_id == "Mun Tahu Udang":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 30)
	elif product_id == "Mapo Tahu":
		ingredients["sapi"][0] += (int(quantity_sold) * 45)
	elif product_id == "Sapo Tahu Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Omelet Udang":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
	elif product_id == "Tahu Homemade Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Tahu Homemade Udang":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 133)
	elif product_id == "Sapi Lada Hitam":
		ingredients["sapi"][0] += (int(quantity_sold) * 150)
	elif product_id == "Sapi Tumis Sichuan":
		ingredients["sapi"][0] += (int(quantity_sold) * 150)
	elif product_id == "Brokoli Sapi Sichuan":
		ingredients["sapi"][0] += (int(quantity_sold) * 45)
	elif product_id == "Buncis Sapi Sichuan":
		ingredients["sapi"][0] += (int(quantity_sold) * 45)
	elif product_id == "Ayam Pang Hkg 1 Ekor":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 1300)
	elif product_id == "Ayam Pang Hkg 1/2 E":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 650)
	elif product_id == "Ayam Pang Hkg 1/4 E":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 325)
	elif product_id == "Ayam Kampung 1 Ekor":
		ingredients["ayam_kampung"][0] += (int(quantity_sold) * 1)
	elif product_id == "Ayam Kampung 1/2 Ekr":
		ingredients["ayam_kampung"][0] += (int(quantity_sold) * 0.5)
	elif product_id == "Ayam Kmpung 1/4 Ekr":
		ingredients["ayam_kampung"][0] += (int(quantity_sold) * 0.25)
	elif product_id == "Ayam Goreng Terasi":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 350)
	elif product_id == "Ayam Saus Keju":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 300)
	elif product_id == "Ayam Kung Pao":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam Aneka Cabe":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 300)
	elif product_id == "Ayam Goreng Mentega":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 300)
	elif product_id == "Ayam Lada Garam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam Goreng Lemon":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam Kuluyuk":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam rambut emas":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam Thousand Island":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Ayam Telor Asin":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Sup Sapo Ikan Gurame":
		ingredients["gurame"][0] += (int(quantity_sold) * 0.5)
	elif product_id == "Gurame Bumbu Rujak":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Gurame Grg ala Thai":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Gurame Tahu Tausi":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Gurame Asam Manis":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Gurame Telor Asin":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Kerapu Grg HongKong":
		ingredients["kerapu"][0] += (int(quantity_sold) * 5.5)
	elif product_id == "Kerapu Grg ala Thai":
		ingredients["kerapu"][0] += (int(quantity_sold) * 5.5)
	elif product_id == "Gurame rambut emas":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Gurame Dua Rasa":
		ingredients["gurame"][0] += (int(quantity_sold) * 1)
	elif product_id == "Polo Pao Panggang":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 33)
	elif product_id == "Siew Mai Grg Tlr Pyh":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 7)
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 67)
	elif product_id == "Pangsit Udang Mayon":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 60)
	elif product_id == "Shanghai Kuo Tie":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 67)
	elif product_id == "Lumpia Udg KulitTahu":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 67)
	elif product_id == "Talas Goreng":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 10)
	elif product_id == "Bakpao Grg Shanghai":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 33)
	elif product_id == "PKT AYM GR MENTEGA":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 150)
	elif product_id == "PKT AYM KULUYUK":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT AYM KUNGPAO":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT AYM LADA GRM":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT AYM LEMON":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT AYM PANG HKG":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 325)
	elif product_id == "PKT CUMI GR TEPUNG":
		ingredients["cumi"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT CUMI LADA GRM":
		ingredients["cumi"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT OMELET UDG":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 28.5)
	elif product_id == "PKT SAPI LADA HITAM":
		ingredients["sapi"][0] += (int(quantity_sold) * 75)
	elif product_id == "PKT CAPCAY AYAM":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "PKT CAPCAY SEAFOOD":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Paket Ayam Terasi":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 175)
	elif product_id == "Paket Ayam T Island":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "Paket Ayam TelorAsin":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "Paket Cumi TelorAsin":
		ingredients["cumi"][0] += (int(quantity_sold) * 60)
	elif product_id == "Nasi GrKampung Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi Gr Kampung Pete":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi Gr Kmp Ikan Asn":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi Goreng XO Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi Grg XO Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Nasi Gr Belacan Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi Gr Blacan Sefod":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Mie Gr Kampung Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Mie Goreng XO Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Mie Grg XO Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Kwetiau Grg XO Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Kwetiau Grg XO Sefod":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Mie Kuah Wonton Udng":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 60)
	elif product_id == "Mie Kuah Aym Png Hkg":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 325)
	elif product_id == "Mie Gr kungpao ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Mie Gr kungpao Sfood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Nasi G tlr asin aym":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi G tlr asn sfood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Ifumie Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Nasi Grg Yang Chow":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 40)
	elif product_id == "Nasi Grg Keju Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "NasiGrg Keju Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Bihun Goreng Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Bihun Goreng Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Udang Grg Tlr Asin":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Grg Mayonnaise":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Lada Garam":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Goreng Mentega":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Goreng Gandum":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Saus Padang":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Kuluyuk":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Udang Rambut Emas":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Cumi Lada Garam":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Cumi Grg Tlr Asin":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Cumi Goreng Tepung":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Cumi rambut emas":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Cumi Saus Padang":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Paket Cumi S Padang":
		ingredients["cumi"][0] += (int(quantity_sold) * 60)
	elif product_id == "Hakau":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 37)
	elif product_id == "Tahu Steam Udang":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 50)
	elif product_id == "Siew Mai":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 7)
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 67)
	elif product_id == "Char Siew Pao":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 33)
	# elif product_id == "Kaki Ayam":
	# 	ingredients[""][0] += (int(quantity_sold) * )
	elif product_id == "Lo Mai Kai":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 67)
	elif product_id == "Pak Choy Dumplings":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 37)
	elif product_id == "Sapo Terong Sichuan":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 45)
	elif product_id == "Cap Cay Ayam":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "Cap Cay Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Kailan crspy cah aym":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 45)

	elif product_id == "Kerapu Grg Bmbu Kari":
		ingredients["kerapu"][0] += (int(quantity_sold) * 5.5)
	elif product_id == "Krp Macan Tim HK 1":
		ingredients["kerapu"][0] += (int(quantity_sold) * 1)
	elif product_id == "Krp Macan Tim Thai 1":
		ingredients["kerapu"][0] += (int(quantity_sold) * 1)
	elif product_id == "Kerapu tim bwng pth":
		ingredients["kerapu"][0] += (int(quantity_sold) * 1)
	elif product_id == "Udang Goreng Tepung":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Ayam Kacang Mns Pds":
		ingredients["ayam_utuh_boiler"][0] += (int(quantity_sold) * 300)
	elif product_id == "Mie Kuah Aym Kam Pek":
		ingredients["ayam_kampung"][0] += (int(quantity_sold) * 0.25)
	elif product_id == "Extra Wonton":
		ingredients["udang_kupas_71_90"][0] += (int(quantity_sold) * 20)
	# elif product_id == "Kepiting Soka T Asin":
	# 	ingredients[""][0] += (int(quantity_sold) * )
	# elif product_id == "Kepiting Soka M Abon":
	# 	ingredients[""][0] += (int(quantity_sold) * )
	# elif product_id == "Kep Soka Grg Tepung":
	# 	ingredients[""][0] += (int(quantity_sold) * )
	elif product_id == "Paket Ayam T Island":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 60)
	elif product_id == "Nasi G tlr asin aym":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 35)
	elif product_id == "Nasi G tlr asn sfood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Ayam remah roti":
		ingredients["ayam_paha_fillet"][0] += (int(quantity_sold) * 120)
	elif product_id == "Udang Remah Roti":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 200)
	elif product_id == "Cumi remah roti":
		ingredients["cumi"][0] += (int(quantity_sold) * 120)
	elif product_id == "Kailan Cah Sapi":
		ingredients["sapi"][0] += (int(quantity_sold) * 75)
	elif product_id == "Nasi Grg Kmp Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)
	elif product_id == "Mie Grg Kmp Seafood":
		ingredients["udang_kulit_pancet_31_40"][0] += (int(quantity_sold) * 57)
		ingredients["cumi"][0] += (int(quantity_sold) * 30)

def output():
	print("OUTPUT")
	for ingredient in ingredients.keys():
		print(ingredient + ": " + str(ingredients.get(ingredient)[0]) + " " + str(ingredients.get(ingredient)[1]))

if __name__ == "__main__":
	main()
