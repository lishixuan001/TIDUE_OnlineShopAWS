import re
from transactions.models import *

# ==================================================== #
#                  Helper Functions                    #
# ==================================================== #

def username_exist(username):
    """
    :param username: The username to be tested
    :return: A bool indicating if the username is taken
    """
    return User.objects.filter(username=username).exists()


def setup_database():
    for i in range(len(Product.objects.all())):
        Product.objects.all()[i].delete()
    Product.objects.create(name="惠氏启赋有机3段奶粉", price=429, idx="1", stock=20)
    Product.objects.create(name="哆啦A梦超薄纸尿裤L68", price=69.9, idx="2", stock=20)
    Product.objects.create(name="雅培小安素900g", price=179, idx="3", stock=30)
    Product.objects.create(name="禾洋洋婴儿饼干3盒3味", price=78, idx="4", stock=30)
    Product.objects.create(name="纽因贝湿巾", price=78, idx="5", stock=40)
    Product.objects.create(name="贝亲宝宝鸡肉蔬菜粥", price=11, idx="6", stock=40)