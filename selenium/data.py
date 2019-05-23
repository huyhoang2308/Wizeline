# we can store test data in this module like users
users = [{"name": "standard_user", "email": "standard_user", "password": "secret_sauce"},
         {"name": "locked_out_user", "email": "locked_out_user", "password": "secret_sauce"}]

items = [{"name": "Sauce Labs Backpack", "title": "Sauce Labs Backpack",\
         "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.", 
         "price": "$29.99"},
         {"name": "Sauce Labs Bike Light","title": "Sauce Labs Bike Light",\
         "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included", 
         "price": "$9.99"}]

def get_user(name):
    try:
        return (user for user in users if user["name"] == name).__next__()
    except:
        print ("\n     User %s is not defined, enter a valid user.\n" %name)

def get_user_data(name):
    return (list(user.values()) for user in users if user["name"] == name).__next__()

def get_item(name):
    try:
        return (item for item in items if item["name"] == name).__next__()
    except:
        print(("\n     Item %s is not defined.\n" %name))

def get_item_data(name):
    return (list(item.values()) for item in items if items["name"] == name).__next__()


print (get_item("Sauce Labs Backpack")['title'])