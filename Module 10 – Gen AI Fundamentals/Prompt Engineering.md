# Module: Prompt Engineering – Techniques, Best Practices & Ethics (Cognizant Technical Assessment)

Prompt Engineering is one of the most important skills for developers using **Generative AI**. A well-written prompt helps AI generate **more accurate, useful, and reliable responses**. It is widely used in software development, testing, cloud computing, data analysis, and content creation.

---

# What is Prompt Engineering?

## Definition

**Prompt Engineering** is the process of designing and writing effective instructions (called **prompts**) to guide an AI model in producing the desired output.

A **prompt** is simply the input or question given to an AI model.

---

## Why It Matters for Developers

Developers use prompt engineering to:

* Generate code
* Debug programs
* Explain algorithms
* Write documentation
* Create test cases
* Generate SQL queries
* Automate repetitive tasks

A better prompt usually produces a better response.

---

## Real-Life Example

### Weak Prompt

```text
Write code.
```

AI does not know:

* Programming language
* Functionality
* Input
* Output

Result:

A vague or incorrect answer.

---

### Good Prompt

```text
Write a C# method that returns the largest number in an integer array.
Include comments and explain the time complexity.
```

The AI understands:

* Language → C#
* Task → Find largest number
* Output → Method with comments
* Extra requirement → Time complexity

Result:

A much more useful response.

---

# Prompt Engineering Workflow

```text
User Prompt
      │
      ▼
AI Model
      │
Understands Instructions
      │
      ▼
Generates Output
      │
      ▼
User Reviews & Improves Prompt (if needed)
```

---

# Prompting Techniques

There are several techniques used to improve AI responses.

---

# 1. Zero-Shot Prompting

## Definition

**Zero-shot prompting** means asking the AI to perform a task **without providing any examples**.

The model relies only on the instruction.

---

## Example

Prompt

```text
Translate the sentence "Good Morning" into French.
```

AI Output

```text
Bonjour
```

---

## Coding Example

Prompt

```text
Write a Python program to check whether a number is prime.
```

No example is provided.

The AI directly generates the solution.

---

## Advantages

* Simple
* Fast
* Useful for common tasks

---

## Limitations

* May not produce the exact format you expect.
* Less effective for complex tasks.

---

# 2. Few-Shot Prompting

## Definition

**Few-shot prompting** provides one or more examples before asking the AI to perform a similar task.

The examples guide the model.

---

## Example

Prompt

```text
Input: 2 + 3
Output: 5

Input: 10 + 7
Output: 17

Input: 15 + 8
Output:
```

AI Output

```text
23
```

---

## Coding Example

Prompt

```text
Example

Input:
5

Output:
25

Now write a Python program that calculates the square of a number entered by the user.
```

The example helps the AI understand the expected behavior.

---

## Advantages

* Higher accuracy
* Better formatting
* Useful for structured tasks

---

# 3. Chain-of-Thought Prompting

## Definition

**Chain-of-thought prompting** asks the model to reason through a problem in multiple steps before producing the final answer.

> **Note:** For exams and interviews, know the concept. In practice, you don't always need to ask for the reasoning; often it's enough to ask for a correct solution and explanation.

---

## Example

Prompt

```text
A shop sells one notebook for $10.
Ravi buys 4 notebooks.

Think through the calculation step by step and then give the final total.
```

AI

* Price of one notebook = $10
* Quantity = 4
* Total = $40

Final Answer

```text
$40
```

---

## Coding Example

Prompt

```text
Analyze the following Python code, identify the bug, explain the cause, and then provide the corrected version.
```

---

## Advantages

* Better for complex reasoning
* Useful for debugging
* Helpful for algorithm explanations

---

## Limitations

* Responses can be longer.
* Not necessary for simple questions.

---

# Comparison of Prompting Techniques

| Technique        | Description                                               | Example                                                         |
| ---------------- | --------------------------------------------------------- | --------------------------------------------------------------- |
| Zero-shot        | No examples are provided                                  | "Write a Java program to sort an array."                        |
| Few-shot         | One or more examples guide the model                      | Show two input/output examples before asking a similar question |
| Chain-of-thought | Ask the model to reason through the task before answering | "Explain how you identified the bug, then provide the fix."     |

---

# Best Practices for Prompt Engineering

---

# 1. Write Clear Instructions

Avoid vague prompts.

### Poor Prompt

```text
Write something about Java.
```

### Better Prompt

```text
Explain Java inheritance with an example suitable for beginners.
```

---

# 2. Provide Context

Context helps the AI understand the situation.

### Example

```text
You are helping a beginner learn Python.
Explain loops using simple language and examples.
```

---

# 3. Specify the Output Format

Tell the AI exactly how you want the answer.

Examples

```text
Answer in bullet points.
```

```text
Provide a table.
```

```text
Return only JSON.
```

```text
Generate Markdown documentation.
```

---

# 4. Iterate and Refine

If the first answer is not satisfactory:

Improve the prompt.

Example

First Prompt

```text
Explain Docker.
```

Improved Prompt

```text
Explain Docker for beginners.
Include architecture, advantages, commands, and one real-world example.
```

Better prompt → Better answer.

---

# Prompt Improvement Example

```text
Poor Prompt
      │
      ▼
General Answer
      │
Improve Prompt
      │
      ▼
Specific Instructions
      │
      ▼
High-Quality Response
```

