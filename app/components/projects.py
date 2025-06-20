"""
Projects Section Component
Showcase of key AI/ML projects with descriptions, technologies, and links.
"""

from nicegui import ui


def create_projects_section():
    """Create the projects section with portfolio showcase."""
    
    with ui.element('section').props('id="projects"').classes('section-padding bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 gap-12'):
            
            # Section Header
            with ui.column().classes('text-center gap-4'):
                ui.label('Featured Projects').classes('text-4xl font-bold text-gradient')
                ui.label('AI solutions that make a real-world impact').classes('text-xl text-gray-600')
            
            # Projects Grid
            projects = [
                {
                    'title': 'Medical Image Analysis Platform',
                    'description': 'Deep learning system for automated detection of lung diseases in chest X-rays. Achieved 94% accuracy and deployed in 3 hospitals, helping radiologists reduce diagnosis time by 40%.',
                    'image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=400&h=250&fit=crop',
                    'technologies': ['TensorFlow', 'Python', 'Docker', 'AWS', 'React'],
                    'github': 'https://github.com/alexchen/medical-imaging',
                    'demo': 'https://medical-ai-demo.com',
                    'category': 'Computer Vision'
                },
                {
                    'title': 'Intelligent Customer Support Bot',
                    'description': 'NLP-powered chatbot using transformer models to handle customer inquiries. Processes 10,000+ queries daily with 89% resolution rate, reducing support costs by 60%.',
                    'image': 'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=400&h=250&fit=crop',
                    'technologies': ['PyTorch', 'Hugging Face', 'FastAPI', 'PostgreSQL', 'Redis'],
                    'github': 'https://github.com/alexchen/support-bot',
                    'demo': 'https://support-bot-demo.com',
                    'category': 'Natural Language Processing'
                },
                {
                    'title': 'Predictive Maintenance System',
                    'description': 'IoT sensor data analysis using machine learning to predict equipment failures. Implemented across 50+ manufacturing facilities, reducing downtime by 35% and maintenance costs by $2M annually.',
                    'image': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&h=250&fit=crop',
                    'technologies': ['Scikit-learn', 'Apache Kafka', 'InfluxDB', 'Grafana', 'Kubernetes'],
                    'github': 'https://github.com/alexchen/predictive-maintenance',
                    'demo': 'https://maintenance-ai-demo.com',
                    'category': 'Time Series Analysis'
                },
                {
                    'title': 'Real-time Fraud Detection',
                    'description': 'Machine learning pipeline for detecting fraudulent transactions in real-time. Processes 1M+ transactions per day with <100ms latency and 99.2% accuracy, preventing $5M in fraud annually.',
                    'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=400&h=250&fit=crop',
                    'technologies': ['XGBoost', 'Apache Spark', 'Kafka', 'Elasticsearch', 'MLflow'],
                    'github': 'https://github.com/alexchen/fraud-detection',
                    'demo': 'https://fraud-ai-demo.com',
                    'category': 'Machine Learning'
                },
                {
                    'title': 'Autonomous Drone Navigation',
                    'description': 'Computer vision and reinforcement learning system for autonomous drone navigation in complex environments. Successfully tested in urban and rural scenarios with 95% navigation accuracy.',
                    'image': 'https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=400&h=250&fit=crop',
                    'technologies': ['OpenCV', 'TensorFlow', 'ROS', 'Python', 'C++'],
                    'github': 'https://github.com/alexchen/drone-navigation',
                    'demo': 'https://drone-ai-demo.com',
                    'category': 'Reinforcement Learning'
                },
                {
                    'title': 'Content Generation Platform',
                    'description': 'GPT-based system for automated content creation and optimization. Generates high-quality marketing copy, blog posts, and social media content, increasing content team productivity by 300%.',
                    'image': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=400&h=250&fit=crop',
                    'technologies': ['OpenAI API', 'LangChain', 'FastAPI', 'React', 'MongoDB'],
                    'github': 'https://github.com/alexchen/content-ai',
                    'demo': 'https://content-ai-demo.com',
                    'category': 'Generative AI'
                }
            ]
            
            with ui.grid(columns=2).classes('gap-8 w-full').style('grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));'):
                for project in projects:
                    with ui.card().classes('card-hover overflow-hidden'):
                        # Project Image
                        ui.image(project['image']).classes('project-image')
                        
                        with ui.card_section().classes('p-6'):
                            # Category Badge
                            ui.label(project['category']).classes('tech-tag mb-3 inline-block')
                            
                            # Project Title
                            ui.label(project['title']).classes('text-xl font-semibold text-gray-800 mb-3')
                            
                            # Description
                            ui.label(project['description']).classes('text-gray-600 leading-relaxed mb-4')
                            
                            # Technologies
                            ui.label('Technologies:').classes('text-sm font-medium text-gray-700 mb-2')
                            with ui.row().classes('gap-2 mb-4').style('flex-wrap: wrap;'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('tech-tag')
                            
                            # Action Buttons
                            with ui.row().classes('gap-3'):
                                ui.button('View Code', 
                                    on_click=lambda url=project['github']: ui.run_javascript(f'window.open("{url}", "_blank")')
                                ).classes('btn-outline flex-1').props('icon="fab fa-github"')
                                
                                ui.button('Live Demo', 
                                    on_click=lambda url=project['demo']: ui.run_javascript(f'window.open("{url}", "_blank")')
                                ).classes('btn-primary flex-1').props('icon="launch"')
            
            # Call to Action
            with ui.column().classes('text-center gap-4 mt-12'):
                ui.label('Want to see more projects?').classes('text-xl text-gray-700')
                ui.button('View All Projects on GitHub', 
                    on_click=lambda: ui.run_javascript(f'window.open("{settings.PORTFOLIO_GITHUB}", "_blank")')
                ).classes('btn-primary text-lg px-8 py-3').props('icon="fab fa-github"')