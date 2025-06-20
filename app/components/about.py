"""
About Section Component
Detailed information about background, expertise, and passion for AI.
"""

from nicegui import ui


def create_about_section():
    """Create the about section with personal and professional information."""
    
    with ui.element('section').props('id="about"').classes('section-padding bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 gap-12'):
            
            # Section Header
            with ui.column().classes('text-center gap-4'):
                ui.label('About Me').classes('text-4xl font-bold text-gradient')
                ui.label('Get to know the person behind the AI').classes('text-xl text-gray-600')
            
            # Content Grid
            with ui.row().classes('gap-12 items-start').style('flex-wrap: wrap;'):
                
                # Left Column - Personal Story
                with ui.column().classes('flex-1 min-w-96 gap-6'):
                    ui.label('My Journey in AI').classes('text-2xl font-semibold text-gray-800')
                    
                    ui.markdown('''
                    I discovered my passion for artificial intelligence during my computer science studies, 
                    where I was fascinated by the potential of machines to learn and make intelligent decisions. 
                    This curiosity led me to pursue advanced studies in machine learning and deep learning.
                    
                    Over the past 5 years, I've had the privilege of working on diverse AI projects, from 
                    computer vision systems that help doctors diagnose diseases to natural language processing 
                    models that improve customer experiences. Each project has taught me something new and 
                    reinforced my belief in AI's power to create positive change.
                    
                    When I'm not coding, you'll find me reading the latest AI research papers, contributing 
                    to open-source projects, or mentoring aspiring data scientists. I believe in the 
                    importance of making AI accessible and ethical for everyone.
                    ''').classes('text-gray-700 leading-relaxed')
                
                # Right Column - Key Stats and Highlights
                with ui.column().classes('flex-1 min-w-96 gap-6'):
                    ui.label('Key Highlights').classes('text-2xl font-semibold text-gray-800')
                    
                    # Stats Cards
                    stats = [
                        {'number': '50+', 'label': 'AI Projects Completed', 'icon': 'fas fa-project-diagram'},
                        {'number': '5+', 'label': 'Years of Experience', 'icon': 'fas fa-calendar-alt'},
                        {'number': '15+', 'label': 'Research Papers Published', 'icon': 'fas fa-file-alt'},
                        {'number': '100K+', 'label': 'Lines of Code Written', 'icon': 'fas fa-code'}
                    ]
                    
                    with ui.grid(columns=2).classes('gap-4 w-full'):
                        for stat in stats:
                            with ui.card().classes('card-hover p-6 text-center'):
                                ui.icon(stat['icon']).classes('text-3xl text-blue-600 mb-2')
                                ui.label(stat['number']).classes('text-2xl font-bold text-gray-800')
                                ui.label(stat['label']).classes('text-sm text-gray-600')
                    
                    # Certifications
                    ui.label('Certifications').classes('text-xl font-semibold text-gray-800 mt-6')
                    certifications = [
                        'AWS Certified Machine Learning - Specialty',
                        'Google Cloud Professional ML Engineer',
                        'TensorFlow Developer Certificate',
                        'Deep Learning Specialization (Coursera)'
                    ]
                    
                    for cert in certifications:
                        with ui.row().classes('items-center gap-3 mb-2'):
                            ui.icon('verified').classes('text-green-600')
                            ui.label(cert).classes('text-gray-700')