#### Commands

```bash
docker build -t app
```

```bash
docker run -p 5000:5000 app 
```

Overiding the cmd
```bash
docker run -p 5000:5000 app2.py
```
Overiding the entrypoint
```bash
docker run -it --entrypoint /bin/bash app
```