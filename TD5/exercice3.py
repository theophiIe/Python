nameFile = raw_input("Le nom du fichier : ")

f = open(nameFile, "r")
seq = ""
ligne = f.readline() 

while(ligne != "") :
		seq = seq + ligne[:len(ligne)-1]
		ligne = f.readline()

f.close()

print "Choix 1 : transformation de la sequence en son transcrit et sauvegarde dans un fichier\nChoix 2: transformation de la sequence en son inverse complementaire et sauvegarde dans un fichier"

while(1) : 
	choix = raw_input("Quelle choix voulez-vous faire (1/2): ")
	if choix == "1" or choix == "2" :
		break

if choix == "1" :
	seq = seq.replace("T", "U")
	h = open("SeqtransExo3.txt", "w")
	h.write(seq)
	h.close()
	
elif choix == "2" :
	brinCmpl = ""
	i = len(seq)

	while i != 0:
		if seq[i-1] == "A":
			brinCmpl = brinCmpl + "T"
		
		if seq[i-1] == "T":
			brinCmpl = brinCmpl + "A"
		
		if seq[i-1] == "C":
			brinCmpl = brinCmpl + "G"
		
		if seq[i-1] == "G":
			brinCmpl = brinCmpl + "C"
	
		i = i-1
	
	g = open("SeqInvCompExo3.txt", "w")
	g.write(brinCmpl)
	g.close()