---

# Ethical Considerations

Prompt engineering should be used responsibly.

---

# 1. Avoid Bias

Do not write prompts that encourage unfair, discriminatory, or harmful outputs.

Instead:

Use neutral and respectful language.

---

# 2. Verify Accuracy

Generative AI can make mistakes.

Always:

* Verify facts.
* Test generated code.
* Review important outputs.

---

# 3. Protect Privacy

Never include confidential information in prompts.

Avoid sharing:

* Passwords
* API Keys
* Bank account details
* Personal identification numbers
* Company confidential data

---

# 4. Use AI Responsibly

AI should:

* Assist developers.
* Improve productivity.
* Support learning.

Developers remain responsible for reviewing and validating AI-generated work.

---

# Ethical AI Workflow

```text
Write Prompt
      │
      ▼
AI Generates Response
      │
      ▼
Review Output
      │
      ▼
Check Accuracy
      │
      ▼
Use Responsibly
```

---

# Hands-on: Writing Coding Prompts

---

## Example 1 – C#

Prompt

```text
Write a C# method that checks whether a string is a palindrome.
Include comments and explain the time complexity.
```

---

## Example 2 – Java

Prompt

```text
Write a Java program to sort an integer array using Bubble Sort.
Explain each step.
```

---

## Example 3 – Python

Prompt

```text
Write a Python function that removes duplicate elements from a list while preserving the original order.
```

---

## Example 4 – SQL

Prompt

```text
Write an SQL query to display the top five highest-paid employees from the Employee table.
```

---

## Example 5 – HTML & CSS

Prompt

```text
Create a responsive login page using HTML and CSS.
Center the login form and make it mobile-friendly.
```

---

## Example 6 – JavaScript

Prompt

```text
Write a JavaScript function that validates an email address using a regular expression.
Include test examples.
```

---

# Complete Example

Suppose a developer needs a REST API.

### Poor Prompt

```text
Write API.
```

The AI has little information.

### Better Prompt

```text
Write a Spring Boot REST API in Java to manage student records.

Requirements:
- CRUD operations
- MySQL database
- Input validation
- Exception handling
- Maven project
- Include sample JSON requests and responses
```

This prompt is specific, provides context, and defines the expected output.

---

# Prompt Engineering Summary

| Topic                      | Purpose                                          |
| -------------------------- | ------------------------------------------------ |
| Prompt Engineering         | Writing effective instructions for AI            |
| Zero-shot Prompting        | Direct instruction without examples              |
| Few-shot Prompting         | Provide examples before asking the task          |
| Chain-of-thought Prompting | Ask for step-by-step reasoning for complex tasks |
| Clear Instructions         | Reduce ambiguity                                 |
| Context                    | Help AI understand the task                      |
| Output Format              | Specify tables, bullets, JSON, etc.              |
| Iteration                  | Improve prompts based on results                 |
| Ethics                     | Avoid bias, verify accuracy, protect privacy     |

---

# Advantages of Prompt Engineering

* Better AI responses
* More accurate code generation
* Faster debugging
* Improved documentation
* Better learning experience
* Higher productivity
* Reduced ambiguity
* Easier automation

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Prompt Engineering?

**Answer:** Prompt Engineering is the process of designing clear and effective prompts that guide an AI model to generate accurate and useful responses.

---

### 2. Why is Prompt Engineering important for developers?

**Answer:** It helps developers generate code, debug programs, create documentation, automate tasks, and obtain more accurate AI responses.

---

### 3. What is Zero-shot Prompting?

**Answer:** Zero-shot prompting asks the AI to perform a task without providing any examples.

---

### 4. What is Few-shot Prompting?

**Answer:** Few-shot prompting provides one or more examples before asking the AI to perform a similar task, improving consistency and accuracy.

---

### 5. What is Chain-of-thought Prompting?

**Answer:** Chain-of-thought prompting asks the AI to reason through a complex problem step by step before producing the final answer.

---

### 6. Name four Prompt Engineering best practices.

**Answer:**

* Write clear instructions.
* Provide relevant context.
* Specify the desired output format.
* Refine and improve prompts based on the results.

---

### 7. What are the ethical considerations when using Generative AI?

**Answer:**

* Avoid biased prompts.
* Verify AI-generated information.
* Protect confidential and personal data.
* Use AI responsibly and review generated content before use.

---

### 8. Give an example of a good coding prompt.

**Answer:**

```text
Write a C# method that finds the maximum element in an integer array.
Include comments, explain the time complexity, and provide sample input and output.
```

---

# Quick Revision (1-Minute)

| Topic              | Key Point                                             |
| ------------------ | ----------------------------------------------------- |
| Prompt Engineering | Writing effective instructions for AI                 |
| Zero-shot          | Direct task without examples                          |
| Few-shot           | Task with guiding examples                            |
| Chain-of-thought   | Reason through complex tasks before answering         |
| Clear Instructions | Improve accuracy                                      |
| Context            | Helps AI understand requirements                      |
| Output Format      | Request tables, JSON, bullets, etc.                   |
| Iteration          | Refine prompts for better results                     |
| Ethics             | Avoid bias, verify outputs, protect privacy           |
| Coding Prompt      | Be specific about language, task, and expected output |
