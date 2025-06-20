"""
Skills Section Component
Interactive visualization of technical skills and expertise areas.
"""

from nicegui import ui


def create_skills_section():
    """Create the skills section with interactive skill bars and categories."""
    
    with ui.element('section').props('id="skills"').classes('section-padding'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 gap-12'):
            
            # Section Header
            with ui.column().classes('text-center gap-4'):
                ui.label('Technical Skills').classes('text-4xl font-bold text-gradient')
                ui.label('Technologies and tools I work with').classes('text-xl text-gray-600')
            
            # Skills Categories
            with ui.row().classes('gap-8 w-full').style('flex-wrap: wrap;'):
                
                # Programming Languages
                with ui.card().classes('flex-1 min-w-80 card-hover p-6'):
                    ui.label('Programming Languages').classes('text-xl font-semibold text-gray-800 mb-4')
                    
                    skills = [
                        {'name': 'Python', 'level': 95},
                        {'name': 'R', 'level': 85},
                        {'name': 'SQL', 'level': 90},
                        {'name': 'JavaScript', 'level': 75},
                        {'name': 'Java', 'level': 70},
                        {'name': 'C++', 'level': 65}
                    ]
                    
                    for skill in skills:
                        with ui.column().classes('gap-2 mb-4'):
                            with ui.row().classes('justify-between items-center'):
                                ui.label(skill['name']).classes('font-medium text-gray-700')
                                ui.label(f"{skill['level']}%").classes('text-sm text-gray-500')
                            
                            with ui.element('div').classes('skill-bar'):
                                ui.element('div').classes('skill-progress').style(f'width: {skill["level"]}%;')
                
                # ML/AI Frameworks
                with ui.card().classes('flex-1 min-w-80 card-hover p-6'):
                    ui.label('ML/AI Frameworks').classes('text-xl font-semibold text-gray-800 mb-4')
                    
                    frameworks = [
                        {'name': 'TensorFlow', 'level': 90},
                        {'name': 'PyTorch', 'level': 88},
                        {'name': 'Scikit-learn', 'level': 95},
                        {'name': 'Keras', 'level': 85},
                        {'name': 'Hugging Face', 'level': 80},
                        {'name': 'OpenCV', 'level': 75}
                    ]
                    
                    for framework in frameworks:
                        with ui.column().classes('gap-2 mb-4'):
                            with ui.row().classes('justify-between items-center'):
                                ui.label(framework['name']).classes('font-medium text-gray-700')
                                ui.label(f"{framework['level']}%").classes('text-sm text-gray-500')
                            
                            with ui.element('div').classes('skill-bar'):
                                ui.element('div').classes('skill-progress').style(f'width: {framework["level"]}%;')
            
            # Second Row
            with ui.row().classes('gap-8 w-full').style('flex-wrap: wrap;'):
                
                # Cloud & DevOps
                with ui.card().classes('flex-1 min-w-80 card-hover p-6'):
                    ui.label('Cloud & DevOps').classes('text-xl font-semibold text-gray-800 mb-4')
                    
                    cloud_skills = [
                        {'name': 'AWS', 'level': 85},
                        {'name': 'Google Cloud', 'level': 80},
                        {'name': 'Docker', 'level': 90},
                        {'name': 'Kubernetes', 'level': 75},
                        {'name': 'MLflow', 'level': 85},
                        {'name': 'Apache Airflow', 'level': 70}
                    ]
                    
                    for skill in cloud_skills:
                        with ui.column().classes('gap-2 mb-4'):
                            with ui.row().classes('justify-between items-center'):
                                ui.label(skill['name']).classes('font-medium text-gray-700')
                                ui.label(f"{skill['level']}%").classes('text-sm text-gray-500')
                            
                            with ui.element('div').classes('skill-bar'):
                                ui.element('div').classes('skill-progress').style(f'width: {skill["level"]}%;')
                
                # Specializations
                with ui.card().classes('flex-1 min-w-80 card-hover p-6'):
                    ui.label('AI Specializations').classes('text-xl font-semibold text-gray-800 mb-4')
                    
                    specializations = [
                        'Natural Language Processing',
                        'Computer Vision',
                        'Deep Learning',
                        'MLOps & Model Deployment',
                        'Time Series Analysis',
                        'Reinforcement Learning',
                        'Generative AI',
                        'Model Optimization'
                    ]
                    
                    with ui.grid(columns=2).classes('gap-3'):
                        for spec in specializations:
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('check_circle').classes('text-green-600 text-sm')
                                ui.label(spec).classes('text-sm text-gray-700')