# TheBrain API Quickstart - Python

This is an example project that demonstrates how to make a call to TheBrain's API to create a thought. It uses the [Flask](https://flask.palletsprojects.com/en/3.0.x/) web framework. Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd thebrain-api-quickstart-python
   ```

4. Create a new virtual environment:

   Linux/macOS:
   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```
   Windows:
   ```cmd
   $ python -m venv venv
   $ venv/Scripts/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://app.thebrain.com/apiKeys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000).
