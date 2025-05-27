# Content Alignment Algorithm (CAA)

**Docker Hub:** [dairymuffin/caa:1.0](https://hub.docker.com/r/dairymuffin/caa)

## Quickstart

Clone, pull, and run:

    git clone https://github.com/DairyMuffin/caa.git
    cd caa
    docker pull dairymuffin/caa:1.0
    docker run --rm -e API_KEY=demo -p 8080:8080 dairymuffin/caa:1.0

Test the endpoint:

    curl -X POST http://localhost:8080/scan \
      -H "Content-Type: application/json" \
      -d '{"text":"Hello\n\nWorld","threshold":0.8}'

---

## CI Status

[![CI](https://github.com/DairyMuffin/caa/actions/workflows/ci.yml/badge.svg)](https://github.com/DairyMuffin/caa/actions)
