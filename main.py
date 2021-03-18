import file_operations
import random

from faker import Faker

NUMBER_OF_CARDS = 10
MIN_SKILL_LEVEL = 8
MAX_SKILL_LEVEL = 14

def generate_fake_card_context(faker, runic_skills):
    random_skills = {}
    for num, skill in enumerate(random.sample(runic_skills, 3), 1):
      random_skills[f"skill_{num}"] = skill

    full_name_male = [faker.first_name_male(), faker.last_name_male()] 
    full_name_female = [faker.first_name_female(), faker.last_name_female()]
    first_name, last_name = random.choice([full_name_male, full_name_female])

    context = {
      "first_name": first_name,
      "last_name": last_name,
      "job": faker.job(),
      "town": faker.city(),
      "strength": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
      "agility": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
      "endurance": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
      "intelligence": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
      "luck": random.randint(MIN_SKILL_LEVEL, MAX_SKILL_LEVEL),
      **random_skills
    }

    return context

def main():
    skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]

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
    runic_skills = [] 
    for skill in skills:
        for letter, runic_letter in runic_letters_mapping.items():
            skill = skill.replace(letter, runic_letter)
        runic_skills.append(skill)

    for num in range(1, NUMBER_OF_CARDS + 1):
        card_context = generate_fake_card_context(Faker("ru_RU"), runic_skills)
        file_operations.render_template("src/charsheet.svg", f"output/svg/charsheet-{num}.svg", card_context)

if __name__ == "__main__":
    main()