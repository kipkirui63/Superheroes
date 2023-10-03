# phase4-wk-2

# Flask Code Challenge - Superheroes

Welcome to the Flask Code Challenge - Superheroes! In this assessment, you'll be working on building a Flask API for tracking heroes and their superpowers. You will also find a fully built React frontend application to test your API's functionality.

## Setup

To get started, follow these setup instructions:

1. Download the dependencies for the frontend and backend by running the following commands:
   ```sh
   pipenv install
   npm install --prefix client
   ```

2. Generate the database models and seed data:
   - Start by creating the necessary models and migrations for the database tables. Refer to the domain diagram in the project for reference.
   - Establish the relationships between the models:
     - A `Hero` has many `Power`s through `HeroPower`
     - A `Power` has many `Hero`s through `HeroPower`
     - A `HeroPower` belongs to a `Hero` and belongs to a `Power`
   - Run the migrations:
     ```sh
     flask db upgrade
     ```
   - Seed the database with initial data using the provided `app/seed.py` file:
     ```sh
     python app/seed.py
     ```
     > If the provided seed file doesn't work, you can generate your own seed data.

3. Run the Flask API on [`localhost:5555`](http://localhost:5555) using the following command:
   ```sh
   python app.py
   ```

4. Run the React app on [`localhost:4000`](http://localhost:4000) to interact with the API via the frontend:
   ```sh
   npm start --prefix client
   ```

5. You can also run tests using `pytest -x` to check your work.

## Models

In this project, you need to create the following relationships in your database:

- A `Hero` has many `Power`s through `HeroPower`
- A `Power` has many `Hero`s through `HeroPower`
- A `HeroPower` belongs to a `Hero` and belongs to a `Power`

Ensure that you add the necessary code in the model files to establish these relationships.

## Validations

Implement validations in the models:

- For the `HeroPower` model:
  - `strength` must be one of the following values: 'Strong', 'Weak', 'Average'
- For the `Power` model:
  - `description` must be present and at least 20 characters long

## Routes

Set up the following routes with the specified JSON data formats and HTTP verbs:

### GET /heroes

Returns a list of heroes in the following JSON format:

```json
[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "id": 3, "name": "Gwen Stacy", "super_name": "Spider-Gwen" }
]
```

### GET /heroes/:id

If the `Hero` with the specified `id` exists, it returns JSON data in the following format:

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"
    }
  ]
}
```

If the `Hero` does not exist, it returns the following JSON data along with the appropriate HTTP status code:

```json
{
  "error": "Hero not found"
}
```

### GET /powers

Returns a list of powers in the following JSON format:

```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  },
  {
    "id": 2,
    "name": "flight",
    "description": "gives the wielder the ability to fly through the skies at supersonic speed"
  }
]
```

### GET /powers/:id

If the `Power` with the specified `id` exists, it returns JSON data in the following format:

```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

If the `Power` does not exist, it returns the following JSON data along with the appropriate HTTP status code:

```json
{
  "error": "Power not found"
}
```

### PATCH /powers/:id

This route updates an existing `Power`. It accepts an object with the following properties in the request body:

```json
{
  "description": "Updated description"
}
```

If the `Power` exists and is updated successfully (passes validations), it updates its description and returns JSON data in the following format:

```json
{
  "id": 1,
  "name": "super strength",
  "description": "Updated description"
}
```

If the `Power` does not exist, it returns the following JSON data along with the appropriate HTTP status code:

```json
{
  "error": "Power not found"
}
```

If the `Power` is **not** updated successfully (does not pass validations), it returns the following JSON data along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

### POST /hero_powers

This route creates a new `HeroPower` that is associated with an existing `Power` and `Hero`. It accepts an object with the following properties in the request body:

```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

If the `HeroPower` is created successfully, it sends back a response with the data related to the `Hero` in the following format:

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"
    }
  ]
}
```

If the `HeroPower` is **not** created successfully, it returns the following JSON data along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

