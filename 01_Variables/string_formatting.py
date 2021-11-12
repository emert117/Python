name = "emre"
greeting = f"Hello {name}"

print(greeting)
print(f"Hello {name}")

greeting2 = "Hello {}" # template
with_name = greeting2.format(name)
print(with_name)

longer_phrase = "Hello {} Today is {}"
formatted = longer_phrase.format("yunus", "friday")
print(formatted)