"""
Experience Section Component
Professional experience timeline with roles, companies, and achievements.
"""

from nicegui import ui


def create_experience_section():
    """Create the experience section with professional timeline."""
    
    with ui.element('section').props('id="experience"').classes('section-padding'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 gap-12'):
            
            # Section Header
            with ui.column().classes('text-center gap-4'):
                ui.label('Professional Experience').classes('text-4xl font-bold text-gradient')
                ui.label('My journey in AI and machine learning').classes('text-xl text-gray-600')
            
            # Experience Timeline
            experiences = [
                {
                    'title': 'Senior AI Engineer',
                    'company': 'TechCorp AI Solutions',
                    'period': '2022 - Present',
                    'location': 'San Francisco, CA',
                    'description': 'Lead AI engineer responsible for developing and deploying machine learning solutions at scale.',
                    'achievements': [
                        'Led a team of 5 ML engineers in building a real-time recommendation system serving 10M+ users',
                        'Designed and implemented MLOps pipeline reducing model deployment time from weeks to hours',
                        'Increased model accuracy by 15% through advanced feature engineering and ensemble methods',
                        'Mentored junior engineers and established ML best practices across the organization'
                    ],
                    'technologies': ['TensorFlow', 'PyTorch', 'Kubernetes', 'AWS', 'MLflow', 'Apache Spark']
                },
                {
                    'title': 'Machine Learning Engineer',
                    'company': 'DataDriven Analytics',
                    'period': '2020 - 2022',
                    'location': 'Seattle, WA',
                    'description': 'Developed end-to-end ML solutions for enterprise clients across various industries.',
                    'achievements': [
                        'Built computer vision system for quality control in manufacturing, reducing defect rates by 40%',
                        'Implemented NLP pipeline for sentiment analysis processing 1M+ social media posts daily',
                        'Optimized existing models achieving 3x faster inference time while maintaining accuracy',
                        'Collaborated with product teams to integrate ML capabilities into customer-facing applications'
                    ],
                    'technologies': ['Scikit-learn', 'OpenCV', 'Docker', 'PostgreSQL', 'FastAPI', 'React']
                },
                {
                    'title': 'Data Scientist',
                    'company': 'FinTech Innovations',
                    'period': '2019 - 2020',
                    'location': 'New York, NY',
                    'description': 'Applied machine learning to financial data for risk assessment and fraud detection.',
                    'achievements': [
                        'Developed fraud detection model reducing false positives by 60% and saving $2M annually',
                        'Created credit risk assessment system improving loan approval accuracy by 25%',
                        'Built automated trading algorithms generating 18% annual returns',
                        'Presented findings to C-level executives and regulatory bodies'
                    ],
                    'technologies': ['Python', 'R', 'XGBoost', 'SQL', 'Tableau', 'Apache Airflow']
                },
                {
                    'title': 'Junior Data Scientist',
                    'company': 'StartupAI',
                    'period': '2018 - 2019',
                    'location': 'Austin, TX',
                    'description': 'First role in AI/ML, focused on data analysis and building predictive models.',
                    'achievements': [
                        'Analyzed customer behavior data leading to 20% increase in user retention',
                        'Built predictive models for demand forecasting improving inventory management',
                        'Automated data preprocessing pipelines reducing manual work by 80%',
                        'Contributed to open-source ML libraries with 500+ GitHub stars'
                    ],
                    'technologies': ['Python', 'Pandas', 'Matplotlib', 'Jupyter', 'Git', 'Linux']
                }
            ]
            
            # Timeline
            with ui.column().classes('gap-8'):
                for i, exp in enumerate(experiences):
                    with ui.row().classes('gap-8 items-start'):
                        # Timeline indicator
                        with ui.column().classes('items-center gap-2 flex-shrink-0'):
                            ui.element('div').classes('w-4 h-4 bg-blue-600 rounded-full')
                            if i < len(experiences) - 1:
                                ui.element('div').classes('w-0.5 h-32 bg-gray-300')
                        
                        # Experience Card
                        with ui.card().classes('card-hover flex-1 p-6'):
                            # Header
                            with ui.row().classes('justify-between items-start mb-4').style('flex-wrap: wrap;'):
                                with ui.column().classes('gap-1'):
                                    ui.label(exp['title']).classes('text-xl font-semibold text-gray-800')
                                    ui.label(exp['company']).classes('text-lg text-blue-600 font-medium')
                                    ui.label(exp['location']).classes('text-sm text-gray-500')
                                
                                ui.label(exp['period']).classes('text-sm font-medium text-gray-600 bg-gray-100 px-3 py-1 rounded-full')
                            
                            # Description
                            ui.label(exp['description']).classes('text-gray-600 mb-4')
                            
                            # Achievements
                            ui.label('Key Achievements:').classes('font-medium text-gray-800 mb-2')
                            for achievement in exp['achievements']:
                                with ui.row().classes('items-start gap-2 mb-2'):
                                    ui.icon('check_circle').classes('text-green-600 text-sm mt-1 flex-shrink-0')
                                    ui.label(achievement).classes('text-gray-700 text-sm')
                            
                            # Technologies
                            ui.label('Technologies Used:').classes('font-medium text-gray-800 mb-2 mt-4')
                            with ui.row().classes('gap-2').style('flex-wrap: wrap;'):
                                for tech in exp['technologies']:
                                    ui.label(tech).classes('tech-tag')
            
            # Education Section
            with ui.column().classes('gap-8 mt-16'):
                ui.label('Education').classes('text-3xl font-bold text-gradient text-center mb-8')
                
                education = [
                    {
                        'degree': 'Master of Science in Computer Science',
                        'school': 'Stanford University',
                        'period': '2016 - 2018',
                        'specialization': 'Artificial Intelligence Track',
                        'gpa': '3.9/4.0',
                        'thesis': 'Deep Reinforcement Learning for Autonomous Navigation'
                    },
                    {
                        'degree': 'Bachelor of Science in Computer Engineering',
                        'school': 'UC Berkeley',
                        'period': '2012 - 2016',
                        'specialization': 'Machine Learning Minor',
                        'gpa': '3.8/4.0',
                        'honors': 'Magna Cum Laude, Phi Beta Kappa'
                    }
                ]
                
                with ui.row().classes('gap-8').style('flex-wrap: wrap;'):
                    for edu in education:
                        with ui.card().classes('card-hover flex-1 min-w-96 p-6'):
                            ui.label(edu['degree']).classes('text-lg font-semibold text-gray-800 mb-2')
                            ui.label(edu['school']).classes('text-blue-600 font-medium mb-1')
                            ui.label(edu['period']).classes('text-gray-500 text-sm mb-3')
                            
                            if 'specialization' in edu:
                                with ui.row().classes('items-center gap-2 mb-2'):
                                    ui.icon('school').classes('text-gray-600 text-sm')
                                    ui.label(f"Specialization: {edu['specialization']}").classes('text-gray-700 text-sm')
                            
                            if 'gpa' in edu:
                                with ui.row().classes('items-center gap-2 mb-2'):
                                    ui.icon('grade').classes('text-gray-600 text-sm')
                                    ui.label(f"GPA: {edu['gpa']}").classes('text-gray-700 text-sm')
                            
                            if 'thesis' in edu:
                                with ui.row().classes('items-center gap-2 mb-2'):
                                    ui.icon('article').classes('text-gray-600 text-sm')
                                    ui.label(f"Thesis: {edu['thesis']}").classes('text-gray-700 text-sm')
                            
                            if 'honors' in edu:
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('emoji_events').classes('text-yellow-600 text-sm')
                                    ui.label(edu['honors']).classes('text-gray-700 text-sm')