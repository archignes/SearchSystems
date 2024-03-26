# Search Systems API

The Search Systems API provides a means to interact with a curated list of search system objects. It currently offers functionalities to retrieve the entire list, a specific system by ID, or the count of all available systems.

[![Sync Repository to API](https://github.com/archignes/SearchSystems/actions/workflows/main.yml/badge.svg)](https://github.com/archignes/SearchSystems/actions/workflows/main.yml) [![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fxbq1s7ts13.execute-api.us-east-1.amazonaws.com%2Fbeta%2F%3Faction%3Dgithub-shield&label=Count%20of%20Systems)](https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?action=count)

**Note:** The Search Systems API is currently in development. We recommend not relying on it for critical applications.

This API was originally written to deduplicate efforts on [Searchevals.com](https://searchevals.com/) and [Searchjunct.com](https://searchjunct.com/) and as part of the Archignes goal of supporting exit and voice in search.

## API Endpoint

Currently, the API is accessible via:

```
https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta
```

## Authentication

Access to the Search Systems API does not currently require authentication.

## Endpoints

### Get All Search Systems

Retrieves a comprehensive list of search systems.

- **URL:** `/`
- **Method:** `GET`
- **Query Parameters:** `action=systems` - Triggers the systems action.
- **Response:** `200 OK` - Returns a JSON array of search system objects (see [systems.json](systems.json)).

Example: [https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?action=systems](https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?action=systems)

### Get Search System by ID

Fetches a search system specified by its ID.

- **URL:** `/`
- **Method:** `GET`
- **Query Parameters:** `id` (required) - The unique identifier for the desired search system.
- **Response:**
  - `200 OK` - Success, returns the search system object.
  - `404 Not Found` - When the specified ID does not exist, returns `{"message": "System not found"}`.

Example: [https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?id=ecosia](https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?id=ecosia)

Example response:

```json
{
name: "Ecosia",
id: "ecosia",
search_index: "bing",
charity_search_engine: true,
base_url: "https://www.ecosia.org",
search_link: "https://www.ecosia.org/search?q=%s",
wikipedia_link: "https://en.wikipedia.org/wiki/Ecosia",
android_choice_screen_options: true,
default_in_browser: [
"Brave",
"Safari"
],
nonprofit_verification: "https://www.bcorporation.net/en-us/find-a-b-corp/company/ecosia-gmbh/",
twitter_link: "https://twitter.com/ecosia"
}
```

### Get Search System Count

Provides the total number of available search systems.

- **URL:** `/`
- **Method:** `GET`
- **Query Parameters:** `action=count` - Triggers the count action.
- **Response:** `200 OK` - Returns a JSON object with the total count.

Example: [https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?action=count](https://xbq1s7ts13.execute-api.us-east-1.amazonaws.com/beta/?action=count)

Example response:

```json
{
count: "42"
}
```

## Search System Object Structure

The schema in the [schema.json](schema.json) file describes the structure of each search system object (including any optional properties). The required structure for each search system object is as follows:

```json
{
  "name": "Search System Name",
  "id": "search-system-id",
  "search_link": "https://example.com/search?q=%s"
}
```

- `name`: The system's name.
- `id`: A unique identifier.
- `search_link`: URL template for searches. Replace `%s` with your query.

## Error Handling

The API communicates issues through standard HTTP status codes:

- `200 OK` - The request was successful.
- `404 Not Found` - The requested resource was not found.
- `500 Internal Server Error` - An unexpected error occurred on the server.

## Validation

The [schema.json](schema.json) file contains the JSON schema for the search system data and [validate.js](validate.js) uses [Ajv](https://ajv.js.org/) to validate that [systems.json](systems.json) follows the schema. Perform validation with `npm test`.

## Formating

Prettier is used to format the JSON files. Run `npm run format`.

## Repo hooks

[Husky](https://typicode.github.io/husky/) pre-commit hooks to run the validation and formatting (with [lint-staged](https://github.com/lint-staged/lint-staged)) before committing changes.

## TODO

- [ ] Setup on `api.archignes/systems`
- [ ] Setup GitHub Actions to show status of the schema validation and the API.
- [ ] Show implementation in Searchevals.com and Searchjunct.com

## Contributing

To contribute to the search systems data:

1. Fork the repository.
2. Update the `systems.json` file with your changes.
3. Submit a pull request detailing your modifications.

Ensure your contributions match the established data structure and include all necessary information.

## License

This project is distributed under the [MIT License](LICENSE).
