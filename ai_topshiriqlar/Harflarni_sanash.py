# Harflarni sanash
# Kurs: Dasturlash / IT
# Mavzu: String metodlari — 1: lower, upper, strip, title
# Ball: 100
# Aziz Academy — AI Topshiriq

s = input().strip()

hisob = {}

for harf in s:
    hisob[harf] = hisob.get(harf, 0) + 1 
    
eng_kop = max(hisob.values())

harflar = []
for harf in hisob:
    if hisob[harf] == eng_kop:
        harflar.append(harf)
        
harf = sorted(harflar)[0]

print(harf)
print(eng_kop)