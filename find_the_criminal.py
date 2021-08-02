sample = ['GTA','GGG','CAC']
#the function will take in a file, read it,add the file's contents to an empty string and return the updated string.
def read_dna(dna_file):
  dna_data=""
  with open(dna_file, "r") as f: #open dna_file in read-only mode
    for line in f:
      dna_data += line
  return dna_data

# next we need a method that will take a string, create a list of codons from that string, and return the list.
def dna_codons(dna):
  codons=[]
  for i in range (0,len(dna)-3+1,3):
    pattern=dna[i:i+3]
    codons.append(pattern)
  return codons

  #next step is to create a method that will iterare through both the sample and a suspect's

def match_dna(dna):
  matches=0
  for codon in dna:
    if codon in sample:
      matches+=1
  return matches

def is_criminal(dna_sample):
  dna_data=read_dna(dna_sample)
  codons=dna_codons(dna_data)
  num_matches=match_dna(codons)
  if num_matches >=3:
    print "the number matched is: %s, the investigation should continue." % num_matches
  else:
    print" the number matched is: %s, the suspect can be freed" % num_matches

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
