def tailgating_awareness():
    print("Scenario: You are entering a secure building, and someone asks to follow behind you without a badge.")
    response = input("Do you let them in? (yes/no): ").strip().lower()



    if response == 'yes':
        print("❌ Security Risk: This could be a tailgating attack. Always verify access.")
    else:
        print("✅ Correct: Never allow unauthorized individuals to piggyback.")




tailgating_awareness()