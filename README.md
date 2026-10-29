# College Information Chatbot

## About the Project

The College Information Chatbot is a beginner-friendly, rule-based chatbot built using Python. It responds to greetings, provides a fictional college introduction, and answers questions about teachers using predefined information and conditional statements.

## Features

- **Greeting Handling:** Responds to `hi`, `hello`, `hey`, and `yo`.
- **Goodbye Responses:** Responds to `bye`, `see you`, and `thanks`.
- **College Introduction:** Provides a short introduction to Green Valley College.
- **Teacher Information:** Provides information about Ram Sharma, Sita Karki, and Hari Shah.
- **Full Names:** Answers questions about teachers' full names.
- **Subjects:** Identifies the subjects taught by teachers.
- **Qualifications:** Provides teachers' academic qualifications.
- **Teacher Introductions:** Gives a short introduction to individual teachers.
- **Pronoun Handling:** Uses the previously mentioned teacher to interpret pronouns such as `he`, `his`, `him`, `she`, and `her`.

## Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- `if`, `elif`, and `else` statements
- `for` loops
- String operations

## Sample Teacher Information

| Teacher | Subject | Qualification |
|---|---|---|
| Ram Sharma | Physics | M.Sc. Physics |
| Sita Karki | Chemistry | M.Sc. Chemistry |
| Hari Shah | Mathematics | M.Sc. Mathematics |

*These are fictional example records and should not be treated as verified information about a real college.*

## How to Run

1. Install Python on your computer.
2. Save your chatbot code in a file named `main.py`.
3. Open a terminal in the project folder.
4. Run the following command:

   ```bash
   python main.py
   ```

5. Type a question when the chatbot displays `TYPE:`.

## Example Conversation

```text
TYPE: hello
BOT: Hi, how can I help you?

TYPE: what is ram name
BOT: Ram Sharma is his full name.

TYPE: which subject does he teach
BOT: He is a Physics teacher.

TYPE: what is sita qualification
BOT: Her qualification is M.Sc. Chemistry.

TYPE: about college
Green Valley College is a fictional educational institution focused on quality education, student development, and academic excellence.
```

*Responses depend on the exact wording of the user's input and the chatbot's matching rules.*

## Current Limitations

- The chatbot relies on keyword matching rather than natural-language understanding.
- It may produce unexpected or repeated responses for some inputs.
- Pronoun handling depends on the previously selected teacher.
- It does not yet reliably handle multiple questions in one sentence.
- Teacher information is stored directly in the Python code.
- The chatbot does not verify information against official college records.

## Future Improvements

- Prevent duplicate responses.
- Improve pronoun handling and conversation context.
- Organize functions and dictionaries more efficiently.
- Add information about classrooms, sections, attendance, library policies, and examinations.
- Improve responses to unknown or ambiguous questions.

## Project Goal

The goal is to build a reliable College Information Chatbot step by step while learning Python programming fundamentals.

## Author

Developed as a Python learning project.
