# Module: Responsive Design 

---

# 1. Mobile-First Design

### Definition

Mobile-First Design is an approach where a website is designed for **mobile devices first**, then enhanced for tablets and desktops using media queries.

**Why Mobile-First?**

* Most users browse on mobile devices.
* Faster loading on small devices.
* Better user experience.
* Easier to scale to larger screens.

---

### Example

```css
/* Mobile Design */
.container{
    font-size:16px;
    padding:10px;
}

/* Desktop Design */
@media (min-width:768px){
    .container{
        font-size:20px;
        padding:20px;
    }
}
```

---

### Output

* **Mobile:** Small font and padding.
* **Desktop:** Larger font and padding.

---

### Advantages

✔ Better mobile performance

✔ Easier responsive development

✔ Improved SEO

✔ Better user experience

---

### Cognizant Interview Questions

**Q1. What is Mobile-First Design?**

Mobile-First Design means designing the website for mobile devices first and then adding styles for larger screens.

**Q2. Why is Mobile-First preferred?**

Because most users access websites from mobile devices, and it improves performance and usability.

---

############################################################

# 2. Media Queries

### Definition

Media Queries allow different CSS styles to be applied based on the device's screen size, resolution, or orientation.

---

### Syntax

```css
@media (condition){
    /* CSS Code */
}
```

---

### Example

```css
body{
    background-color:white;
}

@media (max-width:600px){
    body{
        background-color:lightblue;
    }
}
```

---

### Output

* Screen width **greater than 600px** → White background.
* Screen width **600px or less** → Light blue background.

---

### Common Breakpoints

| Device  | Width            |
| ------- | ---------------- |
| Mobile  | 0–767px          |
| Tablet  | 768–1023px       |
| Laptop  | 1024–1439px      |
| Desktop | 1440px and above |

---

### Advantages

✔ Responsive layouts

✔ Better readability

✔ Supports multiple devices

---

### Interview Question

**What is a Media Query?**

A Media Query applies CSS styles based on screen size or device characteristics.

---

############################################################

# 3. Fluid Layouts

### Definition

A Fluid Layout automatically adjusts according to the screen size using **relative units** like `%`, `vw`, and `em` instead of fixed pixels.

---

### Example

```css
.container{
    width:80%;
    margin:auto;
}
```

---

### Output

* On small screens → Container becomes narrower.
* On large screens → Container becomes wider automatically.

---

### Fixed Layout vs Fluid Layout

| Fixed Layout       | Fluid Layout                |
| ------------------ | --------------------------- |
| Uses pixels (`px`) | Uses `%`, `vw`, `em`, `rem` |
| Fixed width        | Flexible width              |
| Less responsive    | Fully responsive            |

---

### Advantages

✔ Adapts to different screens

✔ Better responsiveness

✔ Less scrolling

---

### Interview Question

**What is a Fluid Layout?**

A layout that resizes automatically using relative units instead of fixed widths.

---

############################################################

# 4. CSS Grid & Flexbox

## CSS Flexbox

### Definition

Flexbox is a **one-dimensional** layout system used to arrange items in a row or column.

---

### Example

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
}
```

---

### Output

```text
1    2    3
```

---

## CSS Grid

### Definition

CSS Grid is a **two-dimensional** layout system that controls both rows and columns.

---

### Example

```css
.container{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}
```

---

### Output

```text
A     B

