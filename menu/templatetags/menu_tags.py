from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import MenuItem
from ..utils import get_selected_item_id_list, get_child_items

register = template.Library()


@register.inclusion_tag('menu/includes/menu.html', takes_context=True, name='draw_menu')
def draw_menu(context, menu):
    try:
        # items = MenuItem.objects.filter(menu__title=menu)
        items = MenuItem.objects.filter(menu__slug=menu)

        items_values = items.values()

        root_item = [item for item in items_values.filter(parent=None)]

        selected_item_url = context['item']
        selected_item = items.get(url=selected_item_url)

        selected_item_id_list = get_selected_item_id_list(selected_item, root_item, selected_item.id)

        for item in root_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)

        result_dict = {'items': root_item}

    except (KeyError, ObjectDoesNotExist):
        result_dict = {
            'items': [
                # item for item in MenuItem.objects.filter(menu__title=menu, parent=None).values()
                item for item in MenuItem.objects.filter(menu__slug=menu, parent=None).values()
            ]
        }

    result_dict['menu'] = menu

    return result_dict
