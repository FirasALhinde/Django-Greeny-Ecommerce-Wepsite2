import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()


from faker import Faker
import random
from products.models import Product ,Brand ,Category

def seed_brand(n):
    fake =Faker()
    images = ['1.jfif','2.jfif','3.jfif','4.png']
    for _ in range(n):
        name = fake.name()
        image = f'Brand/{images[random.randint(0,3)]}'
        Brand.objects.create(
            name = name ,
            image = image,
        )
    print(f"Seed {n}Brand")


def seed_category(n):
    fake =Faker()
    images = ['1.jfif','2.jfif','3.jfif','4.png']
    for _ in range(n):
        name = fake.name()
        image = f'Category/{images[random.randint(0,3)]}'
        Category.objects.create(
            name = name ,
            image = image,
        )
    print(f"Seed {n} Category")

def seed_product(n):
    fake =Faker()
    flag_type = ['New','Feature']
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','10.jpg','16.jpg']
    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        brand = Brand.objects.get(id = random.randint(1,20))
        price = round(random.uniform(2.99,99.99),2)
        desc = fake.text(max_nb_chars =1000)
        flag = flag_type[random.randint(0,1)]
        # category = Category.objects.get(id = random.randint(1,20))
        image = f'Products/{images[random.randint(0,9)]}'
        Product.objects.create(
            name = name,
            sku = sku,
            brand = brand,
            price = price,
            desc = desc,
            flat = flag ,
            # category = category ,
            image = image,
        )
    print(f"Seed {n} Products")



# seed_product(1000)
# seed_brand(20)
seed_category(1000)
