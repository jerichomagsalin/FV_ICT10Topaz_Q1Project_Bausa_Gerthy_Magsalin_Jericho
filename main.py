from pyscript import display

# Python functions need to be used to generate the Receipt and to generate the SKU.

def initial_order (e):
    document.getElementById("initialorder").innerHTML = ""

    popsicle = float(document.getElementById('popsicle').value)
    c_juice = float(document.getElementById('c_juice').value)
    m_shake = float(document.getElementById('m_shake').value)
    hc_sandwich = float(document.getElementById('hc_sandwich').value)
    hotdog = float(document.getElementById('hotdog').value)

    subtotal = popsicle + c_juice + m_shake + hc_sandwich + hotdog

    vat = subtotal * 0.12
    
    total = subtotal + vat

    document.getElementById("initialorder").innerHTML = total
    display(subtotal, target = "initialorder")
   
    
def create_sku(e):
    document.getElementById("cr_sku").innerHTML = ""


    
