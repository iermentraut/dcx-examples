# dcx (work in progress)

Docker-Compose allows you to include different docker-compose files by running `docker-compose -f docker-compose.yml -f docker-compose.custom.yml`, define [COMPOSE_FILE](https://docs.docker.com/compose/reference/envvars/#compose_file) in your `.env` file or even work with specific [Profiles](https://docs.docker.com/compose/profiles/) but in some cases it can be a pain in the a**. 

That's why `dcx` has a different approach to manage multiple `docker-compose.yml` and `.env` files. With `dcx` you will be able to organise your files in modularised components. All your modularised components will be merged into one single `docker-compose.yml` and `.env` at the end.

## Examples

### .env

`env/20-services/test.env`:

```env
HELLO="World"
GREETING="Mars"
COMPOSE_UID="${COMPOSE_UID:-1000}
```

`env/99-overrides/test.env`:

```env
GREETING="${HELLO}"
```

**Result**

```env
HELLO="World"
GREETING="World"
COMPOSE_UID="1000"
```

### docker-compose.yml

`compose/21-volumes/httpd.yaml`:

```yaml
---
volumes:
  httpd:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: $PWD/htdocs
```

`compose/22-services/httpd.yaml`:

```yaml
---
services:
  httpd:
    image: 'httpd:2.4'
    volumes:
      httpd: {}
```

`compose/99-overrides/httpd-dev.yaml`:

```yaml
---
services:
  httpd:
    ports:
      - 80:80
```

**Result**

```yaml
---
volumes:
  httpd:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: $PWD/htdocs
      
services:
  httpd:
    image: 'httpd:2.4'
    volumes:
      httpd: {}
    ports:
      - 80:80
```

## Usage
Create or update `.env` and `docker-compose.yml` by executing:

```bash
./dcx
```

## Initial setup

```bash
git clone git@github.com:iermentraut/dcx.git ~/dcx
cd ~/dcx
rm -rf .git .gitignore
git init
```
