def concatenate(*args, **kwargs):
    concatenated_string = ""
    for word in args:
        concatenated_string += word

    for key, value in kwargs.items():
        if key in concatenated_string:
            concatenated_string = concatenated_string.replace(key, value)

    return concatenated_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
