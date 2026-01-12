class Mahsulot:
    def __init__(self, nomi, narxi, soni):
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni

    def umumiy_narx(self):
        return self.narxi * self.soni


def chek_chiqarish(mahsulotlar):
    jami = 0
    print("Chek:")
    print("-" * 30)
    for m in mahsulotlar:
        summa = m.umumiy_narx()
        jami += summa
        print(f"{m.nomi} | {m.soni} dona | {summa} so‘m")
    print("-" * 30)
    print(f"Jami to‘lov: {jami} so‘m")


m1 = Mahsulot("Non", 3000, 2)
m2 = Mahsulot("Sut", 8000, 1)
m3 = Mahsulot("Shakar", 10000, 3)

mahsulotlar = [m1, m2, m3]
chek_chiqarish(mahsulotlar)
