import json
from pyweb import pydom
import time

from pyscript import document, window, when

def get_subcats():
    food_subcat = list(eval(pydom['#food_subcat'][0].html))
    drinks_subcat = list(eval(pydom['#drinks_subcat'][0].html))
    dessert_subcat = list(eval(pydom['#dessert_subcat'][0].html))
    return food_subcat, drinks_subcat, dessert_subcat


@when('change', '#id_category')
def subcat_condition():
    if not pydom['#id_category'][0].options[0].value:
        pydom['#id_category'][0].options.remove(0)
    
    food_subcat, drinks_subcat, dessert_subcat = get_subcats()

    subcat = pydom['#id_sub_category'][0]
    subcat.options.clear()
    category = pydom['#id_category'][0].options.selected.value
    if category == 'DRINKS':
        [subcat.options.add(value=value, html=text) for value, text in drinks_subcat]
    elif category == 'FOOD':
        [subcat.options.add(value=value, html=text) for value, text in food_subcat]
    elif category == 'DESSERT':
        [subcat.options.add(value=value, html=text) for value, text in dessert_subcat]
    else:
        subcat.options.add(value="Hookah", html="Hookah")
        
    select2 = pydom['.select2']
    # i=0
    # while not select2 and i < 5:
    #     time.sleep(1)
    #     i += 1
    if select2:
        select2 = select2[0]
    
        classes = "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
        
        if not classes in select2.classes:
            select2.add_class(classes.split())
    
window.onload = subcat_condition()