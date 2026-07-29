# Module: Web Foundations

---

# 1. HTML5 Semantic Elements

### Definition

HTML5 Semantic Elements are HTML tags that clearly describe the purpose and meaning of the content inside them. They improve code readability, SEO, and accessibility.

Older HTML used many `<div>` tags, while HTML5 provides meaningful tags.

---

## Common Semantic Elements

| Element        | Purpose                  |
| -------------- | ------------------------ |
| `<header>`     | Top section of webpage   |
| `<nav>`        | Navigation links         |
| `<section>`    | A section of content     |
| `<article>`    | Independent article/blog |
| `<aside>`      | Sidebar content          |
| `<main>`       | Main webpage content     |
| `<footer>`     | Bottom section           |
| `<figure>`     | Image with caption       |
| `<figcaption>` | Caption of image         |

---

## Example

```html
<!DOCTYPE html>
<html>
<head>
<title>Semantic HTML</title>
</head>

<body>

<header>
    <h1>My Website</h1>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
</nav>

<main>

<section>
    <h2>Latest News</h2>

    <article>
        <h3>AI Technology</h3>
        <p>Artificial Intelligence is changing the world.</p>
    </article>

</section>

<aside>
    Advertisement
</aside>

</main>

<footer>
    Copyright 2026
</footer>

</body>
</html>
```

---

### Output Structure

```
Header

Navigation

Main
   Section
      Article

Sidebar

Footer
```

---

### Advantages

✔ Better SEO

✔ Easy to understand

✔ Improves Accessibility

✔ Easy Maintenance

---

### Cognizant Interview Questions

**Q1. Why use semantic elements instead of div?**

Answer:
Semantic elements clearly describe the purpose of content, making webpages easier for developers, search engines, and screen readers to understand.

---

**Q2. Difference between `<section>` and `<article>`?**

Section = Groups related content.

Article = Independent content that can stand alone.

---

############################################################

# 2. CSS3 Flexbox

### Definition

Flexbox (Flexible Box Layout) is a one-dimensional layout system used to arrange items in a row or column.

Best for:

* Navigation bars
* Cards
* Buttons
* Centering elements

---

## Important Properties

### Parent Properties

```
display: flex;
flex-direction
justify-content
align-items
flex-wrap
gap
```

---

### Child Properties

```
flex
order
align-self
```

---

## Example

```html
<div class="container">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>
```

```css
.container{
display:flex;
justify-content:center;
align-items:center;
gap:20px;
height:200px;
border:2px solid black;
}
```

---

### Output

```
      1    2    3
```

(All items centered.)

---

### justify-content

Controls horizontal alignment.

```
flex-start
center
flex-end
space-between
space-around
space-evenly
```

---

### align-items

Controls vertical alignment.

```
stretch
center
flex-start
flex-end
```

---

### Example

```css
display:flex;
justify-content:space-between;
align-items:center;
```

Output

```
1                    2                    3
```

---

### Advantages

✔ Easy alignment

✔ Responsive design

✔ Less CSS code

---

### Interview Question

**Difference between justify-content and align-items?**

justify-content → Main axis

align-items → Cross axis

---

############################################################

# 3. CSS Grid

### Definition

CSS Grid is a two-dimensional layout system.

It controls both rows and columns.

Used for:

* Dashboards
* Gallery
* Complete webpage layout

---

## Example

```html
<div class="grid">

<div>A</div>
<div>B</div>
<div>C</div>
<div>D</div>

</div>
```

```css
.grid{

display:grid;

grid-template-columns:1fr 1fr;

gap:10px;

}
```

---

### Output

```
A     B

C     D
```

---

### Important Properties

```
display:grid;

grid-template-columns

grid-template-rows

gap

grid-column

grid-row
```

---

### Example

```css
grid-template-columns:100px 200px 100px;
```

Creates

```
100px

200px

100px
```

columns.

---

### Advantages

✔ Best for webpage layouts

✔ Responsive

✔ Controls rows and columns

---

### Flexbox vs Grid

| Flexbox         | Grid             |
| --------------- | ---------------- |
| One-dimensional | Two-dimensional  |
| Row OR Column   | Rows AND Columns |
| Components      | Full Layout      |
| Easier          | More Powerful    |

---

### Interview Question

