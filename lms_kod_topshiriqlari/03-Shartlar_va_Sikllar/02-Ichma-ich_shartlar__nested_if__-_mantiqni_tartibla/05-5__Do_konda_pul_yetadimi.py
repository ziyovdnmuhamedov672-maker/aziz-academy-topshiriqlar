pul = int(input())
narx = int(input())
if pul >= narx:
    if pul == narx:
        print("Aniq yetdi")
    else:
        print("Qaytim:",pul - narx)
else:
    print("Pul yetmaydi")