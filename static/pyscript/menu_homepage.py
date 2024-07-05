from pyscript import document, window, when
from pyweb import pydom
from js import console

main_page = pydom['#consumer-menu-page'][0]
if not main_page:
    main_page.show_me()

@when('click', 'li')
def show_category(event):
    target_id = event.target.closest('li').getAttribute('id')
    if not target_id:
        return
    caps = target_id.split('-')[0].upper()
    target_element = pydom[f"#id_{caps}"][0]
    element_class = target_element.classes
    if 'hidden' in element_class:
        target_element.remove_class('hidden')
        target_element.add_class(['block', 'animate-opacity'])
        tab_element_a = pydom[f'#{target_id}'][0].find('a')[0]
        tab_element_a.remove_class(['hover:text-gray-600', 'hover:border-gray-300', 'dark:hover:text-gray-300', 'border-transparent'])
        tab_element_a.add_class(['text-blue-600', 'border-blue-600', 'dark:text-blue-500', 'dark:border-blue-500', 'active'])
        
        tab_element_svg = pydom[f'#{target_id}'][0].find('svg')[0]
        tab_element_svg.remove_class(['text-gray-400', 'group-hover:text-gray-500', 'dark:text-gray-500', 'dark:group-hover:text-gray-300'])
        tab_element_svg.add_class(['text-blue-600', 'dark:text-blue-500'])
        
        tab_element_svg._js.setAttribute('fill', 'currentColor')

    for e in pydom['#consumer-menu-page'][0].children:
        if not f"id_{caps}" == e.id and e._js.tagName == 'DIV':
            if 'block' in pydom[f'#{e.id}'][0].classes:
                
                pydom[f'#{e.id}'][0].remove_class(['block', 'animate-opacity'])
                pydom[f'#{e.id}'][0].add_class('hidden')

                tab_id = f"#{e.id.split('_')[1].lower()}-tab"
                tab_element_a = pydom[tab_id][0].find('a')[0]
                tab_element_a.remove_class(['text-blue-600', 'border-blue-600', 'dark:text-blue-500', 'dark:border-blue-500', 'active'])
                tab_element_a.add_class(['hover:text-gray-600', 'hover:border-gray-300', 'dark:hover:text-gray-300', 'border-transparent'])
                
                tab_element_svg = pydom[tab_id][0].find('svg')[0]
                tab_element_svg.remove_class(['text-blue-600', 'dark:text-blue-500'])
                tab_element_svg.add_class(['text-gray-400', 'group-hover:text-gray-500', 'dark:text-gray-500', 'dark:group-hover:text-gray-300'])
                
                tab_element_svg._js.setAttribute('fill', 'currentColor')



@when('click', 'li')
def show_sub_category(event):
    subcat = event.target.innerHTML
    subcat_els = pydom['h1']
    [s.parent._js.scrollIntoView({ 'behavior': 'smooth' }) for s in subcat_els if subcat == s.html]
