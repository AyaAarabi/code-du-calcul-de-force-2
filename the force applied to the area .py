P=float(input("entrez la valeur de pression :"))
A=float(input("entrez la valeur de surface : "))
try :
    F= P*A
    print("la valeur de la force est appliquée sur la surface :" ,F,"N")
except:
    print("la valeur de pression ou/et de surface que vous avez donné est inccorect")