C     D
```

---

### Flexbox vs Grid

| Flexbox             | Grid                  |
| ------------------- | --------------------- |
| One-dimensional     | Two-dimensional       |
| Best for components | Best for full layouts |
| Easier to learn     | More powerful         |

---

### Advantages

✔ Responsive layouts

✔ Easy alignment

✔ Cleaner code

---

### Interview Question

**When should Flexbox be used instead of Grid?**

Use Flexbox for arranging items in a single row or column. Use Grid for complete page layouts involving rows and columns.

---

############################################################

# 5. Viewport Units

### Definition

Viewport units size elements relative to the browser window.

---

### Common Units

| Unit   | Meaning                             |
| ------ | ----------------------------------- |
| `vw`   | 1% of viewport width                |
| `vh`   | 1% of viewport height               |
| `vmin` | Smaller of viewport width or height |
| `vmax` | Larger of viewport width or height  |

---

### Example

```css
.box{
    width:50vw;
    height:50vh;
    background:lightgreen;
}
```

---

### Output

If browser size is **1000px × 800px**:

* Width = **500px**
* Height = **400px**

---

### Advantages

✔ Responsive sizing

✔ Adapts to screen size

✔ Less need for media queries

---

### Interview Question

**What does `100vh` mean?**

It means the element's height is equal to **100% of the viewport height**.

---

############################################################

# 6. Container Queries

### Definition

Container Queries allow styles to change based on the **size of a parent container**, rather than the entire browser window.

Unlike Media Queries, which depend on the viewport, Container Queries depend on the container's dimensions.

---

### Example

```css
.card-container{
    container-type:inline-size;
}

@container (min-width:500px){

.card{
    display:flex;
}

}
```

---

### Output

* If the container width is **500px or more**, the card is displayed using Flexbox.
* If the container is smaller, the default layout is used.

---

### Media Query vs Container Query

| Media Query            | Container Query                |
| ---------------------- | ------------------------------ |
| Based on viewport size | Based on parent container size |
| Responsive page layout | Responsive components          |
| Uses `@media`          | Uses `@container`              |

---

### Advantages

✔ Better reusable components

✔ Component-level responsiveness

✔ Easier maintenance

---

### Interview Question

**Why use Container Queries?**

Container Queries make components responsive based on the size of their parent container, making them more reusable in different layouts.

---

# Responsive Design – Cognizant Technical Assessment Frequently Asked Questions

### 1. What is Responsive Design?

Responsive Design is a web design approach that ensures a website adapts to different screen sizes and devices.

---

### 2. What is Mobile-First Design?

Designing for mobile devices first and then enhancing the layout for tablets and desktops.

---

### 3. What are Media Queries?

CSS rules that apply styles based on screen size or other device characteristics.

---

### 4. What is a Fluid Layout?

A layout that uses relative units such as `%`, `vw`, or `rem` to adapt to different screen sizes.

---

### 5. Difference between Flexbox and Grid?

| Flexbox                | Grid                            |
| ---------------------- | ------------------------------- |
| One-dimensional layout | Two-dimensional layout          |
| Row or column          | Rows and columns                |
| Ideal for components   | Ideal for complete page layouts |

---

### 6. What are Viewport Units?

Viewport units (`vw`, `vh`, `vmin`, `vmax`) size elements relative to the browser window.

---

### 7. What is `100vw`?

It means the element's width equals **100% of the viewport width**.

---

### 8. What is `100vh`?

It means the element's height equals **100% of the viewport height**.

---

### 9. What are Container Queries?

CSS rules that style elements based on the size of their parent container instead of the viewport.

---

### 10. Difference between Media Queries and Container Queries?

| Media Queries                | Container Queries                 |
| ---------------------------- | --------------------------------- |
| Based on screen size         | Based on parent container size    |
| Used for page responsiveness | Used for component responsiveness |

---

# Responsive Design Interview Quick Revision Table

| Concept             | Key Point                                                  |
| ------------------- | ---------------------------------------------------------- |
| Responsive Design   | Adapts web pages to different devices and screen sizes     |
| Mobile-First Design | Design for mobile first, then scale up                     |
| Media Queries       | Apply CSS based on viewport size                           |
| Fluid Layouts       | Use relative units (`%`, `vw`, `rem`) for flexible layouts |
| Flexbox             | One-dimensional layout (row or column)                     |
| CSS Grid            | Two-dimensional layout (rows and columns)                  |
| Viewport Units      | `vw`, `vh`, `vmin`, `vmax` for responsive sizing           |
| Container Queries   | Style components based on the parent container size        |

