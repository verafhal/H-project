import pytest
from utils.json_helpers import safe_json_parse


@pytest.mark.api
def test_get_all_posts(api_request_context):
    """Positive Test: Get all posts and verify count and structure."""

    # Prepare the endpoint
    endpoint = "/posts"

    # Send GET request
    response = api_request_context.get("/posts")

    # Verify status code is 200 OK
    assert response.status == 200, "Expected status code 200 for GET /posts"

    # Assert: Safely parse JSON
    posts = safe_json_parse(response)

    # Assert there are exactly 100 posts
    assert len(posts) == 100, f"Expected 100 posts, but got {len(posts)}"

    # Validate the structure and types of one sample post
    sample_post = posts[0]
    assert isinstance(sample_post['userId'], int), "userId should be an integer"
    assert isinstance(sample_post['id'], int), "id should be an integer"
    assert isinstance(sample_post['title'], str), "title should be a string"
    assert isinstance(sample_post['body'], str), "body should be a string"



@pytest.mark.api
def test_get_post_by_valid_id(api_request_context):
    """Positive Test: Get post with valid ID and validate fields."""

    # Set a valid post ID
    post_id = 10
    endpoint = f"/posts/{post_id}"

    # Send GET request and capture the response
    response = api_request_context.get(endpoint)

    # Verify status code is 200 OK
    assert response.status == 200, f"Expected status code 200 for GET /posts/{post_id}"

    # Assert: Safely parse JSON
    post = safe_json_parse(response)

    # Validate the returned post structure
    assert post['id'] == post_id, f"Expected post id to be {post_id}"
    assert isinstance(post['userId'], int), "userId should be an integer"
    assert isinstance(post['title'], str), "title should be a string"
    assert isinstance(post['body'], str), "body should be a string"



@pytest.mark.api
def test_get_post_by_invalid_id(api_request_context):
    """Negative Test: Get post with invalid ID and expect 404."""

    # Set an invalid post ID
    invalid_id = 150
    endpoint = f"/posts/{invalid_id}"

    # Send GET request and capture the response
    response = api_request_context.get(endpoint)

    # Verify status code is 404 Not Found
    assert response.status == 404, f"Expected status code 404 for GET /posts/{invalid_id}"



@pytest.mark.api
def test_create_new_post(api_request_context):
    """Positive Test: Create a new post with valid payload."""

    # Prepare the payload data
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    endpoint = "/posts"

    # Send POST request and capture the response
    response = api_request_context.post(endpoint, data=payload)

    # Verify status code is 201 Created
    assert response.status == 201, "Expected status code 201 for POST /posts"

    # Assert: Safely parse JSON
    created_post = safe_json_parse(response)

    # Verify the response body includes created post data
    assert created_post["title"] == payload["title"], "Title mismatch in created post"
    assert created_post["body"] == payload["body"], "Body mismatch in created post"
    assert created_post["userId"] == payload["userId"], "userId mismatch in created post"
    assert "id" in created_post, "Response should contain new post ID"



@pytest.mark.api
def test_create_post_missing_fields(api_request_context):
    """Negative Test: Try creating a post with missing required fields."""

    # Prepare an incomplete payload (missing title and body)
    incomplete_payload = {
        "userId": 1
    }
    endpoint = "/posts"

    # Send POST request with incomplete payload and capture the response
    response = api_request_context.post(endpoint, data=incomplete_payload)

    # Check the response
    # Note: JSONPlaceholder returns 201 even for incomplete data (mock behavior)
    assert response.status == 201, "Expected status code 201 even for incomplete POST (mock behavior)"

    # Assert: Safely parse JSON
    created_post = safe_json_parse(response)

    # Verify that missing fields are indeed missing or empty
    assert created_post.get("title") in (None, ""), "Title should be missing or empty"
    assert created_post.get("body") in (None, ""), "Body should be missing or empty"
    assert created_post["userId"] == incomplete_payload["userId"], "userId mismatch in created post"