When should Grid be used?

Answer:

When designing complete webpage layouts involving both rows and columns.

---

############################################################

# 4. JavaScript ES6+

ES6 (ECMAScript 2015) introduced many modern JavaScript features.

---

# 4.1 let and const

### let

Variable can be changed.

```javascript
let age = 20;

age = 25;

console.log(age);
```

Output

```
25
```

---

### const

Cannot be reassigned.

```javascript
const pi = 3.14;

pi = 3.141;
```

Output

```
Error
```

---

### Difference

| let              | const           |
| ---------------- | --------------- |
| Can change value | Cannot reassign |
| Block scope      | Block scope     |

---

### Interview Question

Difference between var, let, and const?

* **var:** Function-scoped, can be redeclared and updated.
* **let:** Block-scoped, can be updated but not redeclared in the same scope.
* **const:** Block-scoped, cannot be reassigned after initialization.

---

############################################################

# 4.2 Arrow Functions

### Definition

Arrow functions provide a shorter syntax for writing functions.

---

### Normal Function

```javascript
function add(a,b){
return a+b;
}

console.log(add(5,3));
```

Output

```
8
```

---

### Arrow Function

```javascript
const add=(a,b)=>a+b;

console.log(add(5,3));
```

Output

```
8
```

---

### Advantages

✔ Short syntax

✔ Cleaner code

✔ Does not have its own `this` (uses surrounding context)

---

### Interview Question

Why use arrow functions?

Because they provide shorter syntax and preserve the surrounding `this` context.

---

############################################################

# 4.3 Promises

### Definition

A Promise represents the result of an asynchronous operation.

A Promise has three states:

* Pending
* Fulfilled
* Rejected

---

### Example

```javascript
let promise = new Promise((resolve,reject)=>{

let success=true;

if(success)
resolve("Login Successful");

else
reject("Login Failed");

});

promise
.then(result=>console.log(result))
.catch(error=>console.log(error));
```

---

Output

```
Login Successful
```

---

### Interview Question

Why are promises used?

Promises help manage asynchronous tasks and avoid callback hell.

---

############################################################

# 4.4 Async and Await

### Definition

`async` and `await` make asynchronous code easier to read and write.

* `async` declares an asynchronous function.
* `await` pauses execution until a Promise resolves.

---

### Example

```javascript
function fetchData(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve("Data Received");

},2000);

});

}

async function display(){

let result=await fetchData();

console.log(result);

}

display();
```

---

Output (after 2 seconds)

```
Data Received
```

---

### Advantages

✔ Cleaner than `.then()`

✔ Easier to debug

✔ Looks like synchronous code

---

### Interview Question

Difference between Promise and async/await?

* **Promise:** Uses `.then()` and `.catch()` to handle asynchronous operations.
* **async/await:** Built on Promises, providing a cleaner and more readable syntax.

---

############################################################

# 4.5 JavaScript Modules

### Definition

Modules allow JavaScript code to be split into multiple files and reused.

---

### File: `math.js`

```javascript
export function add(a,b){
return a+b;
}
```

---

### File: `main.js`

```javascript
import { add } from "./math.js";

console.log(add(10,20));
```

---

Output

```
30
```

---

### Advantages

✔ Code reusability

✔ Better organization

✔ Easy maintenance

✔ Avoids global variable conflicts

---

### Interview Question

Why use modules?

Modules organize code into reusable files, improve maintainability, and prevent global namespace pollution.

---

# Cognizant Technical Assessment – Frequently Asked Questions

1. **What are semantic HTML elements?**
   HTML tags that describe the purpose of the content, improving readability, SEO, and accessibility.

2. **Difference between Flexbox and Grid?**
   Flexbox is one-dimensional (row or column), while Grid is two-dimensional (rows and columns).

3. **Difference between `let`, `const`, and `var`?**
   `var` is function-scoped; `let` and `const` are block-scoped. `const` cannot be reassigned.

4. **What is an arrow function?**
   A concise way to write functions using `=>`.

5. **What is a Promise?**
   An object representing the eventual completion or failure of an asynchronous operation.

6. **Why use `async/await`?**
   It simplifies asynchronous programming by making Promise-based code easier to read.

7. **What are JavaScript modules?**
   Separate files that export and import code, making applications modular and reusable.

