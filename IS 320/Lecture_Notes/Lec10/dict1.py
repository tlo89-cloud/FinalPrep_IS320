"""
going over indexing and dicts and shi


if x in 

"""

# word = "hello"

# for letter in word:
#     print(letter.upper())

    
capitals = {"USA":"DC", "UK": "London"}
# capitals.clear()   # how to empty out a dict
# if capitals:
#     print(capitals)
# else:
#     print("No data to display")
# if not capitals:
#     print("No data to display")
# else:
#     print(capitals)


country = "JAPAN"
capital = "Tokyo"
capitals[country] = capital

country = "USA"
capital = "Washington DC"
capitals[country] = capital


# search / retrevial
if not capitals:
    print("No data to search in")
else:
    country = input("enter country >>").upper()
    if country in capitals:
        print(capitals[country])
    else:
        print("We do not know")


# for key in capitals:
#     value = capitals[key]
#     print(key, value)

# for country in capitals:
#     captial = capitals[country]

country = "USA"
print(f"Popped: {capitals.pop(country)}")   # del from the dict
print(capitals)



