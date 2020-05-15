# LTLTLT 

This is an Aliexpress Scraper / price tracker that is modeled and named after CamelCamelCamel for Amazon. LTLTLT is the initials for CamelCamelCamel in Chinese. 

To get started run:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec python manage.py migrate --no-input
docker-compose -f docker-compose.prod.yml exec python manage.py collectstatic --no-input
```

Then you are off and running. 