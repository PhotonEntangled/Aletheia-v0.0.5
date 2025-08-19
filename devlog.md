# Development Log

## 2025-08-18: Debugging Static Asset Loading Issues

### Issue Description
After rebranding the application from "Khoj" to "Aletheia", static assets (logo files and webmanifest) are not loading properly, resulting in 404 errors:

```
2025-08-18T19:09:37.368Z 10.0.1.15:48092 - "GET /Aletheia_logo_text.svg HTTP/1.1" 404
2025-08-18T19:09:37.579Z 10.0.1.15:40060 - "GET /static/aletheia.webmanifest HTTP/1.1" 404
2025-08-18T19:10:26.500Z 10.0.1.15:44216 - "GET /Aletheia_logo.svg HTTP/1.1" 404
```

### Changes Made So Far
1. Updated `src/interface/web/app/components/logo/khojLogo.tsx` to use the correct paths with `/static/` prefix
2. Created a new `aletheia.webmanifest` file based on the existing `khoj.webmanifest`
3. Updated all references to the webmanifest file in HTML files and Android configuration
4. Built and deployed a new Docker image with these changes (ghcr.io/photonentangled/aletheia:0.0.5)

### Debugging Results
Despite the above changes, the issue persists. Analysis reveals multiple potential causes:

1. **Inconsistent URL Paths**: Some references use `/Aletheia_logo.svg` (without `/static/` prefix) while others use `/static/Aletheia_logo.svg`
2. **Django Static Files Configuration**: The `static/aletheia.webmanifest` 404 suggests Django's static file serving may be incorrectly configured
3. **Static File Collection**: The `collectstatic` command in the Docker build may not be capturing all necessary files
4. **File Location**: Files may not be in the expected location within the Docker container

### Next Steps
1. **Analyze Docker Build**: Inspect the Dockerfile and verify the static file collection process
2. **Review Django Settings**: Check `settings.py` for proper static file configuration (STATIC_URL, STATIC_ROOT, STATICFILES_DIRS)
3. **Audit Frontend Code**: Search for references to logo files without the `/static/` prefix
4. **Fix Hardcoded Paths**: Update all asset paths to consistently use `/static/` prefix
5. **Rebuild and Verify**: Rebuild Docker image and test with comprehensive monitoring

### Complexity Assessment
Based on Task Master complexity analysis, this is a moderate complexity issue (scores between 1-4) involving several components:
- Analyzing Dockerfile and container filesystem (complexity: 2)
- Reviewing Django static file configuration (complexity: 4) 
- Auditing frontend code for incorrect paths (complexity: 2)
- Fixing hardcoded paths in Next.js (complexity: 3)
- Updating HTML links (complexity: 1)

The core issue appears to be mismatched expectations between the frontend code references and the Django static file serving configuration. The Django server expects paths with `/static/` prefix, but some frontend code is still using direct paths without the prefix.
