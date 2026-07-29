# Module: Web Accessibility (a11y)

---

# 1. Web Accessibility (a11y)

### Definition

**Web Accessibility (a11y)** means designing and developing websites so that **everyone**, including people with disabilities, can use them effectively.

Accessibility helps users with:

* Visual impairments
* Hearing impairments
* Motor disabilities
* Cognitive disabilities

**Why is Accessibility Important?**

* Equal access for all users
* Better user experience
* Legal compliance (WCAG)
* Improves SEO

---

### Example

```html
<button>Submit</button>
```

A screen reader announces:

```
Button, Submit
```

---

### Advantages

✔ Accessible to everyone

✔ Better SEO

✔ Improved usability

✔ Legal compliance

---

### Cognizant Interview Questions

**Q1. What is Web Accessibility (a11y)?**

Web Accessibility ensures that websites can be used by everyone, including people with disabilities.

**Q2. Why is accessibility important?**

It improves usability, supports users with disabilities, enhances SEO, and helps meet legal standards.

---

############################################################

# 2. WCAG 2.1 Guidelines

### Definition

**WCAG (Web Content Accessibility Guidelines) 2.1** is an international standard that provides recommendations for making web content accessible.

It is based on four principles called **POUR**.

---

## The Four Principles (POUR)

| Principle      | Meaning                                                                 |
| -------------- | ----------------------------------------------------------------------- |
| Perceivable    | Users must be able to perceive the content.                             |
| Operable       | Users must be able to interact with the interface.                      |
| Understandable | Content and controls should be easy to understand.                      |
| Robust         | Content should work with different browsers and assistive technologies. |

---

### Example

```html
<img src="logo.png" alt="Company Logo">
```

The `alt` text helps screen readers describe the image.

---

### WCAG Conformance Levels

| Level | Description                                |
| ----- | ------------------------------------------ |
| A     | Minimum accessibility                      |
| AA    | Standard level (most websites target this) |
| AAA   | Highest accessibility level                |

---

### Advantages

✔ International standard

✔ Better user experience

✔ Supports assistive technologies

---

### Interview Question

**What are the four WCAG principles?**

Perceivable, Operable, Understandable, and Robust (POUR).

---

############################################################

# 3. ARIA Attributes

### Definition

**ARIA (Accessible Rich Internet Applications)** attributes provide additional information to assistive technologies when native HTML semantics are not sufficient.

Common ARIA attributes:

* `aria-label`
* `aria-labelledby`
* `aria-hidden`
* `aria-expanded`
* `aria-live`

---

### Example

```html
<button aria-label="Close Menu">
    X
</button>
```

A screen reader announces:

```
Close Menu Button
```

---

### Another Example

```html
<input
type="text"
aria-label="Search">
```

---

### Advantages

✔ Better screen reader support

✔ Improves accessibility

✔ Useful for dynamic content

---

### Interview Question

**What is ARIA?**

ARIA provides accessibility information for assistive technologies, especially when semantic HTML alone is not enough.

---

############################################################

# 4. Semantic HTML

### Definition

Semantic HTML uses meaningful HTML elements that clearly describe the purpose of the content.

---

### Common Semantic Elements

| Tag         | Purpose             |
| ----------- | ------------------- |
| `<header>`  | Page header         |
| `<nav>`     | Navigation menu     |
| `<main>`    | Main content        |
| `<section>` | Related content     |
| `<article>` | Independent content |
| `<aside>`   | Sidebar             |
| `<footer>`  | Footer              |

---

### Example

```html
<header>

<h1>My Website</h1>

</header>

<nav>

<a href="#">Home</a>

</nav>

<main>

<section>

<h2>News</h2>

</section>

</main>

<footer>

Copyright 2026

</footer>
```

---

### Advantages

✔ Better SEO

✔ Easier maintenance

✔ Improved accessibility

---

### Interview Question

**Why is Semantic HTML important?**

It helps browsers, search engines, and screen readers understand the structure and meaning of the webpage.

---

############################################################

# 5. Keyboard Navigation

### Definition

Keyboard Navigation allows users to access and use a website without a mouse.

Users typically navigate using:

* **Tab**
* **Shift + Tab**
* **Enter**
* **Space**
* **Arrow Keys**

---

### Example

```html
<button>Save</button>

<a href="#">Home</a>

<input type="text">
```

Pressing **Tab** moves the keyboard focus through these elements.

---

### Best Practices

* Ensure all interactive elements are keyboard accessible.
* Keep a visible focus indicator.
* Avoid keyboard traps.
* Use a logical tab order.

