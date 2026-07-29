
Kanban is a **Lean and Agile workflow management method** used to visualize work, improve efficiency, and deliver work continuously. Unlike Scrum, Kanban **does not require fixed-length sprints**. Instead, work items move through different stages as they are completed.

---

# What is Kanban?

## Definition

**Kanban** is a visual project management method that helps teams:

* Visualize workflow
* Limit work in progress (WIP)
* Improve efficiency
* Deliver work continuously
* Identify bottlenecks

The word **Kanban** is a Japanese term meaning **"Visual Card" or "Signboard."**

---

## Real-Life Example

Imagine ordering food at a restaurant.

The order moves through these stages:

```text
Order Taken → Cooking → Ready → Served
```

Everyone can see the current status of the order.

Similarly, software tasks move through different stages on a Kanban board.

---

# Kanban Workflow

```text
To Do  →  In Progress  →  Testing  →  Done
```

Each task moves from left to right until it is completed.

---

# Example

Suppose a team is developing an **Online Shopping Application**.

| To Do   | In Progress | Testing      | Done      |
| ------- | ----------- | ------------ | --------- |
| Payment | Login       | Registration | Dashboard |
| Search  | Cart        |              |           |

The board helps everyone know the status of every task.

---

# 1. Kanban Principles

Kanban follows several key principles.

---

## A. Visualize the Workflow

Represent work visually using a Kanban board.

### Example

Instead of asking,

"What is the status of Login?"

Anyone can simply check the board.

---

## B. Limit Work in Progress (WIP)

Do not start too many tasks at once.

Finish existing work before beginning new work.

### Example

Bad Practice

Developer starts:

* Login
* Dashboard
* Payment
* Search
* Reports

Nothing gets completed quickly.

---

Good Practice

Developer works on:

* Login ✔
* Complete it
* Then start Dashboard

This improves focus and quality.

---

## C. Manage Workflow

Monitor how tasks move through the workflow.

If too many tasks remain in Testing, it indicates a bottleneck.

---

## D. Continuous Improvement

Teams regularly improve their workflow.

Example:

Old process

Testing takes 5 days.

After improvement

Testing takes only 2 days.

---

# Example Kanban Board

```text
----------------------------------------------------
| TO DO | IN PROGRESS | TESTING | DONE             |
----------------------------------------------------
| Login | Dashboard   | Search  | Registration     |
| Cart  | Payment     |         |                  |
----------------------------------------------------
```

---

# 2. Visualizing Work

## Definition

Visualizing work means displaying all tasks on a Kanban board so everyone knows:

* What needs to be done
* What is currently being worked on
* What is completed

---

## Benefits

* Better communication
* Transparency
* Easy progress tracking
* Faster issue detection

---

## Example

Task:

Develop Login Page

Moves through

```text
To Do
   ↓
In Progress
   ↓
Testing
   ↓
Done
```

---

# 3. WIP (Work In Progress) Limits

## Definition

A WIP limit is the **maximum number of tasks allowed in a workflow stage at one time**.

Purpose:

* Prevent overload
* Improve focus
* Increase throughput
* Reduce unfinished work

---

## Example

Kanban Board

| Stage       | WIP Limit |
| ----------- | --------- |
| To Do       | Unlimited |
| In Progress | 2         |
| Testing     | 2         |
| Done        | Unlimited |

If **In Progress = 2 tasks**, no new task can be started until one is completed.

---

### Scenario

Current Tasks

In Progress

* Login
* Dashboard

A new task, Payment, cannot be started until Login or Dashboard is finished.

---

## Advantages

* Better quality
* Faster completion
* Reduced multitasking
* Easier workload management

---

# 4. Cumulative Flow Diagram (CFD)

## Definition

A **Cumulative Flow Diagram (CFD)** is a chart that shows how many tasks are in each workflow stage over time.

It helps identify:

* Workflow stability
* Bottlenecks
* Delivery speed
* Team performance

---

## Example

Week 1

| Stage       | Tasks |
| ----------- | ----- |
| To Do       | 10    |
| In Progress | 2     |
| Testing     | 1     |
| Done        | 2     |

Week 2

| Stage       | Tasks |
| ----------- | ----- |
| To Do       | 7     |
| In Progress | 2     |
| Testing     | 2     |
| Done        | 4     |

The number of completed tasks ("Done") increases over time, indicating progress.

---

