import file_operations
import random

from faker import Faker

def convert_to_runic_word(word):
    runic_letters_mapping = {
      'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
      'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
      'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
      'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
      'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
      'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
      'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
      'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
      'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
      'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
      'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
      'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
      'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
      'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
      'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
      'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
      'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
      'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
      'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
      'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
      'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
      'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
      ' ': ' '
    }
    runic_word = ""
    for letter in word:
      if letter in runic_letters_mapping.keys():
        runic_word += letter.replace(letter, runic_letters_mapping[letter])
    return runic_word

def generate_fake_card_context(faker_instance, runic_skills):
    random_runic_skills = random.sample(runic_skills, 3)

    context = {
      "first_name": faker_instance.first_name_male(),
      "last_name": faker_instance.last_name_male(),
      "job": faker_instance.job(),
      "town": faker_instance.city(),
      "strength": random.randint(8, 14),
      "agility": random.randint(8, 14),
      "endurance": random.randint(8, 14),
      "intelligence": random.randint(8, 14),
      "luck": random.randint(8, 14),
      "skill_1": random_runic_skills[0],
      "skill_2": random_runic_skills[1],
      "skill_3": random_runic_skills[2]
    }

    return context

def main():
    skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]

    runic_skills = [ convert_to_runic_word(skill) for skill in skills ]
    
    for i in range(1,11):
      card_context = generate_fake_card_context(Faker("ru_RU"), runic_skills)
      file_operations.render_template("src/charsheet.svg", f"output/svg/charsheet-{i}.svg", card_context)

if __name__ == "__main__":
    main()