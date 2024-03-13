import llm

model = llm.get_model("palm")
model.key = "AIzaSyDGbGJ7WK6Jj1cqDfqvjpREEd0WSvbu2fM"

response = model.prompt("what is 5 + 5")

print(response.text())