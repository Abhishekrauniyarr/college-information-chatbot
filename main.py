greet = ["hi", "hello", "hey", "yo"]
bye = ["bye", "see you", "thanks"]

# Storing the previous teacher for pronoun handling
n = None

while True:
    if __name__ == "__main__":
        user = input("TYPE: ")
        user = user.lower()

        # Greeting
        for word in greet:
            if user == word:
                print("BOT: Hi, how can I help you?")

        # Goodbye
        for word in bye:
            if user == word:
                print("BOT: Bye, have a good day!")

        # Introduction about the college
        if "about" in user and "college" in user:
            print(
                "Green Valley College is a fictional educational institution "
                "focused on quality education, student development, "
                "and academic excellence."
            )

    # TEACHER INFORMATION DICTIONARIES

    teachers = ["ram", "sita", "hari"]

    ram = {
        "name": "Ram Sharma",
        "subject": "Physics",
        "qualification": "M.Sc. Physics"
    }

    sita = {
        "name": "Sita Karki",
        "subject": "Chemistry",
        "qualification": "M.Sc. Chemistry"
    }

    hari = {
        "name": "Hari Shah",
        "subject": "Mathematics",
        "qualification": "M.Sc. Mathematics"
    }

    # FUNCTION FOR RAM'S INFORMATION

    def ramm():
        if "what" in user and "name" in user:
            return f"BOT: {ram.get('name')} is his full name."

        elif "which" in user and "subject" in user:
            return f"BOT: He is a {ram.get('subject')} teacher."

        elif "what" in user and "qualification" in user:
            return f"BOT: His qualification is {ram.get('qualification')}."

        elif "about" in user and ("ram" in user or "him" in user):
            return (
                "BOT: Ram Sharma is a Physics teacher with an M.Sc. in Physics. "
                "With his academic background and knowledge of the subject, "
                "he is qualified to teach physics and help students understand "
                "its fundamental concepts, theories, and practical applications."
            )

        elif "ram" in user:
            return "What do you want to know about him?"

        else:
            return (
                "I don't have that information about Ram. "
                "Is there anything else you want to know?"
            )

    # FUNCTION FOR SITA'S INFORMATION

    def sitaa():
        if "what" in user and "name" in user:
            return f"BOT: {sita.get('name')} is her full name."

        elif "which" in user and "subject" in user:
            return f"BOT: She is a {sita.get('subject')} teacher."

        elif "what" in user and "qualification" in user:
            return f"BOT: Her qualification is {sita.get('qualification')}."

        elif "about" in user and ("sita" in user or "her" in user):
            return (
                "BOT: Sita Karki is a Chemistry teacher with an M.Sc. in Chemistry. "
                "She teaches Chemistry and helps students understand its concepts and applications."
            )

        elif "sita" in user:
            return "What do you want to know about her?"

        else:
            return (
                "I don't have that information about Sita. "
                "Is there anything else you want to know?"
            )

    # FUNCTION FOR HARI'S INFORMATION

    def harii():
        if "what" in user and "name" in user:
            return f"BOT: {hari.get('name')} is his full name."

        elif "which" in user and "subject" in user:
            return f"BOT: He is a {hari.get('subject')} teacher."

        elif "what" in user and "qualification" in user:
            return f"BOT: His qualification is {hari.get('qualification')}."

        elif "about" in user and ("hari" in user or "him" in user):
            return (
                "BOT: Hari Shah is a Mathematics teacher who holds an M.Sc. in Mathematics. "
                "He specializes in Mathematics and can help students understand mathematical concepts and solve problems."
            )

        elif "hari" in user:
            return "What do you want to know about him?"

        else:
            return (
                "I don't have that information about Hari. "
                "Is there anything else you want to know?"
            )

    # TEACHER INFORMATION RUNNING

    h = ["he", "his", "him"]
    s = ["she", "her"]
    words = user.split()

    if "ram" in words:
        n = "ram"
        print(ramm())

    elif "sita" in words:
        n = "sita"
        print(sitaa())

    elif "hari" in words:
        n = "hari"
        print(harii())

    elif "he" in words or "his" in words or "him" in words:
        if n == "ram":
            print(ramm())
        elif n == "hari":
            print(harii())
        else:
            print("Whom are you referring to?")

    elif "she" in words or "her" in words:
        if n == "sita":
            print(sitaa())
        else:
            print("Whom are you referring to?")