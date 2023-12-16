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