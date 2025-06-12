from main import is_fake_live

stream = {
    "has_live_chat": False,
    "content_id": "abc123",
    "archived_upload_ids": ["abc123"],
    "source_type": "pre_encoded",
    "original_upload_time": "2023-11-17 12:00",
    "current_stream_time": "2025-06-10 18:30"
}

print(is_fake_live(stream))
