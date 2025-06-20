"""
Hero Section Component
Eye-catching introduction with professional photo and key information.
"""

from nicegui import ui
from app.config import settings


def create_hero_section():
    """Create the hero section with professional introduction."""
    
    with ui.element('section').classes('hero-gradient section-padding text-white'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 items-center text-center gap-8'):
            
            # Profile Image
            ui.image('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face').classes(
                'w-48 h-48 rounded-full border-4 border-white shadow-lg animate-fade-in'
            ).style('object-fit: cover;')
            
            # Name and Title
            with ui.column().classes('gap-4 animate-fade-in'):
                ui.label(settings.PORTFOLIO_NAME).classes('text-5xl font-bold mb-2')
                ui.label(settings.PORTFOLIO_TITLE).classes('text-xl text-blue-100 mb-4')
                
                # Brief Introduction
                ui.label(
                    "Passionate AI Engineer with 5+ years of experience building intelligent systems "
                    "that solve real-world problems. Specialized in machine learning, deep learning, "
                    "and MLOps with a track record of deploying scalable AI solutions."
                ).classes('text-lg text-blue-50 max-w-3xl leading-relaxed')
            
            # Call-to-Action Buttons
            with ui.row().classes('gap-4 mt-8 animate-fade-in'):
                ui.button('View My Work', on_click=lambda: ui.run_javascript('document.getElementById("projects").scrollIntoView({behavior: "smooth"})')).classes(
                    'btn-primary text-lg px-8 py-3'
                )
                ui.button('Download Resume', on_click=lambda: ui.notify('Resume download would be implemented here', type='info')).classes(
                    'btn-outline text-lg px-8 py-3 text-white border-white hover:bg-white hover:text-blue-600'
                )
            
            # Social Links
            with ui.row().classes('gap-6 mt-8 animate-fade-in'):
                ui.link('', settings.PORTFOLIO_GITHUB, new_tab=True).classes('text-white hover:text-blue-200 transition-colors').style('font-size: 1.5rem;').props('icon="fab fa-github"')
                ui.link('', settings.PORTFOLIO_LINKEDIN, new_tab=True).classes('text-white hover:text-blue-200 transition-colors').style('font-size: 1.5rem;').props('icon="fab fa-linkedin"')
                ui.link('', f'mailto:{settings.PORTFOLIO_EMAIL}').classes('text-white hover:text-blue-200 transition-colors').style('font-size: 1.5rem;').props('icon="fas fa-envelope"')
    
    # Add scroll indicator
    with ui.column().classes('w-full items-center -mt-8 relative z-10'):
        ui.icon('keyboard_arrow_down').classes('text-white text-4xl animate-bounce cursor-pointer').on('click', 
            lambda: ui.run_javascript('document.getElementById("about").scrollIntoView({behavior: "smooth"})'))