order_html = """
<div class="flex flex-col justify-between gap-1 max-w-xs text-center bg-gradient-to-bl from-orange-300 to-orange-100 border border-spacing-1 border-blue-300 rounded-md py-1 my-2">
    <div class="flex flex-col justify-evenly text-sm font-normal font-mono">
        <div class="">Table Number : <span class="text-lg font-semibold font-sans bg-teal-300 rounded-md px-2 mx-2 text-red-950 border border-blue-700 table-number">{{order.table_num}}</span></div>
        <div class="">Order ID : <span class="text-md font-semibold px-5 font-sans">{{order.order_id}}</span></div>
        <div class="">Order placed by : <span class="text-md font-semibold font-sans">{{order.employee.full_name}}</span></div>
        <div class="">Ordered Time : <span class="text-md font-semibold font-sans">{{order.order_placed|timesince}} ago</span></div>
    </div>
    <div class="ordered-items-all font-serif">
        <div class="food-ordered-items-all">
            <p class="font-mono font-bold text-red-600">Food items ordered</p>
            {% for item in order.orderitem_set.all %}
            {% if item.product.category == 'FOOD' %}
            <div class="flex flex-col justify-between">
                <div class="flex justify-between text-center px-2 mx-4">
                    <p>{{item.product.title}}</p>
                    <p class="font-bold">{{item.quantity}}</p>
                </div>
                <div>
                    <p>{{item.preference}}</p>
                </div>
            </div>
            {% endif %}
            {% endfor %}
        </div>
        <div class="food-ordered-items-all">
            <p class="font-mono font-bold text-red-600">Drinks items ordered</p>
            {% for item in order.orderitem_set.all %}
            {% if item.product.category == 'DRINKS' %}
            <div class="flex flex-col justify-between font-serif">
                <div class="flex justify-between text-center px-2 mx-4">
                    <p>{{item.product.title}}</p>
                    <p class="font-bold">{{item.quantity}}</p>
                </div>
                <div>
                    <p>{{item.preference}}</p>
                </div>
            </div>
            {% endif %}
            {% endfor %}
        </div>
        <div class="food-ordered-items-all">
            <p class="font-mono font-bold text-red-600">Hookah items ordered</p>
            {% for item in order.orderitem_set.all %}
            {% if item.product.category == 'HOOKAH' %}
            <div class="flex flex-col justify-between font-serif">
                <div class="flex justify-between text-center px-2 mx-4">
                    <p>{{item.product.title}}</p>
                    <p class="font-bold">{{item.quantity}}</p>
                </div>
                <div>
                    <p>{{item.preference}}</p>
                </div>
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
    <div class="inline-flex rounded-md shadow-sm justify-center gap-2" role="group">
        <button class="relative inline-flex items-center justify-center p-0.5 px-1 mb-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-red-200 via-red-300 to-yellow-200 group-hover:from-red-200 group-hover:via-red-300 group-hover:to-yellow-200 dark:text-white dark:hover:text-gray-900 focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 order-prepared">
        <span class="relative px-2 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
        Order Prepared
        </span>
        </button>
        <button class="relative inline-flex items-center justify-center p-0.5 px-1 mb-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-red-200 via-red-300 to-yellow-200 group-hover:from-red-200 group-hover:via-red-300 group-hover:to-yellow-200 dark:text-white dark:hover:text-gray-900 focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 order-completed">
        <span class="relative px-2 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
        Order Completed
        </span>
        </button>
    </div>
</div>
"""


edit_menu_form = """
{% load add_class %}
            <input type="hidden" name="csrfmiddlewaretoken" value="{{csrf_token}}">
            {{ form.media }}
            <div class="w-full">
                <div class="mx-2 items-center w-full">
                    {{form.title|add_class:"text-center text-[10px] lg:text-base rounded-md py-1 w-full"}}
                </div>
                <div class="text-center">
                    <img class="p-2 rounded-t-lg w-20 lg:w-40 h-20 lg:h-40 object-cover inline-block" src="{{form.instance.dish_image.url}}" alt="product image" />
                    {{form.dish_image|add_class:"text-[8px] lg:text-sm w-full text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"}}
                </div>
                <div class="text-[8px] lg:text-sm mt-1">
                    {{form.description|add_class:"h-12 w-full lg:h-24 text-[8px] lg:text-sm"}}
                </div>
                <div class="flex-col justify-center border-t-4 pt-2 mt-2 font-medium text-[8px] lg:text-sm w-full">
                    <div class="grid grid-cols-9 justify-between text-[8px] lg:text-xs items-center">
                        <p class="col-span-3 text-xs">Price </p>
                        <p class="col-span-1 text-center mt-1">:</p>
                        {{form.price|add_class:"rounded-md text-[8px] lg:text-xs my-1 col-span-5 w-auto"}}
                        <p class="col-span-3 text-xs">Category </p>
                        <p class="col-span-1 text-center mt-1">:</p>
                        {{form.category|add_class:"rounded-md text-[8px] lg:text-xs col-span-5 mb-1 w-auto"}}
                        <p class="col-span-3 text-xs">Sub Category </p>
                        <p class="col-span-1 text-center mt-1">:</p>
                        {{form.sub_category|add_class:"rounded-md text-[8px] lg:text-xs col-span-5 mb-1 w-auto"}}
                        <p class="col-span-3 text-xs ">Is Non-veg </p>
                        <p class="col-span-1 text-center mt-1">:</p>
                        {{form.is_non_veg|add_class:"rounded-md text-[8px] lg:text-xs col-span-5 mb-1 w-auto"}}
                        <p class="hidden">col-span-5</p>
                    </div>
                </div>
                <div class="pt-4 text-center">
                    <button class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-[8px] lg:text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-cyan-500 to-blue-500 group-hover:from-cyan-500 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-cyan-200 dark:focus:ring-cyan-800">
                        <span class="relative px-5 py-1 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0 save" id="save-{{slug_title}}">
                        Save
                        </span>
                    </button>   
                </div>
            </div>
            """