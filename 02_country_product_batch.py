plc = "037-00901-00027"
print("Product Lot Number: ", plc)
cc = plc[:3]
pc = plc[4:9]
bn = plc[-5:]
print("Country Code: ", cc)
print("Product Code: ", pc)
print("Batch Number: ", bn)
