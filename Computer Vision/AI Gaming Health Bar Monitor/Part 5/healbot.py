

import pyautogui


spells = {
    'big_heal': '1',
    'small_heal': '2',
}


def cast_spell(spell_name):
    key = spells[spell_name]
    pyautogui.press(key)
    print(f"Casting {spell_name}...")



if __name__ == '__main__':
    cast_spell('big_heal')

    