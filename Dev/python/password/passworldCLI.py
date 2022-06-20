from libs.password import Password as pwd


for i in range(0, 100000):
    print(f"#{i + 1} : {pwd(length = 32, has_specials=True)}")