---

### Advantages

✔ Helps users with motor disabilities

✔ Faster navigation

✔ Better accessibility

---

### Interview Question

**Why is keyboard navigation important?**

It allows users who cannot use a mouse to access and operate the website.

---

############################################################

# 6. Screen Reader Support

### Definition

A **Screen Reader** is software that reads webpage content aloud for users who are blind or have low vision.

Examples:

* **NVDA**
* **JAWS**
* **VoiceOver** (Apple)

---

### Example

```html
<img src="profile.jpg"
alt="Profile Picture">
```

The screen reader says:

```
Profile Picture
```

Without `alt` text, the image may not be described properly.

---

### Best Practices

✔ Provide `alt` text for images.

✔ Use semantic HTML.

✔ Use proper headings (`<h1>`–`<h6>`).

✔ Label form controls.

---

### Advantages

✔ Supports visually impaired users

✔ Better navigation

✔ Improved accessibility

---

### Interview Question

**What is a Screen Reader?**

A Screen Reader is assistive software that reads webpage content aloud for visually impaired users.

---

############################################################

# 7. Color Contrast

### Definition

Color Contrast is the difference in brightness between text and its background.

Good contrast makes content easier to read, especially for users with low vision or color blindness.

---

### Good Example

```css
body{

background:white;

color:black;

}
```

---

### Poor Example

```css
body{

background:white;

color:lightgray;

}
```

The second example is difficult to read.

---

### WCAG Contrast Ratios

| Text Type                        | Minimum Contrast Ratio |
| -------------------------------- | ---------------------- |
| Normal Text                      | 4.5 : 1                |
| Large Text (18pt+ or 14pt bold+) | 3 : 1                  |

---

### Advantages

✔ Better readability

✔ Supports color-blind users

✔ Meets WCAG standards

---

### Interview Question

**Why is color contrast important?**

It ensures text is readable for users with low vision and helps websites meet accessibility standards.

---

# Web Accessibility (a11y) – Cognizant Technical Assessment Frequently Asked Questions

### 1. What is Web Accessibility (a11y)?

Designing websites so everyone, including people with disabilities, can access and use them.

---

### 2. What does WCAG stand for?

**Web Content Accessibility Guidelines**.

---

### 3. What are the four WCAG principles?

| Principle      | Meaning                           |
| -------------- | --------------------------------- |
| Perceivable    | Users can perceive content        |
| Operable       | Users can interact with content   |
| Understandable | Content is easy to understand     |
| Robust         | Works with assistive technologies |

---

### 4. What is ARIA?

ARIA (Accessible Rich Internet Applications) provides additional accessibility information for assistive technologies.

---

### 5. What is Semantic HTML?

HTML elements that describe the meaning and structure of content, improving accessibility and SEO.

---

### 6. Why is keyboard navigation important?

It allows users who cannot use a mouse to navigate and interact with websites.

---

### 7. What is a Screen Reader?

Software that reads webpage content aloud for users with visual impairments.

---

### 8. Why should images have `alt` text?

So screen readers can describe images to users who cannot see them.

---

### 9. What is the minimum WCAG contrast ratio for normal text?

**4.5 : 1**

---

### 10. Difference between Semantic HTML and ARIA?

| Semantic HTML                                             | ARIA                                                              |
| --------------------------------------------------------- | ----------------------------------------------------------------- |
| Uses meaningful HTML elements like `<header>` and `<nav>` | Adds accessibility information using attributes like `aria-label` |
| Preferred whenever possible                               | Used when semantic HTML alone is not sufficient                   |
| Built into HTML                                           | Enhances accessibility for complex or custom UI                   |

---

# Web Accessibility Interview Quick Revision Table

| Concept                  | Key Point                                                   |
| ------------------------ | ----------------------------------------------------------- |
| Web Accessibility (a11y) | Makes websites usable by everyone                           |
| WCAG 2.1                 | International accessibility guidelines                      |
| POUR                     | Perceivable, Operable, Understandable, Robust               |
| ARIA                     | Accessibility attributes for assistive technologies         |
| Semantic HTML            | Meaningful HTML elements that improve accessibility         |
| Keyboard Navigation      | Enables website use without a mouse                         |
| Screen Reader Support    | Allows content to be read aloud for visually impaired users |
| Color Contrast           | Ensures text is readable against its background             |
| Alt Text                 | Describes images for screen readers                         |
| WCAG AA Contrast         | Minimum **4.5:1** for normal text                           |

