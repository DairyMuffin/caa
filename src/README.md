# Content Alignment Algorithm (CAA)

> A lightweight service that computes alignment scores for text segments.

## Table of Contents

1. [Quickstart](#quickstart)  
2. [Installation](#installation)  
3. [Usage](#usage)  
   - [CLI](#cli)  
   - [HTTP API](#http-api)  
4. [Configuration](#configuration)  
5. [Examples](#examples)  
6. [Testing](#testing)  
7. [Development](#development)  
8. [Troubleshooting](#troubleshooting)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## Quickstart

```bash
docker pull dairymuffin/caa:1.0
docker run --rm -e API_KEY=YOUR_KEY -p 8080:8080 dairymuffin/caa:1.0
