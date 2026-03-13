# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Bug 1: The attempts left counter was wrong at the start

Expected:
When the game starts, the number of attempts left should equal the total number of attempts allowed for the selected difficulty.

Actual:
The game always shows one fewer attempt than expected when the game begins.

Bug 2: Hard difficulty uses a smaller range than Normal difficulty

Expected:
Hard mode should be more difficult than Normal mode, so its number range should be equal to or larger than Normal mode.

Actual:
Normal mode uses the range 1 to 100, but Hard mode uses 1 to 50, which actually makes Hard mode easier in terms of guessing range.

Bug 3: The hint messages are reversed

Expected:
If the player's guess is higher than the secret number, the game should tell them to go lower.
If the player's guess is lower than the secret number, the game should tell them to go higher.

Actual:
The game does the opposite:

when the guess is too high, it says “Go HIGHER!”

when the guess is too low, it says “Go LOWER!”

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Correct suggestion from AI

What the AI suggested:
Copilot pointed out that the new_game logic resets the secret number using random.randint(1, 100), which is hardcoded and does not respect the selected difficulty level.

Was the suggestion correct?
Yes, the suggestion was correct.

How I verified it:
I reviewed the code and noticed that when starting a new game, the secret number was always generated within the range 1–100, regardless of the selected difficulty. This contradicted the game design, since each difficulty level should have its own range defined by get_range_for_difficulty(). Based on this suggestion, I modified the code so that the new secret number is generated using the low and high values returned from get_range_for_difficulty(difficulty). After making this change, the game correctly resets the secret number according to the selected difficulty.

Incorrect or misleading suggestion from AI

What the AI suggested:
While helping me generate tests, Copilot automatically removed the existing starter tests and replaced them with new ones.

Was the suggestion correct?
This suggestion was misleading.

How I verified it:
After reviewing the assignment instructions, I realized that the starter tests were required and should not be removed. The AI had made an assumption and modified the tests without explicitly asking. To correct this, I restored the original starter tests and ensured they remained in the project. This experience showed that AI tools can sometimes make decisions that do not align with assignment requirements, so it is important to carefully review their suggestions instead of accepting them automatically.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I confirmed that a bug was fixed by reviewing the code changes and running tests with pytest. I also checked the behavior manually in the game when necessary. If the code logic matched the expected behavior and the tests passed, I considered the bug fixed.

For example, I fixed the hint direction bug in check_guess(). Previously, when a guess was higher than the secret number, the game incorrectly suggested going higher. After fixing the logic, I ran the test:

def test_regression_high_guess_says_go_lower():
outcome, message = check_guess(60, 50)
assert outcome == "Too High"
assert "LOWER" in message

This confirmed that the game now correctly tells the player to go lower when the guess is too high. I also used a similar test to verify the opposite case.

AI tools helped me understand how to structure some of the tests, but I verified them myself by checking the assignment requirements and running pytest to ensure the results matched the expected behavior.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time the user interacts with the app, such as clicking a button or entering input. This means that variables defined in the script will reset unless their values are stored somewhere.

To solve this problem, Streamlit provides session state, which allows the app to remember values between reruns. For example, the secret number and the number of attempts must be stored in st.session_state, otherwise they would reset every time the player submits a guess.

In simple terms, reruns mean the script starts over each time, and session state is how Streamlit remembers important data so the game can continue working correctly.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future labs and projects is being very specific with Copilot about which file or files it should reference. Giving it the right context makes its suggestions much more relevant and reduces confusion.

One thing I would do differently next time is write more precise prompts and instructions. In this project, when I asked AI to help write tests, it removed the starter tests, which was not what the assignment required. That showed me I need to be clearer about constraints and expected boundaries.

This project changed the way I think about AI-generated code because it showed me that AI code is not automatically correct or complete. It can be helpful, but I still need to carefully review every suggested change before accepting it.
