from pyscript import display, document
# crucial for python connection

# Python functions need to be used to generate the Receipt and to generate the SKU.

def initial_order (e):
    document.getElementById("initialorder").innerHTML = ""

    popsicle = float(document.getElementById('popsicle').value)
    c_juice = float(document.getElementById('c_juice').value)
    m_shake = float(document.getElementById('m_shake').value)
    hc_sandwich = float(document.getElementById('hc_sandwich').value)
    hotdog = float(document.getElementById('hotdog').value)

    # affirming checkbox value (issue)
    # problem, the background shifts when create order is pressed

    # subtotal = (popsicle * popsicle.checked) + (c_juice * c_juice.checked) + (m_shake * m_shake.checked) +  (hc_sandwich * hc_sandwich.checked) + (hotdog * hotdog.checked)

    subtotal = popsicle # for now

    vat = subtotal * 0.12
    
    total = subtotal + vat

    document.getElementById("initialorder").innerHTML = total
    display(subtotal, target = "initialorder")
   
    
def create_sku(e):
    document.getElementById("create_sku").innerHTML = ""


    
