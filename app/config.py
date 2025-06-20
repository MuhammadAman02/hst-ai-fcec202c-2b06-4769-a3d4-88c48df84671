"""
Portfolio Configuration
Centralized configuration management using Pydantic settings.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Server Configuration
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    RELOAD: bool = False
    ENVIRONMENT: str = "production"
    
    # Portfolio Information
    PORTFOLIO_NAME: str = "Alex Chen"
    PORTFOLIO_TITLE: str = "AI Engineer & Machine Learning Specialist"
    PORTFOLIO_EMAIL: str = "alex.chen@example.com"
    PORTFOLIO_LINKEDIN: str = "https://linkedin.com/in/alexchen"
    PORTFOLIO_GITHUB: str = "https://github.com/alexchen"
    PORTFOLIO_LOCATION: str = "San Francisco, CA"
    
    # Contact Form Configuration (Optional)
    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: int = 587
    EMAIL_USERNAME: Optional[str] = None
    EMAIL_PASSWORD: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()