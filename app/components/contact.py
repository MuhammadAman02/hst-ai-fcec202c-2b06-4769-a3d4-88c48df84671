"""
Contact Section Component
Contact form and information for getting in touch.
"""

from nicegui import ui
from app.config import settings


def create_contact_section():
    """Create the contact section with form and contact information."""
    
    with ui.element('section').props('id="contact"').classes('section-padding bg-gray-50'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 gap-12'):
            
            # Section Header
            with ui.column().classes('text-center gap-4'):
                ui.label("Let's Work Together").classes('text-4xl font-bold text-gradient')
                ui.label('Ready to bring AI solutions to your business?').classes('text-xl text-gray-600')
            
            # Contact Content
            with ui.row().classes('gap-12 items-start').style('flex-wrap: wrap;'):
                
                # Contact Information
                with ui.column().classes('flex-1 min-w-96 gap-8'):
                    ui.label('Get In Touch').classes('text-2xl font-semibold text-gray-800')
                    
                    ui.markdown('''
                    I'm always interested in discussing new opportunities, innovative projects, 
                    and collaborations in the AI space. Whether you're looking to implement 
                    machine learning solutions, need consultation on AI strategy, or want to 
                    explore research partnerships, I'd love to hear from you.
                    ''').classes('text-gray-700 leading-relaxed mb-6')
                    
                    # Contact Details
                    contact_info = [
                        {'icon': 'email', 'label': 'Email', 'value': settings.PORTFOLIO_EMAIL, 'link': f'mailto:{settings.PORTFOLIO_EMAIL}'},
                        {'icon': 'location_on', 'label': 'Location', 'value': settings.PORTFOLIO_LOCATION, 'link': None},
                        {'icon': 'fab fa-linkedin', 'label': 'LinkedIn', 'value': 'Connect with me', 'link': settings.PORTFOLIO_LINKEDIN},
                        {'icon': 'fab fa-github', 'label': 'GitHub', 'value': 'View my code', 'link': settings.PORTFOLIO_GITHUB}
                    ]
                    
                    for info in contact_info:
                        with ui.row().classes('items-center gap-4 mb-4'):
                            ui.icon(info['icon']).classes('text-blue-600 text-xl')
                            with ui.column().classes('gap-1'):
                                ui.label(info['label']).classes('text-sm font-medium text-gray-600')
                                if info['link']:
                                    ui.link(info['value'], info['link'], new_tab=True).classes('text-gray-800 hover:text-blue-600 transition-colors')
                                else:
                                    ui.label(info['value']).classes('text-gray-800')
                    
                    # Availability Status
                    with ui.card().classes('card-hover p-4 mt-6'):
                        with ui.row().classes('items-center gap-3'):
                            ui.icon('circle').classes('text-green-500 text-sm')
                            ui.label('Available for new projects').classes('font-medium text-gray-800')
                        ui.label('Currently accepting freelance and consulting opportunities').classes('text-sm text-gray-600 mt-2')
                
                # Contact Form
                with ui.column().classes('flex-1 min-w-96'):
                    with ui.card().classes('card-hover p-6'):
                        ui.label('Send a Message').classes('text-xl font-semibold text-gray-800 mb-6')
                        
                        # Form fields
                        name_input = ui.input('Your Name').classes('w-full mb-4').props('outlined')
                        email_input = ui.input('Your Email').classes('w-full mb-4').props('outlined type=email')
                        subject_input = ui.input('Subject').classes('w-full mb-4').props('outlined')
                        message_input = ui.textarea('Your Message').classes('w-full mb-6').props('outlined rows=5')
                        
                        # Submit button
                        def handle_contact_form():
                            """Handle contact form submission."""
                            if not all([name_input.value, email_input.value, subject_input.value, message_input.value]):
                                ui.notify('Please fill in all fields', type='warning')
                                return
                            
                            # In a real implementation, you would send the email here
                            # For now, we'll just show a success message
                            ui.notify(
                                f'Thank you {name_input.value}! Your message has been sent. I\'ll get back to you soon.',
                                type='positive',
                                timeout=5000
                            )
                            
                            # Clear form
                            name_input.value = ''
                            email_input.value = ''
                            subject_input.value = ''
                            message_input.value = ''
                        
                        ui.button('Send Message', on_click=handle_contact_form).classes('btn-primary w-full').props('icon="send"')
                        
                        ui.label('I typically respond within 24 hours').classes('text-sm text-gray-500 text-center mt-4')
            
            # Call to Action
            with ui.column().classes('text-center gap-6 mt-16'):
                ui.label('Ready to start your AI journey?').classes('text-2xl font-semibold text-gray-800')
                ui.label('Let\'s discuss how artificial intelligence can transform your business').classes('text-lg text-gray-600')
                
                with ui.row().classes('gap-4 justify-center').style('flex-wrap: wrap;'):
                    ui.button('Schedule a Call', 
                        on_click=lambda: ui.notify('Calendar booking would be implemented here', type='info')
                    ).classes('btn-primary text-lg px-8 py-3').props('icon="calendar_today"')
                    
                    ui.button('Download Resume', 
                        on_click=lambda: ui.notify('Resume download would be implemented here', type='info')
                    ).classes('btn-outline text-lg px-8 py-3').props('icon="download"')