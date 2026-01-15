# HTML & CSS Responsive Website

A modern, responsive website built with HTML5, CSS3, and vanilla JavaScript, demonstrating front-end development best practices.

## 📋 Features

- Fully responsive design
- Modern CSS Grid and Flexbox layouts
- Mobile-first approach
- Cross-browser compatibility
- Semantic HTML5
- CSS animations and transitions
- Interactive JavaScript components
- Multi-page structure

## 🏗️ Project Structure

```
html-css-app/
├── index.html              # Home page
├── pages/
│   ├── about.html         # About page
│   ├── services.html      # Services page
│   └── contact.html       # Contact page
├── css/
│   ├── styles.css         # Main stylesheet
│   ├── responsive.css     # Responsive styles
│   └── animations.css     # Animation styles
├── js/
│   ├── main.js           # Main JavaScript
│   └── utils.js          # Utility functions
├── images/
│   └── .gitkeep
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Any modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Local web server for development

### Installation

1. **Clone the repository:**
```bash
cd html-css-app
```

2. **Open in browser:**
   - Simply open `index.html` in your web browser
   - Or use a local server:

**Using Python:**
```bash
python -m http.server 8000
```

**Using Node.js (http-server):**
```bash
npx http-server -p 8000
```

**Using PHP:**
```bash
php -S localhost:8000
```

3. **Access the website:**
   - Navigate to `http://localhost:8000`

## 📱 Responsive Breakpoints

- **Mobile:** < 768px
- **Tablet:** 768px - 1024px
- **Desktop:** > 1024px

## 🎨 Features Demonstrated

### HTML5
- Semantic elements (header, nav, main, section, article, footer)
- Forms with validation
- Accessibility features (ARIA labels, alt text)

### CSS3
- CSS Grid and Flexbox layouts
- CSS Variables (Custom Properties)
- Media queries for responsiveness
- Transitions and animations
- Modern selectors and pseudo-classes

### JavaScript
- DOM manipulation
- Event handling
- Form validation
- Mobile menu toggle
- Smooth scrolling

## 🌐 Pages

### Home (index.html)
- Hero section
- Features showcase
- Call-to-action sections

### About (pages/about.html)
- Company information
- Team section
- Mission and values

### Services (pages/services.html)
- Service offerings
- Pricing information
- Feature comparison

### Contact (pages/contact.html)
- Contact form
- Location information
- Social media links

## 🎯 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Customization

### Colors
Edit CSS variables in `css/styles.css`:
```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --text-color: #333;
  --background-color: #fff;
}
```

### Layout
Modify grid and flexbox properties in respective CSS files.

### Content
Update HTML files with your own content, images, and text.

## 🔧 Development

### Adding New Pages
1. Create new HTML file in `pages/` directory
2. Copy structure from existing pages
3. Update navigation links in all pages
4. Add page-specific styles if needed

### Adding Styles
1. Add styles to appropriate CSS file
2. Use CSS variables for consistency
3. Follow mobile-first approach
4. Test across different screen sizes

## 📄 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to fork and customize for your own projects!
