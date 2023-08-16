# argument, parameters

def full_name(firstname,lastname):   # ==> parameters(tanımlarken parameters)
    return f"Your name is {firstname} {lastname}."

sonuc = full_name("Bartu","Akdoğan")  # ==> arguments(okuturken arguments)
sonuc = full_name(lastname="Akdoğan",firstname="Bartu")
print(sonuc)    