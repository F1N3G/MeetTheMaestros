# Meet the Maestros - Classical Composers Web Application

## Overview

This is a Flask-based web application that showcases classical composers with biographical information, key compositions, and multimedia content. The application presents an elegant, dark-themed interface highlighting the lives and works of famous composers like Mozart, Beethoven, and Bach.

## System Architecture

### Frontend Architecture
- **Technology**: HTML5, CSS3, JavaScript (ES6+)
- **Framework**: Bootstrap 5 with custom dark theme
- **Styling**: Custom CSS with Google Fonts (Playfair Display, Crimson Text)
- **Icons**: Font Awesome 6.0
- **Responsive Design**: Mobile-first approach with Bootstrap's responsive grid system

### Backend Architecture
- **Framework**: Flask (Python)
- **Architecture Pattern**: Simple MVC pattern
- **Session Management**: Flask sessions with configurable secret key
- **Logging**: Python's built-in logging module configured for DEBUG level

### Data Storage
- **Data Model**: In-memory Python dictionary structure
- **No Database**: Currently uses hardcoded composer data within the application
- **Data Structure**: Nested dictionaries containing composer information including:
  - Biographical details
  - Key compositions
  - Portrait images
  - YouTube embed links

## Key Components

### 1. Application Core (`app.py`)
- Flask application initialization
- Composer data management
- Route handling (implied but not visible in current code)
- Session configuration with environment variable support

### 2. Frontend Templates (`templates/index.html`)
- Single-page application structure
- Navigation system with anchor links
- Responsive layout with Bootstrap components
- Integration points for dynamic content

### 3. Static Assets
- **CSS**: Custom styling with classical music theme variables
- **JavaScript**: Interactive features including smooth scrolling, navigation updates, and scroll animations
- **Design System**: Consistent color scheme with classical gold and dark blue palette

### 4. Entry Point (`main.py`)
- Application launcher importing from the main Flask app

## Data Flow

1. **Application Startup**: Flask app initializes with composer data loaded into memory
2. **Request Handling**: Routes serve HTML templates with embedded data
3. **Client Interaction**: JavaScript handles smooth scrolling, navigation updates, and visual animations
4. **Data Presentation**: Static data is rendered into HTML templates for display

## External Dependencies

### Python Dependencies
- Flask (web framework)
- Standard library modules (os, logging)

### Frontend Dependencies
- Bootstrap 5 CSS framework (CDN)
- Font Awesome 6.0 (CDN)
- Google Fonts (CDN)

### Media Content
- Portrait images sourced from Pixabay
- YouTube embeds for musical examples

## Deployment Strategy

### Environment Configuration
- Session secret key configurable via `SESSION_SECRET` environment variable
- Development-ready with DEBUG logging enabled
- Suitable for platforms like Replit, Heroku, or traditional hosting

### Scalability Considerations
- Current architecture is suitable for small to medium traffic
- In-memory data storage limits horizontal scaling
- Future database integration would enable better scalability

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 03, 2025. Initial setup

## Notes for Development

### Current Limitations
- Incomplete composer data (truncated biography text in Bach entry)
- No database persistence
- Limited to predefined composer set
- No user interaction features (comments, favorites, etc.)

### Future Enhancement Opportunities
- Database integration for dynamic content management
- User authentication and personalization
- Search and filtering capabilities
- Audio player integration
- Content management system for adding new composers
- Performance optimization for larger datasets

### Technical Debt
- Hardcoded data should be moved to external data source
- Route definitions are not visible in current code structure
- Error handling mechanisms need implementation
- Testing framework not yet established