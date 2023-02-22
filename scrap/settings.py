# Obey robots.txt rules
ROBOTSTXT_OBEY = False


HTTPCACHE_ENABLED = True

LOG_LEVEL = "DEBUG" # or "INFO" in production
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # we should use headers
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"

settings={
    "FEED_EXPORT_ENCODING":FEED_EXPORT_ENCODING,
    "REQUEST_FINGERPRINTER_IMPLEMENTATION":REQUEST_FINGERPRINTER_IMPLEMENTATION,
    "DEFAULT_REQUEST_HEADERS":DEFAULT_REQUEST_HEADERS,
    "LOG_LEVEL":LOG_LEVEL,
    "HTTPCACHE_ENABLED":HTTPCACHE_ENABLED,
    "ROBOTSTXT_OBEY":ROBOTSTXT_OBEY,
}