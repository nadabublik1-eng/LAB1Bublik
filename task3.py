print("Введіть текст (для завершення введіть 'END' з нового рядка):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

text = " ".join(lines)
words = text.split()

freq = {}
for word in words:
    clean_word = word.strip(".,!?:;\"'").lower()
    if clean_word:
        freq[clean_word] = freq.get(clean_word, 0) + 1

sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

print("\nЧастоти слів (за спаданням):")
for key, value in sorted_freq.items():
    print(f"{key}: {value}")

frequent_words = {k: v for k, v in freq.items() if v >= 2}
print("\nСлова, що зустрічаються 2 і більше разів:")
print(frequent_words)