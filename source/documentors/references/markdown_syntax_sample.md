(MyST Markdown Syntax Sample)=

# MyST Markdown Syntax Sample

This page demonstrates MyST Markdown syntax using examples that correspond to the RST quick reference guide. This serves as a practical example of how to write Open edX documentation using MyST Markdown.

```{contents} Contents
:depth: 1
:local:
```

## Section Structure Example

This demonstrates how to structure content with multiple heading levels and sections.

### Subsection Example

Content for this subsection to demonstrate heading hierarchy.

### Another Subsection

More content to show section organization.

## Inline Markup Demonstration

This section shows various **bold** formatting, *italic* text, and `mono-spaced` code snippets. You can also create {guilabel}`GUI elements` that stand out in the documentation.

## Lists and Organization

You can create both numbered and bulleted lists:

1. First ordered item

   * Sub-item under first item
   * Another sub-item

2. Second ordered item

Here's an unordered list:

* First bullet point

  1. Numbered sub-item
  2. Another numbered sub-item

* Second bullet point

## Linking Examples

### External Links

You can have [inline links](https://example.com) or use [reference-style links] for cleaner text when the same link appears multiple times.

[reference-style links]: http://example.com/?lorem=Lorem%20ipsum%20dolor%20sit

### Internal Document Links

(sample_location)=
#### Sample Location Target

This heading has a label that can be referenced from elsewhere.

You can link back to {ref}`sample_location` from anywhere in the document.

### Cross-Document Links

Link to {doc}`quick_reference` or other documentation files using the doc role.

## Directives and Admonitions

MyST Markdown supports many useful directives:

```{warning}
This is a warning directive.

It will be styled to stand out in the documentation.
```

```{note}
This is a note directive.

It will stand out but not as much as a warning.
```

```{seealso}
[Open edX Documentation](https://docs.openedx.org)
: Link to the main documentation site

[MyST Parser Documentation](https://myst-parser.readthedocs.io/)
: Complete MyST Markdown documentation
```

## Code Examples

Here's a Python code block:

```python
def hello_world():
    """A simple function demonstration."""
    print("Hello, Open edX documentation!")
    return True
```

And here's some generic code:

```
Generic code block without syntax highlighting.
Could be configuration files or pseudo-code.
```

## Images and Media

```{image} /_static/open-edx-logo-color.png
:alt: Open edX Logo
:width: 200px
```

## Tables

Here's a simple table in Markdown format:

| Feature | RST | MyST Markdown |
|---------|-----|---------------|
| Headings | Underlines with symbols | Hash symbols (#) |
| Bold text | `**bold**` | `**bold**` |
| Code blocks | `.. code-block::` | ```` ```language ```` |
| Directives | `.. directive::` | ```` ```{directive} ```` |

## Sidebars and Special Content

```{sidebar} Sample Sidebar
This is sidebar content that appears alongside the main text. It's useful for:
- Additional context
- Related information
- Quick tips
```

## Substitutions

MyST Markdown supports substitutions just like RST. These would be defined in the substitutions.txt file:

A line of text with a |Platform name| substitution inserted.

## Advanced Features

### Tab Sets (like in the quick reference)

`````{tab-set}

````{tab-item} Option A
This is content for the first tab.

```python
# Python code in tab A
print("Tab A content")
```
````

````{tab-item} Option B
This is content for the second tab.

```javascript
// JavaScript code in tab B
console.log("Tab B content");
```

````
`````

### Complex Nested Content

````{note}
This note contains nested content:

1. A numbered list item

   ```python
   # Code within a list within a note
   def nested_example():
       return "Complex nesting works!"
   ```

2. Another item with **bold** and *italic* text

   ```{warning}
   Even warnings can be nested inside notes!
   ```
````

## Conclusion

This sample demonstrates the key MyST Markdown features available for Open edX documentation. The syntax is clean, readable, and powerful enough to handle complex documentation needs while remaining approachable for new contributors.

---

**Maintenance Chart**

| Review Date | Working Group Reviewer | Release | Test Situation |
|-------------|------------------------|---------|----------------|
|             |                        |         |                |
