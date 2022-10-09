model = input("Enter full mac model: ")  # Example: macbook pro
a = model.split()
model_1 = a[0]
series = a[1]
year = 2016
size = "15'"
result = str("!my computer is %s: release - %d, the lineup %s %s?" % (model_1, year, series, size))
result_1 = str("my computer is %s: release - %d, the lineup %s %s" % (((model_1[::-1]).upper()), year,
                                                                      ((series[::-1]).capitalize()), size))
result_2 = str(f"!my computer is {model_1[::-1].upper()}: release - {year}, the lineup {series[::-1].capitalize()} "
               f"{size}?")
result_3 = str("!my computer is {}: release - {}, the lineup {} {}?".format((model_1[::-1]).upper(), year,
                                                                            (series[::-1]).capitalize(), size))

source_file = open('print_result.txt', 'w')
print(result, end="<<<>>>", file=source_file)
print(result_1, end="<<<>>>", file=source_file)
print(result_2, end="<<<>>>", file=source_file)
print(result_3, file=source_file)

source_file.close()
