# docker-data-science
A microservice that bootstraps any data scientist with Anaconda3 and the ccxt library using Jupyter Notebook as an IDE

## Setup

This application is containerized using Docker, so running it is quite simple.

- Ensure Docker is installed on your local system.

- Clone the repo: ```git clone https://github.com/tradery/docker-data-science.git```

**Inside the app directory:**
- Build the container through Docker: ```docker-compose build```

- Launch the container through Docker: ```docker-compose up```

- View the Juypter Notebook in a browser: ```http://0.0.0.0:8888```

- Login (password is root)
