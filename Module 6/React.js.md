# Module: React.js

---

# 1. JSX (JavaScript XML)

### Definition

JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code inside JavaScript. React converts JSX into regular JavaScript using Babel.

**Why use JSX?**

* Easier to write UI
* Improves readability
* Allows JavaScript expressions inside HTML

---

### Syntax

```jsx
const element = <h1>Hello React!</h1>;
```

---

### Example

```jsx
function App() {
  return (
    <h1>Welcome to React</h1>
  );
}

export default App;
```

**Output**

```
Welcome to React
```

---

### JavaScript Expression in JSX

```jsx
function App() {
  const name = "John";

  return <h1>Hello {name}</h1>;
}
```

**Output**

```
Hello John
```

---

### Rules of JSX

* Must return a single parent element.
* Close all tags.
* Use `className` instead of `class`.
* JavaScript expressions are enclosed in `{}`.

---

### Example

```jsx
return (
  <div>
    <h1>Hello</h1>
    <p>React</p>
  </div>
);
```

---

### Advantages

✔ Easy to read

✔ Looks like HTML

✔ Supports JavaScript expressions

✔ Faster UI development

---

### Cognizant Interview Questions

**Q1. What is JSX?**

JSX is a syntax extension that allows writing HTML-like code inside JavaScript. It is converted into JavaScript by Babel.

**Q2. Why use `className` instead of `class`?**

Because `class` is a reserved keyword in JavaScript.

---

############################################################

# 2. Components

### Definition

A Component is a reusable piece of UI. Every React application is built using components.

Types of Components:

* Functional Component
* Class Component (older approach)

Today, Functional Components are preferred.

---

### Functional Component Example

```jsx
function Welcome() {
  return <h1>Welcome to React</h1>;
}

export default Welcome;
```

---

### Using Component

```jsx
import Welcome from "./Welcome";

function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}
```

---

### Output

```
Welcome to React
```

---

### Advantages

✔ Reusable

✔ Easy to maintain

✔ Modular code

✔ Independent UI blocks

---

### Interview Question

**What is a React component?**

A reusable JavaScript function that returns JSX to display part of the user interface.

---

############################################################

# 3. Props (Properties)

### Definition

Props are used to pass data from a Parent Component to a Child Component.

Props are **read-only**.

---

### Child Component

```jsx
function Student(props) {
  return <h2>Name: {props.name}</h2>;
}

export default Student;
```

---

### Parent Component

```jsx
import Student from "./Student";

function App() {
  return (
    <Student name="Rahul" />
  );
}
```

---

### Output

```
Name: Rahul
```

---

### Multiple Props

```jsx
function Student(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>{props.age}</p>
    </div>
  );
}
```

```jsx
<Student name="Rahul" age="20" />
```

---

### Advantages

✔ Pass data

✔ Reusable components

✔ Parent-child communication

---

### Interview Question

**Can props be modified?**

No. Props are immutable (read-only).

---

############################################################

# 4. State

### Definition

State stores data that can change during the component's lifetime.

When state changes, React automatically updates the UI.

---

### Example

```jsx
import { useState } from "react";

function Counter() {

  const [count, setCount] = useState(0);

  return (
    <div>

      <h2>{count}</h2>

      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>

    </div>
  );
}
```

---

### Output

Initially

```
0
```

After Button Click

```
1
```

---

### Props vs State

| Props                  | State                    |
| ---------------------- | ------------------------ |
| Passed from parent     | Managed inside component |
| Read-only              | Can change               |
| Used for communication | Used for dynamic data    |

---

### Interview Question

**Difference between Props and State?**

Props are passed from the parent and cannot be modified by the child. State belongs to the component and can be updated using state setter functions.

---

############################################################

# 5. Hooks

Hooks allow Functional Components to use React features like state and lifecycle methods.

---

# 5.1 useState()

### Definition

`useState()` is used to create and update state.

---

### Syntax

```jsx
const [state, setState] = useState(initialValue);
```

---

### Example

```jsx
import { useState } from "react";

function App() {

  const [name, setName] = useState("John");

  return (

    <div>

      <h2>{name}</h2>

      <button onClick={() => setName("David")}>
        Change
      </button>

    </div>

  );
}
```

---

### Output

Initially

```
John
```

After Click

```
David
```

---

### Advantages

✔ Simple state management

✔ Automatic UI update

---

### Interview Question

**Why use useState()?**

To store and update data inside Functional Components.

---

############################################################

# 5.2 useEffect()

### Definition

`useEffect()` performs side effects such as:

* API calls
* Timers
* Event listeners
* Updating the document title

---

### Syntax

```jsx
useEffect(() => {

}, []);
```

---

### Example

