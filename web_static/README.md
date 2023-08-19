# AirBnB Clone Project

This project involves creating a series of HTML pages and stylesheets to build a user interface for an AirBnB-like application. Each step involves implementing specific layout and styling requirements.

## Project Structure

The project consists of several HTML files and CSS files, organized into directories according to their purpose.

### Directory Structure

- `web_static/`
  - `0-index.html`: HTML page with inline styling for header and footer.
  - `1-index.html`: HTML page with head tag styling for header and footer.
  - `2-index.html`: HTML page with external CSS files for header and footer.
  - `3-index.html`: HTML page with enhanced styling using external CSS files.
  - `4-index.html`: HTML page with filters box and search button.
  - `5-index.html`: HTML page with extended filters box.
  - `6-index.html`: HTML page with dropdowns in filters box.
  - `7-index.html`: HTML page with filters and results sections.
  - `8-index.html`: HTML page with detailed place information.
  - `100-index.html`: HTML page with improved place information.
  - `101-index.html`: HTML page with Flexbox layout for places.
  - `102-index.html`: HTML page with responsive design.
  - `103-index.html`: HTML page with enhanced accessibility support.

- `styles/`
  - `2-common.css`: Global style (body).
  - `2-header.css`: Header style.
  - `2-footer.css`: Footer style.
  - `3-common.css`: Global style (body).
  - `3-header.css`: Header style.
  - `3-footer.css`: Footer style.
  - `4-common.css`: Global style (body and .container styles).
  - `3-header.css`: Header style.
  - `3-footer.css`: Footer style.
  - `4-filters.css`: Filters style.
  - `5-filters.css`: Filters style.
  - `6-filters.css`: Filters style.
  - `7-places.css`: Places style.
  - `8-places.css`: Places style.
  - `100-places.css`: Improved places style.
  - `101-places.css`: Flexbox layout for places.
  - `102-common.css`: Common style for responsive design.
  - `102-header.css`: Header style for responsive design.
  - `102-footer.css`: Footer style for responsive design.
  - `102-filters.css`: Filters style for responsive design.
  - `102-places.css`: Places style for responsive design.
  - `103-common.css`: Common style for accessibility.
  - `103-header.css`: Header style for accessibility.
  - `103-footer.css`: Footer style for accessibility.
  - `103-filters.css`: Filters style for accessibility.
  - `103-places.css`: Places style for accessibility.

- `images/`: Folder to store images.

## Usage Instructions

1. Clone the GitHub repository: [AirBnB_clone](https://github.com/your_username/AirBnB_clone)
2. Navigate to the `web_static` directory.
3. Open the desired HTML file in a web browser to view the corresponding page.
4. The CSS files in the `styles` directory provide styling for the HTML pages.

## Additional Steps

### 9. Display Additional Place Information

Layout: (based on 8-index.html)

- Add more information to a Place article:
  - List of Amenities:
    - `<div>` with classname `amenities`
    - Margin top 40px
    - Contains:
      - Title:
        - `<h2>` with text "Amenities"
        - Font size 16px
        - Border bottom #DDDDDD 1px
    - List of amenities:
      - `<ul>` and `<li>` for each amenity
      - No list style
      - Icons on the left: Pet friendly, TV, Wifi, etc…

  - List of Reviews:
    - `<div>` with classname `reviews`
    - Margin top 40px
    - Contains:
      - Title:
        - `<h2>` with text "Reviews"
        - Font size 16px
        - Border bottom #DDDDDD 1px
    - List of review:
      - `<ul>` and `<li>` for each review
      - No list style
      - A review is described by:
        - `<h3>` tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
        - `<p>` tag for the text (font size 12px)

### 10. Flex (Advanced)

Improve the Places section by using Flexible boxes for all Place articles.

[Flexbox Froggy](https://flexboxfroggy.com/) is a great resource for learning about Flexbox.

### 11. Responsive Design (Advanced)

Improve the page by adding responsive design to display correctly on mobile or small screens.

### 12. Accessibility (Advanced)

Improve the page by adding Accessibility support.

## Credits

This project is inspired by the AirBnB platform and its user interface.

