import random
import os
from enum import Enum
from typing import Dict, List, Optional, Tuple

class RoomType(Enum):
    COMBAT = "Боевая комната"
    REST = "Комната отдыха"
    TREASURE = "Комната с сундуком"

class ItemType(Enum):
    WEAPON = "Оружие"
    ARMOR = "Броня"
    POTION = "Зелье"
    GOLD = "Золото"
    ARTIFACT = "Артефакт"

class Race(Enum):
    HUMAN = "Человек"
    ELF = "Эльф"
    DWARF = "Дворф"
    HALFLING = "Полурослик"

class Item:
    def __init__(self, name: str, item_type: ItemType, value: int = 0, 
                 attack_bonus: int = 0, defense_bonus: int = 0, 
                 hp_bonus: int = 0, agility_bonus: int = 0):
        self.name = name
        self.type = item_type
        self.value = value  
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.hp_bonus = hp_bonus
        self.agility_bonus = agility_bonus
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type.value})"

class Character:
    def __init__(self, race: Race):
        self.race = race
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        self.skill_points = 0
        
        if race == Race.HUMAN:
            self.base_hp = 100
            self.base_attack = 15
            self.base_defense = 15
            self.base_agility = 15
        elif race == Race.ELF:
            self.base_hp = 120
            self.base_attack = 15
            self.base_defense = 10
            self.base_agility = 15
        elif race == Race.HALFLING:
            self.base_hp = 80
            self.base_attack = 10
            self.base_defense = 10
            self.base_agility = 25            
        else:  # DWARF
            self.base_hp = 130
            self.base_attack = 20
            self.base_defense = 25
            self.base_agility = 10
        # Текущие характеристики (могут меняться в бою):
        self.current_hp = self.base_hp
        self.max_hp = self.base_hp
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.agility = self.base_agility
        # Инвентарь и снаряжение:
        self.inventory: List[Item] = []
        self.max_inventary = 10
        self.equipped_weapon: Optional[Item] = None
        self.equipped_armor: Optional[Item] = None
        self.gold = 0
    # Пересчитывает характеристики с учетом экипировки
    def update_stats(self):
        self.max_hp = self.base_hp
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.agility = self.base_agility
        
        if self.equipped_weapon:
            self.attack += self.equipped_weapon.attack_bonus
        if self.equipped_armor:
            self.defense += self.equipped_armor.defense_bonus
            self.max_hp += self.equipped_armor.hp_bonus
        
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    
    def add_xp(self, amount: int):
        self.xp += amount
        print(f"Получено {amount} опыта!")
        while self.xp >= self.xp_to_next_level:
            self.level_up()
    
    def level_up(self):
        self.xp -= self.xp_to_next_level
        self.level += 1
        self.skill_points += 3 
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.base_hp += random.randint(5, 10)
        self.base_attack += 1
        self.base_defense += 1
        self.current_hp = self.max_hp = self.base_hp
        self.update_stats()
        
        print(f"\n!!! Поздравляем! Вы достигли {self.level} уровня! !!!")
        print(f"У вас {self.skill_points} очков характеристик для распределения")
    
    def use_skill_point(self, stat: str):
        if self.skill_points <= 0:
            return False
        
        if stat == "hp":
            self.base_hp += 5
        elif stat == "attack":
            self.base_attack += 3
        elif stat == "defense":
            self.base_defense += 2
        elif stat == "agility":
            self.base_agility += 2
        else:
            return False
        
        self.skill_points -= 1
        self.update_stats()
        return True
    
    def equip_item(self, item: Item):
        if item.type == ItemType.WEAPON:
            if self.equipped_weapon:
                self.unequip_item(self.equipped_weapon)
            self.equipped_weapon = item
            print(f"Вы экипировали: {item.name}")
        elif item.type == ItemType.ARMOR:
            if self.equipped_armor:
                self.unequip_item(self.equipped_armor)
            self.equipped_armor = item
            print(f"Вы экипировали: {item.name}")
        
        self.update_stats()
    
    def unequip_item(self, item: Item):
        if item == self.equipped_weapon:
            self.equipped_weapon = None
        elif item == self.equipped_armor:
            self.equipped_armor = None
        
        self.update_stats()
    
    def heal(self, amount: int):
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        print(f"Восстановлено {amount} HP")
    
    def take_damage(self, damage: int) -> bool:
        actual_damage = max(1, damage - self.defense // 2)
        self.current_hp -= actual_damage
        print(f"Получено {actual_damage} урона")
        return self.current_hp <= 0

class Enemy:
    def __init__(self, floor: int):
        self.names = ["Гоблин", "Скелет", "Орк", "Тролль", "Призрак", "Минотавр", "Дракон"]
        self.name = random.choice(self.names)
        self.level = max(1, floor)
    
        self.max_hp = random.randint(40, 60) + (floor * 10)
        self.current_hp = self.max_hp
        self.attack = random.randint(5, 25) + floor
        self.defense = random.randint(10, 20) + floor
        self.agility = random.randint(5, 30)
        self.xp_reward = random.randint(20, 40) + (floor * 5)
        self.gold_reward = random.randint(5, 20) + floor
    
    def take_damage(self, damage: int) -> bool:
        actual_damage = max(1, damage - self.defense // 2)
        self.current_hp -= actual_damage
        return self.current_hp <= 0
    
    def attack_target(self, target: Character) -> bool:
        if random.randint(1, 100) <= target.agility:
            print(f"{self.name} промахнулся!")
            return False
        
        damage = random.randint(self.attack // 2, self.attack)
        print(f"{self.name} атакует и наносит {damage} урона!")
        return target.take_damage(damage)

class Dungeon:
    def __init__(self):
        self.floor = 1
        self.room_count = 0
        self.rooms_per_floor = 5
    
    def generate_rooms(self) -> Tuple[RoomType, RoomType]:
        room_types = [RoomType.COMBAT, RoomType.REST, RoomType.TREASURE]
        weights = [0.5, 0.3, 0.2]  

        if self.floor > 3:
            weights = [0.6, 0.2, 0.2] 
        
        left_room = random.choices(room_types, weights=weights)[0]
        right_room = random.choices(room_types, weights=weights)[0]
        
        return left_room, right_room
    
    def should_change_floor(self) -> bool:
        self.room_count += 1
        if self.room_count >= self.rooms_per_floor:
            self.floor += 1
            self.room_count = 0
            return True
        return False

class Game:
    def __init__(self):
        self.character: Optional[Character] = None
        self.dungeon = Dungeon()
        self.current_enemy: Optional[Enemy] = None
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear") #Очистка экрана
    
    def show_title(self):
        print("=" * 50)
        print("      ТЕКСТОВАЯ RPG - ПОДЗЕМЕЛЬЕ И ВКУСНОСТИ")
        print("=" * 50)
        print()
    
    def create_character(self):
        self.clear_screen()
        self.show_title()
        print("Создание нового персонажа:")
        print("=" * 50)

        print("Выберите расу:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф")
        print("4 - Полурослик")
        print()
        
        while True:
            choice = input("Ваш выбор (1-4): ")
            if choice == "1":
                race = Race.HUMAN
                break
            elif choice == "2":
                race = Race.ELF
                break
            elif choice == "3":
                race = Race.DWARF
                break            
            elif choice == "4":
                race = Race.HALFLING
                break
            else:
                print("Неверный выбор, попробуйте снова")
        character_name = input("Введие имя вашего персонажа: ").strip()
        
        self.character = Character(race)
        self.character.name = character_name if character_name else "Безымянный герой"
        
        print(f"\nПерсонаж {self.character.name} создан!")
        self.show_character_stats()
        input("\nНажмите Enter чтобы продолжить...")
    
    def show_character_stats(self):
        if not self.character:
            return
        
        print("\n" + "=" * 50)
        print("ХАРАКТЕРИСТИКИ ПЕРСОНАЖА")
        print("=" * 50)
        print(f"Имя: {self.character.name}")
        print(f"Раса: {self.character.race.value}")
        print(f"Уровень: {self.character.level}")
        print(f"Опыт: {self.character.xp}/{self.character.xp_to_next_level}")
        print(f"HP: {self.character.current_hp}/{self.character.max_hp}")
        print(f"Атака: {self.character.attack}")
        print(f"Защита: {self.character.defense}")
        print(f"Ловкость: {self.character.agility}")
        print(f"Золото: {self.character.gold}")
        print(f"Очки прокачки: {self.character.skill_points}")
        
        if self.character.equipped_weapon:
            print(f"Оружие: {self.character.equipped_weapon.name}")
        if self.character.equipped_armor:
            print(f"Броня: {self.character.equipped_armor.name}")
        print("=" * 50)
    
    def show_inventory(self):
        if not self.character:
            return
        
        self.clear_screen()
        print("=" * 40)
        print("ИНВЕНТАРЬ")
        print("=" * 40)
        
        if not self.character.inventory:
            print("Инвентарь пуст")
        else:
            for i, item in enumerate(self.character.inventory, 1):
                print(f"{i}. {item}")
        
        print("\nЭкипировано:")
        print(f"Оружие: {self.character.equipped_weapon or 'Нет'}")
        print(f"Броня: {self.character.equipped_armor or 'Нет'}")
        
        print("\n1. Использовать предмет")
        print("2. Экипировать предмет")
        print("3. Выбросить предмет")
        print("4. Назад")
        
        choice = input("\nВаш выбор: ")
        
        if choice == "1" and self.character.inventory:
            self.use_item()
        elif choice == "2" and self.character.inventory:
            self.equip_from_inventory()
        elif choice == "3" and self.character.inventory:
            self.drop_item()
    
    def use_item(self):
        print("\nКакой предмет использовать?")
        for i, item in enumerate(self.character.inventory, 1):
            print(f"{i}. {item}")
        try:
            idx = int(input("Номер предмета: ")) - 1
            if 0 <= idx < len(self.character.inventory):
                item = self.character.inventory[idx]
                
                if item.type == ItemType.POTION:
                    if "здоровья" in item.name.lower():
                        self.character.heal(item.hp_bonus)
                    elif "силы" in item.name.lower():
                        self.character.base_attack += item.attack_bonus
                        self.character.update_stats()
                        print(f"Атака увеличена на {item.attack_bonus}!")
                    
                    self.character.inventory.pop(idx)
                else:
                    print("Этот предмет нельзя использовать")
            else:
                print("Неверный номер")
        except ValueError:
            print("Ошибка ввода")
    
    def equip_from_inventory(self):
        print("\nКакой предмет экипировать?")
        for i, item in enumerate(self.character.inventory, 1):
            print(f"{i}. {item}")
        try:
            idx = int(input("Номер предмета: ")) - 1
            if 0 <= idx < len(self.character.inventory):
                item = self.character.inventory[idx]
                
                if item.type in [ItemType.WEAPON, ItemType.ARMOR]:
                    self.character.equip_item(item)
                    self.character.inventory.pop(idx)
                else:
                    print("Этот предмет нельзя экипировать")
                input("\nНажмите Enter чтобы продолжить...")
            else:
                print("Неверный номер")
        except ValueError:
            print("Ошибка ввода")
    
    def drop_item(self):
        print("\nКакой предмет выбросить?")
        for i, item in enumerate(self.character.inventory, 1):
            print(f"{i}. {item}")
        try:
            idx = int(input("Номер предмета: ")) - 1
            if 0 <= idx < len(self.character.inventory):
                item = self.character.inventory.pop(idx)
                print(f"Вы выбросили: {item.name}")
            else:
                print("Неверный номер")
        except ValueError:
            print("Ошибка ввода")
    
    def distribute_skill_points(self):
        if not self.character or self.character.skill_points <= 0:
            return
        while self.character.skill_points > 0:
            self.clear_screen()
            self.show_character_stats()
            
            print("\nРаспределение очков характеристик:")
            print(f"Доступно очков: {self.character.skill_points}")
            print("1. +5 HP (1 очко)")
            print("2. +3 к атаке (1 очко)")
            print("3. +2 к защите (1 очко)")
            print("4. +2 к ловкости (1 очко)")
            print("5. Выход")
            
            choice = input("\nВаш выбор: ")
            
            if choice == "5":
                break
            stat_map = {"1": "hp", "2": "attack", "3": "defense", "4": "agility"}
            if choice in stat_map:
                if self.character.use_skill_point(stat_map[choice]):
                    print("Характеристика увеличена!")
                else:
                    print("Недостаточно очков!")
            else:
                print("Неверный выбор")
            
            input("\nНажмите Enter чтобы продолжить...")
    
    def generate_item(self) -> Item:
        items = [
            Item("Меч воина", ItemType.WEAPON, attack_bonus=5),
            Item("Копье война", ItemType.WEAPON, attack_bonus=4, agility_bonus=3),
            Item("Кинжал разбойника", ItemType.WEAPON, attack_bonus=3, agility_bonus=4),
            Item("Кожаная броня", ItemType.ARMOR, defense_bonus=2),
            Item("Железная броня", ItemType.ARMOR, defense_bonus=7),
            Item("Кольчуга", ItemType.ARMOR, defense_bonus=5),
            Item("Малое зелье здоровья", ItemType.POTION, hp_bonus=30),
            Item("Большое зелье здоровья", ItemType.POTION, hp_bonus=50),
            Item("Малое зелье силы", ItemType.POTION, attack_bonus=4),
            Item("Большое зелье силы", ItemType.POTION, attack_bonus=7),
            Item("Мешок золота", ItemType.GOLD, value=random.randint(10, 50)),
            Item("Статуя подземного короля", ItemType.ARTIFACT, value=100),
            Item("Ожерелье из драгоценных камней", ItemType.ARTIFACT, value=75),
            Item("Золотая чаша", ItemType.ARTIFACT, value=50)
        ]
        
        item = random.choice(items)
        if self.dungeon.floor > 3:
            if item.type == ItemType.WEAPON:
                item.attack_bonus += self.dungeon.floor // 2
            elif item.type == ItemType.ARMOR:
                item.defense_bonus += self.dungeon.floor // 2
        return item
    
    def enter_room(self, room_type: RoomType):
        self.clear_screen()
        
        if room_type == RoomType.COMBAT:
            print(">> ВЫ ВОШЛИ В БОЕВУЮ КОМНАТУ <<")
            self.start_combat()
        
        elif room_type == RoomType.REST:
            print("~~ ВЫ ВОШЛИ В КОМНАТУ ОТДЫХА ~~")
            print("Вы чувствуете себя в безопасности и можете восстановить силы")
            
            heal_amount = random.randint(10, 30)
            self.character.heal(heal_amount)
            
            if self.character.skill_points > 0:
                print("\nВы можете распределить очки характеристик")
                choice = input("Распределить очки? (д/н): ")
                if choice.lower() == "д":
                    self.distribute_skill_points()
            
            shop_chance = random.randint(1, 2)
            for _ in range(shop_chance):
                if shop_chance == 1:
                    print("="*50)
                    print("Вы встретили странствующего торговца!")
                    print("="*50)
                    print("Однако вы можете лишь продать ему артефакты, найденные в подземелье! Странный...")
                    choice = input("\n Желаете продать ему артефакты? (д/н): ")
                    print("="*50)

                    if choice.lower() == "д":
                        for i, item in enumerate(self.character.inventory, 1):
                            print(f"{i}. {item}")
                        try:
                            idx = int(input("Номер предмета: ")) - 1
                            if 0 <= idx < len(self.character.inventory):
                                item = self.character.inventory[idx]
                                if item.type == ItemType.ARTIFACT:
                                    sold_item = self.character.inventory.pop(idx)
                                    self.character.gold += sold_item.value
                                    print(f"Вы продали {sold_item.name} за {sold_item.value} золота!")
                                else:
                                    print("="*50)
                                    print("Торговец покупает только артефакты!")
                                    print("Пока вы мешкались, торговец успел пропасть из зоны видимости! Ой...")
                            else:
                                print("="*50)
                                print("Неверно набран номер!")
                                print("="*50)
                                print("А пока вы мешкались, торговец успел пропасть из зоны видимости! Ой...")
                        except ValueError:
                            print("="*50)
                            print("Ошибка ввода")
                            print("Пока вы мешкались, торговец успел пропасть из зоны видимости! Ой...")
                    elif choice.lower() == "н":
                        print("Вам машет на прощаение торговец")
                    else:
                        print("Неверно введено!")

        elif room_type == RoomType.TREASURE:
            print("!00! ВЫ ВОШЛИ В КОМНАТУ С СУНДУКОМ !00!")
            print("Перед вами старый сундук...")
            
            items_found = random.randint(1, 3)
            for _ in range(items_found):
                item = self.generate_item()
                
                if item.type == ItemType.GOLD:
                    self.character.gold += item.value
                    print(f"Вы нашли {item.value} золота!")
                elif self.character.max_inventary == len(self.character.inventory):
                    print(f"Вы нашли: {item.name}!")
                    print("Однако ваш инвентарь переполен!")
                else:
                    self.character.inventory.append(item)
                    print(f"Вы нашли: {item.name}!")            
            rare_item = Item("Легендарный меч", ItemType.WEAPON, attack_bonus=10, agility_bonus=5)
            if random.random() < 0.1 and self.dungeon.floor > 7:
                print(f"!!! ВАУ! Вы нашли ЛЕГЕНДАРНЫЙ МЕЧ! !!!")
                if self.character.max_inventary == len(self.character.inventory):
                    print("Однако ваш инвентарь переполен!")
                else:
                    self.character.inventory.append(rare_item)

        input("\nНажмите Enter чтобы продолжить...")
    
    def start_combat(self):
        self.current_enemy = Enemy(self.dungeon.floor)
        print(f"Перед вами {self.current_enemy.name} (Уровень {self.current_enemy.level})!")
        print(f"HP врага: {self.current_enemy.current_hp}")
        
        while self.current_enemy.current_hp > 0 and self.character.current_hp > 0:
            print("\n" + "=" * 50)
            print(f"Ваше HP: {self.character.current_hp}/{self.character.max_hp}")
            print(f"HP врага: {self.current_enemy.current_hp}")
            print("=" * 50)
            
            print("\nВаши действия:")
            print("1. Атаковать")
            print("2. Использовать предмет")
            print("3. Попытаться убежать")
            
            choice = input("\nВаш выбор: ")
            
            if choice == "1": # Атака игрока
                damage = random.randint(self.character.attack // 2, self.character.attack)
                if random.random() < 0.1:  
                    damage *= 2
                    print("КРИТИЧЕСКИЙ УДАР!")
                
                print(f"Вы наносите {damage} урона!")
                if self.current_enemy.take_damage(damage):
                    self.victory()
                    break
                if self.current_enemy.attack_target(self.character): # Контратака врага
                    self.defeat()
                    break
            
            elif choice == "2":
                self.use_item_in_combat()
            
            elif choice == "3":
                if random.random() < 0.3:
                    print("Повезло! Вы успешно сбежали!")
                    break
                else:
                    print("Какая неудача! Не удалось сбежать!")
                    if self.current_enemy.attack_target(self.character):
                        self.defeat()
                        break
    
    def use_item_in_combat(self):
        potions = [item for item in self.character.inventory if item.type == ItemType.POTION]
        
        if not potions:
            print("У вас нет зелий!")
            return
        
        print("\nДоступные зелья:")
        for i, potion in enumerate(potions, 1):
            print(f"{i}. {potion.name}")
        
        try:
            idx = int(input("Номер зелья: ")) - 1
            if 0 <= idx < len(potions):
                potion = potions[idx]
                if "здоровья" in potion.name.lower():
                    self.character.heal(potion.hp_bonus)
                elif "силы" in potion.name.lower():
                    self.character.base_attack += potion.attack_bonus
                    self.character.update_stats()
                    print(f"Атака увеличена на {potion.attack_bonus}!")
                self.character.inventory.remove(potion)
            else:
                print("Неверный номер")
        except ValueError:
            print("Ошибка ввода")
    
    def victory(self):
        print(f"\n!!! ПОБЕДА! Вы победили {self.current_enemy.name}! !!!")
        
        xp = self.current_enemy.xp_reward
        gold = self.current_enemy.gold_reward
        self.character.add_xp(xp)
        self.character.gold += gold
        print(f"Получено {gold} золота!")
        
        if random.random() < 0.4: 
            item = self.generate_item()
            if self.character.max_inventary == len(self.character.inventory):
                print(f"Вы нашли: {item.name}!")
                print("Однако ваш инвентарь переполен!")
            else:
                self.character.inventory.append(item)
                print(f"Вы нашли: {item.name}!")
    
    def defeat(self):
        print(f"\n=== ПОРАЖЕНИЕ! {self.current_enemy.name} победил вас... ===")
        print("Игра окончена")
        print("="*50)
        
        print("\n1. Начать заново")
        print("2. Выйти в главное меню")
        print("3. Выйти из игры")
        
        choice = input("\nВаш выбор: ")
        
        if choice == "1":
            self.create_character()
            self.dungeon = Dungeon()
            self.main_loop()
        elif choice == "2":
            self.main_menu()
        else:
            exit()
    
    def explore_dungeon(self):
        while True:
            self.clear_screen()
            
            print("="*50)
            print(f"       ЭТАЖ {self.dungeon.floor} - КОМНАТА {self.dungeon.room_count + 1}")
            print("="*50)            
            self.show_character_stats()
            
            left_room, right_room = self.dungeon.generate_rooms() # Генерируем комнаты
            
            left_visible = random.random() < 0.5
            right_visible = random.random() < 0.5
            
            print("\nПеред вами развилка:")
            print(f"1 - Слева: {left_room.value if left_visible else '???'}")
            print(f"2 - Справа: {right_room.value if right_visible else '???'}")
            print("="*50)
            print("3 - Открыть инвентарь")
            print("4 - Распределить очки характеристик")
            print("5 - Сохранить игру")
            print("6 - Выйти в главное меню")
            
            choice = input("\nКуда пойти? ")
            
            if choice == "1":
                self.enter_room(left_room)
                if self.dungeon.should_change_floor():
                    self.new_floor_event()
            elif choice == "2":
                self.enter_room(right_room)
                if self.dungeon.should_change_floor():
                    self.new_floor_event()
            elif choice == "3":
                self.show_inventory()
            elif choice == "4":
                self.distribute_skill_points()
            elif choice == "5":
                print("="*50)
                print("Извините, эта функция пока недоступна!")
                input("Нажмите Enter чтобы продолжить...")
            elif choice == "6":
                break
    
    def new_floor_event(self):
        self.clear_screen()
        print("=" * 50)
        print(f"       ВЫ СПУСТИЛИСЬ НА ЭТАЖ {self.dungeon.floor}")
        print("=" * 50)

        reward = random.randint(50, 100) * self.dungeon.floor
        self.character.gold += reward
        print(f"\nЗа смелость вы получаете {reward} золота!")
        self.character.base_hp += 10 # Улучшение характеристик
        self.character.current_hp = self.character.max_hp = self.character.base_hp
        self.character.update_stats()
        print("Ваше максимальное здоровье увеличено на 10!")
        
        input("\nНажмите Enter чтобы продолжить...")
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.show_title()
            
            print("ГЛАВНОЕ МЕНЮ:")
            print("1. Новая игра")
            print("2. Загрузить игру")
            print("3. Выйти")
            
            choice = input("\nВаш выбор: ")          
            if choice == "1":
                self.create_character()
                self.main_loop()
            elif choice == "2":
                print("Извините, эта функция пока недоступна!")
                input("\nНажмите Enter чтобы продолжить...")
            elif choice == "3":
                exit()
    
    def main_loop(self):
        if not self.character:
            return
        
        self.explore_dungeon()

def main():
    game = Game()
    game.main_menu()

if __name__ == "__main__":
    main()