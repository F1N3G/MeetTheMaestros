ClassicalMaestros/
├── app.py # Main Flask application
├── main.py # Application entry point
├── pyproject.toml # Python project configuration
├── replit.md # Project documentation
├── static/
│ ├── css/
│ │ └── style.css # Custom styles and animations
│ └── js/
│ └── script.js # Interactive JavaScript features
└── templates/
└── index.html # Main HTML template

Create virtual environment (recommended)

Install dependencies

Set environment variables (optional)

Run the application

Access the application
Open your browser and navigate to http://localhost:5000

🎨 Features Detail
Composer Data
Each composer profile includes:

Biographical Information: Life story and musical significance
Period Classification: Baroque, Classical, or Romantic era
Birth/Death Years: Historical context
Portrait Images: High-quality images from Pixabay
Key Compositions: Most important and recognizable works
YouTube Integration: Featured performance videos
Interactive Elements
Smooth Scrolling: Navigation links smoothly scroll to sections
Active Navigation: Current section highlights in navigation bar
Hover Effects: Composer cards animate on hover
Scroll Animations: Content fades in as you scroll
Mobile Navigation: Collapsible menu for mobile devices
Keyboard Support: Arrow keys navigate between sections
Responsive Design
Mobile-First: Optimized for mobile devices
Breakpoint Support: Adaptive layouts for all screen sizes
Touch-Friendly: Large tap targets and smooth interactions
Performance Optimized: Lazy loading for media content
🎵 Featured Composers
Wolfgang Amadeus Mozart (1756-1791) - Classical Period
Ludwig van Beethoven (1770-1827) - Classical/Romantic Period
Johann Sebastian Bach (1685-1750) - Baroque Period
Pyotr Ilyich Tchaikovsky (1840-1893) - Romantic Period
Frédéric Chopin (1810-1849) - Romantic Period
🚀 Deployment
Local Development
Production Deployment
The application is configured for deployment on platforms like:

Replit: Ready to run with provided configuration
Heroku: Compatible with Gunicorn WSGI server
Traditional Hosting: Standard Flask deployment
Environment Variables
SESSION_SECRET: Flask session secret key (optional, has default)
🔧 Customization
Adding New Composers
Edit the composers_data dictionary in app.py:

Styling Modifications
Customize the appearance by editing style.css:

CSS variables for colors in :root
Responsive breakpoints
Animation timing and effects
JavaScript Features
Enhance interactivity by modifying script.js:

Scroll behavior
Animation effects
Navigation logic
🎯 Browser Support
Chrome 90+
Firefox 88+
Safari 14+
Edge 90+
Mobile Safari (iOS 14+)
Chrome Mobile (Android 10+)
📝 License
This project is open source and available under the MIT License.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
🐛 Known Issues
Composer data is currently hardcoded (future enhancement: database integration)
Limited to predefined composer set
No user interaction features (comments, favorites, etc.)
🔮 Future Enhancements
Database integration for dynamic content management
User authentication and personalization
Search and filtering capabilities
Audio player integration
Content management system for adding new composers
Performance optimization for larger datasets
Multi-language support
📞 Support
If you have any questions or run into issues, please open an issue on the GitHub repository.
