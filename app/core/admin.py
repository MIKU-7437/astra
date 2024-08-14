from sqladmin import Admin, ModelView

from ..models.product import Product
from ..models.category import Category

from ..core.database import async_engine

# Определяем админ-класс для Category
class CategoryAdmin(ModelView, model=Category):
    column_list = [
        Category.id,
        Category.title,
        Category.is_subcategory,
        Category.created_at,
        Category.updated_at,
    ]
    column_searchable_list = [Category.title]
    column_filters = [Category.is_subcategory, Category.created_at]

    form_columns = [
        'title',  # Название
        'slug',  # Слаг
        'products',  # Продукты
        'description',  # Описание
        'is_subcategory',  # Это подкатегория?
        'created_at',  # Дата создания
        'updated_at',  # Дата обновления
        'sub_categories',  # Подкатегории
        'top_categories',  # Верхние категории
    ]

# Определяем админ-класс для Product
class ProductAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.title,
        Product.price,
        Product.is_available,
        Product.stock,
        Product.photo,
        Product.created_at,
        Product.updated_at,
    ]
    column_searchable_list = [Product.title, Product.slug]
    column_filters = [Product.is_available, Product.price]

    form_columns = [
        'title',  # Название продукта
        'slug',  # Слаг
        'price',  # Цена
        'category',
        'is_available',  # Доступен ли продукт
        'stock',  # Наличие на складе
        'photo',  # Фото продукта
        'description',  # Описание продукта
        'created_at',  # Дата создания
        'updated_at'  # Дата обновления
    ]

# Создаем функцию для регистрации админки
def setup_admin(app):
    admin = Admin(app, async_engine)
    admin.add_view(CategoryAdmin)
    admin.add_view(ProductAdmin)
    return admin
