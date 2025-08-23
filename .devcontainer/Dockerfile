ARG PYTHON_VERSION=3.12
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION} as base

# Install UV and Bun
RUN curl -fsSL https://bun.sh/install | bash && mv /root/.bun/bin/bun /usr/local/bin/bun
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv python pin $PYTHON_VERSION

# Create python virtual environment
RUN uv venv /opt/venv --python $PYTHON_VERSION --seed
# Add venv to PATH for subsequent RUN commands and for the container environment
ENV PATH="/opt/venv/bin:$PATH"
# Tell pip, uv to use this virtual environment
ENV VIRTUAL_ENV="/opt/venv"
ENV UV_PROJECT_ENVIRONMENT="/opt/venv"

# Setup working directory
WORKDIR /workspaces/khoj

# --- STAGE 1: Heavy AI/ML Dependencies ---
FROM base as ml-deps

# Setup python environment with optimized settings for smaller downloads
ENV UV_INDEX="https://download.pytorch.org/whl/cpu" \
    UV_INDEX_STRATEGY="unsafe-best-match" \
    # Avoid downloading unused cuda specific python packages
    CUDA_VISIBLE_DEVICES="" \
    # Use static version to build app without git dependency
    VERSION=0.0.0 \
    # Use embedded db
    USE_EMBEDDED_DB="True" \
    PGSERVER_DATA_DIR="/opt/khoj_db" \
    # Optimize pip/uv for smaller downloads
    PIP_NO_CACHE_DIR=1 \
    UV_NO_CACHE=1

# Copy only the dependency files first for better caching
COPY pyproject.toml README.md ./

# Install ONLY the heavy AI/ML packages first (this layer will be cached)
RUN sed -i "s/dynamic = \\[\"version\"\\]/version = \"$VERSION\"/" pyproject.toml && \
    echo "Installing heavy AI/ML dependencies..." && \
    uv add torch==2.6.0 --index https://download.pytorch.org/whl/cpu && \
    uv add transformers==4.51.0 && \
    uv add sentence-transformers==3.4.1 && \
    uv add "openai-whisper>=20231117" && \
    uv add rapidocr-onnxruntime==1.4.4 && \
    echo "Heavy AI/ML dependencies installed"

# --- STAGE 2: Lightweight Dependencies ---  
FROM base as light-deps

# Copy the heavy ML packages from the previous stage
COPY --from=ml-deps /opt/venv /opt/venv

# Setup environment again
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"
ENV UV_PROJECT_ENVIRONMENT="/opt/venv"
ENV UV_INDEX="https://download.pytorch.org/whl/cpu" \
    UV_INDEX_STRATEGY="unsafe-best-match" \
    CUDA_VISIBLE_DEVICES="" \
    VERSION=0.0.0 \
    USE_EMBEDDED_DB="True" \
    PGSERVER_DATA_DIR="/opt/khoj_db" \
    PIP_NO_CACHE_DIR=1 \
    UV_NO_CACHE=1

# Copy dependency files
COPY pyproject.toml README.md ./

# Install remaining lightweight dependencies (excluding the heavy ones we already have)
RUN sed -i "s/dynamic = \\[\"version\"\\]/version = \"$VERSION\"/" pyproject.toml && \
    echo "Installing remaining lightweight dependencies..." && \
    (uv sync --all-extras --no-install-project --verbose || \
     (echo "UV sync failed, trying without extras..." && uv sync --no-install-project --verbose) || \
     (echo "UV sync still failed, trying pip fallback..." && pip install -e . --no-deps)) && \
    echo "Dependency installation completed" && \
    # Save the lock file generated with correct Linux platform wheels (if it exists)
    (cp uv.lock /opt/uv.lock.linux || echo "No uv.lock to copy") && \
    chown -R vscode:vscode /opt/venv

# --- STAGE 3: Final Development Image ---
FROM light-deps as dev_containers_target_stage

# --- Web App Dependencies ---
# Copy web app manifest files
COPY src/interface/web/package.json src/interface/web/bun.lock /opt/khoj_web/

# Install web app dependencies
RUN cd /opt/khoj_web && bun install && chown -R vscode:vscode .

# The .venv and node_modules are now populated in the image.
# The rest of the source code will be mounted by VS Code from your local checkout,
# overlaying any files copied here if they are part of the workspace mount.
