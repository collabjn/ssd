# VCYou: Startup Success Prediction

## Project Overview
VCYou is a machine learning model designed to assist venture capitalists in making informed financial decisions. This project leverages advanced classifiers to predict the success potential of startups, providing reliable investment insights that can guide venture capital funding strategies.

## Deployment Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/AbeerMathur/VCYou.git
   cd VCYou
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements/development.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

### Production Deployment

1. Install production dependencies:
   ```bash
   pip install -r requirements/production.txt
   ```

2. Set environment variables:
   - DEBUG=False
   - SECRET_KEY=<secure-key>
   - ALLOWED_HOSTS=your-domain.com
   - SENTRY_DSN=<your-sentry-dsn>

3. Collect static files:
   ```bash
   python manage.py collectstatic --no-input
   ```

4. Configure your web server (e.g., Nginx + Gunicorn)

5. Set up SSL certificate

6. Run with gunicorn:
   ```bash
   gunicorn vcyou.wsgi:application
   ```

## Security Considerations
- Always use HTTPS in production
- Keep DEBUG=False in production
- Regularly update dependencies
- Monitor application using Sentry
- Backup database regularly
