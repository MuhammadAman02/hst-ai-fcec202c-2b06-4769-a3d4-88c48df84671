"""
AI Engineer Portfolio - Main Application
Modern, responsive portfolio showcasing AI engineering expertise.
"""

from nicegui import ui
from app.config import settings
from app.components.hero import create_hero_section
from app.components.about import create_about_section
from app.components.skills import create_skills_section
from app.components.projects import create_projects_section
from app.components.experience import create_experience_section
from app.components.contact import create_contact_section
from app.components.footer import create_footer


def setup_portfolio():
    """Setup the portfolio application with all sections."""
    
    # Add custom CSS for modern styling
    ui.add_head_html('''
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --accent-color: #3b82f6;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --border-color: #e5e7eb;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        }
        
        [data-theme="dark"] {
            --text-primary: #f9fafb;
            --text-secondary: #d1d5db;
            --bg-primary: #111827;
            --bg-secondary: #1f2937;
            --border-color: #374151;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background: var(--bg-primary);
        }
        
        .hero-gradient {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .card-hover {
            transition: all 0.3s ease;
            border: 1px solid var(--border-color);
            background: var(--bg-primary);
        }
        
        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        .skill-bar {
            height: 8px;
            background: var(--border-color);
            border-radius: 4px;
            overflow: hidden;
        }
        
        .skill-progress {
            height: 100%;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            border-radius: 4px;
            transition: width 1s ease-in-out;
        }
        
        .section-padding {
            padding: 4rem 0;
        }
        
        .text-gradient {
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .btn-primary {
            background: var(--primary-color);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .btn-primary:hover {
            background: var(--secondary-color);
            transform: translateY(-1px);
        }
        
        .btn-outline {
            background: transparent;
            color: var(--primary-color);
            border: 2px solid var(--primary-color);
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .btn-outline:hover {
            background: var(--primary-color);
            color: white;
        }
        
        @media (max-width: 768px) {
            .section-padding {
                padding: 2rem 0;
            }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.8s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .project-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 0.5rem;
        }
        
        .tech-tag {
            background: var(--bg-secondary);
            color: var(--text-secondary);
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.875rem;
            font-weight: 500;
        }
    </style>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    ''')


@ui.page('/')
def index():
    """Main portfolio page with all sections."""
    
    # Navigation Bar
    with ui.header().classes('bg-white shadow-sm border-b').style('position: fixed; top: 0; z-index: 1000;'):
        with ui.row().classes('w-full max-w-6xl mx-auto px-4 py-3 items-center justify-between'):
            ui.label(settings.PORTFOLIO_NAME).classes('text-xl font-bold text-gradient')
            
            with ui.row().classes('gap-6 items-center'):
                ui.link('About', '#about').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Skills', '#skills').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Projects', '#projects').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Experience', '#experience').classes('text-gray-600 hover:text-blue-600 transition-colors')
                ui.link('Contact', '#contact').classes('text-gray-600 hover:text-blue-600 transition-colors')
    
    # Add top margin to account for fixed header
    ui.html('<div style="height: 80px;"></div>')
    
    # Portfolio Sections
    create_hero_section()
    create_about_section()
    create_skills_section()
    create_projects_section()
    create_experience_section()
    create_contact_section()
    create_footer()


@ui.page('/health')
def health_check():
    """Health check endpoint for deployment monitoring."""
    return {'status': 'healthy', 'service': 'ai-engineer-portfolio'}