### Simple CFD Representation

```text
Tasks
 ^
 |                         Done
 |                      /
 |                  ___/
 |              ___/
 |         ____/
 |______/__________________> Time

To Do decreases gradually.
Done increases steadily.
```

---

## Why CFD is Useful

* Detects bottlenecks
* Tracks progress
* Measures workflow efficiency
* Predicts future delivery

---

# 5. Continuous Delivery

## Definition

Continuous Delivery means software is always in a **deployable state**, allowing new features and fixes to be released quickly whenever needed.

Unlike Scrum, Kanban does **not wait for the end of a sprint**.

---

## Example

Shopping Application

Monday

Login completed

↓

Deploy immediately

Wednesday

Payment completed

↓

Deploy immediately

Friday

Search completed

↓

Deploy immediately

There is no need to wait for a sprint to finish.

---

## Benefits

* Faster customer feedback
* Frequent software releases
* Lower deployment risk
* Faster bug fixes
* Higher customer satisfaction

---

# Scrum vs Kanban

| Scrum                                      | Kanban                                            |
| ------------------------------------------ | ------------------------------------------------- |
| Fixed-length sprints (2–4 weeks)           | Continuous workflow                               |
| Sprint Backlog                             | Kanban Board                                      |
| Scrum Master role                          | No mandatory Scrum Master                         |
| Sprint Planning required                   | Work pulled as capacity becomes available         |
| Changes usually wait until the next sprint | Changes can be added anytime (if capacity allows) |
| Team commits to sprint work                | Focus on continuous flow                          |

---

# Complete Example

A team is building an **Online Banking Application**.

### Kanban Board

| To Do         | In Progress | Testing   | Done         |
| ------------- | ----------- | --------- | ------------ |
| Fund Transfer | Login       | Dashboard | Registration |
| Loan Module   | Payment     |           |              |

### WIP Limit

In Progress = **2**

Current tasks:

* Login
* Payment

Since the limit is reached, **Fund Transfer** cannot move into **In Progress** until one task is completed.

### Continuous Delivery

Monday:

* Registration completed → Deploy

Wednesday:

* Login completed → Deploy

Friday:

* Dashboard completed → Deploy

Customers receive new features without waiting for a sprint to end.

---

# Advantages of Kanban

* Easy to understand and implement
* Visualizes all work clearly
* Reduces multitasking
* Improves productivity
* Identifies bottlenecks quickly
* Supports continuous improvement
* Enables continuous delivery
* Adapts easily to changing priorities

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Kanban?

**Answer:** Kanban is a Lean and Agile workflow management method that visualizes work, limits work in progress, and improves the continuous flow of tasks.

### 2. What are the main Kanban principles?

**Answer:**

* Visualize the workflow
* Limit Work in Progress (WIP)
* Manage workflow
* Continuously improve the process

### 3. What is a Kanban Board?

**Answer:** A visual board that shows the status of work using columns such as **To Do**, **In Progress**, **Testing**, and **Done**.

### 4. What is a WIP Limit?

**Answer:** A Work In Progress limit is the maximum number of tasks allowed in a workflow stage at one time to prevent overload and improve efficiency.

### 5. What is a Cumulative Flow Diagram (CFD)?

**Answer:** A chart that displays the number of tasks in each workflow stage over time, helping teams monitor progress and identify bottlenecks.

### 6. What is Continuous Delivery?

**Answer:** Continuous Delivery is the practice of keeping software ready for deployment so completed features can be released quickly and frequently.

### 7. Kanban vs Scrum?

**Answer:** Scrum uses fixed-length sprints with defined Scrum roles and ceremonies, whereas Kanban uses a continuous workflow, visual boards, WIP limits, and continuous delivery without mandatory sprints.

---

# Quick Revision (1-Minute)

| Topic                   | Key Point                                                   |
| ----------------------- | ----------------------------------------------------------- |
| Kanban                  | Visual workflow management method                           |
| Kanban Board            | Displays task status (To Do → In Progress → Testing → Done) |
| Visualizing Work        | Makes progress transparent and easy to track                |
| WIP Limits              | Restrict the number of active tasks to improve flow         |
| Cumulative Flow Diagram | Shows task flow and helps detect bottlenecks                |
| Continuous Delivery     | Release completed features whenever they are ready          |
| Main Goal               | Improve workflow efficiency and deliver value continuously  |

