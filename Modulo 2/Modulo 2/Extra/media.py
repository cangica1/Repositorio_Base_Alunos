bimestre_1 = float(input("digite a nota do 1 bimestre:"))
bimestre_2 = float(input("digite a nota do seu 2 bimestre:"))
bimestre_3 = float(input("digite a nota do 3 bimestre:"))
bimestre_4 = float(input("digite a nota do 4 bimestre:"))

resultado = bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4
media = resultado / 4

if media >= 7.0:
    print(f"media: {media}, situação: aprovado✅, parabéns continue assim")
elif media >= 5.0 and media < 7.0:
    print(f"media:{media}, situação: recuperação 🚨, tente colar direito da prxoima vez")

else:
    print(f"media:{media}, situação: reprovado❌, te vejo ano que vem de volta no prézinho")