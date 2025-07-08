import json
from datetime import datetime

TIME = {
    "아침": ("09:00", "11:59"),
    "점심": ("12:00", "16:59"),
    "저녁": ("17:00", "21:00")
}

class User:
    def __init__(self, user_id):
        self.user = user_id


class MenuTime:
    def __init__(self, label, menus):
        self.label = label
        self.start_time, self.end_time = TIME[label]
        self.menus = menus

    def now_in_range(self):
        now = datetime.now().time()
        start = datetime.strptime(self.start_time, "%H:%M").time()
        end = datetime.strptime(self.end_time, "%H:%M").time()
        return start <= now <= end


class Restaurant:
    def __init__(self, restaurant_name, menu_dt):
        self.restaurant_name = restaurant_name
        self.menus = [
            MenuTime(label, items)
            for label, items in menu_dt.items()
            if label in TIME
        ]

    def select_menu(self):
        for selected in self.menus:
            if selected.now_in_range():
                return selected
        return None


class MainService:
    def __init__(self, json_path='restaurant.json'):
        self.restaurants = self._load_restaurants(json_path)

    def _load_restaurants(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Restaurant(restaurant_name, menus) for restaurant_name, menus in data.items()]

    def run(self):
        user_id = input("아이디를 입력하세요: ")
        print()
        user = User(user_id)
        print("로그인되었습니다.")
        print()

        for idx, restaurant in enumerate(self.restaurants, 1):
            print(f"{idx}. {restaurant.restaurant_name}")

        while True:
            try:
                selected_restaurant = int(input("식당 번호를 입력하세요: ")) - 1
                if 0 <= selected_restaurant < len(self.restaurants):
                    restaurant = self.restaurants[selected_restaurant]
                    break
                else:
                    print("잘못된 번호입니다. 다시 입력해주세요.")
                    print()
            except ValueError:
                print("번호로 입력해주세요.")
                print()

        menu_list = restaurant.select_menu()
        if not menu_list:
            print("현재 시간에는 주문 가능한 메뉴가 없습니다.")
            return

        print(f"\n{menu_list.label} 메뉴")
        for i, (item, price) in enumerate(menu_list.menus.items(), 1):
            print(f"{i}. {item} - {price} 원")

        while True:
            try:
                selected_menu = int(input("주문할 메뉴 번호를 선택하세요: ")) - 1
                if 0 <= selected_menu < len(menu_list.menus):
                    menu_name = list(menu_list.menus.keys())[selected_menu]
                    price = menu_list.menus[menu_name]
                    break
                else:
                    print("잘못된 번호입니다. 다시 입력해주세요.")
                    print()
            except ValueError:
                print("번호로 입력해주세요.")
                print()

        print(f"\n{price}원이 결제되었습니다!")


if __name__ == '__main__':
    MainService().run()