```jsx
import { useEffect } from "react";

function App() {

  useEffect(() => {
    console.log("Component Loaded");
  }, []);

  return <h1>Hello</h1>;
}
```

---

### Output

```
Component Loaded
```

Runs only once because the dependency array is empty.

---

### Dependency Array

```jsx
useEffect(() => {
   console.log("Runs every render");
});
```

Runs after every render.

---

```jsx
useEffect(() => {
   console.log("Runs once");
}, []);
```

Runs only once.

---

```jsx
useEffect(() => {
   console.log("Runs when count changes");
}, [count]);
```

Runs only when `count` changes.

---

### Advantages

✔ API requests

✔ Timers

✔ Lifecycle replacement

---

### Interview Question

**Why use useEffect()?**

To perform side effects such as fetching data, updating the DOM, or setting up subscriptions.

---

############################################################

# 5.3 useContext()

### Definition

`useContext()` allows data to be shared across multiple components without passing props manually (avoids **prop drilling**).

---

### Create Context

```jsx
import { createContext } from "react";

export const UserContext = createContext();
```

---

### Provide Context

```jsx
<UserContext.Provider value="John">
    <Home />
</UserContext.Provider>
```

---

### Consume Context

```jsx
import { useContext } from "react";
import { UserContext } from "./UserContext";

function Home() {

  const user = useContext(UserContext);

  return <h1>{user}</h1>;
}
```

---

### Output

```
John
```

---

### Advantages

✔ Avoids prop drilling

✔ Global data sharing

✔ Cleaner code

---

### Interview Question

**What problem does useContext solve?**

It allows sharing data across components without passing props through every intermediate component.

---

############################################################

# 6. Routing (React Router)

### Definition

React Router enables navigation between different pages in a Single Page Application (SPA) without reloading the page.

---

### Install

```bash
npm install react-router-dom
```

---

### Example

```jsx
import {
BrowserRouter,
Routes,
Route
} from "react-router-dom";

function Home() {
  return <h1>Home</h1>;
}

function About() {
  return <h1>About</h1>;
}

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Home />} />

        <Route path="/about" element={<About />} />

      </Routes>

    </BrowserRouter>

  );
}
```

---

### Output

```
/        → Home

/about   → About
```

---

### Navigation

```jsx
import { Link } from "react-router-dom";

<Link to="/">Home</Link>

<Link to="/about">About</Link>
```

---

### Advantages

✔ Fast navigation

✔ No page reload

✔ Supports dynamic routes

---

### Interview Question

**Why use React Router?**

To navigate between different pages in a React Single Page Application without refreshing the browser.

---

############################################################

# 7. State Management

### Definition

State Management is the process of storing, updating, and sharing application data efficiently.

There are three common levels:

* Local State (`useState`)
* Shared State (`useContext`)
* Global State (Redux, Zustand, etc.)

---

### Local State Example

```jsx
const [count, setCount] = useState(0);
```

---

### Shared State Example

```jsx
<UserContext.Provider value={theme}>
    <App />
</UserContext.Provider>
```

---

### Redux Example (Basic)

```jsx
const initialState = {
  count: 0
};
```

Redux stores application data in a central store.

---

### State Management Comparison

| Method     | Best Used For                                |
| ---------- | -------------------------------------------- |
| useState   | Local component state                        |
| useContext | Shared data across components                |
| Redux      | Large applications with complex global state |

---

### Advantages

✔ Centralized data management

✔ Easier debugging

✔ Predictable application behavior

✔ Reduces unnecessary prop passing

---

### Interview Question

**When should Redux be used instead of useState?**

Use `useState` for local component data. Use Redux (or another global state library) when many components need access to the same data or the application has complex state logic.

---

# React.js – Cognizant Technical Assessment Frequently Asked Questions

1. **What is JSX?**
   JSX is a syntax extension that allows writing HTML-like code inside JavaScript.

2. **What is a React Component?**
   A reusable JavaScript function that returns JSX to build the user interface.

3. **What are Props?**
   Props are read-only inputs passed from a parent component to a child component.

4. **What is State?**
   State is mutable data managed within a component that triggers UI updates when changed.

5. **What is `useState()`?**
   A Hook used to create and update state in functional components.

6. **What is `useEffect()`?**
   A Hook used for side effects such as API calls, timers, and DOM updates.

7. **What is `useContext()`?**
   A Hook that allows components to share data without prop drilling.

8. **Why use React Router?**
   It enables client-side routing in Single Page Applications without full page reloads.

9. **What is State Management?**
   It is the process of managing application data using tools like `useState`, `useContext`, or Redux.

10. **Difference between Props and State?**

| Props                  | State                       |
| ---------------------- | --------------------------- |
| Passed from parent     | Managed inside component    |
| Read-only              | Mutable                     |
| Used for communication | Used for dynamic UI updates |

