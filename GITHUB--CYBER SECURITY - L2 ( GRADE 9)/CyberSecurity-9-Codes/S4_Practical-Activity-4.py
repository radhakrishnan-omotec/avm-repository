questions = {
    "Encrypting student report cards so only parents can view them protects:": "confidentiality",
    "Verifying downloaded software hasn’t been tampered with protects:": "integrity",
    "Using cloud backups to ensure data is always retrievable supports:": "availability",
}




score = 0

for q, correct in questions.items():
    ans = input(q + "\n> ").strip().lower()
    if ans == correct:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. Correct answer: {correct}\n")



print(f"\n🎓 Final Score: {score}/{len(questions)}")