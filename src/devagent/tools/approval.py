def request_approval(action: str, description: str) -> bool:
    print("\nDevAgent wants to perform an action:")
    print(f"Action: {action}")
    print(f"Description: {description}")

    while True:
        choice = input("Approve this action? (y/n): ").strip().lower()

        if choice == "y":
            print("Action approved.")
            return True

        if choice == "n":
            print("Action rejected.")
            return False

        print("Invalid choice. Enter y or n.")