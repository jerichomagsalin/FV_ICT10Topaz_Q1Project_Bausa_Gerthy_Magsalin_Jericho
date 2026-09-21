from pyscript import document, display

# def adding_numbers(e):
#   document.getElementById("output1").innerHTML = "" # clears previous output
#   num1 = float(document.getElementById('input1').value) # get 1st input
#   num2 = float(document.getElementById('input2').value) # get 2nd input
#   result = num1 + num2 # use operator to compute
#   display(result, target = "output1") #display output in div


# def create_order(e):
#   document.getElementById("output2").innerHTML = "" # clears previous output
#   prod1 = document.getElementById("item1")
    # Calculate
#   subtotal = float(prod1.value) * prod1.checked
#   size = document.querySelector('input[name="size"]:checked')
#   size_price = float(size.value)
#   grandtotal = subtotal + size_price #add current and upsize price
#   display(subtotal, size_price, target="output2")

# def place_order(e):
#   document.getElementById("output3").innerHTML = "" # clears previous output
#   coffee = document.getElementById("coffee")
#   coffee_price = float(coffee.value)
#   display(coffee_price, target="output3")

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


    
