from pyscript import display, document
# crucial for python connection

# Python functions need to be used to generate the Receipt and to generate the SKU.

popsicle = 50 
c_juice = 100
m_shake = 75
hc_sandwich = 120
hotdog = 100

def initial_order (e):
    document.getElementById("subtotal").innerHTML = ""
    document.getElementById("vat").innerHTML = ""
    document.getElementById("total").innerHTML = ""

    # subtotal = float((popsicle * document.getElementById('popsicle').value)) + float((c_juice * document.getElementById('c_juice').value)) + float((m_shake * document.getElementById('m_shake').value)) + float((hc_sandwich * document.getElementById('hc_sandwich').value)) + float((hotdog * document.getElementById('hotdog').value))

    subtotal = (popsicle * float(document.getElementById('popsicle').value)) + (c_juice * float(document.getElementById('c_juice').value)) + (m_shake * float(document.getElementById('m_shake').value)) + (hc_sandwich * float(document.getElementById('hc_sandwich').value)) + (hotdog * float(document.getElementById('hotdog').value))

    vat = subtotal * 0.12
        
    total = subtotal + vat

    display(subtotal, target = "subtotal")
    display(vat, target = "vat")
    display(total, target = "total")
   
    
def create_sku(e):
    document.getElementById("sku").innerHTML = ""
    # document.getElementById("grouplabel").innerHTML = ""
    
    sample = document.getElementById('sample').value
    productname = document.getElementById('productname').value
    productnumber = document.getElementById('productnumber').value

    sku_value = sample + "-" + productname[0:4].upper() + "-" + str(productnumber)
    # groupvalue = "|" + document.getElementById('sample').id + ", " + sample + ", " + sample + "|"

    # display(groupvalue, target = "grouplabel")
    display(sku_value, target = "sku")

    
