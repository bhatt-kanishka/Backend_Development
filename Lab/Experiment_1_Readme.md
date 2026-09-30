# Experiment 1: Demonstration of HTML5 Elements

## Overview
This laboratory experiment demonstrates fundamental and advanced HTML5 elements, including modern semantic markup, responsive structure, complex interactive forms, tabular data representation, multimedia integration, and graphics canvas rendering.

**Target File:** [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1.html)

---

## Objectives
* Understand and implement HTML5 semantic tags for accessibility and structured layout.
* Build comprehensive user input forms using modern HTML5 input types, attributes, and validation.
* Structure tabular data with headers and cell alignment.
* Embed multimedia elements (`<audio>` and `<video>`) without third-party plugins.
* Utilize `<canvas>` for programmatic 2D graphic rendering.

---

## File Breakdown

### [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1.html)
Contains a complete single-page demonstration structured into modular sections:

1. **Header & Navigation (`<header>`, `<nav>`)**:
   - Site title and lab description.
   - Anchor navigation links pointing to in-page section IDs (`#about`, `#form`, `#media`, `#contact`).

2. **Semantic Elements Section (`<section>`, `<article>`, `<aside>`)**:
   - Demonstrates `<article>` containing explanatory text about HTML5 features.
   - Highlights semantic tags: `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, and `<footer>`.
   - Demonstrates `<figure>` and `<figcaption>` for captioned media.
   - Demonstrates `<aside>` for callout information / sidebars.

3. **Data Representation (`<table>`)**:
   - A structured student information table showcasing `<table>`, `<tr>`, `<th>`, and `<td>` with custom borders and styling.

4. **Comprehensive Form Controls (`<form>`)**:
   - Text Input (`type="text"`)
   - Email Input (`type="email"`)
   - Password Input (`type="password"`)
   - Date Picker (`type="date"`)
   - Telephone Input (`type="tel"`)
   - Search Input (`type="search"`)
   - Radio Buttons (`type="radio"`) for gender selection
   - Checkboxes (`type="checkbox"`) for multi-select skills (HTML, CSS, JS)
   - Dropdown selection (`<select>`, `<option>`)
   - Multiline text input (`<textarea>`)
   - Submit Button (`type="submit"`)

5. **Multimedia Controls (`<audio>`, `<video>`)**:
   - Native `<audio controls>` player with fallback message.
   - Native `<video controls>` player with width constraints and format sources.

6. **Canvas Element (`<canvas>`)**:
   - Canvas container configured with JavaScript context scripting (`getContext('2d')`) for drawing shapes and text directly on the page.

---

## How to View and Test

1. **Directly in Browser**:
   - Open `Experiment-1.html` in any modern web browser (Google Chrome, Firefox, Edge, Safari):
     ```bash
     # In Windows PowerShell:
     Start-Process "Experiment-1.html"
     ```

2. **Using a Local Static Server**:
   ```bash
   npx serve .
   # Or using Python:
   python -m http.server 8080
   ```
   Navigate to `http://localhost:8080/Experiment-1.html`.
